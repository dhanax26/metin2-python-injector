import chat
import time
import ui
import event
import net
import chat
import game
class Botdialog(ui.BoardWithTitleBar):

	def __init__(self):
		ui.BoardWithTitleBar.__init__(self)
		self.LoadBoard()

	def LoadBoard(self):
		self.SetCenterPosition()
		self.SetSize(150,110)
		self.Show()
		self.AddFlag("movable")
		self.SetTitleName('Biologo Bot')
		self.SetCloseEvent(self.Close)
		self.comp = Component()
		self.txtcredit = self.comp.TextLine(self, '', 50, 80, self.comp.RGB(255, 0, 128))
		self.LoadButton2()
		self.LoadButton()
	def LoadButton(self):
		self.BuffBotStartButton = ui.Button()
		self.BuffBotStartButton.SetParent(self)
		self.BuffBotStartButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.BuffBotStartButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.BuffBotStartButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.BuffBotStartButton.SetText("ENTREGAR")
		self.BuffBotStartButton.SetPosition(30, 30)
		self.BuffBotStartButton.SetEvent(ui.__mem_func__(self.StartBuffbot))
		self.BuffBotStartButton.Show()
	def LoadButton2(self):
		self.BuffBotStopButton = ui.Button()
		self.BuffBotStopButton.SetParent(self)
		self.BuffBotStopButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.BuffBotStopButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.BuffBotStopButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.BuffBotStopButton.SetText("PARAR BOT")
		self.BuffBotStopButton.SetPosition(30, 55)
		self.BuffBotStopButton.SetEvent(ui.__mem_func__(self.StopBuffbot))
		self.BuffBotStopButton.Show()
	def __del__(self):
		ui.BoardWithTitleBar.__del__(self)

	def Show(self):
		ui.BoardWithTitleBar.Show(self)

	def Close(self):
		self.Hide()
	def StartBuffbot(self):
		self.estado=self.comp.TextLine(self, 'ON', 120, 35, self.comp.RGB(36, 231, 17))
		net.SendChatPacket("/bio")
		self.esperar = WaitingDialog()
		self.esperar.Open(int(30))
		self.esperar.SAFE_SetTimeOverEvent(self.StartBuffbot)
	def StopBuffbot(self):
		self.estado=self.comp.TextLine(self, 'OFF', 120, 35, self.comp.RGB(232, 28, 8))
		self.esperar = WaitingDialog()
		self.esperar.Open(int(0x47BF19673DF52E37F2410011D0FFFFFFFFFFFL))
		self.esperar.SAFE_SetTimeOverEvent(self.StartBuffbot)
	def InstallQuestWindowHook(self):
		self.OldRecv = game.GameWindow.OpenQuestWindow
		game.GameWindow.OpenQuestWindow = self.HookedQuestWindow
	def HookedQuestWindow(self, skin, idx):
		pass
class WaitingDialog(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.eventTimeOver = lambda *arg: None
		self.eventExit = lambda *arg: None

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Open(self, waitTime):
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
		lastTime = max(0, self.endTime - time.clock())
		if 0 == lastTime:
			self.Close()
			self.eventTimeOver()
		else:
			return
class Component:

    def Button(self, parent, buttonName, tooltipText, x, y, func, UpVisual, OverVisual, DownVisual):
        button = ui.Button()
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
        SlotBar.SetParent(parent)
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(5, 1)
        Value.SetMax(max)
        Value.SetText(editlineText)
        Value.Show()
        return (SlotBar, Value)


    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        textline.SetParent(parent)
        textline.SetPosition(x, y)
        if color != None:
            textline.SetFontColor(color[0], color[1], color[2])

        textline.SetText(textlineText)
        textline.Show()
        return textline


    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)


    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider


    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image


    def ComboBox(self, parent, text, x, y, width):
        combo = ui.ComboBox()
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
StartDialog = Botdialog()
StartDialog.Show()