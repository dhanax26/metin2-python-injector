import os
import app
import dbg
import grp
import item
import background
import chr
import chrmgr
import player
import chat
import textTail
import snd
import net
import effect
import wndMgr
import fly
import systemSetting
import quest
import guild
import skill
import messenger
import locale
import constInfo
import exchange
import time
import ui
import interfacemodule
import shop
import uiTip
import pack
import uiCommon

Board1Button = ui.Button()
Board1Line = ui.TextLine()

Refine = 0
MoveSpeed = 0
Combo = 0	
ZoomHack = 0
NoFog = 0
DayNight = 0
EnableSnow = 0

TransferMobs = ""

AttackSpeedHack = ""
MoveSpeedHack = ""

TapferkeitsUmhange = ""

AutoRedPot = 0
AutoBluePot = 0
AutoAttack = 0
AutoPickup = 0
AutoRestart = 0

cRe35Efsun0 = 0
cRe35Efsun1 = 0
cRe35Efsun2 = 0
cRe35Efsun3 = 0
cRe35Efsun4 = 0
EfsunSButonIrcRest = 0	
ENesneKoduIrcRest = 71084
cRe35Bot0 = 0
cRe35Bot1 = 0
cRe35Bot2 = 0
cRe35Bot3 = 0
cRe35Bot4 = 0

AutoPottRed = ""
AutoPottBlue = ""
cRe35TURKMMO = ""
x0 = ""
y0 = ""
z0 = ""
x1 = ""
y1 = ""
x2 = ""
y2 = ""
radius = ""
TapferkeitsUmhange = ""
AutoPickUp = ""
AttackSpeedHack = ""
MoveSpeedHack = ""
telestep = 0
teleport_mode = 0
last_teleport_time = 0
DoublePrevent = "inaktiv"
RestartBot = ""

spamming = 0
Modo = 1
SpambotButton = ui.Button()
SpambotLine = ui.TextLine()
ShortButton = ui.Button()
ShortLine = ui.TextLine()


WHISPER_TYPE = ""
WhisperCount = 0
WhisperColour = ""
WhisperDelay = 0
WhisperAmount = 0
WhisperActivity = ""
ScanStart = 0
ScanEnd = 0

CHAT_TYPE = ""
Count = 0
ChatColour = ""
Delay = 0
Amount = 0
Activity = "Pause"

Bonus0 = 0
Bonus1 = 0
Bonus2 = 0
Bonus3 = 0
Bonus4 = 0
SwitchButton = 0	
Boniswitchvalue = 71084
PRESSWISH0 = 0
PRESSWISH1 = 0
PRESSWISH2 = 0
PRESSWISH3 = 0
PRESSWISH4 = 0

class FishingBot(ui.ScriptWindow):
	Gui = []
	state = "Stop"
	KillFishList = []
	TrashList = []
	Config = (2.5, 1.0)
	UseSmallFishAsBait = 0
	
	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.AddGui()
		
	def __del__(self):
		self.Gui[0].Hide()
		ui.ScriptWindow.__del__(self)

	def GuiParser(self, guiobjects, list):
		for object in guiobjects:
			Object = object[0][0]()
			if object[0][1] != "":
				Object.SetParent(list[object[0][1]])			
			if object[1][0] + object[1][1] != 0:
				Object.SetSize(object[1][0], object[1][1])
			if object[2][0] + object[2][1] != 0:
				Object.SetPosition(object[2][0], object[2][1])				
			for command in object[3]:
				cmd = command[0]
				attr = getattr(Object,cmd)			
				if callable(attr):
					argument = command[1]
					lenght = len(argument)
					if lenght == 1:
						if argument[0] == "":
							attr()
						else:
							attr(argument[0])
					elif lenght == 2:
						attr(argument[0], argument[1])
					elif lenght == 3:
						attr(argument[0], argument[1], argument[2])
					elif lenght == 4:
						attr(argument[0], argument[1], argument[2], argument[3])
			for flag in object[4]:
				Object.AddFlag(str(flag))
			Object.Show()	
			list.append(Object)
		
	def AddGui(self):
		Gui = [
			[[ui.ThinBoard, ""], [750, 330], [0,0], [["SetPosition", [0, 0]]], ["movable", "float"]],			
			[[ui.Button, 0], [0, 0], [720, 20], [['SetUpVisual', ["d:/ymir work/ui/public/close_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/close_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/close_button_03.sub"]], ['SetToolTipText', ["Cerrar", 0, - 23]], ['SetEvent', [lambda : self.__del__()]]], []],	
			[[ui.Button, 0], [0, 0], [475, 180], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Comenzar"]], ['SetEvent', [lambda : self.ChangeState("Start")]]], []],			
			[[ui.Button, 0], [0, 0], [580, 180], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["Parar"]], ['SetEvent', [lambda : self.ChangeState("|cFFFFCC00|H|h<Francoiz> Bot parado!.")]]], []],			
			[[ui.TextLine, 0], [0, 0], [320, 18], [["SetDefaultFontName", [""]],	["SetText", ["Bot de pesca - Multihack Francoiz"]],], []],			
			[[ui.TextLine, 0], [0, 0], [100, 40], [["SetDefaultFontName", [""]],	["SetText", ["Selecciones el pez que quiere matar luego de ser pescado"]],], []],			
			[[ui.TextLine, 0], [0, 0], [430, 70], [["SetDefaultFontName", [""]],	["SetText", ["Tiempo al pescar:"]],], []],			
			[[ui.SliderBar, 0], [0, 0], [505, 70], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.28]]], []],			
			[[ui.TextLine, 0], [0, 0], [690, 70], [["SetDefaultFontName", [""]],	["SetText", ["|cFFFFAA00|H|h2.5 s"]]], []],
			[[ui.TextLine, 0], [0, 0], [430, 100], [["SetDefaultFontName", [""]],	["SetText", ["Por cada pez:"]],], []],						
			[[ui.SliderBar, 0], [0, 0], [505, 100], [["SetEvent", [ui.__mem_func__(self.SetConfig)]], ["SetSliderPos", [0.5]]], []],			
			[[ui.TextLine, 0], [0, 0], [690, 100], [["SetDefaultFontName", [""]],	["SetText", ["|cFFFFAA00|H|h1.0 s"]]], []],			
			[[ui.TextLine, 0], [0, 0], [430, 135], [["SetDefaultFontName", [""]],	["SetText", ["Usar pez pequeño"]],], []],
            [[ui.TextLine, 0], [0, 0], [435, 220], [["SetDefaultFontName", [""]],	["SetText", ["Tiempo al pescar : 2.5 Segundos"]],], []],
            [[ui.TextLine, 0], [0, 0], [435, 245], [["SetDefaultFontName", [""]],	["SetText", ["Tiempo despues de cada pez : 1 Segundo"]],], []],
            [[ui.TextLine, 0], [0, 0], [535, 40], [["SetDefaultFontName", [""]],	["SetText", ["Menu de pesca"]],], []],
            [[ui.TextLine, 0], [0, 0], [560, 300], [["SetDefaultFontName", [""]],	["SetText", ["Bot de pesca - Multihack By Francoiz"]],], []],			
			]
		self.GuiParser(Gui, self.Gui)		
		self.fischies = []
		for i in xrange(27803, 27824):
			self.fischies.append(i)
		self.FishingItems = [27987, 70201, 70202, 70203, 70204, 70205, 70206, 70048, 70049, 70050, 70051]
		for bla in self.FishingItems:
			self.fischies.append(bla)
		tmp = []
		Modi = ["Si", "No"]		
		x = 585
		for mode in Modi:
			button = [[ui.Button, 0], [0, 0], [x, 130], [['SetUpVisual', ["d:/ymir work/ui/public/small_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/small_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/small_button_03.sub"]], ['SetText', [mode]], ['SetEvent', [lambda arg = (Modi.index(mode)): self.UseSmallFishes(arg)]]], []]
			tmp.append(button)
			x += 48		
		x = 40
		y = 70
		for fish in self.fischies:
			Index = self.fischies.index(fish)
			if IsDivideAble(Index, 4):
				x = 40
				y += 30
			ItemName = item.GetItemName(item.SelectItem(fish))
			ItemIcon = item.GetIconImageFileName()
			name = [[ui.Button, 0], [0, 0], [x - 15, y + 0], [['SetUpVisual', ["d:/ymir work/ui/public/large_button_01.sub"]],['SetOverVisual', ["d:/ymir work/ui/public/large_button_02.sub"]], ['SetDownVisual', ["d:/ymir work/ui/public/large_button_03.sub"]], ["SetText", ["|cFFFFAA00|H|h" + ItemName]], ['SetEvent', [lambda arg = (self.fischies.index(fish)): self.SelectFish(arg)]]], []]
			tmp.append(button)
			tmp.append(name)
			x += 100					
		self.GuiParser(tmp, self.Gui)
		
	def UseSmallFishes(self, mode):
		if mode == 1:
			self.UseSmallFishAsBait = 0
			chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Pez pequeño: Descativado")
		else:
			self.UseSmallFishAsBait = 1
			chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Pez pequeño: Activado")
			
	def SelectFish(self, fish):
		try:
			self.fischies.index(27803 + fish)
			try:
				self.KillFishList.remove(int(27803 + fish))
				chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> " + item.GetItemName(item.SelectItem(27803 + fish)) + " No matar al pescar")
			except:
				self.KillFishList.append(int(27803 + fish))
				chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> " + item.GetItemName(item.SelectItem(27803 + fish)) + " Matar al pescar")
		except:
			ItemName = item.GetItemName(item.SelectItem(self.FishingItems[fish-len(self.fischies)]))
			try:
				self.KillFishList.remove(self.FishingItems[fish-len(self.fischies)])
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					chat.AppendChat(1, "|cFFFFAA00|H|h<> " + ItemName + " ")
				else:
					self.TrashList.remove(self.FishingItems[fish-len(self.fischies)])
					chat.AppendChat(1, "|cFFFFAA00|H|h<> " + ItemName + " ")
			except:
				if ItemName == item.GetItemName(item.SelectItem(27987)):
					self.KillFishList.append(self.FishingItems[fish-len(self.fischies)])
					chat.AppendChat(1, "|cFFFFAA00|H|h<> " + ItemName + " ")
				else:
					self.TrashList.append(self.FishingItems[fish-len(self.fischies)])
					chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> " + ItemName + " Tirar al pescar")			

	def SetConfig(self):
		(Delay, Tolerance) = self.Config		
		if self.Gui[7].GetSliderPos() * 9 + 1 != Delay:
			Delay = self.Gui[7].GetSliderPos() * 9 + 1
			try:
				Tmp = str(Delay).split(".")
				Delay = str(Tmp[0]) + "." + Tmp[1][:1]
			except:
				pass
			self.Gui[8].SetText(str("|cFFFFAA00|H|h" + Delay) + " s")			
		if self.Gui[10].GetSliderPos() * 2 != Tolerance:
			Tolerance = self.Gui[10].GetSliderPos() * 2
			try:
				Tmp = str(Tolerance).split(".")
				Tolerance = str(Tmp[0]) + "." + Tmp[1][:1]
			except:
				pass
			self.Gui[11].SetText(str("|cFFFFAA00|H|h" + Tolerance) + " s")			
		self.Config = (Delay, Tolerance)
		
	def ChangeState(self, arg):
		chat.AppendChat(1, str(arg))
		self.state = arg
		if arg == "Start":
			if self.AddBait():
				self.ProcessTimeStamp = app.GetTime()
				self.FishAction()
				self.state = "Waiting"
		else:
			self.FishAction()
		
	def OnRender(self):
		if self.state == "Stop":
			return
		if self.state == "Start":
			if self.ProcessTimeStamp + 6.0 < app.GetTime():
				if self.AddBait():
					self.FishAction()
					self.ProcessTimeStamp = app.GetTime()
					self.state = "Waiting"
					chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Bot continua...")		
		if self.state == "Fish":
			if self.ProcessTimeStamp + float(self.Config[0]) < app.GetTime():
				self.FishAction()
				self.ProcessTimeStamp = app.GetTime()
				self.state = "Start"		
		if self.state == "Waiting":
			if not chrmgr.IsPossibleEmoticon(-1):
				chat.AppendChat(1, "|cFFFFAA00|H|hOltaya Birþey Takýldý... Belirlediðiniz Sürede Olta Çekilecek.")
				self.ProcessTimeStamp = app.GetTime() + float(self.RandomTolerance())
				self.state = "Fish"					
			if self.ProcessTimeStamp + 48.0 < app.GetTime():
				chat.AppendChat(1, "|cFFFFAA00|H|hFrancoiz")
				self.ProcessTimeStamp = app.GetTime()
				self.state = "Start"	
	
	def RandomTolerance(self):
		Tolerance = float(self.Config[1])*10
		Rnd = app.GetRandom(0, int(Tolerance))
		return DivideToFloat(Rnd, 10)
	
	def FishAction(self):
		player.SetAttackKeyState(TRUE)
		player.SetAttackKeyState(FALSE)
		
	def UseFishBait(self):
		return self.UseSmallFishAsBait
		
	def AddBait(self):
		#Balik Oldurme
		for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
			ItemValue = player.GetItemIndex(InventorySlot)
			try:
				self.KillFishList.index(ItemValue)
				net.SendItemUsePacket(InventorySlot)
			except:
				try:
					self.TrashList.index(ItemValue)
					net.SendItemDropPacketNew(InventorySlot, player.GetItemCount(InventorySlot))
				except:
					pass		
		#Kucuk Balik ilk yem yapma
		if self.UseFishBait():
			if player.GetItemCountByVnum(27802) > 0:
				for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
					ItemValue = player.GetItemIndex(InventorySlot)
					if ItemValue == 27802:
						net.SendItemUsePacket(InventorySlot)
						chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Yem Olarak Minik Balýk Kullanýldý..")
						return 1		
		#kücük balýk yoksa,diðer balýða geç
		#yem
		Baits = [27800, 27801]
		Baitcount = 0
		for bait in Baits:
			Baitcount += player.GetItemCountByVnum(bait)	
		if Baitcount <= 0:
			chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Necesita una caña para pescar!.")
			self.state = "Stop"
			return 0
		else:
			for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE*2):
				ItemValue = player.GetItemIndex(InventorySlot)
				try:
					Baits.index(ItemValue)
					net.SendItemUsePacket(InventorySlot)
					chat.AppendChat(1, "|cFFFFAA00|H|h<Francoiz> Bot comenzado.")
					return 1
				except:
					pass
		
def IsDivideAble(x, y):
	if x == 0:
		return
	if float(x/y) == DivideToFloat(x, y):
		return 1
		
def DivideToFloat(x, y):
    y = x * (y**-1)
    return y

FishingBot().Show()

class PickUP(ui.ScriptWindow):

	WHISPER_MODE = ( "Todos", "PJ", )
	COLOUR_MODE_NAME = ( "Normal", "Azul", "Verde", "Rojo", "Rosado", "Random", )
	COLOUR_MODE_INDEX = ( "|h|r",
						"|cFF0080FF|H|h",
						"|cFF00FF00|H|h",
						"|cFFFF0000|H|h", 
						"|cFFFF00FF|H|h",
						"Random", )
	ERROR_MESSAGE_INDEX = ( "El SpamBot ha sido activado",
						"Por favor escoja una forma.",
						"Por favor escoja un color.",
						"Por favor introduzca un texto.",
						"Por favor introduzca los segundos", 
						"Por favor introduzca una cantidad",
						"Por favor introduzca un nombre", )


	CHAT_MODE_NAME = ( locale.CHAT_NORMAL, locale.CHAT_PARTY, locale.CHAT_GUILD, locale.CHAT_SHOUT, "Random", )
	CHAT_MODE_INDEX = ( chat.CHAT_TYPE_TALKING,
						chat.CHAT_TYPE_PARTY,
						chat.CHAT_TYPE_GUILD,
						chat.CHAT_TYPE_SHOUT, 
						"Random", )
	COLOUR1_MODE_NAME = ( "Normal", "Azul", "Verde", "Rojo", "Rosado", "Random", )
	COLOUR1_MODE_INDEX = ( "|h|r",
						"|cFF0080FF|H|h",
						"|cFF00FF00|H|h",
						"|cFFFF0000|H|h", 
						"|cFFFF00FF|H|h",
						"Random", )
	ERROR1_MESSAGE_INDEX = ( "El SpamBot ha sido Activado.",
						"Por favor escoja una forma",
						"Por favor escoja un color.",
						"Por favor introduzca un texto",
						"Por favor introduzca los segundos.", 
						"Por favor introduzca una cantidad.",
						"Itroduzca un numero mayor a 15 segundos.", )
	

	def __init__(self):
		ui.ScriptWindow.__init__(self)
		self.LoadPick()
	
	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Bonuschangevalue(self):
		global Boniswitchvalue
		for i in xrange(player.INVENTORY_PAGE_SIZE*2):
			itemIndex = player.GetItemIndex(i)
			item.SelectItem(itemIndex)
			ItemValue = player.GetItemIndex(i)
			if item.IsAntiFlag(74112) and item.IsFlag(8196) and item.GetItemSubType() == 18:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Gegenstand verzaubern liegt auf Value: " + str(ItemValue))
				Boniswitchvalue = int(ItemValue)
				break
			elif str(item.GetItemName()) == "Gegenstand verzaubern":
				chat.AppendChat(chat.CHAT_TYPE_INFO, "Gegenstand verzaubern liegt auf Value: " + str(ItemValue))
				Boniswitchvalue = int(ItemValue)
				break

	def LoadPick(self):
	
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Multihack By Francoiz")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "youtube.com/user/xFrancoizx")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Contiene:")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Bot de leveo (By Francoiz")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Hacks de camara (By Francoiz)")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Otros hacks (By Francoiz)")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Teleporter hack (By Francoiz)")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "SpamBot (By Francoiz)")
		chat.AppendChat(chat.CHAT_TYPE_NOTICE, "Bot de pesca (Modificado por Francoiz)")
		chat.AppendChat(chat.CHAT_TYPE_INFO, "youtube.com/user/xFrancoizx")
             
		
		self.LoadMainForm()
		self.FaceButton()
		
	def LoadMainForm(self):
		#############################MainForm

		global OnOff1
		self.Board1 = ui.BoardWithTitleBar()
		self.Board1.SetSize(272, 400)
		self.Board1.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board1.AddFlag("movable")
		self.Board1.AddFlag("float")
		self.Board1.SetTitleName("Hack Francoiz")
		self.Board1.SetCloseEvent(self.Board1.Hide)
		self.Board1.Hide()
		#############################nterface
		self.Pick1Message = ui.TextLine()
		self.Pick1Message.SetParent(self.Board1)
		self.Pick1Message.SetPosition(67, 40)
		self.Pick1Message.SetText("Bot de leveo - By Francoiz")
		self.Pick1Message.SetFontColor(1.0, 0.8, 0)
		self.Pick1Message.Show()

		global OnOff2
		self.Board2 = ui.BoardWithTitleBar()
		self.Board2.SetSize(160, 250)
		self.Board2.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board2.AddFlag("movable")
		self.Board2.AddFlag("float")
		self.Board2.SetTitleName("Hack Francoiz")
		self.Board2.SetCloseEvent(self.Board2.Hide)
		self.Board2.Hide()
		#############################nterface
		self.Pick2Message = ui.TextLine()
		self.Pick2Message.SetParent(self.Board2)
		self.Pick2Message.SetPosition(20, 40)
		self.Pick2Message.SetText("Camara Hack - By Francoiz")
		self.Pick2Message.SetFontColor(1.0, 0.8, 0)
		self.Pick2Message.Show()

		global OnOff3
		self.Board3 = ui.BoardWithTitleBar()
		self.Board3.SetSize(300, 190)
		self.Board3.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board3.AddFlag("movable")
		self.Board3.AddFlag("float")
		self.Board3.SetTitleName("Hack Francoiz")
		self.Board3.SetCloseEvent(self.Board3.Hide)
		self.Board3.Hide()
		#############################nterface
		self.Pick3Message = ui.TextLine()
		self.Pick3Message.SetParent(self.Board3)
		self.Pick3Message.SetPosition(73, 40)
		self.Pick3Message.SetText("Velocidad Hack - By Francoiz")
		self.Pick3Message.SetFontColor(1.0, 0.8, 0)
		self.Pick3Message.Show()

		global OnOff4
		self.Board4 = ui.BoardWithTitleBar()
		self.Board4.SetSize(250, 400)
		self.Board4.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board4.AddFlag("movable")
		self.Board4.AddFlag("float")
		self.Board4.SetTitleName("Hack Francoiz")
		self.Board4.SetCloseEvent(self.Board4.Hide)
		self.Board4.Hide()
		#############################nterface
		self.Pick4Message = ui.TextLine()
		self.Pick4Message.SetParent(self.Board4)
		self.Pick4Message.SetPosition(67, 40)
		self.Pick4Message.SetText("Otros hacks - By Francoiz")
		self.Pick4Message.SetFontColor(1.0, 0.8, 0)
		self.Pick4Message.Show()


		global OnOff5
		self.Board5= ui.BoardWithTitleBar()
		self.Board5.SetSize(240, 135)
		self.Board5.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board5.AddFlag("movable")
		self.Board5.AddFlag("float")
		self.Board5.SetTitleName("Hack Francoiz")
		self.Board5.SetCloseEvent(self.Board5.Hide)
		self.Board5.Hide()
		#############################nterface
		self.Pick5Message = ui.TextLine()
		self.Pick5Message.SetParent(self.Board5)
		self.Pick5Message.SetPosition(67, 40)
		self.Pick5Message.SetText("Teleporter - By Francoiz")
		self.Pick5Message.SetFontColor(1.0, 0.8, 0)
		self.Pick5Message.Show()

		

		global OnOff7
		self.Board7 = ui.BoardWithTitleBar()
		self.Board7.SetSize(200, 220)
		self.Board7.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board7.AddFlag("movable")
		self.Board7.AddFlag("float")
		self.Board7.SetTitleName("Hack Francoiz")
		self.Board7.SetCloseEvent(self.Board7.Hide)
		self.Board7.Hide()
		#############################nterface
		self.Pick7Message = ui.TextLine()
		self.Pick7Message.SetParent(self.Board7)
		self.Pick7Message.SetPosition(50, 40)
		self.Pick7Message.SetText("Creditos - By Francoiz")
		self.Pick7Message.SetFontColor(1.0, 0.8, 0)
		self.Pick7Message.Show()

		global OnOff8
		self.Board8 = ui.BoardWithTitleBar()
		self.Board8.SetSize(390, 430)
		self.Board8.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board8.AddFlag("movable")
		self.Board8.AddFlag("float")
		self.Board8.SetTitleName("Hack Francoiz")
		self.Board8.SetCloseEvent(self.Board8.Hide)
		self.Board8.Hide()
		#############################nterface
		self.Pick8Message = ui.TextLine()
		self.Pick8Message.SetParent(self.Board8)
		self.Pick8Message.SetPosition(67, 40)
		self.Pick8Message.SetText("")
		self.Pick8Message.SetFontColor(1.0, 0.8, 0)
		self.Pick8Message.Show()


		global OnOff9
		self.Board9 = ui.BoardWithTitleBar()
		self.Board9.SetSize(390, 430)
		self.Board9.SetPosition(wndMgr.GetScreenWidth()-400,80)
		self.Board9.AddFlag("movable")
		self.Board9.AddFlag("float")
		self.Board9.SetTitleName("Hack Francoiz")
		self.Board9.SetCloseEvent(self.Board9.Hide)
		self.Board9.Hide()
		#############################nterface
		self.Pick9Message = ui.TextLine()
		self.Pick9Message.SetParent(self.Board9)
		self.Pick9Message.SetPosition(67, 40)
		self.Pick9Message.SetText("")
		self.Pick9Message.SetFontColor(1.0, 0.8, 0)
		self.Pick9Message.Show()



		self.MoveSpeedStatsSlotbar = ui.SlotBar()
		self.MoveSpeedStatsSlotbar.SetParent(self.Board3)
		self.MoveSpeedStatsSlotbar.SetSize(30, 18)
		self.MoveSpeedStatsSlotbar.SetPosition(10, 108)
		self.MoveSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
		self.MoveSpeedStatsSlotbar.Show()
		
		self.MoveSpeedStats = ui.EditLine()
		self.MoveSpeedStats.SetParent(self.MoveSpeedStatsSlotbar)
		self.MoveSpeedStats.SetSize(30, 17)
		self.MoveSpeedStats.SetPosition(10, 2)
		self.MoveSpeedStats.SetMax(4)
		self.MoveSpeedStats.SetNumberMode()
		self.MoveSpeedStats.SetFocus()
		self.MoveSpeedStats.SetText("100")
		#self.MoveSpeedStats.SetTabEvent(ui.__mem_func__(self.AttackSpeedStats.SetFocus))
		#self.MoveSpeedStats.SetReturnEvent(ui.__mem_func__(self.AttackSpeedStats.SetFocus))
		self.MoveSpeedStats.Show()

		self.AttackSpeedStatsSlotbar = ui.SlotBar()
		self.AttackSpeedStatsSlotbar.SetParent(self.Board3)
		self.AttackSpeedStatsSlotbar.SetSize(30, 18)
		self.AttackSpeedStatsSlotbar.SetPosition(10, 78)
		self.AttackSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
		self.AttackSpeedStatsSlotbar.Show()
		
		self.AttackSpeedStats = ui.EditLine()
		self.AttackSpeedStats.SetParent(self.AttackSpeedStatsSlotbar)
		self.AttackSpeedStats.SetSize(30, 17)
		self.AttackSpeedStats.SetPosition(10, 2)
		self.AttackSpeedStats.SetMax(4)
		self.AttackSpeedStats.SetNumberMode()
		self.AttackSpeedStats.SetFocus()
		self.AttackSpeedStats.SetText("100")
		self.AttackSpeedStats.SetTabEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		self.AttackSpeedStats.SetReturnEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
		self.AttackSpeedStats.Show()

		self.AutoRedPotLabel = ui.TextLine()	
		self.AutoRedPotLabel.SetParent(self.Board1)
		self.AutoRedPotLabel.SetDefaultFontName()
		self.AutoRedPotLabel.SetPosition(-120, 100)
		self.AutoRedPotLabel.SetFeather()
		self.AutoRedPotLabel.SetWindowHorizontalAlignCenter()
		self.AutoRedPotLabel.SetText("PotasRojas:")
		self.AutoRedPotLabel.SetFontColor(35.0, 0.0, 0.0)
		self.AutoRedPotLabel.SetOutline()
		self.AutoRedPotLabel.Show()	
		
		self.RedPotPercentLabel = ui.TextLine()	
		self.RedPotPercentLabel.SetParent(self.Board1)
		self.RedPotPercentLabel.SetDefaultFontName()
		self.RedPotPercentLabel.SetPosition(-22, 99)
		self.RedPotPercentLabel.SetFeather()
		self.RedPotPercentLabel.SetWindowHorizontalAlignCenter()
		self.RedPotPercentLabel.SetText("%")
		self.RedPotPercentLabel.SetFontColor(35.0, 0.0, 0.0)
		self.RedPotPercentLabel.SetOutline()
		self.RedPotPercentLabel.Show()

		self.SlotBarRedPotting = ui.SlotBar()
		self.SlotBarRedPotting.SetParent(self.Board1)
		self.SlotBarRedPotting.SetSize(30, 18)
		self.SlotBarRedPotting.SetPosition(-42, 98)
		self.SlotBarRedPotting.SetWindowHorizontalAlignCenter()
		self.SlotBarRedPotting.Show()
		
		self.EditLineRedPotting = ui.EditLine()
		self.EditLineRedPotting.SetParent(self.SlotBarRedPotting)
		self.EditLineRedPotting.SetSize(30, 17)
		self.EditLineRedPotting.SetPosition(8, 2)
		self.EditLineRedPotting.SetMax(2)
		self.EditLineRedPotting.SetNumberMode()
		self.EditLineRedPotting.SetText("90")
		self.EditLineRedPotting.SetFocus()
		self.EditLineRedPotting.Show()	

		self.AutoBluePotLabel = ui.TextLine()	
		self.AutoBluePotLabel.SetParent(self.Board1)
		self.AutoBluePotLabel.SetDefaultFontName()
		self.AutoBluePotLabel.SetPosition(-120, 130)
		self.AutoBluePotLabel.SetFeather()
		self.AutoBluePotLabel.SetWindowHorizontalAlignCenter()
		self.AutoBluePotLabel.SetText("PotasAzules:")
		self.AutoBluePotLabel.SetFontColor(0.0, 0.0, 1.0)
		self.AutoBluePotLabel.SetOutline()
		self.AutoBluePotLabel.Show()	
		
		self.BluePotPercentLabel = ui.TextLine()	
		self.BluePotPercentLabel.SetParent(self.Board1)
		self.BluePotPercentLabel.SetDefaultFontName()
		self.BluePotPercentLabel.SetPosition(-22, 130)
		self.BluePotPercentLabel.SetFeather()
		self.BluePotPercentLabel.SetWindowHorizontalAlignCenter()
		self.BluePotPercentLabel.SetText("%")
		self.BluePotPercentLabel.SetFontColor(0.0, 0.0, 1.0)
		self.BluePotPercentLabel.SetOutline()
		self.BluePotPercentLabel.Show()	

		self.SlotBarBluePotting = ui.SlotBar()
		self.SlotBarBluePotting.SetParent(self.Board1)
		self.SlotBarBluePotting.SetSize(30, 18)
		self.SlotBarBluePotting.SetPosition(-42, 128)
		self.SlotBarBluePotting.SetWindowHorizontalAlignCenter()
		self.SlotBarBluePotting.Show()
		
		self.EditLineBluePotting = ui.EditLine()
		self.EditLineBluePotting.SetParent(self.SlotBarBluePotting)
		self.EditLineBluePotting.SetSize(30, 17)
		self.EditLineBluePotting.SetPosition(8, 2)
		self.EditLineBluePotting.SetMax(2)
		self.EditLineBluePotting.SetNumberMode()
		self.EditLineBluePotting.SetText("40")
		self.EditLineBluePotting.SetFocus()
		self.EditLineBluePotting.Show()

		self.AutoAttackLabel = ui.TextLine()	
		self.AutoAttackLabel.SetParent(self.Board1)
		self.AutoAttackLabel.SetDefaultFontName()
		self.AutoAttackLabel.SetPosition(-120, 160)
		self.AutoAttackLabel.SetFeather()
		self.AutoAttackLabel.SetWindowHorizontalAlignCenter()
		self.AutoAttackLabel.SetText("Leveo:")
	#	self.AutoAttackLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoAttackLabel.SetOutline()
		self.AutoAttackLabel.Show()
		
		self.AutoPickLabel = ui.TextLine()	
		self.AutoPickLabel.SetParent(self.Board1)
		self.AutoPickLabel.SetDefaultFontName()
		self.AutoPickLabel.SetPosition(-122, 190)
		self.AutoPickLabel.SetFeather()
		self.AutoPickLabel.SetWindowHorizontalAlignCenter()
		self.AutoPickLabel.SetText("Auto-Agarre:")
	#	self.AutoPickLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoPickLabel.SetOutline()
		self.AutoPickLabel.Show()
		
		self.AutoRestartLabel = ui.TextLine()	
		self.AutoRestartLabel.SetParent(self.Board1)
		self.AutoRestartLabel.SetDefaultFontName()
		self.AutoRestartLabel.SetPosition(-120, 220)
		self.AutoRestartLabel.SetFeather()
		self.AutoRestartLabel.SetWindowHorizontalAlignCenter()
		self.AutoRestartLabel.SetText("Revive aqui:")
	#	self.AutoRestartLabel.SetFontColor(1.0, 0.8, 0)
		self.AutoRestartLabel.SetOutline()
		self.AutoRestartLabel.Show()

		self.ZoomHackLabel = ui.TextLine()
		self.ZoomHackLabel.SetParent(self.Board2)
		self.ZoomHackLabel.SetDefaultFontName()
		self.ZoomHackLabel.SetPosition(-60, 70)
		self.ZoomHackLabel.SetFeather()
		self.ZoomHackLabel.SetWindowHorizontalAlignCenter()
		self.ZoomHackLabel.SetText("Alejar Hack:")
	#	self.ZoomHackLabel.SetFontColor(1.0, 0.8, 0)
		self.ZoomHackLabel.SetOutline()
		self.ZoomHackLabel.Show()	
		
		self.NoFogLabel = ui.TextLine()
		self.NoFogLabel.SetParent(self.Board2)
		self.NoFogLabel.SetDefaultFontName()
		self.NoFogLabel.SetPosition(-60, 100)
		self.NoFogLabel.SetFeather()
		self.NoFogLabel.SetWindowHorizontalAlignCenter()
		self.NoFogLabel.SetText("Sin Niebla:")
	#	self.NoFogLabel.SetFontColor(1.0, 0.8, 0)
		self.NoFogLabel.SetOutline()
		self.NoFogLabel.Show()	

		self.DayNightLabel = ui.TextLine()
		self.DayNightLabel.SetParent(self.Board2)
		self.DayNightLabel.SetDefaultFontName()
		self.DayNightLabel.SetPosition(-60, 130)
		self.DayNightLabel.SetFeather()
		self.DayNightLabel.SetWindowHorizontalAlignCenter()
		self.DayNightLabel.SetText("Dia/Noche:")
	#	self.DayNightLabel.SetFontColor(1.0, 0.8, 0)
		self.DayNightLabel.SetOutline()
		self.DayNightLabel.Show()	
		
		self.SnowLabel = ui.TextLine()
		self.SnowLabel.SetParent(self.Board2)
		self.SnowLabel.SetDefaultFontName()
		self.SnowLabel.SetPosition(-60, 160)
		self.SnowLabel.SetFeather()
		self.SnowLabel.SetWindowHorizontalAlignCenter()
		self.SnowLabel.SetText("Nieve:")
	#	self.SnowLabel.SetFontColor(1.0, 0.8, 0)
		self.SnowLabel.SetOutline()
		self.SnowLabel.Show()

		self.AttackSpeedHackHeadline = ui.TextLine()
		self.AttackSpeedHackHeadline.SetParent(self.Board3)
		self.AttackSpeedHackHeadline.SetDefaultFontName()
		self.AttackSpeedHackHeadline.SetPosition(15, 80)
		self.AttackSpeedHackHeadline.SetFeather()
		self.AttackSpeedHackHeadline.SetText("Velocidad de ataque:")
		self.AttackSpeedHackHeadline.SetOutline()
		self.AttackSpeedHackHeadline.Show()

		self.MoveSpeedHackHeadline = ui.TextLine()
		self.MoveSpeedHackHeadline.SetParent(self.Board3)
		self.MoveSpeedHackHeadline.SetDefaultFontName()
		self.MoveSpeedHackHeadline.SetPosition(15, 110)
		self.MoveSpeedHackHeadline.SetFeather()
		self.MoveSpeedHackHeadline.SetText("Velocidad de movimiento:")
		self.MoveSpeedHackHeadline.SetOutline()
		self.MoveSpeedHackHeadline.Show()

		self.CabosLabel = ui.TextLine()
		self.CabosLabel.SetParent(self.Board1)
		self.CabosLabel.SetDefaultFontName()
		self.CabosLabel.SetPosition(-120, 258)
		self.CabosLabel.SetFeather()
		self.CabosLabel.SetWindowHorizontalAlignCenter()
		self.CabosLabel.SetText("Hack de cabos:")
		self.CabosLabel.SetOutline()
		self.CabosLabel.Show()

		self.CabosSegLabel = ui.TextLine()
		self.CabosSegLabel.SetParent(self.Board1)
		self.CabosSegLabel.SetDefaultFontName()
		self.CabosSegLabel.SetPosition(-12, 258)
		self.CabosSegLabel.SetFeather()
		self.CabosSegLabel.SetWindowHorizontalAlignCenter()
		self.CabosSegLabel.SetText("Segs")
		self.CabosSegLabel.SetOutline()
		self.CabosSegLabel.Show()

		self.TapferkeitsUmhangeDelaySlotbar = ui.SlotBar()
		self.TapferkeitsUmhangeDelaySlotbar.SetParent(self.Board1)
		self.TapferkeitsUmhangeDelaySlotbar.SetSize(30, 18)
		self.TapferkeitsUmhangeDelaySlotbar.SetPosition(-30, 254)
		self.TapferkeitsUmhangeDelaySlotbar.SetWindowHorizontalAlignCenter()
		self.TapferkeitsUmhangeDelaySlotbar.Show()
		
		self.TapferkeitsUmhangeDelay = ui.EditLine()
		self.TapferkeitsUmhangeDelay.SetParent(self.TapferkeitsUmhangeDelaySlotbar)
		self.TapferkeitsUmhangeDelay.SetSize(30, 17)
		self.TapferkeitsUmhangeDelay.SetPosition(8, 2)
		self.TapferkeitsUmhangeDelay.SetMax(3)
		self.TapferkeitsUmhangeDelay.SetNumberMode()
		self.TapferkeitsUmhangeDelay.SetFocus()
		self.TapferkeitsUmhangeDelay.SetText("0")
		#self.TapferkeitsUmhangeDelay.SetTabEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		#self.TapferkeitsUmhangeDelay.SetReturnEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		self.TapferkeitsUmhangeDelay.Show()

		self.ComboLabel = ui.TextLine()
		self.ComboLabel.SetParent(self.Board4)
		self.ComboLabel.SetDefaultFontName()
		self.ComboLabel.SetPosition(-110, 130)
		self.ComboLabel.SetFeather()
		self.ComboLabel.SetWindowHorizontalAlignCenter()
		self.ComboLabel.SetText("Combo:")
		self.ComboLabel.SetOutline()
		self.ComboLabel.Show()

		self.FantasmaLabel = ui.TextLine()
		self.FantasmaLabel.SetParent(self.Board4)
		self.FantasmaLabel.SetDefaultFontName()
		self.FantasmaLabel.SetPosition(-110, 70)
		self.FantasmaLabel.SetFeather()
		self.FantasmaLabel.SetWindowHorizontalAlignCenter()
		self.FantasmaLabel.SetText("Modo Fantasma:")
		self.FantasmaLabel.SetOutline()
		self.FantasmaLabel.Show()

		self.HerreroLabel = ui.TextLine()
		self.HerreroLabel.SetParent(self.Board4)
		self.HerreroLabel.SetDefaultFontName()
		self.HerreroLabel.SetPosition(-110, 100)
		self.HerreroLabel.SetFeather()
		self.HerreroLabel.SetWindowHorizontalAlignCenter()
		self.HerreroLabel.SetText("Herrero:")
		self.HerreroLabel.SetOutline()
		self.HerreroLabel.Show()

		self.ArmaduraLabel = ui.TextLine()
		self.ArmaduraLabel.SetParent(self.Board4)
		self.ArmaduraLabel.SetDefaultFontName()
		self.ArmaduraLabel.SetPosition(50, 190)
		self.ArmaduraLabel.SetFeather()
		self.ArmaduraLabel.SetWindowHorizontalAlignCenter()
		self.ArmaduraLabel.SetText("Armadura")
		self.ArmaduraLabel.SetOutline()
		self.ArmaduraLabel.Show()

		self.ArmorSlotBar = ui.SlotBar()
		self.ArmorSlotBar.SetParent(self.Board4)
		self.ArmorSlotBar.SetSize(125, 18)
		self.ArmorSlotBar.SetPosition(-30, 190)
		self.ArmorSlotBar.SetWindowHorizontalAlignCenter()
		self.ArmorSlotBar.Show()
		
		self.ArmorEditLine = ui.EditLine()
		self.ArmorEditLine.SetParent(self.ArmorSlotBar)
		self.ArmorEditLine.SetSize(125, 17)
		self.ArmorEditLine.SetPosition(5, 2)
		self.ArmorEditLine.SetMax(20)
		self.ArmorEditLine.SetText("11499")
		self.ArmorEditLine.SetFocus()
		self.ArmorEditLine.Show()

		self.ArmaLabel = ui.TextLine()
		self.ArmaLabel.SetParent(self.Board4)
		self.ArmaLabel.SetDefaultFontName()
		self.ArmaLabel.SetPosition(50, 220)
		self.ArmaLabel.SetFeather()
		self.ArmaLabel.SetWindowHorizontalAlignCenter()
		self.ArmaLabel.SetText("Arma")
		self.ArmaLabel.SetOutline()
		self.ArmaLabel.Show()
		
		self.WeaponSlotBar = ui.SlotBar()
		self.WeaponSlotBar.SetParent(self.Board4)
		self.WeaponSlotBar.SetSize(125, 18)
		self.WeaponSlotBar.SetPosition(-30, 220)
		self.WeaponSlotBar.SetWindowHorizontalAlignCenter()
		self.WeaponSlotBar.Show()
		
		self.WeaponEditLine = ui.EditLine()
		self.WeaponEditLine.SetParent(self.WeaponSlotBar)
		self.WeaponEditLine.SetSize(125, 17)
		self.WeaponEditLine.SetPosition(5, 2)
		self.WeaponEditLine.SetMax(20)
		self.WeaponEditLine.SetText("4049")
		self.WeaponEditLine.SetFocus()
		self.WeaponEditLine.Show()

		self.MobLabel = ui.TextLine()
		self.MobLabel.SetParent(self.Board4)
		self.MobLabel.SetDefaultFontName()
		self.MobLabel.SetPosition(50, 250)
		self.MobLabel.SetFeather()
		self.MobLabel.SetWindowHorizontalAlignCenter()
		self.MobLabel.SetText("Pelo")
		self.MobLabel.SetOutline()
		self.MobLabel.Show()

		self.HairSlotBar = ui.SlotBar()
		self.HairSlotBar.SetParent(self.Board4)
		self.HairSlotBar.SetSize(125, 18)
		self.HairSlotBar.SetPosition(-30, 250)
		self.HairSlotBar.SetWindowHorizontalAlignCenter()
		self.HairSlotBar.Show()
		
		self.HairEditLine = ui.EditLine()
		self.HairEditLine.SetParent(self.HairSlotBar)
		self.HairEditLine.SetSize(125, 17)
		self.HairEditLine.SetPosition(5, 2)
		self.HairEditLine.SetMax(20)
		self.HairEditLine.SetText("0")
		self.HairEditLine.SetFocus()
		self.HairEditLine.Show()

		self.ChangeLabel = ui.TextLine()
		self.ChangeLabel.SetParent(self.Board4)
		self.ChangeLabel.SetDefaultFontName()
		self.ChangeLabel.SetPosition(-50, 170)
		self.ChangeLabel.SetFeather()
		self.ChangeLabel.SetWindowHorizontalAlignCenter()
		self.ChangeLabel.SetText("Hack visual")
		self.ChangeLabel.SetFontColor(1.0, 0.8, 0)
		self.ChangeLabel.SetOutline()
		self.ChangeLabel.Show()

		self.TeleportZEditLineSlotBar = ui.SlotBar()
		self.TeleportZEditLineSlotBar.SetParent(self.Board5)
		self.TeleportZEditLineSlotBar.SetSize(43, 18)
		self.TeleportZEditLineSlotBar.SetPosition(-180 + 40 + 120, 135 + 40*3 + 1)
		self.TeleportZEditLineSlotBar.SetWindowHorizontalAlignCenter()
		
		self.TeleportZEditLine = ui.EditLine()
		self.TeleportZEditLine.SetParent(self.TeleportZEditLineSlotBar)
		self.TeleportZEditLine.SetSize(43, 17)
		self.TeleportZEditLine.SetPosition(16, 2)
		self.TeleportZEditLine.SetMax(4)
		self.TeleportZEditLine.SetNumberMode()
		self.TeleportZEditLine.SetFocus()
		self.TeleportZEditLine.SetText("0")
		#self.TeleportZEditLine.SetTabEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		#self.TeleportZEditLine.SetReturnEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))

		self.TeleportYEditLineSlotBar = ui.SlotBar()
		self.TeleportYEditLineSlotBar.SetParent(self.Board5)
		self.TeleportYEditLineSlotBar.SetSize(43, 18)
		self.TeleportYEditLineSlotBar.SetPosition(70, 100)
		self.TeleportYEditLineSlotBar.SetWindowHorizontalAlignCenter()
		self.TeleportYEditLineSlotBar.Show()
		
		self.TeleportYEditLine = ui.EditLine()
		self.TeleportYEditLine.SetParent(self.TeleportYEditLineSlotBar)
		self.TeleportYEditLine.SetSize(43, 17)
		self.TeleportYEditLine.SetPosition(16, 2)
		self.TeleportYEditLine.SetMax(4)
		self.TeleportYEditLine.SetNumberMode()
		self.TeleportYEditLine.SetFocus()
		self.TeleportYEditLine.SetText("0")
		self.TeleportYEditLine.SetTabEvent(ui.__mem_func__(self.TeleportZEditLine.SetFocus))
		self.TeleportYEditLine.SetReturnEvent(ui.__mem_func__(self.TeleportZEditLine.SetFocus))
		self.TeleportYEditLine.Show()

		self.TeleportXEditLineSlotBar = ui.SlotBar()
		self.TeleportXEditLineSlotBar.SetParent(self.Board5)
		self.TeleportXEditLineSlotBar.SetSize(43, 18)
		self.TeleportXEditLineSlotBar.SetPosition(20, 100)
		self.TeleportXEditLineSlotBar.SetWindowHorizontalAlignCenter()
		self.TeleportXEditLineSlotBar.Show()
		
		self.TeleportXEditLine = ui.EditLine()
		self.TeleportXEditLine.SetParent(self.TeleportXEditLineSlotBar)
		self.TeleportXEditLine.SetSize(43, 17)
		self.TeleportXEditLine.SetPosition(16, 2)
		self.TeleportXEditLine.SetMax(4)
		self.TeleportXEditLine.SetNumberMode()
		self.TeleportXEditLine.SetFocus()
		self.TeleportXEditLine.SetText("0")
		self.TeleportXEditLine.SetTabEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
		self.TeleportXEditLine.SetReturnEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
		self.TeleportXEditLine.Show()


		self.TeleporterLabel = ui.TextLine()
		self.TeleporterLabel.SetParent(self.Board5)
		self.TeleporterLabel.SetDefaultFontName()
		self.TeleporterLabel.SetPosition(-110, 60)
		self.TeleporterLabel.SetFeather()
		self.TeleporterLabel.SetWindowHorizontalAlignCenter()
		self.TeleporterLabel.SetText("Pon las coordenadas del lugar al cual desesas ir")
		self.TeleporterLabel.SetOutline()
		self.TeleporterLabel.Show()	


		self.Teleporter1Label = ui.TextLine()
		self.Teleporter1Label.SetParent(self.Board5)
		self.Teleporter1Label.SetDefaultFontName()
		self.Teleporter1Label.SetPosition(-110, 80)
		self.Teleporter1Label.SetFeather()
		self.Teleporter1Label.SetWindowHorizontalAlignCenter()
		self.Teleporter1Label.SetText("Recomendacion.. Procura un lugar no muy lejos..")
		self.Teleporter1Label.SetOutline()
		self.Teleporter1Label.Show()
	



		self.Slotwahl1SlotBar = ui.SlotBar()
		self.Slotwahl1SlotBar.SetParent(self)
		self.Slotwahl1SlotBar.SetSize(130, 50)
		self.Slotwahl1SlotBar.SetPosition(25, 40)
		self.Slotwahl1SlotBar.SetWindowHorizontalAlignCenter()
		self.Slotwahl1SlotBar.Show()
		
		self.InputText1 = ui.EditLine()
		self.InputText1.SetParent(self.Slotwahl1SlotBar)
		self.InputText1.SetMax(70)
		self.InputText1.SetText("Multihack By Francoiz..")
		self.InputText1.SetFocus()
		self.InputText1.Show()
		
		self.Slotwahl1SlotBar2 = ui.SlotBar() 
		self.Slotwahl1SlotBar2.SetParent(self)
		self.Slotwahl1SlotBar2.SetSize(130, 18)
		self.Slotwahl1SlotBar2.SetPosition(25, 95)
		self.Slotwahl1SlotBar2.SetWindowHorizontalAlignCenter()
		self.Slotwahl1SlotBar2.Show()
		
		self.InputSegundos1 = ui.EditLine()
		self.InputSegundos1.SetParent(self.Slotwahl1SlotBar2)
		self.InputSegundos1.SetNumberMode()
		self.InputSegundos1.SetMax(4)
		self.InputSegundos1.SetText("9999")
		self.InputSegundos1.SetFocus()
		self.InputSegundos1.Show()

		self.CreditosLabel = ui.TextLine()
		self.CreditosLabel.SetParent(self.Board7)
		self.CreditosLabel.SetDefaultFontName()
		self.CreditosLabel.SetPosition(-80, 80)
		self.CreditosLabel.SetFeather()
		self.CreditosLabel.SetWindowHorizontalAlignCenter()
		self.CreditosLabel.SetText("Multihack by Francoiz v1.0")
		self.CreditosLabel.SetFontColor(1.0, 0.8, 0)
		self.CreditosLabel.SetOutline()
		self.CreditosLabel.Show()

		self.Creditos1Label = ui.TextLine()
		self.Creditos1Label.SetParent(self.Board7)
		self.Creditos1Label.SetDefaultFontName()
		self.Creditos1Label.SetPosition(-80, 110)
		self.Creditos1Label.SetFeather()
		self.Creditos1Label.SetWindowHorizontalAlignCenter()
		self.Creditos1Label.SetText("(En los codigos colaboro 123klo)")
		self.Creditos1Label.SetFontColor(1.0, 0.8, 0)
		self.Creditos1Label.SetOutline()
		self.Creditos1Label.Show()

		self.Creditos2Label = ui.TextLine()
		self.Creditos2Label.SetParent(self.Board7)
		self.Creditos2Label.SetPosition(35, 175)
		self.Creditos2Label.SetFeather()
		self.Creditos2Label.SetFontName("STENCIL:32")
		self.Creditos2Label.SetText("Francoiz")
		self.Creditos2Label.SetFontColor(1.0, 0.8, 0)
		self.Creditos2Label.SetOutline()
		self.Creditos2Label.Show()









		self.WhisperSpamTitle = ui.TextLine()
		self.WhisperSpamTitle.SetParent(self.Board8)
		self.WhisperSpamTitle.SetPosition(60, 10)
		self.WhisperSpamTitle.SetFeather()
		self.WhisperSpamTitle.SetFontName("STENCIL:32")
		self.WhisperSpamTitle.SetText("")
		self.WhisperSpamTitle.SetFontColor(0.0, 0.7, 1)
		self.WhisperSpamTitle.SetOutline()
		self.WhisperSpamTitle.Show()	

		self.WhisperSpamText = ui.TextLine()
		self.WhisperSpamText.SetParent(self.Board8)
		self.WhisperSpamText.SetDefaultFontName()
		self.WhisperSpamText.SetPosition(50, 45)
		self.WhisperSpamText.SetFeather()
		self.WhisperSpamText.SetText("Texto:")
		self.WhisperSpamText.SetFontColor(0.6, 0.7, 1)
		self.WhisperSpamText.SetOutline()
		self.WhisperSpamText.Show()	

		self.WhisperTypeText = ui.TextLine()
		self.WhisperTypeText.SetParent(self.Board8)
		self.WhisperTypeText.SetDefaultFontName()
		self.WhisperTypeText.SetPosition(50, 90)
		self.WhisperTypeText.SetFeather()
		self.WhisperTypeText.SetText("Forma:")
		self.WhisperTypeText.SetFontColor(0.6, 0.7, 1)
		self.WhisperTypeText.SetOutline()
		self.WhisperTypeText.Show()	

		self.WhisperColourText = ui.TextLine()
		self.WhisperColourText.SetParent(self.Board8)
		self.WhisperColourText.SetDefaultFontName()
		self.WhisperColourText.SetPosition(50, 140)
		self.WhisperColourText.SetFeather()
		self.WhisperColourText.SetText("Color:")
		self.WhisperColourText.SetFontColor(0.6, 0.7, 1)
		self.WhisperColourText.SetOutline()
		self.WhisperColourText.Show()
		
		self.ConfigurationText = ui.TextLine()
		self.ConfigurationText.SetParent(self.Board8)
		self.ConfigurationText.SetFontName("Tahoma:14")
		self.ConfigurationText.SetPosition(50, 190)
		self.ConfigurationText.SetFeather()
		self.ConfigurationText.SetText("Configuracion")
		self.ConfigurationText.SetFontColor(0.6, 0.7, 1)
		self.ConfigurationText.SetOutline()
		self.ConfigurationText.Show()	

		self.CountText = ui.TextLine()
		self.CountText.SetParent(self.Board8)
		self.CountText.SetDefaultFontName()
		self.CountText.SetPosition(50, 210)
		self.CountText.SetFeather()
		self.CountText.SetText("Cantidad:")
		self.CountText.SetFontColor(0.6, 0.7, 1)
		self.CountText.SetOutline()
		self.CountText.Show()	

		self.DelayText = ui.TextLine()
		self.DelayText.SetParent(self.Board8)
		self.DelayText.SetDefaultFontName()
		self.DelayText.SetPosition(150, 210)
		self.DelayText.SetFeather()
		self.DelayText.SetText("Segundos:")
		self.DelayText.SetFontColor(0.6, 0.7, 1)
		self.DelayText.SetOutline()
		self.DelayText.Show()	

		self.PlayernameText = ui.TextLine()
		self.PlayernameText.SetParent(self.Board8)
		self.PlayernameText.SetDefaultFontName()
		self.PlayernameText.SetPosition(240, 210)
		self.PlayernameText.SetFeather()
		self.PlayernameText.SetText("Nombre del PJ:")
		self.PlayernameText.SetFontColor(0.6, 0.7, 1)
		self.PlayernameText.SetOutline()
		self.PlayernameText.Show()	

		self.ErrorText = ui.TextLine()
		self.ErrorText.SetParent(self.Board8)
		self.ErrorText.SetDefaultFontName()
		self.ErrorText.SetPosition(50, 260)
		self.ErrorText.SetFeather()
		self.ErrorText.SetText("Error:")
		self.ErrorText.SetFontColor(0.6, 0.7, 1)
		self.ErrorText.SetOutline()
		self.ErrorText.Show()	

		self.ErrorLog = ui.TextLine()
		self.ErrorLog.SetParent(self.Board8)
		self.ErrorLog.SetDefaultFontName()
		self.ErrorLog.SetPosition(50, 280)
		self.ErrorLog.SetFeather()
		self.ErrorLog.SetText("No hay errores.")
		self.ErrorLog.SetFontColor(1.0, 1.0, 1.0)
		self.ErrorLog.SetOutline()
		self.ErrorLog.Show()	

		self.ErrorLogRight = ui.TextLine()
		self.ErrorLogRight.SetParent(self.Board8)
		self.ErrorLogRight.SetDefaultFontName()
		self.ErrorLogRight.SetPosition(230, 280)
		self.ErrorLogRight.SetFeather()
		self.ErrorLogRight.SetText("")
		self.ErrorLogRight.SetFontColor(1.0, 1.0, 1.0)
		self.ErrorLogRight.SetOutline()
		self.ErrorLogRight.Show()	
		
		self.ErrorLog2 = ui.TextLine()
		self.ErrorLog2.SetParent(self.Board8)
		self.ErrorLog2.SetDefaultFontName()
		self.ErrorLog2.SetPosition(50, 300)
		self.ErrorLog2.SetFeather()
		self.ErrorLog2.SetText("")
		self.ErrorLog2.SetFontColor(1.0, 1.0, 1.0)
		self.ErrorLog2.SetOutline()
		self.ErrorLog2.Show()	
		
		self.ErrorLog2Right = ui.TextLine()
		self.ErrorLog2Right.SetParent(self.Board8)
		self.ErrorLog2Right.SetDefaultFontName()
		self.ErrorLog2Right.SetPosition(230, 300)
		self.ErrorLog2Right.SetFeather()
		self.ErrorLog2Right.SetText("")
		self.ErrorLog2Right.SetFontColor(1.0, 1.0, 1.0)
		self.ErrorLog2Right.SetOutline()
		self.ErrorLog2Right.Show()	
		
		self.LastChangeText = ui.TextLine()
		self.LastChangeText.SetParent(self.Board8)
		self.LastChangeText.SetDefaultFontName()
		self.LastChangeText.SetPosition(50, 325)
		self.LastChangeText.SetFeather()
		self.LastChangeText.SetText("Informacion del bot:")
		self.LastChangeText.SetFontColor(0.6, 0.7, 1)
		self.LastChangeText.SetOutline()
		self.LastChangeText.Show()	

		self.LastChange = ui.TextLine()
		self.LastChange.SetParent(self.Board8)
		self.LastChange.SetDefaultFontName()
		self.LastChange.SetPosition(50, 345)
		self.LastChange.SetFeather()
		self.LastChange.SetText("Ninguna")
		self.LastChange.SetFontColor(1.0, 1.0, 1.0)
		self.LastChange.SetOutline()
		self.LastChange.Show()	

		self.CreatorText = ui.TextLine()
		self.CreatorText.SetParent(self.Board8)
		self.CreatorText.SetDefaultFontName()
		self.CreatorText.SetPosition(305, 405)
		self.CreatorText.SetFeather()
		self.CreatorText.SetText("SpamBot")
		self.CreatorText.SetFontColor(1.0, 0.5, 0.5)
		self.CreatorText.SetOutline()
		self.CreatorText.Show()	










		self.PlayerWhisperSpamSlotBar = ui.SlotBar()
		self.PlayerWhisperSpamSlotBar.SetParent(self.Board8)
		self.PlayerWhisperSpamSlotBar.SetSize(80, 18)
		self.PlayerWhisperSpamSlotBar.SetPosition(83, 230)
		self.PlayerWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.PlayerWhisperSpamSlotBar.Show()
		
		self.PlayerWhisperSpamEditLine = ui.EditLine()
		self.PlayerWhisperSpamEditLine.SetParent(self.PlayerWhisperSpamSlotBar)
		self.PlayerWhisperSpamEditLine.SetSize(80, 17)
		self.PlayerWhisperSpamEditLine.SetPosition(10, 2)
		self.PlayerWhisperSpamEditLine.SetMax(12)
		self.PlayerWhisperSpamEditLine.SetFocus()
		self.PlayerWhisperSpamEditLine.SetText("")
		self.PlayerWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.StartSpamBot))
		self.PlayerWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.StartSpamBot))
		self.PlayerWhisperSpamEditLine.Show()


		self.DelayWhisperSpamSlotBar = ui.SlotBar()
		self.DelayWhisperSpamSlotBar.SetParent(self.Board8)
		self.DelayWhisperSpamSlotBar.SetSize(60, 18)
		self.DelayWhisperSpamSlotBar.SetPosition(-17, 230)
		self.DelayWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.DelayWhisperSpamSlotBar.Show()
		
		self.DelayWhisperSpamEditLine = ui.EditLine()
		self.DelayWhisperSpamEditLine.SetParent(self.DelayWhisperSpamSlotBar)
		self.DelayWhisperSpamEditLine.SetSize(60, 17)
		self.DelayWhisperSpamEditLine.SetPosition(10, 2)
		self.DelayWhisperSpamEditLine.SetMax(3)
		self.DelayWhisperSpamEditLine.SetNumberMode()
		self.DelayWhisperSpamEditLine.SetFocus()
		self.DelayWhisperSpamEditLine.SetText("0")
		self.DelayWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.PlayerWhisperSpamEditLine.SetFocus))
		self.DelayWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.PlayerWhisperSpamEditLine.SetFocus))
		self.DelayWhisperSpamEditLine.Show()


		self.CountWhisperSpamSlotBar = ui.SlotBar()
		self.CountWhisperSpamSlotBar.SetParent(self.Board8)
		self.CountWhisperSpamSlotBar.SetSize(60, 18)
		self.CountWhisperSpamSlotBar.SetPosition(-117, 230)
		self.CountWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.CountWhisperSpamSlotBar.Show()
		
		self.CountWhisperSpamEditLine = ui.EditLine()
		self.CountWhisperSpamEditLine.SetParent(self.CountWhisperSpamSlotBar)
		self.CountWhisperSpamEditLine.SetSize(60, 17)
		self.CountWhisperSpamEditLine.SetPosition(10, 2)
		self.CountWhisperSpamEditLine.SetMax(5)
		self.CountWhisperSpamEditLine.SetNumberMode()
		self.CountWhisperSpamEditLine.SetFocus()
		self.CountWhisperSpamEditLine.SetText("0")
		self.CountWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.DelayWhisperSpamEditLine.SetFocus))
		self.CountWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.DelayWhisperSpamEditLine.SetFocus))
		self.CountWhisperSpamEditLine.Show()


		self.WhisperSpamSlotBar = ui.SlotBar()
		self.WhisperSpamSlotBar.SetParent(self.Board8)
		self.WhisperSpamSlotBar.SetSize(300, 18)
		self.WhisperSpamSlotBar.SetPosition(0, 60)
		self.WhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.WhisperSpamSlotBar.Show()
		
		self.WhisperSpamEditLine = ui.EditLine()
		self.WhisperSpamEditLine.SetParent(self.WhisperSpamSlotBar)
		self.WhisperSpamEditLine.SetSize(300, 17)
		self.WhisperSpamEditLine.SetPosition(10, 2)
		self.WhisperSpamEditLine.SetMax(64)
		self.WhisperSpamEditLine.SetFocus()
		self.WhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.CountWhisperSpamEditLine.SetFocus))
		self.WhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.CountWhisperSpamEditLine.SetFocus))
		self.WhisperSpamEditLine.Show()










		self.ChatSpamTitle = ui.TextLine()
		self.ChatSpamTitle.SetParent(self.Board9)
		self.ChatSpamTitle.SetPosition(80, 10)
		self.ChatSpamTitle.SetFeather()
		self.ChatSpamTitle.SetFontName("STENCIL:32")
		self.ChatSpamTitle.SetText("")
		self.ChatSpamTitle.SetFontColor(0.0, 0.7, 1)
		self.ChatSpamTitle.SetOutline()
		self.ChatSpamTitle.Show()	

		self.ChatSpamText = ui.TextLine()
		self.ChatSpamText.SetParent(self.Board9)
		self.ChatSpamText.SetDefaultFontName()
		self.ChatSpamText.SetPosition(50, 45)
		self.ChatSpamText.SetFeather()
		self.ChatSpamText.SetText("Texto:")
		self.ChatSpamText.SetFontColor(0.6, 0.7, 1)
		self.ChatSpamText.SetOutline()
		self.ChatSpamText.Show()	

		self.ChatTypeText = ui.TextLine()
		self.ChatTypeText.SetParent(self.Board9)
		self.ChatTypeText.SetDefaultFontName()
		self.ChatTypeText.SetPosition(50, 90)
		self.ChatTypeText.SetFeather()
		self.ChatTypeText.SetText("Forma:")
		self.ChatTypeText.SetFontColor(0.6, 0.7, 1)
		self.ChatTypeText.SetOutline()
		self.ChatTypeText.Show()	

		self.ChatColourText = ui.TextLine()
		self.ChatColourText.SetParent(self.Board9)
		self.ChatColourText.SetDefaultFontName()
		self.ChatColourText.SetPosition(50, 140)
		self.ChatColourText.SetFeather()
		self.ChatColourText.SetText("Color:")
		self.ChatColourText.SetFontColor(0.6, 0.7, 1)
		self.ChatColourText.SetOutline()
		self.ChatColourText.Show()
		
		self.Configuration1Text = ui.TextLine()
		self.Configuration1Text.SetParent(self.Board9)
		self.Configuration1Text.SetFontName("Tahoma:14")
		self.Configuration1Text.SetPosition(50, 190)
		self.Configuration1Text.SetFeather()
		self.Configuration1Text.SetText("Configuracion")
		self.Configuration1Text.SetFontColor(0.6, 0.7, 1)
		self.Configuration1Text.SetOutline()
		self.Configuration1Text.Show()	

		self.Count1Text = ui.TextLine()
		self.Count1Text.SetParent(self.Board9)
		self.Count1Text.SetDefaultFontName()
		self.Count1Text.SetPosition(50, 210)
		self.Count1Text.SetFeather()
		self.Count1Text.SetText("Cantidad:")
		self.Count1Text.SetFontColor(0.6, 0.7, 1)
		self.Count1Text.SetOutline()
		self.Count1Text.Show()	

		self.Delay1Text = ui.TextLine()
		self.Delay1Text.SetParent(self.Board9)
		self.Delay1Text.SetDefaultFontName()
		self.Delay1Text.SetPosition(150, 210)
		self.Delay1Text.SetFeather()
		self.Delay1Text.SetText("Segundos:")
		self.Delay1Text.SetFontColor(0.6, 0.7, 1)
		self.Delay1Text.SetOutline()
		self.Delay1Text.Show()	

		self.Error1Text = ui.TextLine()
		self.Error1Text.SetParent(self.Board9)
		self.Error1Text.SetDefaultFontName()
		self.Error1Text.SetPosition(50, 260)
		self.Error1Text.SetFeather()
		self.Error1Text.SetText("Error:")
		self.Error1Text.SetFontColor(0.6, 0.7, 1)
		self.Error1Text.SetOutline()
		self.Error1Text.Show()	

		self.Error1Log = ui.TextLine()
		self.Error1Log.SetParent(self.Board9)
		self.Error1Log.SetDefaultFontName()
		self.Error1Log.SetPosition(50, 280)
		self.Error1Log.SetFeather()
		self.Error1Log.SetText("No hay errores")
		self.Error1Log.SetFontColor(1.0, 1.0, 1.0)
		self.Error1Log.SetOutline()
		self.Error1Log.Show()	

		self.Error1LogRight = ui.TextLine()
		self.Error1LogRight.SetParent(self.Board9)
		self.Error1LogRight.SetDefaultFontName()
		self.Error1LogRight.SetPosition(230, 280)
		self.Error1LogRight.SetFeather()
		self.Error1LogRight.SetText("")
		self.Error1LogRight.SetFontColor(1.0, 1.0, 1.0)
		self.Error1LogRight.SetOutline()
		self.Error1LogRight.Show()	
		
		self.Error1Log2 = ui.TextLine()
		self.Error1Log2.SetParent(self.Board9)
		self.Error1Log2.SetDefaultFontName()
		self.Error1Log2.SetPosition(50, 300)
		self.Error1Log2.SetFeather()
		self.Error1Log2.SetText("")
		self.Error1Log2.SetFontColor(1.0, 1.0, 1.0)
		self.Error1Log2.SetOutline()
		self.Error1Log2.Show()	
		
		self.Error1Log2Right = ui.TextLine()
		self.Error1Log2Right.SetParent(self.Board9)
		self.Error1Log2Right.SetDefaultFontName()
		self.Error1Log2Right.SetPosition(230, 300)
		self.Error1Log2Right.SetFeather()
		self.Error1Log2Right.SetText("")
		self.Error1Log2Right.SetFontColor(1.0, 1.0, 1.0)
		self.Error1Log2Right.SetOutline()
		self.Error1Log2Right.Show()	
		
		self.Last1ChangeText = ui.TextLine()
		self.Last1ChangeText.SetParent(self.Board9)
		self.Last1ChangeText.SetDefaultFontName()
		self.Last1ChangeText.SetPosition(50, 325)
		self.Last1ChangeText.SetFeather()
		self.Last1ChangeText.SetText("Informacion del bot:")
		self.Last1ChangeText.SetFontColor(0.6, 0.7, 1)
		self.Last1ChangeText.SetOutline()
		self.Last1ChangeText.Show()	

		self.Last1Change = ui.TextLine()
		self.Last1Change.SetParent(self.Board9)
		self.Last1Change.SetDefaultFontName()
		self.Last1Change.SetPosition(50, 345)
		self.Last1Change.SetFeather()
		self.Last1Change.SetText("Ninguna")
		self.Last1Change.SetFontColor(1.0, 1.0, 1.0)
		self.Last1Change.SetOutline()
		self.Last1Change.Show()	

		self.Creator1Text = ui.TextLine()
		self.Creator1Text.SetParent(self.Board9)
		self.Creator1Text.SetDefaultFontName()
		self.Creator1Text.SetPosition(305, 410)
		self.Creator1Text.SetFeather()
		self.Creator1Text.SetText("Chat Spam")
		self.Creator1Text.SetFontColor(1.0, 0.5, 0.5)
		self.Creator1Text.SetOutline()
		self.Creator1Text.Show()	






		self.DelayChatSpamSlotBar = ui.SlotBar()
		self.DelayChatSpamSlotBar.SetParent(self.Board9)
		self.DelayChatSpamSlotBar.SetSize(60, 18)
		self.DelayChatSpamSlotBar.SetPosition(-17, 230)
		self.DelayChatSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.DelayChatSpamSlotBar.Show()
		
		self.DelayChatSpamEditLine = ui.EditLine()
		self.DelayChatSpamEditLine.SetParent(self.DelayChatSpamSlotBar)
		self.DelayChatSpamEditLine.SetSize(60, 17)
		self.DelayChatSpamEditLine.SetPosition(10, 2)
		self.DelayChatSpamEditLine.SetMax(3)
		self.DelayChatSpamEditLine.SetNumberMode()
		self.DelayChatSpamEditLine.SetFocus()
		self.DelayChatSpamEditLine.SetText("0")
		self.DelayChatSpamEditLine.SetTabEvent(ui.__mem_func__(self.Start1SpamBot))
		self.DelayChatSpamEditLine.SetReturnEvent(ui.__mem_func__(self.Start1SpamBot))
		self.DelayChatSpamEditLine.Show()

		self.CountChatSpamSlotBar = ui.SlotBar()
		self.CountChatSpamSlotBar.SetParent(self.Board9)
		self.CountChatSpamSlotBar.SetSize(60, 18)
		self.CountChatSpamSlotBar.SetPosition(-117, 230)
		self.CountChatSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.CountChatSpamSlotBar.Show()
		
		self.CountChatSpamEditLine = ui.EditLine()
		self.CountChatSpamEditLine.SetParent(self.CountChatSpamSlotBar)
		self.CountChatSpamEditLine.SetSize(60, 17)
		self.CountChatSpamEditLine.SetPosition(10, 2)
		self.CountChatSpamEditLine.SetMax(5)
		self.CountChatSpamEditLine.SetNumberMode()
		self.CountChatSpamEditLine.SetFocus()
		self.CountChatSpamEditLine.SetText("0")
		self.CountChatSpamEditLine.SetTabEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		self.CountChatSpamEditLine.SetReturnEvent(ui.__mem_func__(self.DelayChatSpamEditLine.SetFocus))
		self.CountChatSpamEditLine.Show()

		self.ChatSpamSlotBar = ui.SlotBar()
		self.ChatSpamSlotBar.SetParent(self.Board9)
		self.ChatSpamSlotBar.SetSize(300, 18)
		self.ChatSpamSlotBar.SetPosition(0, 60)
		self.ChatSpamSlotBar.SetWindowHorizontalAlignCenter()
		self.ChatSpamSlotBar.Show()
		
		self.ChatSpamEditLine = ui.EditLine()
		self.ChatSpamEditLine.SetParent(self.ChatSpamSlotBar)
		self.ChatSpamEditLine.SetSize(300, 17)
		self.ChatSpamEditLine.SetPosition(10, 2)
		self.ChatSpamEditLine.SetMax(64)
		self.ChatSpamEditLine.SetFocus()
		self.ChatSpamEditLine.SetTabEvent(ui.__mem_func__(self.CountChatSpamEditLine.SetFocus))
		self.ChatSpamEditLine.SetReturnEvent(ui.__mem_func__(self.CountChatSpamEditLine.SetFocus))
		self.ChatSpamEditLine.Show()









		self.PJText = ui.TextLine()
		self.PJText.SetParent(self.Board4)
		self.PJText.SetDefaultFontName()
		self.PJText.SetPosition(20, 330)
		self.PJText.SetFeather()
		self.PJText.SetText("Esconder PJ")
		self.PJText.SetOutline()
		self.PJText.Show()	



		#############################Buttons

		self.PJButton = ui.Button()
		self.PJButton.SetParent(self.Board4)
		self.PJButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.PJButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.PJButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.PJButton.SetToolTipText("Ocultar/Mostrar PJ")
		self.PJButton.SetText("Ocultar")
		self.PJButton.SetPosition(100, 330)
		self.PJButton.SetEvent(ui.__mem_func__(self.PJ))
		self.PJButton.Show()





		self.Colour1List = []
		self.ChatTypeList = []

		x = 55
		i = 0
		for Chattype in self.CHAT_MODE_NAME:
			ChattypeButton = ui.Button()
			ChattypeButton.SetParent(self.Board9)
			ChattypeButton.SetPosition(x, 110)
			ChattypeButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			ChattypeButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			ChattypeButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			ChattypeButton.SetText(Chattype)
			ChattypeButton.Show()

			Type = self.CHAT_MODE_INDEX[i]
			ChattypeButton.SetEvent(lambda arg = Type: self.UseChatType(arg))
			ChattypeButton.SetEvent(lambda arg = Type: self.UseChatType(arg))
			self.ChatTypeList.append(ChattypeButton)
			x += 48
			i += 1

		x = 55
		i = 0
		for Colour in self.COLOUR1_MODE_NAME:
			Colour1Button = ui.Button()
			Colour1Button.SetParent(self.Board9)
			Colour1Button.SetPosition(x, 160)
			Colour1Button.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			Colour1Button.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			Colour1Button.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			Colour1Button.SetText(Colour)
			Colour1Button.Show()

			Type = self.COLOUR1_MODE_INDEX[i]
			Colour1Button.SetEvent(lambda arg = Type: self.UseChatColour(arg))
			Colour1Button.SetEvent(lambda arg = Type: self.UseChatColour(arg))
			self.Colour1List.append(Colour1Button)
			x += 48
			i += 1

		self.StartChatSpamButton = ui.Button()
		self.StartChatSpamButton.SetParent(self.Board9)
		self.StartChatSpamButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StartChatSpamButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StartChatSpamButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StartChatSpamButton.SetText("Comenzar")
		self.StartChatSpamButton.SetPosition(15, 380)
		self.StartChatSpamButton.SetEvent(ui.__mem_func__(self.Start1SpamBot))
		self.StartChatSpamButton.Show()

		self.StopChatSpamButton = ui.Button()
		self.StopChatSpamButton.SetParent(self.Board9)
		self.StopChatSpamButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StopChatSpamButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StopChatSpamButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StopChatSpamButton.SetText("Parar")
		self.StopChatSpamButton.SetPosition(195, 380)
		self.StopChatSpamButton.SetEvent(ui.__mem_func__(self.Stop1SpamBot))
		self.StopChatSpamButton.Show()
		





		

		self.ColourList = []
		self.WhisperTypeList = []

		x = 55
		i = 0
		for Whispertype in self.WHISPER_MODE:
			WhispertypeButton = ui.Button()
			WhispertypeButton.SetParent(self.Board8)
			WhispertypeButton.SetPosition(x, 110)
			WhispertypeButton.SetUpVisual("d:/ymir work/ui/public/small_button_01.sub")
			WhispertypeButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			WhispertypeButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			WhispertypeButton.SetText(Whispertype)
			WhispertypeButton.Show()

			Type = self.WHISPER_MODE[i]
			WhispertypeButton.SetEvent(lambda arg = Type: self.UseWhisperType(arg))
			WhispertypeButton.SetEvent(lambda arg = Type: self.UseWhisperType(arg))
			self.WhisperTypeList.append(WhispertypeButton)
			x += 48
			i += 1

		x = 55
		i = 0
		for Colour in self.COLOUR_MODE_NAME:
			ColourButton = ui.Button()
			ColourButton.SetParent(self.Board8)
			ColourButton.SetPosition(x, 160)
			ColourButton.SetUpVisual("d:/ymir work/ui/public/small_Button_01.sub")
			ColourButton.SetOverVisual("d:/ymir work/ui/public/small_button_02.sub")
			ColourButton.SetDownVisual("d:/ymir work/ui/public/small_button_03.sub")
			ColourButton.SetText(Colour)
			ColourButton.Show()

			Type = self.COLOUR_MODE_INDEX[i]
			ColourButton.SetEvent(lambda arg = Type: self.UseWhisperColour(arg))
			ColourButton.SetEvent(lambda arg = Type: self.UseWhisperColour(arg))
			self.ColourList.append(ColourButton)
			x += 48
			i += 1

		self.StartWhisperSpamButton = ui.Button()
		self.StartWhisperSpamButton.SetParent(self.Board8)
		self.StartWhisperSpamButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StartWhisperSpamButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StartWhisperSpamButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StartWhisperSpamButton.SetText("Comenzar")
		self.StartWhisperSpamButton.SetPosition(15, 380)
		self.StartWhisperSpamButton.SetEvent(ui.__mem_func__(self.StartSpamBot))
		self.StartWhisperSpamButton.Show()

		self.StopWhisperSpamButton = ui.Button()
		self.StopWhisperSpamButton.SetParent(self.Board8)
		self.StopWhisperSpamButton.SetUpVisual("d:/ymir work/ui/public/xlarge_button_01.sub")
		self.StopWhisperSpamButton.SetOverVisual("d:/ymir work/ui/public/xlarge_button_02.sub")
		self.StopWhisperSpamButton.SetDownVisual("d:/ymir work/ui/public/xlarge_button_03.sub")
		self.StopWhisperSpamButton.SetText("Parar")
		self.StopWhisperSpamButton.SetPosition(195, 380)
		self.StopWhisperSpamButton.SetEvent(ui.__mem_func__(self.StopSpamBot))
		self.StopWhisperSpamButton.Show()















		self.CreditosfrancoizButton = ui.Button()
		self.CreditosfrancoizButton.SetParent(self.Board7)
		self.CreditosfrancoizButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.CreditosfrancoizButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.CreditosfrancoizButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.CreditosfrancoizButton.SetToolTipText("Creditos Francoiz")
		self.CreditosfrancoizButton.SetText("Pagina web")
		self.CreditosfrancoizButton.SetPosition(105, 140)
		self.CreditosfrancoizButton.SetEvent(ui.__mem_func__(self.Creditosfrancoiz))
		self.CreditosfrancoizButton.Show()


		self.SpamfrancoizButton = ui.Button()
		self.SpamfrancoizButton.SetParent(self.Board7)
		self.SpamfrancoizButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SpamfrancoizButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SpamfrancoizButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SpamfrancoizButton.SetToolTipText("Spam Francoiz")
		self.SpamfrancoizButton.SetText("Spam Francoiz")
		self.SpamfrancoizButton.SetPosition(35, 140)
		self.SpamfrancoizButton.SetEvent(ui.__mem_func__(self.Spamfrancoiz))
		self.SpamfrancoizButton.Show()




		self.TeleportButton = ui.Button()
		self.TeleportButton.SetParent(self.Board5)
		self.TeleportButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.TeleportButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.TeleportButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.TeleportButton.SetText("Teleporter")
		self.TeleportButton.SetPosition(10, 100)
		self.TeleportButton.SetEvent(ui.__mem_func__(self.TeleportToCoordinates))
		self.TeleportButton.Show()

		self.ChangeButton = ui.Button()
		self.ChangeButton.SetParent(self.Board4)
		self.ChangeButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		self.ChangeButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		self.ChangeButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		self.ChangeButton.SetText("Generar")
		self.ChangeButton.SetPosition(80, 280)
		self.ChangeButton.SetEvent(ui.__mem_func__(self.EqChange))
		self.ChangeButton.SetToolTipText("")
		self.ChangeButton.Show()

		self.HerreroButton = ui.Button()
		self.HerreroButton.SetParent(self.Board4)
		self.HerreroButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.HerreroButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.HerreroButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.HerreroButton.SetText("Mejorar")
		self.HerreroButton.SetPosition(100, 97)
		self.HerreroButton.SetEvent(ui.__mem_func__(self.RefineOneTime))
		self.HerreroButton.SetToolTipText("")
		self.HerreroButton.Show()

		self.FantasmaButton = ui.Button()
		self.FantasmaButton.SetParent(self.Board4)
		self.FantasmaButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.FantasmaButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.FantasmaButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.FantasmaButton.SetText("Fantasma")
		self.FantasmaButton.SetPosition(100, 67)
		self.FantasmaButton.SetEvent(ui.__mem_func__(self.GhostMod))
		self.FantasmaButton.Show()

		self.ComboTypeButton = ui.Button()
		self.ComboTypeButton.SetParent(self.Board4)
		self.ComboTypeButton.SetPosition(100, 127)
		self.ComboTypeButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.ComboTypeButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.ComboTypeButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.ComboTypeButton.SetEvent(ui.__mem_func__(self.Combo))
		self.ComboTypeButton.SetText("Desactivado")
		self.ComboTypeButton.Show()
		

		self.CabosButton = ui.Button()
		self.CabosButton.SetParent(self.Board1)
		self.CabosButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.CabosButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.CabosButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.CabosButton.SetText("Cabos")
		self.CabosButton.SetPosition(200, 252)
		self.CabosButton.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))
		self.CabosButton.Show()

		self.TapferkeitsUmhangeImage = ui.ExpandedImageBox()
		self.TapferkeitsUmhangeImage.SetParent(self.Board1)
		self.TapferkeitsUmhangeImage.SetPosition(161, 248)
		self.TapferkeitsUmhangeImage.LoadImage(str("icon/item/70038.tga"))
		self.TapferkeitsUmhangeImage.Show()
		
		self.TapferkeitsUmhangeButton = ui.Button()
		self.TapferkeitsUmhangeButton.SetParent(self.TapferkeitsUmhangeImage)
		self.TapferkeitsUmhangeButton.SetPosition(20, 10)
		self.TapferkeitsUmhangeButton.SetSize(70, 40)
		self.TapferkeitsUmhangeButton.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))
		self.TapferkeitsUmhangeButton.Show()
		
		self.TapferkeitsUmhangeImageActivated = ui.ExpandedImageBox()
		self.TapferkeitsUmhangeImageActivated.SetParent(self.Board1)
		self.TapferkeitsUmhangeImageActivated.SetPosition(161, 248)
		self.TapferkeitsUmhangeImageActivated.LoadImage(str("icon/item/30040.tga"))
		
		self.TapferkeitsUmhangeButtonActivated = ui.Button()
		self.TapferkeitsUmhangeButtonActivated.SetParent(self.TapferkeitsUmhangeImageActivated)
		self.TapferkeitsUmhangeButtonActivated.SetPosition(20, 10)
		self.TapferkeitsUmhangeButtonActivated.SetSize(70, 40)
		self.TapferkeitsUmhangeButtonActivated.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))

		self.AttackSpeedStatusButton = ui.Button()
		self.AttackSpeedStatusButton.SetParent(self.Board3)
		self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AttackSpeedStatusButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AttackSpeedStatusButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AttackSpeedStatusButton.SetText("Desactivado")
		self.AttackSpeedStatusButton.SetPosition(190, 77)
		self.AttackSpeedStatusButton.SetEvent(ui.__mem_func__(self.AttackSpeedStatus))
		self.AttackSpeedStatusButton.Show()

		self.MoveSpeedStatusButton = ui.Button()
		self.MoveSpeedStatusButton.SetParent(self.Board3)
		self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.MoveSpeedStatusButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.MoveSpeedStatusButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.MoveSpeedStatusButton.SetText("Desactivado")
		self.MoveSpeedStatusButton.SetPosition(190, 107)
		self.MoveSpeedStatusButton.SetEvent(ui.__mem_func__(self.MoveSpeedStatus))
		self.MoveSpeedStatusButton.Show()

		self.AutoRedPotButton = ui.Button()
		self.AutoRedPotButton.SetParent(self.Board1)
		self.AutoRedPotButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoRedPotButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoRedPotButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
                self.AutoRedPotButton.SetText("Desactivado")
		self.AutoRedPotButton.SetPosition(148, 97)
		self.AutoRedPotButton.SetEvent(ui.__mem_func__(self.AutoRedPot))
		self.AutoRedPotButton.Show()
		
		self.AutoBluePotButton = ui.Button()
		self.AutoBluePotButton.SetParent(self.Board1)
		self.AutoBluePotButton.SetPosition(148, 127)
		self.AutoBluePotButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoBluePotButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoBluePotButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoBluePotButton.SetEvent(ui.__mem_func__(self.AutoBluePot))
		self.AutoBluePotButton.SetText("Desactivado")
		self.AutoBluePotButton.Show()

		self.AutoAttackButton = ui.Button()
		self.AutoAttackButton.SetParent(self.Board1)
		self.AutoAttackButton.SetPosition(75, 157)
		self.AutoAttackButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoAttackButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoAttackButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoAttackButton.SetEvent(ui.__mem_func__(self.AutoAttack))
		self.AutoAttackButton.SetText("Desactivado")
		self.AutoAttackButton.Show()
		
		self.AutoPickupButton = ui.Button()
		self.AutoPickupButton.SetParent(self.Board1)
		self.AutoPickupButton.SetPosition(75, 187)
		self.AutoPickupButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoPickupButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoPickupButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoPickupButton.SetEvent(ui.__mem_func__(self.AutoPickup))
		self.AutoPickupButton.SetText("Desactivado")
		self.AutoPickupButton.Show()
		
		self.AutoRestartButton = ui.Button()
		self.AutoRestartButton.SetParent(self.Board1)
		self.AutoRestartButton.SetPosition(75, 217)
		self.AutoRestartButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.AutoRestartButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.AutoRestartButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.AutoRestartButton.SetEvent(ui.__mem_func__(self.AutoRestart))
		self.AutoRestartButton.SetText("Desactivado")
		self.AutoRestartButton.Show()

		self.ZoomHackButton = ui.Button()
		self.ZoomHackButton.SetParent(self.Board2)
		self.ZoomHackButton.SetPosition(75, 67)
		self.ZoomHackButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.ZoomHackButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.ZoomHackButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.ZoomHackButton.SetEvent(ui.__mem_func__(self.ZoomHack))
		self.ZoomHackButton.SetText("Desactivado")
		self.ZoomHackButton.Show()
		
		self.NoFogButton = ui.Button()
		self.NoFogButton.SetParent(self.Board2)
		self.NoFogButton.SetPosition(75, 97)
		self.NoFogButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.NoFogButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.NoFogButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.NoFogButton.SetEvent(ui.__mem_func__(self.NoFog))
		self.NoFogButton.SetText("Desactivado")
		self.NoFogButton.Show()

		self.DayNightButton = ui.Button()
		self.DayNightButton.SetParent(self.Board2)
		self.DayNightButton.SetPosition(75, 127)
		self.DayNightButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.DayNightButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.DayNightButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.DayNightButton.SetEvent(ui.__mem_func__(self.DayNight))
		self.DayNightButton.SetText("Dia")
		self.DayNightButton.Show()
		
		self.SnowButton = ui.Button()
		self.SnowButton.SetParent(self.Board2)
		self.SnowButton.SetPosition(75, 157)
		self.SnowButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
		self.SnowButton.SetOverVisual("d:/ymir work/ui/public/middle_button_02.sub")
		self.SnowButton.SetDownVisual("d:/ymir work/ui/public/middle_button_03.sub")
		self.SnowButton.SetEvent(ui.__mem_func__(self.EnableSnow))
		self.SnowButton.SetText("Desactivado")
		self.SnowButton.Show()

	def FaceButton(self):
	
		global Leveo1Button
		Leveo1Button = ui.Button()
		Leveo1Button.SetText("")
		Leveo1Button.SetPosition(wndMgr.GetScreenWidth()-100,220)
		Leveo1Button.SetSize(88, 21)
		Leveo1Button.SetEvent(self.Board1.Show)
		Leveo1Button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		Leveo1Button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		Leveo1Button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		Leveo1Button.Show()
		
		global Leveo1Text
		Leveo1Text = ui.TextLine()
		Leveo1Text.SetParent(Leveo1Button)
		Leveo1Text.SetVerticalAlignCenter()
		Leveo1Text.SetHorizontalAlignCenter()
		Leveo1Text.SetPosition(43,10)
		Leveo1Text.SetText("Leveo Bot")
		Leveo1Text.Show()

		global CamaraButton
		CamaraButton = ui.Button()
		CamaraButton.SetText("")
		CamaraButton.SetPosition(wndMgr.GetScreenWidth()-100,280)
		CamaraButton.SetSize(88, 21)
		CamaraButton.SetEvent(self.Board2.Show)
		CamaraButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		CamaraButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		CamaraButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		CamaraButton.Show()
		
		global CamaraText
		CamaraText = ui.TextLine()
		CamaraText.SetParent(CamaraButton)
		CamaraText.SetVerticalAlignCenter()
		CamaraText.SetHorizontalAlignCenter()
		CamaraText.SetPosition(43,10)
		CamaraText.SetText("Camara Hack")
		CamaraText.Show()

		global VelocidadButton
		VelocidadButton = ui.Button()
		VelocidadButton.SetText("")
		VelocidadButton.SetPosition(wndMgr.GetScreenWidth()-100,310)
		VelocidadButton.SetSize(88, 21)
		VelocidadButton.SetEvent(self.Board3.Show)
		VelocidadButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		VelocidadButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		VelocidadButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		VelocidadButton.Show()
		
		global VelocidadText
		VelocidadText = ui.TextLine()
		VelocidadText.SetParent(VelocidadButton)
		VelocidadText.SetVerticalAlignCenter()
		VelocidadText.SetHorizontalAlignCenter()
		VelocidadText.SetPosition(43,10)
		VelocidadText.SetText("Velocidad Hack")
		VelocidadText.Show()

		global OtrosButton
		OtrosButton = ui.Button()
		OtrosButton.SetText("")
		OtrosButton.SetPosition(wndMgr.GetScreenWidth()-100,250)
		OtrosButton.SetSize(88, 21)
		OtrosButton.SetEvent(self.Board4.Show)
		OtrosButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		OtrosButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		OtrosButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		OtrosButton.Show()
		
		global OtrosText
		OtrosText = ui.TextLine()
		OtrosText.SetParent(OtrosButton)
		OtrosText.SetVerticalAlignCenter()
		OtrosText.SetHorizontalAlignCenter()
		OtrosText.SetPosition(43,10)
		OtrosText.SetText("Otros hacks")
		OtrosText.Show()

		global TeleporterButton
		TeleporterButton = ui.Button()
		TeleporterButton.SetText("")
		TeleporterButton.SetPosition(wndMgr.GetScreenWidth()-100,340)
		TeleporterButton.SetSize(88, 21)
		TeleporterButton.SetEvent(self.Board5.Show)
		TeleporterButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		TeleporterButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		TeleporterButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		TeleporterButton.Show()
		
		global TeleporterText
		TeleporterText = ui.TextLine()
		TeleporterText.SetParent(TeleporterButton)
		TeleporterText.SetVerticalAlignCenter()
		TeleporterText.SetHorizontalAlignCenter()
		TeleporterText.SetPosition(43,10)
		TeleporterText.SetText("Teleporter hack")
		TeleporterText.Show()

		global CreditosButton
		CreditosButton = ui.Button()
		CreditosButton.SetText("")
		CreditosButton.SetPosition(wndMgr.GetScreenWidth()-100,430)
		CreditosButton.SetSize(88, 21)
		CreditosButton.SetEvent(self.Board7.Show)
		CreditosButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		CreditosButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		CreditosButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		CreditosButton.Show()
		
		global CreditosText
		CreditosText = ui.TextLine()
		CreditosText.SetParent(CreditosButton)
		CreditosText.SetVerticalAlignCenter()
		CreditosText.SetHorizontalAlignCenter()
		CreditosText.SetPosition(43,10)
		CreditosText.SetText("Creditos")
		CreditosText.Show()

		global SpammerButton
		SpammerButton = ui.Button()
		SpammerButton.SetText("")
		SpammerButton.SetPosition(wndMgr.GetScreenWidth()-100,370)
		SpammerButton.SetSize(88, 21)
		SpammerButton.SetEvent(self.Board8.Show)
		SpammerButton.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		SpammerButton.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		SpammerButton.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		SpammerButton.Show()
		
		global SpammerText
		SpammerText = ui.TextLine()
		SpammerText.SetParent(SpammerButton)
		SpammerText.SetVerticalAlignCenter()
		SpammerText.SetHorizontalAlignCenter()
		SpammerText.SetPosition(43,10)
		SpammerText.SetText("Spam Chat")
		SpammerText.Show()

		global Spammer1Button
		Spammer1Button = ui.Button()
		Spammer1Button.SetText("")
		Spammer1Button.SetPosition(wndMgr.GetScreenWidth()-100,400)
		Spammer1Button.SetSize(88, 21)
		Spammer1Button.SetEvent(self.Board9.Show)
		Spammer1Button.SetUpVisual("d:/ymir work/ui/public/large_button_01.sub")
		Spammer1Button.SetOverVisual("d:/ymir work/ui/public/large_button_02.sub")
		Spammer1Button.SetDownVisual("d:/ymir work/ui/public/large_button_03.sub")
		Spammer1Button.Show()
		
		global Spammer1Text
		Spammer1Text = ui.TextLine()
		Spammer1Text.SetParent(Spammer1Button)
		Spammer1Text.SetVerticalAlignCenter()
		Spammer1Text.SetHorizontalAlignCenter()
		Spammer1Text.SetPosition(43,10)
		Spammer1Text.SetText("SpamBot")
		Spammer1Text.Show()


	def SendGoldDown(self):
		net.SendGoldDropPacketNew(500)
	
	def OpenInv(self):
		ToggleInventoryWindow()


	def PJ(self):

		global NoFog
		
		if NoFog == 0:
			NoFog = 1
			self.PJButton.SetText("Mostrar")
			player.HidePlayer()
		else:	
			NoFog = 0
			self.PJButton.SetText("Ocultar")
			player.ShowPlayer()

	
	def UseChatType(self, mode):
		global CHAT_TYPE
		if mode != "Random":
			CHAT_TYPE = mode
		else:
			Rnd = int(app.GetRandom(0,3))
			CHAT_TYPE = self.CHAT_MODE_INDEX[int(Rnd)]
		if int(CHAT_TYPE) == 3:
			ChatType = 1
		elif int(CHAT_TYPE) == 4:
			ChatType = 2
		elif int(CHAT_TYPE) == 6:
			ChatType = 3
		else:
			ChatType = int(CHAT_TYPE)
		self.Last1Change.SetText("Forma elegida: " + str(self.CHAT_MODE_NAME[int(ChatType)]))

	def UseChatColour(self, colour):
		global ChatColour
		ChatColour = str(colour)
		if ChatColour.find(str(self.COLOUR1_MODE_INDEX[0])) != -1:
			ChatType = str(self.COLOUR1_MODE_NAME[0])
		elif ChatColour.find(str(self.COLOUR1_MODE_INDEX[1])) != -1:
			ChatType = str(self.COLOUR1_MODE_NAME[1])
		elif ChatColour.find(str(self.COLOUR1_MODE_INDEX[2])) != -1:
			ChatType = str(self.COLOUR1_MODE_NAME[2])
		elif ChatColour.find(str(self.COLOUR1_MODE_INDEX[3])) != -1:
			ChatType = str(self.COLOUR1_MODE_NAME[3])
		elif ChatColour.find(str(self.COLOUR1_MODE_INDEX[4])) != -1:
			ChatType = str(self.COLOUR1_MODE_NAME[4])
		else:
			ChatType = ChatColour
		self.Last1Change.SetText("Color elegido: " + str(ChatType))
		
	def Stop1SpamBot(self):
		global Activity
		global Count
		Activity = "Pause"
		Count = 0
		self.Last1Change.SetText("El Chat spam Ha sido parado")

	def Start1SpamBot(self):
		global Count
		global CHAT_TYPE
		global ChatColour
		global Delay
		global Amount
		global Activity
		self.Error1Log.SetText("No hay errores")
		self.Error1LogRight.SetText("")
		self.Error1Log2.SetText("")
		self.Error1Log2Right.SetText("")
		State = "Allow"
		if int(Count) != 0:
			Message = str(self.ERROR1_MESSAGE_INDEX[0])
			self.Error1Log.SetText(str(Message))
		if CHAT_TYPE == "":
			Message = str(self.ERROR1_MESSAGE_INDEX[1])
			if self.Error1Log.GetText() != "No hay errores":
				self.Error1Log2.SetText(str(Message))
			else:
				self.Error1Log.SetText(str(Message))
		if ChatColour == "":
			Message = str(self.ERROR1_MESSAGE_INDEX[2])
			if self.Error1Log.GetText() != "keiner":
				if self.Error1Log2.GetText() != "":
					self.Error1LogRight.SetText(str(Message))
				else:
					self.Error1Log2.SetText(str(Message))
			else:
				self.Error1Log.SetText(str(Message))			
		if str(self.ChatSpamEditLine.GetText()) == "":
			Message = str(self.ERROR1_MESSAGE_INDEX[3])
			if self.Error1Log.GetText() != "No hay errores":
				if self.Error1Log2.GetText() != "":
					if self.Error1LogRight.GetText() != "":
						self.Error1Log2Right.SetText(str(Message))
					else:
						self.Error1LogRight.SetText(str(Message))
				else:
					self.Error1Log2.SetText(str(Message))
			else:
				self.Error1Log.SetText(str(Message))
		if CHAT_TYPE == 6 and int(self.DelayChatSpamEditLine.GetText()) < 15:
			Message = str(self.ERROR1_MESSAGE_INDEX[6])
			State = "Banned"
			if self.Error1Log.GetText() != "No hay errores":
				if self.Error1Log2.GetText() != "":
					if self.Error1LogRight.GetText() != "":
						self.Error1Log2Right.SetText(str(Message))
					else:
						self.Error1LogRight.SetText(str(Message))
				else:
					self.Error1Log2.SetText(str(Message))
			else:
				self.Error1Log.SetText(str(Message))
		if str(self.DelayChatSpamEditLine.GetText()) == "":
			if CHAT_TYPE != 6:
				Message = str(self.ERROR1_MESSAGE_INDEX[4])
				if self.Error1Log.GetText() != "No hay errores":
					if self.Error1Log2.GetText() != "":
						if self.Error1LogRight.GetText() != "":
							self.Error1Log2Right.SetText(str(Message))
						else:
							self.Error1LogRight.SetText(str(Message))
					else:
						self.Error1Log2.SetText(str(Message))
				else:
					self.Error1Log.SetText(str(Message))
		if int(self.CountChatSpamEditLine.GetText()) <= 0 or str(self.CountChatSpamEditLine.GetText()) == "":
			Message = str(self.ERROR1_MESSAGE_INDEX[5])
			if self.Error1Log.GetText() != "No hay errores":
				if self.Error1Log2.GetText() != "":
					if self.Error1LogRight.GetText() != "":
						self.Error1Log2Right.SetText(str(Message))
					else:
						self.Error1LogRight.SetText(str(Message))
				else:
					self.Error1Log2.SetText(str(Message))
			else:
				self.Error1Log.SetText(str(Message))
		if CHAT_TYPE != "" and (int(self.CountChatSpamEditLine.GetText()) > 0 or str(self.CountChatSpamEditLine.GetText()) == "") and str(self.DelayChatSpamEditLine.GetText()) != "" and ChatColour != "" and int(Count) == 0 and State == "Allow":
			Delay = int(self.DelayChatSpamEditLine.GetText())
			Amount = int(self.CountChatSpamEditLine.GetText())
			self.Last1Change.SetText("El SpamBot Chat ha comenzado!")
			Activity = "Spam"
			self.Spam()			
		
	def Spam(self):
		global ChatColour
		global CHAT_TYPE
		global Count
		global Delay
		global Amount
		global Activity
		if int(Amount) > int(Count):
			if ChatColour != "Random":
				if Activity == "Spam":
					net.SendChatPacket(str(ChatColour) + str(self.ChatSpamEditLine.GetText()), CHAT_TYPE)
					self.Last1Change.SetText("Chatspamcount: " + str(Count))
			elif ChatColour == "Random":
				if Activity == "Spam":
					net.SendChatPacket("|c"+ str(self.random1_color()) +"|H|h " + str(self.ChatSpamEditLine.GetText()), CHAT_TYPE)
					self.Last1Change.SetText("Chatspamcount: " + str(Count))
			if Activity == "Spam":
				Count += 1
				self.WaitingDelay = WaitingDialog()
				self.WaitingDelay.Open(float(Delay))
				self.WaitingDelay.SAFE_SetTimeOverEvent(self.Spam)
		else:
			Count = 0
			self.Last1Change.SetText("El spamBot Chat ha finalizado con exito..")
	
	def random1_color(self):
		COLOR_RANGE = (50, 255)
		
		rgb = list()
		for c in range(0, 4):
			rgb.append(app.GetRandom(COLOR_RANGE[0], COLOR_RANGE[1]))
    
		return "".join([hex(c)[2:].upper() for c in rgb])
		








		
	def UseWhisperType(self, mode):
		global WHISPER_TYPE
		self.LastChange.SetText("Forma elegida: " + str(mode))
		WHISPER_TYPE = mode

	def UseWhisperColour(self, colour):
		global WhisperColour
		WhisperColour = str(colour)
		if WhisperColour.find(str(self.COLOUR_MODE_INDEX[0])) != -1:
			WhisperType = str(self.COLOUR_MODE_NAME[0])
		elif WhisperColour.find(str(self.COLOUR_MODE_INDEX[1])) != -1:
			WhisperType = str(self.COLOUR_MODE_NAME[1])
		elif WhisperColour.find(str(self.COLOUR_MODE_INDEX[2])) != -1:
			WhisperType = str(self.COLOUR_MODE_NAME[2])
		elif WhisperColour.find(str(self.COLOUR_MODE_INDEX[3])) != -1:
			WhisperType = str(self.COLOUR_MODE_NAME[3])
		elif WhisperColour.find(str(self.COLOUR_MODE_INDEX[4])) != -1:
			WhisperType = str(self.COLOUR_MODE_NAME[4])
		else:
			WhisperType = WhisperColour
		self.LastChange.SetText("Color elegido: " + str(WhisperType))
		
	def StopSpamBot(self):
		global WhisperActivity
		global WhisperCount
		WhisperActivity = "Pause"
		WhisperCount = 0
		self.LastChange.SetText("SpamBot parado")

	def StartSpamBot(self):
		global WhisperCount
		global WHISPER_TYPE
		global WhisperColour
		global WhisperDelay
		global WhisperAmount
		global WhisperActivity
		self.SetVIDRange()
		self.ErrorLog.SetText("No hay errores")
		self.ErrorLogRight.SetText("")
		self.ErrorLog2.SetText("")
		self.ErrorLog2Right.SetText("")
		if int(WhisperCount) != 0:
			Message = str(self.ERROR_MESSAGE_INDEX[0])
			self.ErrorLog.SetText(str(Message))
		if WHISPER_TYPE == "":
			Message = str(self.ERROR_MESSAGE_INDEX[1])
			if self.ErrorLog.GetText() != "keiner":
				self.ErrorLog2.SetText(str(Message))
			else:
				self.ErrorLog.SetText(str(Message))
		elif WHISPER_TYPE == "Player" and str(self.PlayerWhisperSpamEditLine.GetText()) == "":
			Message = str(self.ERROR_MESSAGE_INDEX[6])
			if self.ErrorLog.GetText() != "keiner":
				if self.ErrorLog2.GetText() != "":
					self.ErrorLogRight.SetText(str(Message))
				else:
					self.ErrorLog2.SetText(str(Message))
			else:
				self.ErrorLog.SetText(str(Message))			
		if WhisperColour == "":
			Message = str(self.ERROR_MESSAGE_INDEX[2])
			if self.ErrorLog.GetText() != "No hay errores":
				if self.ErrorLog2.GetText() != "":
					self.ErrorLogRight.SetText(str(Message))
				else:
					self.ErrorLog2.SetText(str(Message))
			else:
				self.ErrorLog.SetText(str(Message))			
		if str(self.WhisperSpamEditLine.GetText()) == "":
			Message = str(self.ERROR_MESSAGE_INDEX[3])
			if self.ErrorLog.GetText() != "No hay errores":
				if self.ErrorLog2.GetText() != "":
					if self.ErrorLogRight.GetText() != "":
						self.ErrorLog2Right.SetText(str(Message))
					else:
						self.ErrorLogRight.SetText(str(Message))
				else:
					self.ErrorLog2.SetText(str(Message))
			else:
				self.ErrorLog.SetText(str(Message))
		if str(self.DelayWhisperSpamEditLine.GetText()) == "":
			if WHISPER_TYPE != 6:
				Message = str(self.ERROR_MESSAGE_INDEX[4])
				if self.ErrorLog.GetText() != "No hay errores":
					if self.ErrorLog2.GetText() != "":
						if self.ErrorLogRight.GetText() != "":
							self.ErrorLog2Right.SetText(str(Message))
						else:
							self.ErrorLogRight.SetText(str(Message))
					else:
						self.ErrorLog2.SetText(str(Message))
				else:
					self.ErrorLog.SetText(str(Message))
		if int(self.CountWhisperSpamEditLine.GetText()) <= 0 or str(self.CountWhisperSpamEditLine.GetText()) == "":
			Message = str(self.ERROR_MESSAGE_INDEX[5])
			if self.ErrorLog.GetText() != "No hay errores":
				if self.ErrorLog2.GetText() != "":
					if self.ErrorLogRight.GetText() != "":
						self.ErrorLog2Right.SetText(str(Message))
					else:
						self.ErrorLogRight.SetText(str(Message))
				else:
					self.ErrorLog2.SetText(str(Message))
			else:
				self.ErrorLog.SetText(str(Message))
		if WHISPER_TYPE != "" and (int(self.CountWhisperSpamEditLine.GetText()) > 0 or str(self.CountWhisperSpamEditLine.GetText()) == "") and str(self.DelayWhisperSpamEditLine.GetText()) != "" and WhisperColour != "" and int(WhisperCount) == 0:
			WhisperDelay = int(self.DelayWhisperSpamEditLine.GetText())
			WhisperAmount = int(self.CountWhisperSpamEditLine.GetText())
			self.LastChange.SetText("El spamBot ha comenzado!")
			WhisperActivity = "Spam"
			self.WhisperSpam()
		
	def WhisperSpam(self):
		global WhisperColour
		global WHISPER_TYPE
		global WhisperCount
		global WhisperDelay
		global WhisperAmount
		global WhisperActivity
		global ScanStart
		global ScanEnd
		if int(WhisperAmount) > int(WhisperCount):
			if WhisperColour != "Random":
				if WhisperActivity == "Spam":
					if str(WHISPER_TYPE) == "Player":
						net.SendWhisperPacket(str(self.PlayerWhisperSpamEditLine.GetText()), str(WhisperColour) + str(self.WhisperSpamEditLine.GetText()))							
						self.LastChange.SetText("Canditdad elegida: " + str(WhisperCount))
					elif str(WHISPER_TYPE) == "All":
						for i in xrange(ScanStart, ScanEnd):
							Player = chr.GetNameByVID(i)
							Race = chr.GetInstanceType(i)
							PlayerName = player.GetName()
							if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != "None" and str(Player) != "" and str(Player) != str(PlayerName):
								net.SendWhisperPacket(str(Player), str(WhisperColour) + str(self.WhisperSpamEditLine.GetText()))							
								self.LastChange.SetText("Cantidad elegida: " + str(WhisperCount))
			elif WhisperColour == "Random":
				if WhisperActivity == "Spam":
					if str(WHISPER_TYPE) == "Player":
						net.SendWhisperPacket(str(self.PlayerWhisperSpamEditLine.GetText()), "|c"+ str(self.random_color()) +"|H|h " + str(self.WhisperSpamEditLine.GetText()))							
						self.LastChange.SetText("Cantidad elegida: " + str(WhisperCount))
					elif str(WHISPER_TYPE) == "All":
						for i in xrange(ScanStart, ScanEnd):
							Player = chr.GetNameByVID(i)
							Race = chr.GetInstanceType(i)
							PlayerName = player.GetName()
							if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != "None" and str(Player) != "" and str(Player) != str(PlayerName):
								net.SendWhisperPacket(str(Player), "|c"+ str(self.random_color()) +"|H|h " + str(self.WhisperSpamEditLine.GetText()))							
								self.LastChange.SetText("Cantidad elegida: " + str(WhisperCount))
			if WhisperActivity == "Spam":
				WhisperCount += 1
				self.WaitingDelay = WaitingDialog()
				self.WaitingDelay.Open(float(WhisperDelay))
				self.WaitingDelay.SAFE_SetTimeOverEvent(self.WhisperSpam)
		else:
			WhisperCount = 0
			self.LastChange.SetText("El spamBot ha finalizado con exito")
	
	def random_color(self):
		COLOR_RANGE = (50, 255)
		
		rgb = list()
		for c in range(0, 4):
			rgb.append(app.GetRandom(COLOR_RANGE[0], COLOR_RANGE[1]))
    
		return "".join([hex(c)[2:].upper() for c in rgb])

	def SetVIDRange(self):
		global ScanStart
		global ScanEnd
		for i in range(500, 3000000):
			Player = chr.GetNameByVID(i)
			Race = chr.GetInstanceType(i)
			if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != "None" and str(Player) != "":
				ScanStart = int(i-500)
				ScanEnd = int(i+50000)
				break


	def Creditosfrancoiz(self):

		os.system("start http://www.youtube.com/user/xFrancoizx")

	def Spamfrancoiz(self):
		chattext = self.InputText1.GetText()
		chatSegundos = self.InputSegundos1.GetText()
		
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
		net.SendChatPacket(chattext, chat.CHAT_TYPE_SHOUT)
		
		self.dela = WaitingDialog()
		self.dela.Open(int(chatSegundos))
		self.dela.SAFE_SetTimeOverEvent(self.NormalSpam)



	


	def TeleportToCoordinates(self):
		global telestep
		global teleport_mode
		x_coordinate = self.TeleportXEditLine.GetText()
		y_coordinate = self.TeleportYEditLine.GetText()
		z_coordinate = self.TeleportZEditLine.GetText()
		x_coordinate = int(x_coordinate)*100
		y_coordinate = int(y_coordinate)*100
		z_coordinate = int(z_coordinate)*100
		(ax, ay, az) = player.GetMainCharacterPosition()
		teleport_mode = 1
		
###Teleport.35cRe.TR.design		
		if int(x_coordinate) < int(ax):
			while int(x_coordinate) < int(ax):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax) - 2000, int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
				
			chr.SetPixelPosition(int(x_coordinate), int(ay))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(x_coordinate) > int(ax):
			while int(x_coordinate) > int(ax):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax) + 2000, int(ay))
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
				
			chr.SetPixelPosition(int(x_coordinate), int(ay))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(y_coordinate) < int(ay):
			while int(y_coordinate) < int(ay):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax), int(ay) - 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1
			
			chr.SetPixelPosition(int(ax), int(y_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(y_coordinate) > int(ay):
			while int(y_coordinate) > int(ay):
				if telestep > 10:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax), int(ay) + 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(y_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

		if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
			while int(z_coordinate) < int(az):
				if telestep > 7:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax), int(ay), int(az) - 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
			
		if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
			while int(z_coordinate) > int(az):
				if telestep > 7:
					chat.AppendChat(chat.CHAT_TYPE_INFO, "Por favor espere 5 segundos..")
					return
				chr.SetPixelPosition(int(ax), int(ay), int(az) + 2000)
				player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
				player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
				(ax, ay, az) = player.GetMainCharacterPosition()
				telestep = telestep + 1

			chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
			player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
			player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
		
		teleport_mode = 0








	def EqChange(self):
		ArmorValue = self.ArmorEditLine.GetText()
		WeaponValue = self.WeaponEditLine.GetText()
		HairValue = self.HairEditLine.GetText()
		if ArmorValue == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte gebe eine Rüstungsvalue ein!") 
		if WeaponValue == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte gebe eine Waffenvalue ein!")
		if HairValue == "":
			chat.AppendChat(chat.CHAT_TYPE_INFO, "Bitte gebe eine Haarvalue ein!")
		else:	
			chr.SetArmor(int(ArmorValue))
			chr.SetWeapon(int(WeaponValue))
			chr.SetHair(int(HairValue))
			chr.Refresh()


	def Combo(self):
		
		global Combo
		
		if Combo == 0:
			Combo = 1
			self.ComboTypeButton.SetText("Activado")
			chr.testSetComboType(2)
		else:	
			Combo = 0
			self.ComboTypeButton.SetText("Desactivado")
			chr.testSetComboType(0)

			
	def RefineOneTime(self):
	
		global Refine
	
		if Refine == 0:
			Refine = 1
			net.SendRefinePacket(int(0), int(0))    
		else:	
			Refine = 0
			net.SendRefinePacket(int(0), int(0))
		


	def GhostMod(self):
		
		chr.Revive()


	def SetTapferkeitsUmhange(self):
		global TapferkeitsUmhange
		if TapferkeitsUmhange == "":	
			TapferkeitsUmhange = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")
			self.TapferkeitsUmhangeButtonActivated.Show()
			self.TapferkeitsUmhangeImageActivated.Show()
			self.UseTapferkeitsUmhange()
		else:
			TapferkeitsUmhange = ""
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")
			self.TapferkeitsUmhangeButtonActivated.Hide()
			self.TapferkeitsUmhangeImageActivated.Hide()
			
	def UseTapferkeitsUmhange(self):
		if TapferkeitsUmhange != "":
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				ItemValue = player.GetItemIndex(i)
				if ItemValue == 70038:
					TapferkeitsUmhangeWaitingDelay = self.TapferkeitsUmhangeDelay.GetText()
					net.SendItemUsePacket(i)
					self.TapferkeitsUmhangDelay = WaitingDialog()
					self.TapferkeitsUmhangDelay.Open(int(TapferkeitsUmhangeWaitingDelay))
					self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.UseTapferkeitsUmhange)
					break
		else:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")	


	def AttackSpeedStatus(self):
		global AttackSpeedHack
		CurrentAttackSpeedHack = self.AttackSpeedStats.GetText()
		if AttackSpeedHack == "":
			AttackSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")
			chr.SetAttackSpeed(int(CurrentAttackSpeedHack))
			self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_03.sub")
			self.AttackSpeedStatusButton.SetText("Activado")
		elif int(CurrentAttackSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")		
		else:
			if int(CurrentAttackSpeedHack) > 0.01:
				AttackSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
				chr.SetAttackSpeed(int(player.GetStatus(player.ATT_SPEED)))
				self.AttackSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
				self.AttackSpeedStatusButton.SetText("Desactivado")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")		
			
	
	def MoveSpeedStatus(self):
		global MoveSpeedHack
		CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
		if MoveSpeedHack == "":
			MoveSpeedHack = 1
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")
			chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
			if int(CurrentMoveSpeedHack) > 200:
				self.MoveSpeedFix = WaitingDialog()
				self.MoveSpeedFix.Open(0.5)
				self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)
			self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_03.sub")
			self.MoveSpeedStatusButton.SetText("Activado")
		elif int(CurrentMoveSpeedHack) < 0.01:
			chat.AppendChat(chat.CHAT_TYPE_INFO, "")		
		else:
			if int(CurrentMoveSpeedHack) > 0.01:
				MoveSpeedHack = ""
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
				chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
				self.MoveSpeedStatusButton.SetUpVisual("d:/ymir work/ui/public/middle_button_01.sub")
				self.MoveSpeedStatusButton.SetText("Desactivado")
			else:
				chat.AppendChat(chat.CHAT_TYPE_INFO, "")
				
	def MoveSpeedHackFixLoop1(self):
		chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
		self.MoveSpeedHackFixLoop2()

	def MoveSpeedHackFixLoop2(self):
		global MoveSpeedHack
		if MoveSpeedHack != "":
			CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
			chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
			self.MoveSpeedFix = WaitingDialog()
			self.MoveSpeedFix.Open(0.5)
			self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)				


	def ZoomHack(self):
		
		global ZoomHack
		
		if ZoomHack == 0:
			ZoomHack = 1
			self.ZoomHackButton.SetText("Activado")
			app.SetCameraMaxDistance(100000)	
		else:	
			ZoomHack = 0
			self.ZoomHackButton.SetText("Desactivado")
			app.SetCameraMaxDistance(2500)	
	
	def NoFog(self):
	
		global NoFog
		
		if NoFog == 0:
			NoFog = 1
			self.NoFogButton.SetText("Activado")
			app.SetMinFog(900000)
		else:	
			NoFog = 0
			self.NoFogButton.SetText("Desactivado")
			app.SetMinFog(2500)

	def DayNight(self):
	
		global DayNight
		
		if DayNight == 0:
			DayNight = 1
			self.DayNightButton.SetText("Noche")
			background.SetEnvironmentData(1)
			background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
			
		else:	
			DayNight = 0
			self.DayNightButton.SetText("Dia")
			background.SetEnvironmentData(0)
			
	def EnableSnow(self):
		
		global EnableSnow
		
		if EnableSnow == 0:
			EnableSnow = 1
			self.SnowButton.SetText("Nieve")
			background.EnableSnow(1)
		else:	
			EnableSnow = 0
			self.SnowButton.SetText("Desactivado")
			background.EnableSnow(0)


	def AutoRedPot(self):

		global AutoRedPot
		
		if AutoRedPot == 0:
			AutoRedPot = 1
			self.AutoRedPotButton.SetText("Activado")
			self.EnableRedAutoPotting()
			
		else:	
			AutoRedPot = 0
			self.AutoRedPotButton.SetText("Desactivado")
			self.DisableRedAutoPotting()
			
	def EnableRedAutoPotting(self):
		
		MaxTP = player.GetStatus(player.MAX_HP)
		ActualTP = player.GetStatus(player.HP)
		RedPercentValue = self.EditLineRedPotting.GetText()
		
		if (float(ActualTP) / (float(MaxTP)) * 100) < int(RedPercentValue):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				RedPott = player.GetItemIndex(i)
				if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableRedAutoPotting)
			
	def DisableRedAutoPotting(self):
		
		for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				RedPott = player.GetItemIndex(i)
				if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableRedAutoPotting)


	def AutoBluePot(self):

		global AutoBluePot
		
		if AutoBluePot == 0:
			AutoBluePot = 1
			self.AutoBluePotButton.SetText("Activado")
			self.EnableBlueAutoPotting()
			
		else:	
			AutoBluePot = 0
			self.AutoBluePotButton.SetText("Desactivado")
			self.DisableBlueAutoPotting()
			
	def EnableBlueAutoPotting(self):

		MaxSP = player.GetStatus(player.MAX_SP)
		ActualSP = player.GetStatus(player.SP)
		BluePercentValue = self.EditLineBluePotting.GetText()
		
		if (float(ActualSP) / (float(MaxSP)) * 100) < int(BluePercentValue):
			for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				BluePott = player.GetItemIndex(i)
				if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
					net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableBlueAutoPotting)
			
	def DisableBlueAutoPotting(self):
		
		for i in xrange(player.INVENTORY_PAGE_SIZE*3):
				BluePott = player.GetItemIndex(i)
				if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
				#	net.SendItemUsePacket(i)
					break
					
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableBlueAutoPotting)

			
	def AutoAttack(self):
		
		global AutoAttack
		
		if AutoAttack == 0:
			AutoAttack = 1
			self.AutoAttackButton.SetText("Activado")	
			self.EnableAutoAttack()
		else:	
			AutoAttack = 0
			self.AutoAttackButton.SetText("Desactivado")
			self.DisableAutoAttack()
		
	def EnableAutoAttack(self):
	
		Direction = app.GetRandom(0,7)
		player.SetAttackKeyState(TRUE)
		chr.SetDirection(Direction)
		
		
		
		self.delay = WaitingDialog()
		self.delay.Open(int(1.0))
		self.delay.SAFE_SetTimeOverEvent(self.EnableAutoAttack)
			
	def DisableAutoAttack(self):
	
		player.SetAttackKeyState(FALSE)
		
		self.delay = WaitingDialog()
		self.delay.Open(int(99999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableAutoAttack)

		
	def AutoPickup(self):

		global AutoPickup
		
		if AutoPickup == 0:
			AutoPickup = 1
			self.AutoPickupButton.SetText("Activado")	
			self.EnableAutoPickup()
		else:	
			AutoPickup = 0
			self.AutoPickupButton.SetText("Desactivado")
			self.DisableAutoPickup()
		
	def EnableAutoPickup(self):
		
		
		
		player.PickCloseItem() 
		
		self.delay = WaitingDialog()
		self.delay.Open(int(0.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableAutoPickup)
			
	def DisableAutoPickup(self):
		
		player.PickCloseItem()
		
		self.delay = WaitingDialog()
		self.delay.Open(int(999999999999999999999999999999))
		self.delay.SAFE_SetTimeOverEvent(self.DisableAutoPickup)
		
	
	def AutoRestart(self):

		global AutoRestart
		
		if AutoRestart == 0:
			AutoRestart = 1
			self.AutoRestartButton.SetText("Activado")	
			self.EnableRestart()
		else:	
			AutoRestart = 0
			self.AutoRestartButton.SetText("Desactivado")
			self.DisableRestart()
		
	def EnableRestart(self):
		
		net.SendChatPacket("/restart_here")
	
		self.delay = WaitingDialog()
		self.delay.Open(int(2.5))
		self.delay.SAFE_SetTimeOverEvent(self.EnableRestart)
		


		
		
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
		
StartDialog = PickUP()
StartDialog.Board.Hide()