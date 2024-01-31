import ui
import dbg
import app
import chr
import chat
import net

action = 0

class detector(ui.Window):
	def __init__(self):
		ui.Window.__init__(self)
		self.BuildWindow()

	def __del__(self):
		ui.Window.__del__(self)

	def BuildWindow(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(191, 141)
		self.Board.SetPosition(120, 90)
		self.Board.AddFlag('movable')
		self.Board.AddFlag('float')
		self.Board.SetTitleName('GM Detector')
		self.Board.SetCloseEvent(self.Close)
		self.Board.Show()
		self.__BuildKeyDict()
		self.comp = Component()

		self.logout = self.comp.Button(self.Board, 'Logout', '', 115, 73, self.logout_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
		self.exit = self.comp.Button(self.Board, 'Exit', '', 17, 73, self.exit_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
		self.Start = self.comp.Button(self.Board, 'Start', '', 17, 98, self.Start_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.Stop = self.comp.Button(self.Board, 'Stop', '', 132, 97, self.Stop_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
		self.slotbar_delay, self.delay = self.comp.EditLine(self.Board, '1', 103, 34, 25, 15, 3)
		self.Delaytxt = self.comp.TextLine(self.Board, 'Delay:', 55, 34, self.comp.RGB(255, 255, 255))
		self.iftxt = self.comp.TextLine(self.Board, 'Elija la función deseada:', 51, 55, self.comp.RGB(255, 255, 255))
		self.by = self.comp.TextLine(self.Board, 'Eternal 1337 by dhanax26', 70, 102, self.comp.RGB(650, 244, 246))
	
	def logout_func(self):
		global action
		action = 2
		chat.AppendChat(chat.CHAT_TYPE_INFO, "¡La función LogOut está arreglada para la próxima actualización!")
	
	def exit_func(self):
		global action
		action = 1
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "¡Cuando aparezca GM, el cliente se cerrará!")
	
	def Stop_func(self):
		self.gm = WaitingDialog()
		self.gm.Open(int(9999999999999999999999999))
		self.gm.SAFE_SetTimeOverEvent(self.Stop_func)
	
	def Start_func(self):
		self.gm = WaitingDialog()
		self.gm.Open(int(self.delay.GetText()))
		self.gm.SAFE_SetTimeOverEvent(self.Start_func)
		global action
		for vid in xrange(1, 100000):
			vid2 = chr.GetInstanceType(vid)
			if vid2 == chr.INSTANCE_TYPE_PLAYER and chr.GetNameByVID(vid) != "None" and (chr.IsGameMaster(vid) or chr.GetNameByVID(vid)[0] == "(" or chr.GetNameByVID(vid)[0] == "["):
					chat.AppendChat(chat.CHAT_TYPE_INFO, str(chr.GetNameByVID(vid)) + " apareció cerca !!!")
					if action == 1:
						chat.AppendChat(chat.CHAT_TYPE_INFO, str(chr.GetNameByVID(vid)) + " apareció cerca !!!!!!")
						app.Exit()
	
	def __BuildKeyDict(self):
		onPressKeyDict = {}
		onPressKeyDict[app.DIK_F5]	= lambda : self.OpenWindow()
		self.onPressKeyDict = onPressKeyDict
	
	def OnKeyDown(self, key):
		try:
			self.onPressKeyDict[key]()
		except KeyError:
			pass
		except:
			raise
		return TRUE
	
	def OpenWindow(self):
		if self.Board.IsShow():
			self.Board.Hide()
		else:
			self.Board.Show()
	
	def Close(self):
		self.Board.Hide()

class Component:
	def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
		button = ui.Button()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetEvent(func)
		return button

	def ToggleButton(self, parent, buttonName, tooltipText, x, y, funcUp, funcDown, UpVisual, OverVisual, DownVisual):
		button = ui.ToggleButton()
		if parent != None:
			button.SetParent(parent)
		button.SetPosition(x, y)
		button.SetUpVisual(UpVisual)
		button.SetOverVisual(OverVisual)
		button.SetDownVisual(DownVisual)
		button.SetText(buttonName)
		button.SetToolTipText(tooltipText)
		button.Show()
		button.SetToggleUpEvent(funcUp)
		button.SetToggleDownEvent(funcDown)
		return button

	def EditLine(self, parent, editlineText, x, y, width, heigh, max):
		SlotBar = ui.SlotBar()
		if parent != None:
			SlotBar.SetParent(parent)
		SlotBar.SetSize(width, heigh)
		SlotBar.SetPosition(x, y)
		SlotBar.Show()
		Value = ui.EditLine()
		Value.SetParent(SlotBar)
		Value.SetSize(width, heigh)
		Value.SetPosition(1, 1)
		Value.SetMax(max)
		Value.SetLimitWidth(width)
		Value.SetMultiLine()
		Value.SetText(editlineText)
		Value.Show()
		return SlotBar, Value

	def TextLine(self, parent, textlineText, x, y, color):
		textline = ui.TextLine()
		if parent != None:
			textline.SetParent(parent)
		textline.SetPosition(x, y)
		if color != None:
			textline.SetFontColor(color[0], color[1], color[2])
		textline.SetText(textlineText)
		textline.Show()
		return textline

	def RGB(self, r, g, b):
		return (r*255, g*255, b*255)

	def SliderBar(self, parent, sliderPos, func, x, y):
		Slider = ui.SliderBar()
		if parent != None:
			Slider.SetParent(parent)
		Slider.SetPosition(x, y)
		Slider.SetSliderPos(sliderPos / 100)
		Slider.Show()
		Slider.SetEvent(func)
		return Slider

	def ExpandedImage(self, parent, x, y, img):
		image = ui.ExpandedImageBox()
		if parent != None:
			image.SetParent(parent)
		image.SetPosition(x, y)
		image.LoadImage(img)
		image.Show()
		return image

	def ComboBox(self, parent, text, x, y, width):
		combo = ui.ComboBox()
		if parent != None:
			combo.SetParent(parent)
		combo.SetPosition(x, y)
		combo.SetSize(width, 15)
		combo.SetCurrentItem(text)
		combo.Show()
		return combo

	def ThinBoard(self, parent, moveable, x, y, width, heigh, center):
		thin = ui.ThinBoard()
		if parent != None:
			thin.SetParent(parent)
		if moveable == TRUE:
			thin.AddFlag('movable')
			thin.AddFlag('float')
		thin.SetSize(width, heigh)
		thin.SetPosition(x, y)
		if center == TRUE:
			thin.SetCenterPosition()
		thin.Show()
		return thin

	def Gauge(self, parent, width, color, x, y):
		gauge = ui.Gauge()
		if parent != None:
			gauge.SetParent(parent)
		gauge.SetPosition(x, y)
		gauge.MakeGauge(width, color)
		gauge.Show()
		return gauge

	def ListBoxEx(self, parent, x, y, width, heigh):
		bar = ui.Bar()
		if parent != None:
			bar.SetParent(parent)
		bar.SetPosition(x, y)
		bar.SetSize(width, heigh)
		bar.SetColor(0x77000000)
		bar.Show()
		ListBox=ui.ListBoxEx()
		ListBox.SetParent(bar)
		ListBox.SetPosition(0, 0)
		ListBox.SetSize(width, heigh)
		ListBox.Show()
		scroll = ui.ScrollBar()
		scroll.SetParent(ListBox)
		scroll.SetPosition(width-15, 0)
		scroll.SetScrollBarSize(heigh)
		scroll.Show()
		ListBox.SetScrollBar(scroll)
		return bar, ListBox

class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
		import time
		curTime = time.clock()
		self.endTime = curTime + waitTime

		self.Show()		

	def Close(self):
		self.Hide()

	def Destroy(self):
		self.Hide()

	def SAFE_SetTimeOverEvent(self, event):
		self.eventTimeOver = ui.__mem_func__(event)

	def SAFE_SetExitEvent(self, event):
		self.eventExit = ui.__mem_func__(event)
		
	def OnUpdate(self):
		import time
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
		
	def OnPressExitKey(self):
		self.Close()
		return TRUE
	
		
detector().Show()
