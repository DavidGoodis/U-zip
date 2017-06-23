# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Apr 24 2017)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.lib.agw.ribbon as rb
import wx.aui
import wx.dataview

loadtool = 1000
savetool = 1001
saveastool = 1002
quit = 1003


###########################################################################
## Class Zipper
###########################################################################

class Zipper(wx.Frame):
	def __init__(self, parent):
		wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"Zipper", pos=wx.DefaultPosition, size=wx.Size(561, 802), style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

		self.SetSizeHints(wx.DefaultSize, wx.DefaultSize)
		self.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOWTEXT))
		self.SetBackgroundColour(wx.Colour(240, 240, 240))

		self.m_menubar = wx.MenuBar(0)
		self.m_menuFile = wx.Menu()
		self.m_menuLoad = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"Load", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menuLoad.SetBitmap(wx.Bitmap(u"ui/load.png", wx.BITMAP_TYPE_ANY))
		self.m_menuFile.Append(self.m_menuLoad)

		self.m_menuSave = wx.MenuItem(self.m_menuFile, wx.ID_ANY, u"Save", wx.EmptyString, wx.ITEM_NORMAL)
		self.m_menuSave.SetBitmap(wx.Bitmap(u"ui/write.png", wx.BITMAP_TYPE_ANY))
		self.m_menuFile.Append(self.m_menuSave)

		self.m_menubar.Append(self.m_menuFile, u"File")

		self.SetMenuBar(self.m_menubar)

		bSizer1 = wx.BoxSizer(wx.VERTICAL)

		self.m_ribbonBar = rb.RibbonBar(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_BAR_DEFAULT_STYLE)
		self.m_ribbonPage = rb.RibbonPage(self.m_ribbonBar, wx.ID_ANY, u"MyRibbonPage", wx.NullBitmap, 0)
		self.m_ribbonPanel = rb.RibbonPanel(self.m_ribbonPage, wx.ID_ANY, wx.EmptyString, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE)
		self.m_ribbonToolBar = rb.RibbonToolBar(self.m_ribbonPanel, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_ribbonToolBar.AddSimpleTool(loadtool, wx.ArtProvider.GetBitmap(wx.ART_FILE_OPEN, wx.ART_TOOLBAR), u"Load job from json file")
		self.m_ribbonToolBar.AddSimpleTool(savetool, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE, wx.ART_TOOLBAR), u"Save current job to json file")
		self.m_ribbonToolBar.AddSimpleTool(saveastool, wx.ArtProvider.GetBitmap(wx.ART_FILE_SAVE_AS, wx.ART_TOOLBAR), u"Save current job to new json file")
		self.m_ribbonPanel2 = rb.RibbonPanel(self.m_ribbonPage, wx.ID_ANY, wx.EmptyString, wx.NullBitmap, wx.DefaultPosition, wx.DefaultSize, wx.lib.agw.ribbon.RIBBON_PANEL_DEFAULT_STYLE)
		self.m_ribbonToolBar2 = rb.RibbonToolBar(self.m_ribbonPanel2, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_ribbonToolBar2.AddSimpleTool(quit, wx.ArtProvider.GetBitmap(wx.ART_QUIT, wx.ART_TOOLBAR), wx.EmptyString)
		self.m_ribbonBar.Realize()

		bSizer1.Add(self.m_ribbonBar, 0, wx.ALL | wx.EXPAND, 2)

		self.m_auinotebook1 = wx.aui.AuiNotebook(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_BOTTOM | wx.aui.AUI_NB_TAB_FIXED_WIDTH | wx.aui.AUI_NB_TAB_MOVE)
		self.m_auinotebook1.SetBackgroundColour(wx.Colour(240, 240, 240))

		self.m_scrolledWindowArchive = wx.ScrolledWindow(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
		self.m_scrolledWindowArchive.SetScrollRate(5, 5)
		bSizer7 = wx.BoxSizer(wx.VERTICAL)

		bSizerFolderSelect = wx.BoxSizer(wx.VERTICAL)

		self.m_dirPicker = wx.DirPickerCtrl(self.m_scrolledWindowArchive, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
											wx.DIRP_CHANGE_DIR | wx.DIRP_DIR_MUST_EXIST | wx.DIRP_SMALL | wx.DIRP_USE_TEXTCTRL)
		self.m_dirPicker.SetBackgroundColour(wx.Colour(240, 240, 240))

		bSizerFolderSelect.Add(self.m_dirPicker, 0, wx.ALL | wx.EXPAND, 2)

		self.m_checkRecursive = wx.CheckBox(self.m_scrolledWindowArchive, wx.ID_ANY, u"Recursive (include subfolders)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT | wx.CHK_2STATE)
		self.m_checkRecursive.SetValue(True)
		bSizerFolderSelect.Add(self.m_checkRecursive, 0, wx.ALIGN_RIGHT | wx.ALL, 5)

		bSizer7.Add(bSizerFolderSelect, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 2)

		sbSizerFilters = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindowArchive, wx.ID_ANY, u"Filters"), wx.VERTICAL)

		sbSizerExtensions = wx.StaticBoxSizer(wx.StaticBox(sbSizerFilters.GetStaticBox(), wx.ID_ANY, u"Extensions"), wx.HORIZONTAL)

		bSizer20 = wx.BoxSizer(wx.VERTICAL)

		self.m_staticText7 = wx.StaticText(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, u"Extentions to ignore", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText7.Wrap(-1)
		bSizer20.Add(self.m_staticText7, 0, wx.ALL, 2)

		m_listBoxExcludeChoices = []
		self.m_listBoxExclude = wx.ListBox(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxExcludeChoices, wx.LB_EXTENDED | wx.LB_NEEDED_SB)
		self.m_listBoxExclude.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
		self.m_listBoxExclude.SetMaxSize(wx.Size(-1, 200))

		bSizer20.Add(self.m_listBoxExclude, 0, wx.ALL | wx.EXPAND, 2)

		sbSizerExtensions.Add(bSizer20, 1, wx.EXPAND, 5)

		bSizer5 = wx.BoxSizer(wx.VERTICAL)

		self.m_buttonMinus = wx.BitmapButton(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_GO_FORWARD, wx.ART_BUTTON), wx.DefaultPosition, wx.DefaultSize,
											 wx.BU_AUTODRAW)
		bSizer5.Add(self.m_buttonMinus, 0, wx.ALL | wx.FIXED_MINSIZE, 1)

		self.m_buttonPlus = wx.BitmapButton(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_GO_BACK, wx.ART_BUTTON), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
		bSizer5.Add(self.m_buttonPlus, 0, wx.ALL | wx.FIXED_MINSIZE, 1)

		sbSizerExtensions.Add(bSizer5, 0, wx.ALIGN_BOTTOM, 2)

		bSizer21 = wx.BoxSizer(wx.VERTICAL)

		bSizer22 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText71 = wx.StaticText(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, u"Extentions detected", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText71.Wrap(-1)
		bSizer22.Add(self.m_staticText71, 0, wx.ALIGN_BOTTOM | wx.ALIGN_RIGHT | wx.ALL, 2)

		self.m_bpButtonRefresh = wx.BitmapButton(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_REPORT_VIEW, wx.ART_BUTTON), wx.DefaultPosition, wx.DefaultSize,
												 wx.BU_AUTODRAW)
		self.m_bpButtonRefresh.SetToolTipString(u"Refresh extensions list from disk")

		bSizer22.Add(self.m_bpButtonRefresh, 0, wx.ALIGN_TOP, 2)

		bSizer21.Add(bSizer22, 1, wx.ALIGN_RIGHT, 0)

		m_listBoxIncludeChoices = []
		self.m_listBoxInclude = wx.ListBox(sbSizerExtensions.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_listBoxIncludeChoices, wx.LB_EXTENDED | wx.LB_NEEDED_SB)
		self.m_listBoxInclude.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_WINDOW))
		self.m_listBoxInclude.SetMaxSize(wx.Size(-1, 200))

		bSizer21.Add(self.m_listBoxInclude, 0, wx.ALL | wx.EXPAND, 2)

		sbSizerExtensions.Add(bSizer21, 1, wx.EXPAND, 5)

		sbSizerFilters.Add(sbSizerExtensions, 1, wx.EXPAND, 2)

		sbSizerSize = wx.StaticBoxSizer(wx.StaticBox(sbSizerFilters.GetStaticBox(), wx.ID_ANY, u"Size"), wx.HORIZONTAL)

		self.m_checkBoxSize = wx.CheckBox(sbSizerSize.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerSize.Add(self.m_checkBoxSize, 0, wx.ALL, 5)

		m_choiceSizeOpChoices = []
		self.m_choiceSizeOp = wx.Choice(sbSizerSize.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSizeOpChoices, 0)
		self.m_choiceSizeOp.SetSelection(0)
		sbSizerSize.Add(self.m_choiceSizeOp, 1, wx.ALL, 5)

		self.m_textCtrlSize = wx.TextCtrl(sbSizerSize.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrlSize.SetBackgroundColour(wx.Colour(224, 224, 224))

		sbSizerSize.Add(self.m_textCtrlSize, 1, wx.ALL, 5)

		m_choiceSizeUnitChoices = []
		self.m_choiceSizeUnit = wx.Choice(sbSizerSize.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceSizeUnitChoices, 0)
		self.m_choiceSizeUnit.SetSelection(0)
		sbSizerSize.Add(self.m_choiceSizeUnit, 1, wx.ALL, 5)

		sbSizerFilters.Add(sbSizerSize, 0, wx.EXPAND, 2)

		sbSizerTime = wx.StaticBoxSizer(wx.StaticBox(sbSizerFilters.GetStaticBox(), wx.ID_ANY, u"Time"), wx.HORIZONTAL)

		self.m_checkBoxTime = wx.CheckBox(sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, wx.CHK_2STATE)
		sbSizerTime.Add(self.m_checkBoxTime, 0, wx.ALL, 5)

		m_choiceTimeOpChoices = []
		self.m_choiceTimeOp = wx.Choice(sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceTimeOpChoices, 0)
		self.m_choiceTimeOp.SetSelection(0)
		sbSizerTime.Add(self.m_choiceTimeOp, 1, wx.ALL, 5)

		self.m_textCtrlTime = wx.TextCtrl(sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrlTime.SetBackgroundColour(wx.Colour(224, 224, 224))

		sbSizerTime.Add(self.m_textCtrlTime, 1, wx.ALL, 5)

		m_choiceTimeUnitChoices = []
		self.m_choiceTimeUnit = wx.Choice(sbSizerTime.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceTimeUnitChoices, 0)
		self.m_choiceTimeUnit.SetSelection(0)
		sbSizerTime.Add(self.m_choiceTimeUnit, 1, wx.ALL, 5)

		sbSizerFilters.Add(sbSizerTime, 0, wx.EXPAND, 2)

		sbSizerName = wx.StaticBoxSizer(wx.StaticBox(sbSizerFilters.GetStaticBox(), wx.ID_ANY, u"File name"), wx.HORIZONTAL)

		self.m_checkBoxFilename = wx.CheckBox(sbSizerName.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerName.Add(self.m_checkBoxFilename, 0, wx.ALL, 5)

		m_choiceFilenameChoices = []
		self.m_choiceFilename = wx.Choice(sbSizerName.GetStaticBox(), wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, m_choiceFilenameChoices, 0)
		self.m_choiceFilename.SetSelection(0)
		sbSizerName.Add(self.m_choiceFilename, 1, wx.ALL, 5)

		self.m_staticText1 = wx.StaticText(sbSizerName.GetStaticBox(), wx.ID_ANY, u"with name having", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText1.Wrap(-1)
		sbSizerName.Add(self.m_staticText1, 0, wx.ALL, 5)

		self.m_textCtrlFilename = wx.TextCtrl(sbSizerName.GetStaticBox(), wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrlFilename.SetBackgroundColour(wx.Colour(224, 224, 224))

		sbSizerName.Add(self.m_textCtrlFilename, 1, wx.ALL, 5)

		sbSizerFilters.Add(sbSizerName, 0, wx.EXPAND, 2)

		bSizer7.Add(sbSizerFilters, 0, wx.ALL | wx.EXPAND, 2)

		sbSizerPrefs = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindowArchive, wx.ID_ANY, u"Preferences"), wx.VERTICAL)

		self.m_checkBoxDelOriginal = wx.CheckBox(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"Delete original file after it has been archived", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs.Add(self.m_checkBoxDelOriginal, 0, wx.ALL, 5)

		self.m_radioOriginalFolder = wx.RadioButton(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"Create archive in the same folder as the original", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
		self.m_radioOriginalFolder.SetValue(True)
		sbSizerPrefs.Add(self.m_radioOriginalFolder, 0, wx.ALL, 5)

		self.m_radioBtnPlaceSpec = wx.RadioButton(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"Place archive in a specific folder", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs.Add(self.m_radioBtnPlaceSpec, 0, wx.ALL, 5)

		self.m_dirPickerSpec = wx.DirPickerCtrl(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL)
		self.m_dirPickerSpec.Enable(False)

		sbSizerPrefs.Add(self.m_dirPickerSpec, 0, wx.ALL | wx.EXPAND, 5)

		self.m_checkBoxTimestamp = wx.CheckBox(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"Append timestamp to archive file", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs.Add(self.m_checkBoxTimestamp, 0, wx.ALL, 5)

		self.m_textCtrlTimeStamp = wx.TextCtrl(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"_%Y%m%d", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrlTimeStamp.Enable(False)

		sbSizerPrefs.Add(self.m_textCtrlTimeStamp, 0, wx.ALL | wx.EXPAND, 5)

		bSizer13 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText2 = wx.StaticText(sbSizerPrefs.GetStaticBox(), wx.ID_ANY, u"All format codes available at ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText2.Wrap(-1)
		self.m_staticText2.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
		self.m_staticText2.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))

		bSizer13.Add(self.m_staticText2, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 5)

		sbSizerPrefs.Add(bSizer13, 1, wx.EXPAND, 5)

		bSizer7.Add(sbSizerPrefs, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 2)

		bSizer6 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer6.SetMinSize(wx.Size(-1, 60))
		self.m_buttonCancel = wx.Button(self.m_scrolledWindowArchive, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer6.Add(self.m_buttonCancel, 0, wx.ALL | wx.FIXED_MINSIZE, 5)

		self.m_buttonArchive = wx.Button(self.m_scrolledWindowArchive, wx.ID_ANY, u"Archive now", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer6.Add(self.m_buttonArchive, 0, wx.ALL | wx.FIXED_MINSIZE, 5)

		bSizer7.Add(bSizer6, 1, wx.ALIGN_RIGHT | wx.FIXED_MINSIZE, 5)

		self.m_scrolledWindowArchive.SetSizer(bSizer7)
		self.m_scrolledWindowArchive.Layout()
		bSizer7.Fit(self.m_scrolledWindowArchive)
		self.m_auinotebook1.AddPage(self.m_scrolledWindowArchive, u"Archival job", False, wx.NullBitmap)
		self.m_scrolledWindowRestore = wx.ScrolledWindow(self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL | wx.VSCROLL)
		self.m_scrolledWindowRestore.SetScrollRate(5, 5)
		bSizer71 = wx.BoxSizer(wx.VERTICAL)

		bSizerFolderSelect1 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_dirPickerRestore = wx.DirPickerCtrl(self.m_scrolledWindowRestore, wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize,
												   wx.DIRP_CHANGE_DIR | wx.DIRP_DIR_MUST_EXIST | wx.DIRP_SMALL | wx.DIRP_USE_TEXTCTRL)
		self.m_dirPickerRestore.SetBackgroundColour(wx.Colour(240, 240, 240))

		bSizerFolderSelect1.Add(self.m_dirPickerRestore, 1, wx.ALL | wx.EXPAND, 2)

		self.m_checkRecursiveRestore = wx.CheckBox(self.m_scrolledWindowRestore, wx.ID_ANY, u"Recursive (include subfolders)", wx.DefaultPosition, wx.DefaultSize, wx.ALIGN_RIGHT | wx.CHK_2STATE)
		self.m_checkRecursiveRestore.SetValue(True)
		bSizerFolderSelect1.Add(self.m_checkRecursiveRestore, 0, wx.ALIGN_CENTER_VERTICAL | wx.ALIGN_RIGHT | wx.ALL, 5)

		self.m_bpButton6 = wx.BitmapButton(self.m_scrolledWindowRestore, wx.ID_ANY, wx.ArtProvider.GetBitmap(wx.ART_FIND, wx.ART_BUTTON), wx.DefaultPosition, wx.DefaultSize, wx.BU_AUTODRAW)
		bSizerFolderSelect1.Add(self.m_bpButton6, 0, wx.ALL, 5)

		bSizer71.Add(bSizerFolderSelect1, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 5)

		bSizer23 = wx.BoxSizer(wx.VERTICAL)

		self.m_dataViewCtrlZipView = wx.dataview.DataViewCtrl(self.m_scrolledWindowRestore, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_dataViewColumnFiles = self.m_dataViewCtrlZipView.AppendTextColumn(u"File", 0)
		self.m_dataViewColumn2 = self.m_dataViewCtrlZipView.AppendToggleColumn(u"selection", 0)
		bSizer23.Add(self.m_dataViewCtrlZipView, 1, wx.ALL | wx.EXPAND, 5)

		bSizer71.Add(bSizer23, 1, wx.EXPAND, 5)

		sbSizerPrefs1 = wx.StaticBoxSizer(wx.StaticBox(self.m_scrolledWindowRestore, wx.ID_ANY, u"Preferences"), wx.VERTICAL)

		self.m_checkBoxDelOriginal1 = wx.CheckBox(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"Delete original file after it has been archived", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs1.Add(self.m_checkBoxDelOriginal1, 0, wx.ALL, 5)

		self.m_radioOriginalFolder1 = wx.RadioButton(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"Create archive in the same folder as the original", wx.DefaultPosition, wx.DefaultSize, wx.RB_GROUP)
		self.m_radioOriginalFolder1.SetValue(True)
		sbSizerPrefs1.Add(self.m_radioOriginalFolder1, 0, wx.ALL, 5)

		self.m_radioBtnPlaceSpec1 = wx.RadioButton(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"Place archive in a specific folder", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs1.Add(self.m_radioBtnPlaceSpec1, 0, wx.ALL, 5)

		self.m_dirPickerSpec1 = wx.DirPickerCtrl(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE | wx.DIRP_SMALL)
		self.m_dirPickerSpec1.Enable(False)

		sbSizerPrefs1.Add(self.m_dirPickerSpec1, 0, wx.ALL | wx.EXPAND, 5)

		self.m_checkBoxTimestamp1 = wx.CheckBox(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"Append timestamp to archive file", wx.DefaultPosition, wx.DefaultSize, 0)
		sbSizerPrefs1.Add(self.m_checkBoxTimestamp1, 0, wx.ALL, 5)

		self.m_textCtrlTimeStamp1 = wx.TextCtrl(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"_%Y%m%d", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_textCtrlTimeStamp1.Enable(False)

		sbSizerPrefs1.Add(self.m_textCtrlTimeStamp1, 0, wx.ALL | wx.EXPAND, 5)

		bSizer131 = wx.BoxSizer(wx.HORIZONTAL)

		self.m_staticText21 = wx.StaticText(sbSizerPrefs1.GetStaticBox(), wx.ID_ANY, u"All format codes available at ", wx.DefaultPosition, wx.DefaultSize, 0)
		self.m_staticText21.Wrap(-1)
		self.m_staticText21.SetFont(wx.Font(8, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_ITALIC, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString))
		self.m_staticText21.SetForegroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_3DDKSHADOW))

		bSizer131.Add(self.m_staticText21, 0, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.TOP, 5)

		sbSizerPrefs1.Add(bSizer131, 1, wx.EXPAND, 5)

		bSizer71.Add(sbSizerPrefs1, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 2)

		bSizer61 = wx.BoxSizer(wx.HORIZONTAL)

		bSizer61.SetMinSize(wx.Size(-1, 60))
		self.m_buttonCancel1 = wx.Button(self.m_scrolledWindowRestore, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer61.Add(self.m_buttonCancel1, 0, wx.ALL | wx.FIXED_MINSIZE, 5)

		self.m_buttonArchive1 = wx.Button(self.m_scrolledWindowRestore, wx.ID_ANY, u"Archive now", wx.DefaultPosition, wx.DefaultSize, 0)
		bSizer61.Add(self.m_buttonArchive1, 0, wx.ALL | wx.FIXED_MINSIZE, 5)

		bSizer71.Add(bSizer61, 1, wx.ALIGN_RIGHT | wx.FIXED_MINSIZE, 5)

		self.m_scrolledWindowRestore.SetSizer(bSizer71)
		self.m_scrolledWindowRestore.Layout()
		bSizer71.Fit(self.m_scrolledWindowRestore)
		self.m_auinotebook1.AddPage(self.m_scrolledWindowRestore, u"Restore job", True, wx.NullBitmap)

		bSizer1.Add(self.m_auinotebook1, 1, wx.ALL | wx.EXPAND, 5)

		bSizer10 = wx.BoxSizer(wx.VERTICAL)

		self.m_gauge = wx.Gauge(self, wx.ID_ANY, 100, wx.DefaultPosition, wx.Size(-1, -1), wx.GA_HORIZONTAL | wx.GA_SMOOTH)
		self.m_gauge.SetValue(0)
		self.m_gauge.SetMaxSize(wx.Size(-1, 15))

		bSizer10.Add(self.m_gauge, 0, wx.ALL | wx.EXPAND, 5)

		bSizer1.Add(bSizer10, 0, wx.ALL | wx.EXPAND | wx.FIXED_MINSIZE, 5)

		self.SetSizer(bSizer1)
		self.Layout()
		self.m_statusBar = self.CreateStatusBar(3, 0, wx.ID_ANY)

		self.Centre(wx.HORIZONTAL)

		# Connect Events
		self.Bind(wx.EVT_MENU, self.loadJob, id=self.m_menuLoad.GetId())
		self.Bind(wx.EVT_MENU, self.saveJob, id=self.m_menuSave.GetId())
		self.Bind(rb.EVT_RIBBONTOOLBAR_CLICKED, self.loadJob, id=loadtool)
		self.Bind(rb.EVT_RIBBONTOOLBAR_CLICKED, self.saveJob, id=savetool)
		self.Bind(rb.EVT_RIBBONTOOLBAR_CLICKED, self.saveJob, id=saveastool)
		self.Bind(rb.EVT_RIBBONTOOLBAR_CLICKED, self.exit, id=quit)
		self.m_dirPicker.Bind(wx.EVT_DIRPICKER_CHANGED, self.startRefreshExtensionList)
		self.m_buttonMinus.Bind(wx.EVT_BUTTON, self.RemIgnoreExtension)
		self.m_buttonPlus.Bind(wx.EVT_BUTTON, self.addIgnoreExtension)
		self.m_bpButtonRefresh.Bind(wx.EVT_BUTTON, self.startRefreshExtensionList)
		self.m_radioOriginalFolder.Bind(wx.EVT_RADIOBUTTON, self.toggleSpecFolder)
		self.m_radioBtnPlaceSpec.Bind(wx.EVT_RADIOBUTTON, self.toggleSpecFolder)
		self.m_checkBoxTimestamp.Bind(wx.EVT_CHECKBOX, self.toggleTimestamp)
		self.m_buttonCancel.Bind(wx.EVT_BUTTON, self.cancelArchive)
		self.m_buttonArchive.Bind(wx.EVT_BUTTON, self.startArchive)
		self.m_dirPickerRestore.Bind(wx.EVT_DIRPICKER_CHANGED, self.startRefreshExtensionList)
		self.m_bpButton6.Bind(wx.EVT_BUTTON, self.startPopulateZipView)
		self.m_radioOriginalFolder1.Bind(wx.EVT_RADIOBUTTON, self.toggleSpecFolder)
		self.m_radioBtnPlaceSpec1.Bind(wx.EVT_RADIOBUTTON, self.toggleSpecFolder)
		self.m_checkBoxTimestamp1.Bind(wx.EVT_CHECKBOX, self.toggleTimestamp)
		self.m_buttonCancel1.Bind(wx.EVT_BUTTON, self.cancelArchive)
		self.m_buttonArchive1.Bind(wx.EVT_BUTTON, self.startArchive)

	def __del__(self):
		pass

	# Virtual event handlers, overide them in your derived class
	def loadJob(self, event):
		event.Skip()

	def saveJob(self, event):
		event.Skip()

	def exit(self, event):
		event.Skip()

	def startRefreshExtensionList(self, event):
		event.Skip()

	def RemIgnoreExtension(self, event):
		event.Skip()

	def addIgnoreExtension(self, event):
		event.Skip()

	def toggleSpecFolder(self, event):
		event.Skip()

	def toggleTimestamp(self, event):
		event.Skip()

	def cancelArchive(self, event):
		event.Skip()

	def startArchive(self, event):
		event.Skip()

	def startPopulateZipView(self, event):
		event.Skip()







