import os
import app
import item
import snd
import chat
import net
import locale
import time
import ui
import wndMgr

class PickUP(ui.ScriptWindow):

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadMainForm()
	
	def __del__(self):
		ui.ScriptWindow.__del__(self)
		
	def LoadMainForm(self):
		self.Board = ui.BoardWithTitleBar()
		self.Board.SetSize(220, 120)
		self.Board.SetPosition(120,90)
		self.Board.AddFlag("movable")
		self.Board.AddFlag("float")
		self.Board.SetTitleName("Black Bulls GANG")
		self.Board.SetCloseEvent(self.Board.Hide)
		self.Board.Show()
		
		self.Text1 = ui.TextLine()
		self.Text1.SetParent(self.Board)
		self.Text1.SetPosition(10, 35)
		self.Text1.SetText("Eternal 1337 by dhanax26")
		self.Text1.Show()
		
		self.Text2 = ui.TextLine()
		self.Text2.SetParent(self.Board)
		self.Text2.SetPosition(10, 55)
		self.Text2.SetText("Discord: dhanax26")
		self.Text2.Show()
		
		self.Text3 = ui.TextLine()
		self.Text3.SetParent(self.Board)
		self.Text3.SetPosition(10, 75)
		self.Text3.SetText("Prontamente Auto svside Captcha y Mazmorras Automaticas!")
		self.Text3.Show()
		
StartDialog = PickUP()
StartDialog.Board.Show()