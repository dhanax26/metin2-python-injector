import wndMgr
import locale
import app
import ui
import player
import chr
import chat
import chrmgr
import time
import skill
import nonplayer
import net
import snd
import item
import math
import miniMap
import uiminimap
import background
import exception
import uiCommon
import grp
import os
import shop
import ServerInfo
import game
import chat
import thread


class SelectModDialog(ui.ThinBoard):
	MOD_LIST = ("Biologo Automatico",
	            "Rotador De Equipo",
				"Mini Level Bot",
				"General",
				"Recoger Rapido",
				"Levelbot",
				"MultiHack2",
				"Fish Bot",
				"Detector GM Avanzado",
				"Información",
	            "Exit",)

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.__Load_ModDialog()
		
	def __del__(self):
		ui.ThinBoard.__del__(self)

	def Destroy(self):
		self.Hide()
		return TRUE
		
		
	def __Load_ModDialog(self):
		self.SetPosition(wndMgr.GetScreenWidth() - 120, wndMgr.GetScreenHeight() - 410)
		self.AddFlag("movable")
		self.SetSize(109, 400)
		self.Show()
		
		self.LoadTextLines()
		self.LoadButtons()
		
	def LoadButtons(self):	
		self.ModList = []

		x = 10
		i = 0
		y = 40
		for Modname in self.MOD_LIST:
			SelectModButton = ui.Button()
			SelectModButton.SetParent(self)
			SelectModButton.SetPosition(x, y)
			SelectModButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
			SelectModButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
			SelectModButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
			SelectModButton.SetText(Modname)
			SelectModButton.Show()

			Mod = self.MOD_LIST[i]
			SelectModButton.SetEvent(lambda arg = Mod: self.SelectMod(arg))
			SelectModButton.SetEvent(lambda arg = Mod: self.SelectMod(arg))
			self.ModList.append(SelectModButton)
			x += 0
			y += 24
			i += 1
		
		self.CloseButton = ui.Button()
		self.CloseButton.SetParent(self)
		self.CloseButton.SetPosition(89, 4)
		self.CloseButton.SetUpVisual("d:/ymir work/ui/public/close_button_01.sub")
		self.CloseButton.SetOverVisual("d:/ymir work/ui/public/close_button_02.sub")
		self.CloseButton.SetDownVisual("d:/ymir work/ui/public/close_button_03.sub")
		self.CloseButton.SetToolTipText(locale.UI_CLOSE, 0, - 23)
		self.CloseButton.SetEvent(ui.__mem_func__(self.Close))
		self.CloseButton.Show()
		
	def LoadTextLines(self):
		self.WhisperSpamTitle = ui.TextLine()
		self.WhisperSpamTitle.SetParent(self)
		self.WhisperSpamTitle.SetPosition(25, 15)
		self.WhisperSpamTitle.SetFeather()
		self.WhisperSpamTitle.SetDefaultFontName()
		self.WhisperSpamTitle.SetText("ClientMod")
		self.WhisperSpamTitle.SetFontColor(0.6, 0.7, 1.0)
		self.WhisperSpamTitle.SetOutline()
		self.WhisperSpamTitle.Show()	
	
	def SelectMod(self, mod):	
		if str(mod) == "Biologo Automatico":
			execfile('TooLHack/Hack/autoattack.py',{})

		elif str(mod) == "Rotador De Equipo":
			execfile('TooLHack/Hack/fragmente.py',{})
			
		elif str(mod) == "Mini Level Bot":
			execfile('TooLHack/Hack/Kickhack.py',{})
			
		elif str(mod) == "General":
			execfile('TooLHack/Hack/General.py',{})
			
		elif str(mod) == "Recoger Rapido":
			execfile('TooLHack/Hack/pickup.py',{})

		elif str(mod) == "Levelbot":
			execfile('TooLHack/Hack/Levelbot.py',{})
			
		elif str(mod) == "MultiHack2":
			execfile('TooLHack/Hack/botBuff.py',{})

		elif str(mod) == "Fish Bot":
			execfile('TooLHack/Hack/buybot.py',{})

		elif str(mod) == "Detector GM Avanzado":
			execfile('TooLHack/Hack/gmdetector.py',{})
			
		elif str(mod) == "Información":
			execfile('TooLHack/Hack/credit.py',{})
			
		elif str(mod) == "Exit":
			execfile('TooLHack/Hack/exitclient.py',{})

	def Show(self):
		ui.ThinBoard.Show(self)
		
	def Close(self):
		self.Hide()
		return TRUE

class ShowMod(ui.ThinBoard):

	def __init__(self):
		ui.ThinBoard.__init__(self)
		self.LoadBoard2()

	def LoadBoard2(self):
		self.SetPosition(wndMgr.GetScreenWidth() - 120, wndMgr.GetScreenHeight() - 440)
		self.SetSize(109, 24)
		self.Show()
		self.AddFlag("float")
		self.load = ui.Button()
		self.load.SetParent(self)
		self.load.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.load.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.load.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.load.SetText("Start")
		self.load.SetPosition(10, 6)
		self.load.SetEvent(ui.__mem_func__(self.shower))
		self.load.Show()

	def shower(self):
	  self.dialstarter=SelectModDialog()
	  self.dialstarter.Show()
	  
StartDialog = ShowMod()
StartDialog.Show()