import sys
import wx
import operator
import os
import timeit
import datetime
import zipfile
import threading
import json
from dateutil import relativedelta
from ZipperWXUI import Zipper


class ZipperUI(Zipper):
	def __init__(self, parent):
		Zipper.__init__(self, parent)

		self.defaultIgnore = [".zip", ".gz", ".tar", ".arc", ".rar", ".bz2", ".7z"]
		self.units = {"Kilobytes": 1000, "Megabytes": 1000000, "Gigabytes": 1000000000}
		self.compop = {"Ignore files smaller than": ">", "Ignore files larger than": "<"}
		self.timefilteropt = {"Ignore files older than": "<", "Ignore files newer than": ">"}
		self.timeunits = ["hours", "weeks", "days", "months", "years"]
		self.filenamefilteropt = {"Only include files": True, "Exclude all files": False}
		self.updateFilters()
		self.stopArchiving = True
		self.SetStatusWidths([-4, -1, -1])
		self.SetStatusText(datetime.datetime.today().strftime("%d-%b-%Y"), number=2)


	def exit(self, event):
		print("exiting")
		self.Close()


	def updateFilters(self):
		self.m_choiceSizeOp.AppendItems(list(self.compop.keys()))
		self.m_choiceSizeUnit.AppendItems(sorted(self.units.keys(), key=operator.itemgetter(1)))
		self.m_choiceTimeUnit.AppendItems(self.timeunits)
		self.m_choiceTimeOp.AppendItems(list(self.timefilteropt.keys()))
		self.m_choiceFilename.AppendItems(list(self.filenamefilteropt.keys()))
		self.SetStatusText("Filters updated.")


	def addIgnoreExtension(self, event):
		try:
			selected =self.m_listBoxInclude.GetSelections()
			for x in selected:
				self.m_listBoxExclude.InsertItems([self.m_listBoxInclude.GetString(x)], 0)
				self.m_listBoxInclude.Delete(x)
		except:
			self.SetStatusText("Cannot add extension to ignore list : " + str(sys.exc_info()[1]))

	def RemIgnoreExtension(self, event):
		try:
			selected =self.m_listBoxExclude.GetSelections()
			for x in selected:
				self.m_listBoxInclude.InsertItems([self.m_listBoxExclude.GetString(x)], 0)
				self.m_listBoxExclude.Delete(x)
		except:
			self.SetStatusText("Cannot remove from ignore list: " + str(sys.exc_info()[1]))


	def toggleSpecFolder(self, event):
		if self.m_radioBtnPlaceSpec.GetValue():
			self.m_dirPickerSpec.Enable()
		else:
			self.m_dirPickerSpec.Disable()


	def toggleTimestamp(self, event):
		if self.m_checkBoxTimestamp.IsChecked():
			self.m_textCtrlTimeStamp.Enable()
		else:
			self.m_textCtrlTimeStamp.Disable()


	def saveJob(self, event):
		try:
			self.SetStatusText("Save current job")
			self.saveJobDialog = wx.FileDialog(self, "Select a destination file to save current job", "", "", "U-zip json files (*.uzip)|*.uzip", wx.FD_SAVE | wx.FD_OVERWRITE_PROMPT)
			self.saveJobDialog.ShowModal()
			savf = self.saveJobDialog.GetPath()
			self.saveJobDialog.Destroy()

			job_obj = {}
			job_obj["ROOT_FOLDER"] = self.m_dirPicker.GetPath()
			job_obj["RECURSIVE"] = self.m_checkRecursive.IsChecked()
			job_obj["FILTERED_EXT"] = self.m_listBoxExclude.GetStrings()
			job_obj["FILTERED_SIZE"] = [self.m_checkBoxSize.IsChecked(), self.m_choiceSizeOp.GetCurrentSelection(), self.m_textCtrlSize.GetLineText(0), self.m_choiceSizeUnit.GetCurrentSelection()]
			job_obj["FILTERED_TIME"] = [self.m_checkBoxTime.IsChecked(), self.m_choiceTimeOp.GetCurrentSelection(), self.m_textCtrlTime.GetLineText(0), self.m_choiceTimeUnit.GetCurrentSelection()]
			job_obj["FILTERED_FILENAME"] = [self.m_checkBoxFilename.IsChecked(), self.m_choiceFilename.GetCurrentSelection(), self.m_textCtrlFilename.GetLineText(0)]
			job_obj["DELETE_ORIGINAL"] = self.m_checkBoxDelOriginal.IsChecked()
			job_obj["ARCHIVE_LOC"] = [self.m_radioOriginalFolder.GetValue(), self.m_dirPickerSpec.GetPath()]
			job_obj["APPEND_TIMESTAMP"] = [self.m_checkBoxTimestamp.IsChecked(), self.m_textCtrlTimeStamp.GetLineText(0)]

			with open(savf, 'w') as jobf:
				json.dump(job_obj, jobf, indent=4)
				self.SetStatusText("Current job saved to {}".format(savf))
		except:
			self.SetStatusText("Error saving current job : {}".format(str(sys.exc_info()[1])))
			return False


	def loadJob(self, event):
		try:
			start = timeit.default_timer()
			self.SetStatusText("Loading existing job from file")
			self.loadJobDialog = wx.FileDialog(self, "Open job file", "", "", "U-zip json files (*.uzip)|*.uzip", wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
			self.loadJobDialog.ShowModal()
			loadf = self.loadJobDialog.GetPath()
			self.loadJobDialog.Destroy()

			with open(loadf) as jobf:
				job_obj = json.load(jobf)

			self.m_dirPicker.SetPath(job_obj["ROOT_FOLDER"])
			self.m_checkRecursive.SetValue(job_obj["RECURSIVE"])
			self.refreshExtensionList()
			exclude_union = list(set(self.m_listBoxExclude.GetStrings()).union(job_obj["FILTERED_EXT"]))
			self.m_listBoxExclude.Clear()
			self.m_listBoxExclude.AppendItems(exclude_union)
			include_diff = list(set(self.m_listBoxInclude.GetStrings()).difference(job_obj["FILTERED_EXT"]))
			self.m_listBoxInclude.Clear()
			self.m_listBoxInclude.AppendItems(include_diff)
			self.m_checkBoxSize.SetValue(job_obj["FILTERED_SIZE"][0])
			self.m_choiceSizeOp.Select(job_obj["FILTERED_SIZE"][1])
			self.m_textCtrlSize.SetLabelText(job_obj["FILTERED_SIZE"][2])
			self.m_choiceSizeUnit.Select(job_obj["FILTERED_SIZE"][3])
			self.m_checkBoxTime.SetValue(job_obj["FILTERED_TIME"][0])
			self.m_choiceTimeOp.Select(job_obj["FILTERED_TIME"][1])
			self.m_textCtrlTime.SetLabelText(job_obj["FILTERED_TIME"][2])
			self.m_choiceTimeUnit.Select(job_obj["FILTERED_TIME"][3])
			self.m_checkBoxFilename.SetValue(job_obj["FILTERED_FILENAME"][0])
			self.m_choiceFilename.Select(job_obj["FILTERED_FILENAME"][1])
			self.m_textCtrlFilename.SetLabelText(job_obj["FILTERED_FILENAME"][2])
			self.m_checkBoxDelOriginal.SetValue(job_obj["DELETE_ORIGINAL"])
			self.m_radioOriginalFolder.SetValue(job_obj["ARCHIVE_LOC"][0])
			self.m_radioBtnPlaceSpec.SetValue(not job_obj["ARCHIVE_LOC"][0])
			self.m_dirPickerSpec.SetPath(job_obj["ARCHIVE_LOC"][1])
			self.toggleSpecFolder(event)
			self.m_checkBoxTimestamp.SetValue(job_obj["APPEND_TIMESTAMP"][0])
			self.m_textCtrlTimeStamp.SetLabelText(job_obj["APPEND_TIMESTAMP"][1])
			self.toggleTimestamp(event)

			end = timeit.default_timer()
			self.SetStatusText("Job loaded from {} in {:.2f} seconds".format(loadf, end - start))
		except:
			self.SetStatusText("Error loading job : {}".format(str(sys.exc_info()[1])))
			return False


	def refreshExtensionList(self):
		try:
			folder = self.m_dirPicker.GetPath()
			if not os.path.isdir(folder):
				self.SetStatusText("Error : select a valid folder first")
				return
			exts = set()  # using a set for unique unordered properties
			self.m_listBoxExclude.Clear()
			self.m_listBoxInclude.Clear()

			self.SetStatusText("Scanning for extensions, please wait...")
			for dirpath, dirnames, filenames in os.walk(folder, topdown=True):
				for filename in filenames:
					exts.add(os.path.splitext(filename)[1])
			for extension in self.defaultIgnore:
				if extension in exts:
					exts.remove(extension)
					self.m_listBoxExclude.Append(extension)
			self.m_listBoxInclude.InsertItems(list(exts), 0)
			self.SetStatusText("Extensions loaded.")
		except:
			self.SetStatusText("Could not refresh extensions : " + str(sys.exc_info()[1]))


	def startRefreshExtensionList(self, event):
		self.refreshExtensionsThread = threading.Thread(target=self.refreshExtensionList)
		self.refreshExtensionsThread.start()


	def startArchive(self, event):
		self.stopArchiving = False
		self.archiveThread = threading.Thread(target=self.archiveNow)
		self.archiveThread.start()

	def startPopulateZipView(self, event):
		self.populateZipView = threading.Thread(target=self.populateZipView)
		self.populateZipView.start()


	def cancelArchive(self, event):
		self.SetStatusText("Process interrupted by the user !")
		self.stopArchiving = True
		self.m_gauge.SetValue(0)


	def populateZipView(self):
		self.SetStatusText("Populating list view...")

		root = self.m_dirPickerRestore.GetPath()
		if not os.path.isdir(root):
			self.SetStatusText("No valid folder selected.")
			return

		for inputfolder, dirnames, filenames in os.walk(root, topdown=True):
			for filename in filenames:
				if os.path.splitext(filename)[1] == ".zip":
					os.path.split()
					self.m_dataViewCtrlZipView.AddChild()



	def archiveNow(self):
		try:
			start = timeit.default_timer()
			self.m_gauge.SetValue(0)

			# Building dictionary of files to archive. Contains inputfile:outputfile
			inout = {}
			root = self.m_dirPicker.GetPath()

			extfilterlist = ['.zip'] + self.m_listBoxExclude.GetStrings()

			self.SetStatusText("Pre-processing...")
			operators = {"<": operator.lt, ">": operator.gt}
			_sizeFilterOn = self.m_checkBoxSize.IsChecked()
			_timefilterOn = self.m_checkBoxTime.IsChecked()
			_namefilterOn = self.m_checkBoxFilename.IsChecked()
			_sizefilter = True
			_timefilter = True
			_filenamefilter = True
			_timestamp_checked = self.m_checkBoxTimestamp.IsChecked()
			_timestamp = self.m_textCtrlTimeStamp.GetLineText(0)
			_spec_checked = self.m_radioBtnPlaceSpec.GetValue()
			_spec_dir = self.m_dirPickerSpec.GetPath()
			_size_op = self.m_choiceSizeOp.GetStringSelection()
			if _sizeFilterOn:
				try:
					_size_filter = int(self.m_textCtrlSize.GetLineText(0)) * int(self.units[self.m_choiceSizeUnit.GetStringSelection()])
				except:
					self.SetStatusText("Error : incorrect size filter parameters : {}".format(str(sys.exc_info()[1])))
					return
			if _timefilterOn:
				try:
					_time_op = self.m_choiceTimeOp.GetStringSelection()
					_time_filter = datetime.datetime.now() - relativedelta.relativedelta(**{self.m_choiceTimeUnit.GetStringSelection(): int(self.m_textCtrlTime.GetLineText(0))})
				except:
					self.SetStatusText("Error : incorrect time filter parameters : {}".format(str(sys.exc_info()[1])))
					return
			if _namefilterOn:
				try:
					if self.m_textCtrlFilename.GetStringSelection() == "":
						raise Exception
					_filename_filter = self.m_textCtrlFilename.GetStringSelection().lower()
					_filename_op = bool(self.filenamefilteropt[self.m_choiceFilename.GetStringSelection()])
				except:
					self.SetStatusText("Error : incorrect file name filter parameters : {}".format(str(sys.exc_info()[1])))
					return
			_only_root = not self.m_checkRecursive.IsChecked()
			for inputfolder, dirnames, filenames in os.walk(root, topdown=True):
				for filename in filenames:
					if self.stopArchiving:
						return
					filetowrite = filename
					# Process preferences
					if _timestamp_checked:
						self.SetStatusText("[Pre-processing] Appending timestamp {}...".format(filename))
						filetowrite = os.path.splitext(filename)[0] + datetime.datetime.now().strftime(_timestamp + os.path.splitext(filename)[1])
					if _spec_checked:
						filetowrite = os.path.join(_spec_dir, filetowrite) + ".zip"
						outputfolder = _spec_dir
						if outputfolder == "":
							self.SetStatusText("Please define a custom folder where to place the archive(s), or change your preferences !")
							return
					else:
						filetowrite = filetowrite + ".zip"
						outputfolder = inputfolder
					# Process Filters
					_extfilter = os.path.splitext(filename)[1] not in extfilterlist
					if _sizeFilterOn:
						_sizefilter = operators[self.compop[_size_op]](os.path.getsize(os.path.join(inputfolder, filename)), _size_filter)
					if _timefilterOn:
						_timefilter = operators[self.timefilteropt[_time_op]](_time_filter, datetime.datetime.fromtimestamp(os.path.getmtime(os.path.join(inputfolder, filename))))
					if _namefilterOn:
						filenamefilter = (filename.lower().find(_filename_filter) != -1) == _filename_op   # '==' is to obtain False+False=True
					if _extfilter and _sizefilter and _timefilter and _filenamefilter and not os.path.exists(os.path.join(outputfolder, filetowrite)):
						self.SetStatusText("[Pre-processing] Adding file {}...".format(filename))
						inout[os.path.join(inputfolder, filename)] = os.path.join(outputfolder, filetowrite)
				if _only_root:
					break

			if not inout:
				self.SetStatusText("Nothing to do.")
				return -1

			self.SetStatusText("Pre-processing done")

			# Archive
			completion = 0
			f = 0
			_total_files = len(inout)
			step = 100 / _total_files
			for inputfile, outputfile in inout.items():
				if self.stopArchiving:
					return
				self.SetStatusText("Archiving {}...".format(inputfile))
				try:
					with zipfile.ZipFile(outputfile, "w", compression=zipfile.ZIP_DEFLATED, allowZip64=True) as zipf:
						zipf.write(inputfile, os.path.split(inputfile)[1])
				except:
					self.SetStatusText("Warning : " + str(sys.exc_info()[1]))
				else:
					if self.m_checkBoxDelOriginal.IsChecked():
						self.SetStatusText("Deleting {}...".format(inputfile))
						os.remove(inputfile)

				completion += step
				f += 1
				self.m_gauge.SetValue(completion)
				self.SetStatusText("{}/{} files ({:.0f}%)".format(f, _total_files, completion), number=1)

			end = timeit.default_timer()
			self.SetStatusText("{} files archived in {:.2f} seconds".format(len(inout), end - start))

			return 0

		except:
			self.SetStatusText("Archival job failed with error : " + str(sys.exc_info()[1]))


class ArchiveThread(threading.Thread):
	def __init__(self, parent, value):
		"""
		@param parent: GUI object that must be updated
		"""
		self.gui = parent
		threading.Thread.__init__(self)
		self.start()


if __name__ == '__main__':
	app = wx.App()

	frame = ZipperUI(parent=None)
	frame.Show()

	app.MainLoop()
