# uncompyle6 version 2.15.0
# Python bytecode 2.2 (60717)
# Decompiled from: Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)]
# Embedded file name: C:\Program Files (x86)\Metin2Guabina\MultihackbyFrancoiz.py
# Compiled at: 2013-11-21 20:26:15
import os, app, dbg, grp, item, background, chr, chrmgr, player, chat, textTail, snd, net, effect, wndMgr, fly, systemSetting, quest, guild, skill, messenger, locale, constInfo, exchange, time, ui, interfacemodule, shop, uiTip, pack, uiCommon, uiPrivateShopBuilder, sys, ime, miniMap
Pj = 0
Gmvisual = 0
Copiar = 0
Board1Button = ui.Button()
Board1Line = ui.TextLine()
CheckGM = 0
Habilidad1V = 0
Habilidad2V = 0
Habilidad3V = 0
Habilidad4V = 0
Habilidad5V = 0
Habilidad6V = 0
LibroBot = 0
teleport_mode = 0
telestep = 0
saved_x = 0
saved_y = 0
visible = FALSE
last_teleport_time = 0
TeleportButton = ui.Button()
textLine = ui.TextLine()
chat.AppendChat(chat.CHAT_TYPE_INFO, 'teleport-module loaded.')
miniMap.UnregisterAtlasWindow()
g_isCreatingWindow = 0
Buffbotstarten = 0
waitingdelay = 0
xBuff = 1
Refine = 0
MoveSpeed = 0
Combo = 0
ZoomHack = 0
Habilidades = 0
NoFog = 0
DayNight = 0
Pararcam = 0
EnableSnow = 0
TransferMobs = ''
AttackSpeedHack = ''
MoveSpeedHack = ''
TapferkeitsUmhange = ''
AutoRedPot = 0
AutoBluePot = 0
AutoPickup = 0
AutoRestart = 0
Modoespada = 0
Modoespada1 = 0
Modoespada2 = 0
ModoDaga1 = 0
ModoDaga2 = 0
ModoChaman1 = 0
ModoChaman2 = 0
ModoGeneral = 0
VidList = []
Ver = 0
AutoPottRed = ''
AutoPottBlue = ''
cRe35TURKMMO = ''
x0 = ''
y0 = ''
z0 = ''
x1 = ''
y1 = ''
x2 = ''
y2 = ''
radius = ''
TapferkeitsUmhange = ''
AutoPickUp = ''
AttackSpeedHack = ''
MoveSpeedHack = ''
telestep = 0
teleport_mode = 0
last_teleport_time = 0
DoublePrevent = 'inaktiv'
RestartBot = ''
Caballo = ''
spamming = 0
Modo = 1
SpambotButton = ui.Button()
SpambotLine = ui.TextLine()
ShortButton = ui.Button()
ShortLine = ui.TextLine()
WHISPER_TYPE = ''
WhisperCount = 0
WhisperColour = ''
WhisperDelay = 0
WhisperAmount = 0
WhisperActivity = ''
ScanStart = 0
ScanEnd = 0
CHAT_TYPE = ''
Count = 0
ChatColour = ''
Delay = 0
Amount = 0
Activity = 'Pause'
Activar = 0
LevelbotModo0 = 0
LevelbotModo1 = 0
LevelbotModo2 = 0

class FishingBot(ui.Window):
    Gui = []
    state = 'Stop'
    KillFishList = []
    TrashList = []
    Config = (2.5, 1.0)
    UseSmallFishAsBait = 0

    def __init__(self):
        ui.Window.__init__(self)
        self.AddGui()

    def __del__(self):
        self.Gui[0].Hide()

    def GuiParser(self, guiobjects, list):
        for object in guiobjects:
            Object = object[0][0]()
            if object[0][1] != '':
                Object.SetParent(list[object[0][1]])
            if object[1][0] + object[1][1] != 0:
                Object.SetSize(object[1][0], object[1][1])
            if object[2][0] + object[2][1] != 0:
                Object.SetPosition(object[2][0], object[2][1])
            for command in object[3]:
                cmd = command[0]
                attr = getattr(Object, cmd)
                if callable(attr):
                    argument = command[1]
                    lenght = len(argument)
                    if lenght == 1:
                        if argument[0] == '':
                            attr()
                        else:
                            attr(argument[0])
                    else:
                        if lenght == 2:
                            attr(argument[0], argument[1])
                        else:
                            if lenght == 3:
                                attr(argument[0], argument[1], argument[2])
                            else:
                                if lenght == 4:
                                    attr(argument[0], argument[1], argument[2], argument[3])

            for flag in object[4]:
                Object.AddFlag(str(flag))

            Object.Show()
            list.append(Object)

    def AddGui(self):
        Gui = [
         [[ui.Board, ''], [350, 330],
          [
           0,
           0],
          [
           [
            'SetPosition',
            [
             0, 0]]], ['movable', 'float']], [[ui.Button, 0], [0, 0], [320, 20], [['SetUpVisual', ['d:/ymir work/ui/public/close_button_01.sub']], ['SetOverVisual', ['d:/ymir work/ui/public/close_button_02.sub']], ['SetDownVisual', ['d:/ymir work/ui/public/close_button_03.sub']], ['SetToolTipText', ['Cerrar', 0, -23]], ['SetEvent', [lambda : self.__del__()]]], []], [[ui.Button, 0], [0, 0], [75, 180], [['SetUpVisual', ['d:/ymir work/ui/public/large_button_01.sub']], ['SetOverVisual', ['d:/ymir work/ui/public/large_button_02.sub']], ['SetDownVisual', ['d:/ymir work/ui/public/large_button_03.sub']], ['SetText', ['Comenzar']], ['SetEvent', [lambda : self.ChangeState('Start')]]], []], [[ui.Button, 0], [0, 0], [180, 180], [['SetUpVisual', ['d:/ymir work/ui/public/large_button_01.sub']], ['SetOverVisual', ['d:/ymir work/ui/public/large_button_02.sub']], ['SetDownVisual', ['d:/ymir work/ui/public/large_button_03.sub']], ['SetText', ['Parar']], ['SetEvent', [lambda : self.ChangeState('Bot parado!.')]]], []], [[ui.TextLine, 0], [0, 0], [135, 18], [['SetDefaultFontName', ['']], ['SetText', ['Bot de pesca v1.0']]], []], [[ui.TextLine, 0], [0, 0], [100, 40], [['SetDefaultFontName', ['']], ['SetText', [' ']]], []], [[ui.TextLine, 0], [0, 0], [30, 70], [['SetDefaultFontName', ['']], ['SetText', ['Tiempo al pescar:']]], []], [[ui.SliderBar, 0], [0, 0], [112, 73], [['SetEvent', [ui.__mem_func__(self.SetConfig)]], ['SetSliderPos', [0.28]]], []], [[ui.TextLine, 0], [0, 0], [292, 70], [['SetDefaultFontName', ['']], ['SetText', ['|cFFFFAA00|H|h2.5 s']]], []], [[ui.TextLine, 0], [0, 0], [30, 100], [['SetDefaultFontName', ['']], ['SetText', ['Por cada pez:']]], []], [[ui.SliderBar, 0], [0, 0], [99, 102], [['SetEvent', [ui.__mem_func__(self.SetConfig)]], ['SetSliderPos', [0.5]]], []], [[ui.TextLine, 0], [0, 0], [283, 100], [['SetDefaultFontName', ['']], ['SetText', ['|cFFFFAA00|H|h1.0 s']]], []], [[ui.TextLine, 0], [0, 0], [30, 135], [['SetDefaultFontName', ['']], ['SetText', ['Usar pez pequeno:']]], []], [[ui.TextLine, 0], [0, 0], [35, 220], [['SetDefaultFontName', ['']], ['SetText', ['Tiempo al pescar: 2.5 segundo/s']]], []], [[ui.TextLine, 0], [0, 0], [35, 245], [['SetDefaultFontName', ['']], ['SetText', ['Tiempo despues de cada pez: 1 segundo/s']]], []], [[ui.TextLine, 0], [0, 0], [135, 40], [['SetDefaultFontName', ['']], ['SetText', [' ']]], []], [[ui.TextLine, 0], [0, 0], [250, 300], [['SetDefaultFontName', ['']], ['SetText', ['By Francoiz']]], []]]
        self.GuiParser(Gui, self.Gui)
        self.FaceButton()
        self.fischies = []
        self.Gui[0].Hide()
        for i in xrange(27803, 27824):
            self.fischies.append(i)

        self.FishingItems = [27987, 70201, 70202, 70203, 70204, 70205, 70206, 70048, 70049, 70050, 70051]
        for bla in self.FishingItems:
            self.fischies.append(bla)

        tmp = []
        Modi = ['Si', 'No']
        x = 135
        for mode in Modi:
            button = [[ui.Button, 0], [0, 0], [x, 130], [['SetUpVisual', ['d:/ymir work/ui/public/small_button_01.sub']], ['SetOverVisual', ['d:/ymir work/ui/public/small_button_02.sub']], ['SetDownVisual', ['d:/ymir work/ui/public/small_button_03.sub']], ['SetText', [mode]], ['SetEvent', [lambda arg=Modi.index(mode): self.UseSmallFishes(arg)]]], []]
            tmp.append(button)
            x += 48

        x = 40
        y = 70
        self.GuiParser(tmp, self.Gui)

    def FaceButton(self):
        global BotonskillButton
        global BotonskillText
        BotonskillButton = ui.Button()
        BotonskillButton.SetText('')
        BotonskillButton.SetPosition(wndMgr.GetScreenWidth() - 100, 430)
        BotonskillButton.SetSize(88, 21)
        BotonskillButton.SetEvent(ui.__mem_func__(self.Mostrar))
        BotonskillButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        BotonskillButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        BotonskillButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        BotonskillButton.Show()
        BotonskillText = ui.TextLine()
        BotonskillText.SetParent(BotonskillButton)
        BotonskillText.SetVerticalAlignCenter()
        BotonskillText.SetHorizontalAlignCenter()
        BotonskillText.SetPosition(43, 10)
        BotonskillText.SetText('Pesca')
        BotonskillText.Show()

    def Mostrar(self):
        self.Gui[0].Show()

    def UseSmallFishes(self, mode):
        if mode == 1:
            self.UseSmallFishAsBait = 0
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Pez pequeno: Descativado')
        else:
            self.UseSmallFishAsBait = 1
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Pez pequeno: Activado')

    def SelectFish(self, fish):
        try:
            self.fischies.index(27803 + fish)
            try:
                self.KillFishList.remove(int(27803 + fish))
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + item.GetItemName(item.SelectItem(27803 + fish)) + ' No matar al pescar')
            except:
                self.KillFishList.append(int(27803 + fish))
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + item.GetItemName(item.SelectItem(27803 + fish)) + ' Matar al pescar')

        except:
            ItemName = item.GetItemName(item.SelectItem(self.FishingItems[fish - len(self.fischies)]))
            try:
                self.KillFishList.remove(self.FishingItems[fish - len(self.fischies)])
                if ItemName == item.GetItemName(item.SelectItem(27987)):
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + ItemName + ' No Tirar al pescar')
                else:
                    self.TrashList.remove(self.FishingItems[fish - len(self.fischies)])
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + ItemName + ' No Tirar al pescar')
            except:
                if ItemName == item.GetItemName(item.SelectItem(27987)):
                    self.KillFishList.append(self.FishingItems[fish - len(self.fischies)])
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + ItemName + ' No Tirar al pescar')
                else:
                    self.TrashList.append(self.FishingItems[fish - len(self.fischies)])
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, '' + ItemName + ' Tirar al pescar')

    def SetConfig(self):
        Delay, Tolerance = self.Config
        if self.Gui[7].GetSliderPos() * 9 + 1 != Delay:
            Delay = self.Gui[7].GetSliderPos() * 9 + 1
            try:
                Tmp = str(Delay).split('.')
                Delay = str(Tmp[0]) + '.' + Tmp[1][:1]
            except:
                pass
            else:
                self.Gui[8].SetText(str('|cFFFFAA00|H|h' + Delay) + ' s')
                self.Gui[13].SetText(str('Tiempo al pescar: ' + Delay + ' segundo/s') + '')
        if self.Gui[10].GetSliderPos() * 2 != Tolerance:
            Tolerance = self.Gui[10].GetSliderPos() * 2
            try:
                Tmp = str(Tolerance).split('.')
                Tolerance = str(Tmp[0]) + '.' + Tmp[1][:1]
            except:
                pass
            else:
                self.Gui[11].SetText(str('|cFFFFAA00|H|h' + Tolerance) + ' s')
                self.Gui[14].SetText(str('Tiempo despues de cada pez: ' + Tolerance) + ' segundo/s')
        self.Config = (Delay, Tolerance)

    def ChangeState(self, arg):
        chat.AppendChat(1, str(arg))
        self.state = arg
        if arg == 'Start':
            if self.AddBait():
                self.ProcessTimeStamp = app.GetTime()
                self.FishAction()
                self.state = 'Waiting'
        else:
            self.FishAction()

    def OnRender(self):
        if self.state == 'Stop':
            return
        if self.state == 'Start':
            if self.ProcessTimeStamp + 6.0 < app.GetTime():
                if self.AddBait():
                    self.FishAction()
                    self.ProcessTimeStamp = app.GetTime()
                    self.state = 'Waiting'
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Bot continua...')
        if self.state == 'Fish':
            if self.ProcessTimeStamp + float(self.Config[0]) < app.GetTime():
                self.FishAction()
                self.ProcessTimeStamp = app.GetTime()
                self.state = 'Start'
        if self.state == 'Waiting':
            if not chrmgr.IsPossibleEmoticon(-1):
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, '')
                self.ProcessTimeStamp = app.GetTime() + float(self.RandomTolerance())
                self.state = 'Fish'
            if self.ProcessTimeStamp + 48.0 < app.GetTime():
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, '')
                self.ProcessTimeStamp = app.GetTime()
                self.state = 'Start'

    def RandomTolerance(self):
        Tolerance = float(self.Config[1]) * 10
        Rnd = app.GetRandom(0, int(Tolerance))
        return DivideToFloat(Rnd, 10)

    def FishAction(self):
        player.SetAttackKeyState(TRUE)
        player.SetAttackKeyState(FALSE)

    def UseFishBait(self):
        return self.UseSmallFishAsBait

    def AddBait(self):
        for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE * 2):
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

        if self.UseFishBait():
            if player.GetItemCountByVnum(27802) > 0:
                for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE * 2):
                    ItemValue = player.GetItemIndex(InventorySlot)
                    if ItemValue == 27802:
                        net.SendItemUsePacket(InventorySlot)
                        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '')
                        return 1

        Baits = [27800, 27801]
        Baitcount = 0
        for bait in Baits:
            Baitcount += player.GetItemCountByVnum(bait)

        if Baitcount <= 0:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'ERROR - Recuerde tener una caa(cania) y gusanos o algun cebo en su inventario.')
            self.state = 'Stop'
            return 0
        for InventorySlot in xrange(player.INVENTORY_PAGE_SIZE * 2):
            ItemValue = player.GetItemIndex(InventorySlot)
            try:
                Baits.index(ItemValue)
                net.SendItemUsePacket(InventorySlot)
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Bot comenzado.')
                return 1
            except:
                pass


def IsDivideAble(x, y):
    if x == 0:
        return
    if float(x / y) == DivideToFloat(x, y):
        return 1


def DivideToFloat(x, y):
    y = x * y ** (-1)
    return y


FishingBot().Show()

class PickUpBot(ui.ScriptWindow):
    MODE_YANG = 2
    MODE_ALL = 1

    def __init__(self, parentUI, mode=0):
        ui.ScriptWindow.__init__(self)
        self.iPL = []
        self.Run = 1
        self.delay = 0.003
        self.NYList = []
        self.mode = mode
        self.parentUI = parentUI

    def SetMode(self, mode):
        if mode == PickUpBot.MODE_ALL:
            self.GetVIDs = self.GetItems
        else:
            if mode == PickUpBot.MODE_YANG:
                self.GetVIDs = self.GetYang
        self.mode = mode

    def SetGhostmode(self, flag=TRUE):
        self.Ghostmode = flag

    def __del__(self):
        self.Cancel()
        ui.ScriptWindow.__del__(self)

    def Cancel(self):
        self.Run = 0

    def PickList(self, ToPick):
        for i in ToPick:
            time.sleep(self.delay)
            self.sendPickUp(i)

    def Revive(self):
        pass

    def GetItems(self):
        List = []
        Picker = textTail.Pick
        for y in xrange(125, 600, 9):
            for x in xrange(300, 825, 31):
                iVID = Picker(x, y)
                if iVID != -1 and iVID not in List:
                    List.append(iVID)

        return List

    def GetVIDs(self):
        pass

    def GetYang(self):
        List = []
        Picker = textTail.Pick
        for y in xrange(125, 600, 9):
            for x in xrange(300, 825, 25):
                FirstCoord = None
                LastCoord = None
                iVID = Picker(x, y)
                if iVID != -1:
                    if iVID not in self.NYList and iVID not in List:
                        for i in xrange(1, 29):
                            if Picker(x - i, y) != iVID:
                                FirstCoord = x - i + 1
                                break

                        if FirstCoord == None:
                            self.NYList.append(iVID)
                            continue
                        for i in xrange(1, 29):
                            if Picker(FirstCoord + i, y) != iVID:
                                LastCoord = FirstCoord + i - 1
                                break

                        if LastCoord == None:
                            self.NYList.append(iVID)
                            continue
                        List.append(iVID)

        return List
        return

    def CountEvents(self, count):
        self.parentUI.GhostLeftTimer(count)
        chr.Revive()

    def OnUpdate(self):
        if not self.Run:
            return
        sendPickUp = net.SendItemPickUpPacket
        for item in self.GetVIDs():
            sendPickUp(item)

    def Start(self):
        self.Run = 1
        if self.mode == 0:
            self.parentUI.UseDefaultModus()
        self.isAlive = 1
        self.Show()

    def FlagRun(self):
        self.Run = 1

    def Stop(self):
        self.Run = 0
        self.Hide()


class CountDown(ui.ScriptWindow):

    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.eventTimeOver = lambda *arg: None
        self.eventExit = lambda *arg: None
        self.eventCountEvent = lambda *arg: None

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Open(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + 1
        self.Counter = waitTime + 1
        self.Show()

    def Close(self):
        self.Hide()

    def Destroy(self):
        self.Hide()

    def SAFE_SetTimeOverEvent(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    def SAFE_SetCountEvent(self, event):
        self.eventCountEvent = ui.__mem_func__(event)

    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.endTime = time.clock() + 1
            self.Counter -= 1
            self.eventCountEvent(self.Counter)
            if self.Counter < 1:
                self.Close()
                self.eventTimeOver()


UPversion = '2.4_2'
Pversion = '1.0'
Pdate = '20.01.2013'

class Dialog1(ui.Window):

    def __init__(self):
        ui.Window.__init__(self)
        self.PickUpBot = PickUpBot(self)
        self.BuildWindow()
        self.x = net.SendItemDropPacketNew
        net.SendItemDropPacketNew = self.DropPacketNew

    def DropPacketNew(self, *args):
        self.PickUpBot.Run = 0
        self.XX = CountDown()
        self.XX.eventTimeOver = lambda SLF=self.PickUpBot: SLF.FlagRun()
        self.XX.Open(5)
        return self.x(*args)

    def __del__(self):
        ui.Window.__del__(self)

    def BuildWindow(self):
        self.Ghostmode = 0
        self.Board = ui.BoardWithTitleBar()
        self.Board.SetSize(299, 120)
        self.Board.SetCenterPosition()
        self.Board.AddFlag('movable')
        self.Board.AddFlag('float')
        self.Board.SetTitleName('Hack Francoiz - Pick hack')
        self.Board.SetCloseEvent(self.Board.Hide)
        self.Board.Hide()
        self.__BuildKeyDict()
        self.FaceButton()
        self.comp = Component()
        self.btnActiv = self.comp.Button(self.Board, 'Desactivado', '', 20, 75, self.ActivFunc, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.title = self.comp.TextLine(self.Board, 'Velocidad:', 15, 49, self.comp.RGB(255, 255, 255))
        self.Speed = self.comp.SliderBar(self.Board, 0.0, self.SetPickSpeed, 64, 51)
        self.lblSpeed = self.comp.TextLine(self.Board, '100', 245, 49, self.comp.RGB(255, 255, 255))

    def FaceButton(self):
        global Boton01Button
        global Boton01Text
        Boton01Button = ui.Button()
        Boton01Button.SetText('')
        Boton01Button.SetPosition(wndMgr.GetScreenWidth() - 100, 400)
        Boton01Button.SetSize(88, 21)
        Boton01Button.SetEvent(ui.__mem_func__(self.Board.Show))
        Boton01Button.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        Boton01Button.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        Boton01Button.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        Boton01Button.Show()
        Boton01Text = ui.TextLine()
        Boton01Text.SetParent(Boton01Button)
        Boton01Text.SetVerticalAlignCenter()
        Boton01Text.SetHorizontalAlignCenter()
        Boton01Text.SetPosition(43, 10)
        Boton01Text.SetText('Pick')
        Boton01Text.Show()

    def ActivFunc(self):
        global Activar
        if Activar == 0:
            Activar = 1
            self.btnActiv.SetText('Activado')
            self.PickUpBot.Start()
        else:
            Activar = 0
            self.btnActiv.SetText('Desactivado')
            self.PickUpBot.Stop()

    def GhostLeftTimer(self, count):
        pass

    def btnYang_func(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_YANG)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))

    def btnEvery_func(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_ALL)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))

    def UseDefaultModus(self):
        self.PickUpBot.SetMode(PickUpBot.MODE_ALL)
        self.btnYang.ButtonText.SetFontColor(*self.comp.RGB(255, 255, 255))
        self.btnEvery.ButtonText.SetFontColor(*self.comp.RGB(200, 200, 200))

    def SetPickSpeed(self):
        speed = int(self.Speed.GetSliderPos() * 1000)
        if speed < 100:
            speed = 100
        self.lblSpeed.SetText(str(speed))
        self.PickUpBot.Movespeed = speed

    def __BuildKeyDict(self):
        onPressKeyDict = {}
        onPressKeyDict[app.DIK_F5] = lambda : self.OpenWindow()
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
        return

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
        return

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
        return (SlotBar, Value)
        return

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
        return

    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)

    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        if parent != None:
            Slider.SetParent(parent)
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos / 100)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider
        return

    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        if parent != None:
            image.SetParent(parent)
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image
        return

    def ComboBox(self, parent, text, x, y, width):
        combo = ui.ComboBox()
        if parent != None:
            combo.SetParent(parent)
        combo.SetPosition(x, y)
        combo.SetSize(width, 15)
        combo.SetCurrentItem(text)
        combo.Show()
        return combo
        return

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
        return

    def Gauge(self, parent, width, color, x, y):
        gauge = ui.Gauge()
        if parent != None:
            gauge.SetParent(parent)
        gauge.SetPosition(x, y)
        gauge.MakeGauge(width, color)
        gauge.Show()
        return gauge
        return

    def ListBoxEx(self, parent, x, y, width, heigh):
        bar = ui.Bar()
        if parent != None:
            bar.SetParent(parent)
        bar.SetPosition(x, y)
        bar.SetSize(width, heigh)
        bar.SetColor(1996488704)
        bar.Show()
        ListBox = ui.ListBoxEx()
        ListBox.SetParent(bar)
        ListBox.SetPosition(0, 0)
        ListBox.SetSize(width, heigh)
        ListBox.Show()
        scroll = ui.ScrollBar()
        scroll.SetParent(ListBox)
        scroll.SetPosition(width - 15, 0)
        scroll.SetScrollBarSize(heigh)
        scroll.Show()
        ListBox.SetScrollBar(scroll)
        return (bar, ListBox)
        return


Dialog1().Show()

class MapTextToolTip(ui.Window):

    def __init__(self):
        ui.Window.__init__(self)
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetHorizontalAlignCenter()
        textLine.SetOutline()
        textLine.SetHorizontalAlignRight()
        textLine.Show()
        self.textLine = textLine

    def __del__(self):
        ui.Window.__del__(self)

    def SetText(self, text):
        self.textLine.SetText(text)

    def SetTooltipPosition(self, PosX, PosY):
        self.textLine.SetPosition(PosX - 5, PosY)

    def SetTextColor(self, TextColor):
        self.textLine.SetPackedFontColor(TextColor)

    def GetTextSize(self):
        return self.textLine.GetTextSize()


class TeleportHackDialog(ui.ScriptWindow):

    class AtlasRenderer(ui.Window):

        def __init__(self):
            ui.Window.__init__(self)
            self.AddFlag('not_pick')

        def OnUpdate(self):
            miniMap.UpdateAtlas()

        def OnRender(self):
            global saved_x
            global last_teleport_time
            global saved_y
            global teleport_mode
            global telestep
            x, y = self.GetGlobalPosition()
            fx = float(x)
            fy = float(y)
            miniMap.RenderAtlas(fx, fy)
            telestep = 0
            if teleport_mode == 1 and app.GetTime() > last_teleport_time + 5:
                last_teleport_time = app.GetTime()
                self.local_Teleport(saved_x, saved_y)
            if app.IsPressed(app.DIK_LSHIFT) == FALSE:
                self.new_teleport_possible = TRUE
            if app.IsPressed(app.DIK_LSHIFT) and self.new_teleport_possible == TRUE:
                self.new_teleport_possible = FALSE
                IsAtlasAvailable, height, width = miniMap.GetAtlasSize()
                if IsAtlasAvailable:
                    xMouse, yMouse = wndMgr.GetMousePosition()
                    if xMouse >= x and xMouse <= x + height and yMouse >= y and yMouse <= y + width:
                        self.local_Teleport((xMouse - x) * 6, (yMouse - y) * 6)

        def local_Teleport(self, ltX, ltY):
            global saved_x
            global saved_y
            global teleport_mode
            global telestep
            teleport_mode = 1
            saved_x = ltX
            saved_y = ltY
            ax, ay, az = player.GetMainCharacterPosition()
            mapName, xBase, yBase = background.GlobalPositionToMapInfo(ax, ay)
            tX = int(ltX) * 100 + xBase
            tY = int(ltY) * 100 + yBase
            if int(tX) < int(ax):
                while int(tX) < int(ax):
                    if telestep > 20:
                        chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos')
                        return
                    chr.SetPixelPosition(int(ax) - 2000, int(ay), int(az))
                    player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                    player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                    ax, ay, az = player.GetMainCharacterPosition()
                    telestep = telestep + 1

                chr.SetPixelPosition(int(tX), int(ay), int(az))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
            if int(tX) > int(ax):
                while int(tX) > int(ax):
                    if telestep > 20:
                        chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos')
                        return
                    chr.SetPixelPosition(int(ax) + 2000, int(ay), int(az))
                    player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                    player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                    ax, ay, az = player.GetMainCharacterPosition()
                    telestep = telestep + 1

                chr.SetPixelPosition(int(tX), int(ay), int(az))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
            ax, ay, az = player.GetMainCharacterPosition()
            if int(tY) < int(ay):
                while int(tY) < int(ay):
                    if telestep > 20:
                        chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos')
                        return
                    chr.SetPixelPosition(int(ax), int(ay) - 2000, int(az))
                    player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                    player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                    ax, ay, az = player.GetMainCharacterPosition()
                    telestep = telestep + 1

                chr.SetPixelPosition(int(ax), int(tY), int(az))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
            if int(tY) > int(ay):
                while int(tY) > int(ay):
                    if telestep > 20:
                        chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos')
                        return
                    chr.SetPixelPosition(int(ax), int(ay) + 2000, int(az))
                    player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                    player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                    ax, ay, az = player.GetMainCharacterPosition()
                    telestep = telestep + 1

                chr.SetPixelPosition(int(ax), int(tY), int(az))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
            teleport_mode = 0

        def ShowAtlas(self):
            miniMap.ShowAtlas()

        def HideAtlas(self):
            miniMap.HideAtlas()

    def __init__(self):
        self.AtlasMainWindow = None
        self.tooltipInfo = MapTextToolTip()
        self.tooltipInfo.Hide()
        self.board = 0
        ui.ScriptWindow.__init__(self)
        return

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def LoadWindow(self):
        global textLine
        global TeleportButton
        try:
            pyScrLoader = ui.PythonScriptLoader()
            pyScrLoader.LoadScriptFile(self, 'UIScript/AtlasWindow.py')
        except:
            import exception
            exception.Abort('AtlasWindow.LoadWindow.LoadScript')
        else:
            try:
                self.board = self.GetChild('board')
                self.board.SetTitleName('Teleporter')
            except:
                import exception
                exception.Abort('AtlasWindow.LoadWindow.BindObject')

        self.AtlasMainWindow = self.AtlasRenderer()
        self.board.SetCloseEvent(self.Hide)
        self.AtlasMainWindow.SetParent(self.board)
        self.AtlasMainWindow.SetPosition(7, 30)
        self.tooltipInfo.SetParent(self.board)
        self.SetCenterPosition()
        self.Hide()
        miniMap.RegisterAtlasWindow(self)
        TeleportButton.SetText('')
        TeleportButton.SetPosition(wndMgr.GetScreenWidth() - 100, 310)
        TeleportButton.SetSize(88, 21)
        TeleportButton.SetEvent(self.Show)
        TeleportButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        TeleportButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        TeleportButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        TeleportButton.Show()
        textLine.SetParent(TeleportButton)
        textLine.SetPosition(43, 10)
        textLine.SetVerticalAlignCenter()
        textLine.SetHorizontalAlignCenter()
        textLine.SetText('Teleporter 2')
        textLine.Show()

    def Destroy(self):
        miniMap.UnregisterAtlasWindow()
        self.ClearDictionary()
        self.AtlasMainWindow = None
        self.board = None
        self.tooltipInfo = None
        return

    def Hide(self):
        if self.AtlasMainWindow:
            self.AtlasMainWindow.HideAtlas()
            self.AtlasMainWindow.Hide()
            TeleportButton.Show()
            textLine.Show()
        ui.ScriptWindow.Hide(self)

    def Show(self):
        global visible
        if self.AtlasMainWindow:
            bGet, iSizeX, iSizeY = miniMap.GetAtlasSize()
            if bGet:
                self.SetSize(iSizeX + 15, iSizeY + 38)
                self.board.SetSize(iSizeX + 15, iSizeY + 38)
                self.AtlasMainWindow.ShowAtlas()
                self.AtlasMainWindow.Show()
                TeleportButton.Show()
        ui.ScriptWindow.Show(self)
        visible = TRUE

    def OnUpdate(self):
        miniMap.ShowAtlas()
        if not self.tooltipInfo:
            return
        self.tooltipInfo.Hide()
        if FALSE == self.board.IsIn():
            return
        mouseX, mouseY = wndMgr.GetMousePosition()
        bFind, sName, iPosX, iPosY, dwTextColor, dwGuildID = miniMap.GetAtlasInfo(mouseX, mouseY)
        if FALSE == bFind:
            return
        if 'empty_guild_area' == sName:
            sName = locale.GUILD_EMPTY_AREA
        self.tooltipInfo.SetText('%s(%d, %d)' % (sName, iPosX, iPosY))
        x, y = self.GetGlobalPosition()
        self.tooltipInfo.SetTooltipPosition(mouseX - x, mouseY - y)
        self.tooltipInfo.SetTextColor(dwTextColor)
        self.tooltipInfo.Show()
        self.tooltipInfo.SetTop()

    def OnPressEscapeKey(self):
        global visible
        visible = FALSE
        self.Hide()
        return TRUE


mainui = TeleportHackDialog()
mainui.LoadWindow()
mainui.Hide()

def GetFakeString(name):
    return '|cffffff00|h%s' % name


def Azulcolor(name):
    return '|cFF0000FF|h%s' % name


def Griscolor(name):
    return '|cff888888|h%s' % name


def Verdecolor(name):
    return '|cff00ff00|h%s' % name


def Celestecolor(name):
    return '|cff00ccff|h%s' % name


def Bioletacolor(name):
    return '|cFF8A2BE2|h%s' % name


def Rojocolor(name):
    return '|cffff0000|h%s' % name


def Negrocolor(name):
    return '|cFF000000|h%s' % name


def Rojoclarocolor(name):
    return '|cffff6060|h%s' % name


def Azulclarocolor(name):
    return '|cffff00ff|h%s' % name


def Aguacolor(name):
    return '|cff00ffff|h%s' % name


def Otrocolor(name):
    return '|cFFFFE4C4|h%s' % name


class ColorShop(ui.Window):

    def __init__(self):
        uiPrivateShopBuilder.Clear()
        ui.Window.__init__(self)
        self.privateShopBuilder = uiPrivateShopBuilder.PrivateShopBuilder()
        self.privateShopBuilder.Close()
        self.board = ui.BoardWithTitleBar()
        self.board.SetSize(274, 200)
        self.board.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.board.AddFlag('movable')
        self.board.AddFlag('float')
        self.board.SetTitleName('Tienda color - Multihack by Francoiz')
        self.board.SetCloseEvent(ui.__mem_func__(self.Close))
        self.Infocolor = ui.TextLine()
        self.Infocolor.SetParent(self.board)
        self.Infocolor.SetDefaultFontName()
        self.Infocolor.SetPosition(23, 35)
        self.Infocolor.SetFeather()
        self.Infocolor.SetText('Nombre de la tienda:')
        self.Infocolor.SetOutline()
        self.Infocolor.Show()
        self.nameSlotBar = ui.SlotBar()
        self.nameSlotBar.SetParent(self.board)
        self.nameSlotBar.SetSize(118, 18)
        self.nameSlotBar.SetPosition(50, 34)
        self.nameSlotBar.SetWindowHorizontalAlignCenter()
        self.nameSlotBar.Show()
        self.nameEditLine = ui.EditLine()
        self.nameEditLine.SetParent(self.nameSlotBar)
        self.nameEditLine.SetSize(118, 17)
        self.nameEditLine.SetPosition(5, 2)
        self.nameEditLine.SetMax(20)
        self.nameEditLine.SetText('')
        self.GrisButton = ui.Button()
        self.GrisButton.SetParent(self.board)
        self.GrisButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.GrisButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.GrisButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.GrisButton.SetText('Gris')
        self.GrisButton.SetPosition(20, 122)
        self.GrisButton.SetEvent(ui.__mem_func__(self.Gris))
        self.VerdeButton = ui.Button()
        self.VerdeButton.SetParent(self.board)
        self.VerdeButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.VerdeButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.VerdeButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.VerdeButton.SetText('Verde')
        self.VerdeButton.SetPosition(200, 62)
        self.VerdeButton.SetEvent(ui.__mem_func__(self.Verde))
        self.CelesteButton = ui.Button()
        self.CelesteButton.SetParent(self.board)
        self.CelesteButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.CelesteButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.CelesteButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.CelesteButton.SetText('Celeste')
        self.CelesteButton.SetPosition(140, 62)
        self.CelesteButton.SetEvent(ui.__mem_func__(self.Celeste))
        self.BioletaButton = ui.Button()
        self.BioletaButton.SetParent(self.board)
        self.BioletaButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.BioletaButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.BioletaButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.BioletaButton.SetText('Morado')
        self.BioletaButton.SetPosition(80, 62)
        self.BioletaButton.SetEvent(ui.__mem_func__(self.Bioleta))
        self.RojoButton = ui.Button()
        self.RojoButton.SetParent(self.board)
        self.RojoButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.RojoButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.RojoButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.RojoButton.SetText('Rojo')
        self.RojoButton.SetPosition(20, 62)
        self.RojoButton.SetEvent(ui.__mem_func__(self.Rojo))
        self.NegroButton = ui.Button()
        self.NegroButton.SetParent(self.board)
        self.NegroButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.NegroButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.NegroButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.NegroButton.SetText('Negro')
        self.NegroButton.SetPosition(200, 92)
        self.NegroButton.SetEvent(ui.__mem_func__(self.Negro))
        self.RojoclaroButton = ui.Button()
        self.RojoclaroButton.SetParent(self.board)
        self.RojoclaroButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.RojoclaroButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.RojoclaroButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.RojoclaroButton.SetText('Rojo claro')
        self.RojoclaroButton.SetPosition(140, 92)
        self.RojoclaroButton.SetEvent(ui.__mem_func__(self.Rojoclaro))
        self.AzulclaroButton = ui.Button()
        self.AzulclaroButton.SetParent(self.board)
        self.AzulclaroButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.AzulclaroButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.AzulclaroButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.AzulclaroButton.SetText('Magneta')
        self.AzulclaroButton.SetPosition(80, 92)
        self.AzulclaroButton.SetEvent(ui.__mem_func__(self.Azulclaro))
        self.AguaButton = ui.Button()
        self.AguaButton.SetParent(self.board)
        self.AguaButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.AguaButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.AguaButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.AguaButton.SetText('Agua')
        self.AguaButton.SetPosition(20, 92)
        self.AguaButton.SetEvent(ui.__mem_func__(self.Agua))
        self.OtroButton = ui.Button()
        self.OtroButton.SetParent(self.board)
        self.OtroButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.OtroButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.OtroButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.OtroButton.SetText('Otro')
        self.OtroButton.SetPosition(80, 122)
        self.OtroButton.SetEvent(ui.__mem_func__(self.Otro))
        self.AzulButton = ui.Button()
        self.AzulButton.SetParent(self.board)
        self.AzulButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.AzulButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.AzulButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.AzulButton.SetText('Azul')
        self.AzulButton.SetPosition(140, 122)
        self.AzulButton.SetEvent(ui.__mem_func__(self.Azul))
        self.yoloButton = ui.Button()
        self.yoloButton.SetParent(self.board)
        self.yoloButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.yoloButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.yoloButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.yoloButton.SetText('Amarillo')
        self.yoloButton.SetPosition(200, 122)
        self.yoloButton.SetEvent(ui.__mem_func__(self.OpenBuilder))

    def __del__(self):
        ui.Window.__del__(self)

    def Close(self):
        self.yoloButton.Hide()
        self.AzulButton.Hide()
        self.GrisButton.Hide()
        self.VerdeButton.Hide()
        self.CelesteButton.Hide()
        self.BioletaButton.Hide()
        self.RojoButton.Hide()
        self.NegroButton.Hide()
        self.RojoclaroButton.Hide()
        self.AzulclaroButton.Hide()
        self.OtroButton.Hide()
        self.AguaButton.Hide()
        self.nameEditLine.Hide()
        self.board.Hide()
        g_isCreatingWindow = 0

    def Show(self):
        self.board.Show()
        self.nameEditLine.Show()
        self.AzulButton.Show()
        self.GrisButton.Show()
        self.VerdeButton.Show()
        self.CelesteButton.Show()
        self.BioletaButton.Show()
        self.RojoButton.Show()
        self.NegroButton.Show()
        self.RojoclaroButton.Show()
        self.AzulclaroButton.Show()
        self.OtroButton.Show()
        self.AguaButton.Show()
        self.yoloButton.Show()
        g_isCreatingWindow = 1

    def OnUpdate(self):
        return

    def Azul(self):
        self.privateShopBuilder.Open(Azulcolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Verde(self):
        self.privateShopBuilder.Open(Verdecolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Celeste(self):
        self.privateShopBuilder.Open(Celestecolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Bioleta(self):
        self.privateShopBuilder.Open(Bioletacolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Rojo(self):
        self.privateShopBuilder.Open(Rojocolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Negro(self):
        self.privateShopBuilder.Open(Negrocolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Rojoclaro(self):
        self.privateShopBuilder.Open(Rojoclarocolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Azulclaro(self):
        self.privateShopBuilder.Open(Azulclarocolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Otro(self):
        self.privateShopBuilder.Open(Otrocolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Gris(self):
        self.privateShopBuilder.Open(Griscolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def Agua(self):
        self.privateShopBuilder.Open(Aguacolor(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()

    def OpenBuilder(self):
        self.privateShopBuilder.Open(GetFakeString(self.nameEditLine.GetText()))
        self.privateShopBuilder.Refresh()
        self.Close()


g_createWindow = ColorShop()

def ShowWindow():
    global g_isCreatingWindow
    if g_isCreatingWindow != 0:
        g_createWindow.Hide()
    else:
        g_createWindow.Show()
    return g_createWindow


createButton = ui.Button()
createButton.SetUpVisual('d:/ymir work/ui/public/large_Button_01.sub')
createButton.SetOverVisual('d:/ymir work/ui/public/large_Button_02.sub')
createButton.SetDownVisual('d:/ymir work/ui/public/large_Button_03.sub')
createButton.SetText('Tienda color')
createButton.SetPosition(wndMgr.GetScreenWidth() - 100, 370)
createButton.SetEvent(ShowWindow)
createButton.Show()

class PickUP(ui.ScriptWindow):
    WHISPER_MODE = ('Todos', 'PJ')
    COLOUR_MODE_NAME = ('Normal', 'Azul', 'Verde', 'Rojo', 'Rosado', 'Amarillo', 'Morado')
    COLOUR_MODE_NAME2 = ('Amarillo2', 'Celeste', 'Agua', 'Rojo2', 'Gris', 'Magenta', 'Noticia')
    COLOUR_MODE_INDEX = ('|h|r', '|cFF0080FF|H|h', '|cFF00FF00|H|h', '|cFFFF0000|H|h', '|cFFFF00FF|H|h', '|cffffff00|H|h', '|cFF8A2BE2|H|h')
    COLOUR_MODE_INDEX2 = ('|cFFFFE4C4|H|h', '|cFF00CCFF|H|h', '|cff00ffff|H|h', '|cffff6060|H|h', '|cff888888|H|h', '|cffff00ff|H|h', '|cFFFFE6BA|H|h')
    ERROR_MESSAGE_INDEX = ('El SpamBot ha sido activado', 'Por favor escoja una forma.', 'Por favor escoja un color.', 'Por favor introduzca un texto.', 'Por favor introduzca los segundos', 'Por favor introduzca una cantidad', 'Por favor introduzca un nombre')
    CHAT_MODE_NAME = (locale.CHAT_NORMAL, locale.CHAT_PARTY, locale.CHAT_GUILD, locale.CHAT_SHOUT, 'Random')
    CHAT_MODE_INDEX = (chat.CHAT_TYPE_TALKING, chat.CHAT_TYPE_PARTY, chat.CHAT_TYPE_GUILD, chat.CHAT_TYPE_SHOUT, 'Random')
    COLOUR1_MODE_NAME = ('Normal', 'Azul', 'Verde', 'Rojo', 'Rosado', 'Amarillo', 'Morado')
    COLOUR1_MODE_NAME2 = ('Amarillo2', 'Celeste', 'Agua', 'Rojo2', 'Gris', 'Magenta', 'Noticia')
    COLOUR1_MODE_INDEX = ('|h|r', '|cFF0080FF|H|h', '|cFF00FF00|H|h', '|cFFFF0000|H|h', '|cFFFF00FF|H|h', '|cffffff00|H|h', '|cFF8A2BE2|H|h')
    COLOUR1_MODE_INDEX2 = ('|cFFFFE4C4|H|h', '|cFF00CCFF|H|h', '|cff00ffff|H|h', '|cffff6060|H|h', '|cff888888|H|h', '|cffff00ff|H|h', '|cFFFFE6BA|H|h')
    ERROR1_MESSAGE_INDEX = ('El SpamBot ha sido Activado.', 'Por favor escoja una forma', 'Por favor escoja un color.', 'Por favor introduzca un texto', 'Por favor introduzca los segundos.', 'Por favor introduzca una cantidad.', 'Itroduzca un numero mayor a 15 segundos.')

    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.LoadPick()

    def __del__(self):
        ui.ScriptWindow.__del__(self)

    def Bonuschangevalue(self):
        global Boniswitchvalue
        for i in xrange(player.INVENTORY_PAGE_SIZE * 2):
            itemIndex = player.GetItemIndex(i)
            item.SelectItem(itemIndex)
            ItemValue = player.GetItemIndex(i)
            if item.IsAntiFlag(74112) and item.IsFlag(8196) and item.GetItemSubType() == 18:
                chat.AppendChat(chat.CHAT_TYPE_INFO, 'Gegenstand verzaubern liegt auf Value: ' + str(ItemValue))
                Boniswitchvalue = int(ItemValue)
                break
            else:
                if str(item.GetItemName()) == 'Gegenstand verzaubern':
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Gegenstand verzaubern liegt auf Value: ' + str(ItemValue))
                    Boniswitchvalue = int(ItemValue)
                    break

    def LoadPick(self):
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Multihack By Francoiz v1.5')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'youtube.com/xFrancoizx o francoiz.net')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Ayuda:')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Para escribir en color se necesita tener en el inventario Cristal de entendimiento')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Para pegar el texto copiado, preciona la tecla CTRL (Control) + V ... CTRL+V')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'rancoiz')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '')
        chat.AppendChat(chat.CHAT_TYPE_INFO, 'youtube.com/xFrancoizx')
        self.LoadMainForm()
        self.FaceButton()

    def LoadMainForm(self):
        self.comp = Component()
        self.Board1 = ui.BoardWithTitleBar()
        self.Board1.SetSize(272, 370)
        self.Board1.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.Board1.AddFlag('movable')
        self.Board1.AddFlag('float')
        self.Board1.SetTitleName('Hack Francoiz')
        self.Board1.SetCloseEvent(self.Board1.Hide)
        self.Board1.Hide()
        self.Pick1Message = ui.TextLine()
        self.Pick1Message.SetParent(self.Board1)
        self.Pick1Message.SetPosition(67, 40)
        self.Pick1Message.SetText('Bot de leveo - By Francoiz')
        self.Pick1Message.SetFontColor(1.0, 0.8, 0)
        self.Pick1Message.Show()
        self.Board2 = ui.BoardWithTitleBar()
        self.Board2.SetSize(160, 250)
        self.Board2.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board2.AddFlag('movable')
        self.Board2.AddFlag('float')
        self.Board2.SetTitleName('Hack Francoiz')
        self.Board2.SetCloseEvent(self.Board2.Hide)
        self.Board2.Hide()
        self.Pick2Message = ui.TextLine()
        self.Pick2Message.SetParent(self.Board2)
        self.Pick2Message.SetPosition(20, 40)
        self.Pick2Message.SetText('Camara - By Francoiz')
        self.Pick2Message.SetFontColor(1.0, 0.8, 0)
        self.Pick2Message.Show()
        self.Board3 = ui.BoardWithTitleBar()
        self.Board3.SetSize(245, 200)
        self.Board3.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board3.AddFlag('movable')
        self.Board3.AddFlag('float')
        self.Board3.SetTitleName('Hack Francoiz')
        self.Board3.SetCloseEvent(self.Board3.Hide)
        self.Board3.Hide()
        self.Pick3Message = ui.TextLine()
        self.Pick3Message.SetParent(self.Board3)
        self.Pick3Message.SetPosition(73, 40)
        self.Pick3Message.SetText('Velocidad - By Francoiz')
        self.Pick3Message.SetFontColor(1.0, 0.8, 0)
        self.Pick3Message.Show()
        self.Board4 = ui.BoardWithTitleBar()
        self.Board4.SetSize(250, 500)
        self.Board4.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board4.AddFlag('movable')
        self.Board4.AddFlag('float')
        self.Board4.SetTitleName('Hack Francoiz')
        self.Board4.SetCloseEvent(self.Board4.Hide)
        self.Board4.Hide()
        self.Pick4Message = ui.TextLine()
        self.Pick4Message.SetParent(self.Board4)
        self.Pick4Message.SetPosition(67, 40)
        self.Pick4Message.SetText('Otros hacks - By Francoiz')
        self.Pick4Message.SetFontColor(1.0, 0.8, 0)
        self.Pick4Message.Show()
        self.Board5 = ui.BoardWithTitleBar()
        self.Board5.SetSize(240, 135)
        self.Board5.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.Board5.AddFlag('movable')
        self.Board5.AddFlag('float')
        self.Board5.SetTitleName('Hack Francoiz')
        self.Board5.SetCloseEvent(self.Board5.Hide)
        self.Board5.Hide()
        self.Pick5Message = ui.TextLine()
        self.Pick5Message.SetParent(self.Board5)
        self.Pick5Message.SetPosition(67, 40)
        self.Pick5Message.SetText('Teleporter - By Francoiz')
        self.Pick5Message.SetFontColor(1.0, 0.8, 0)
        self.Pick5Message.Show()
        self.Board7 = ui.BoardWithTitleBar()
        self.Board7.SetSize(230, 220)
        self.Board7.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board7.AddFlag('movable')
        self.Board7.AddFlag('float')
        self.Board7.SetTitleName('Hack Francoiz')
        self.Board7.SetCloseEvent(self.Board7.Hide)
        self.Board7.Hide()
        self.Pick7Message = ui.TextLine()
        self.Pick7Message.SetParent(self.Board7)
        self.Pick7Message.SetPosition(60, 40)
        self.Pick7Message.SetText('Creditos - By Francoiz')
        self.Pick7Message.SetFontColor(1.0, 0.8, 0)
        self.Pick7Message.Show()
        self.Board8 = ui.BoardWithTitleBar()
        self.Board8.SetSize(200, 200)
        self.Board8.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.Board8.AddFlag('movable')
        self.Board8.AddFlag('float')
        self.Board8.SetTitleName('Hack Francoiz - Teleporter 3')
        self.Board8.SetCloseEvent(self.Board8.Hide)
        self.Board8.Hide()
        self.Pick8Message = ui.TextLine()
        self.Pick8Message.SetParent(self.Board8)
        self.Pick8Message.SetPosition(67, 40)
        self.Pick8Message.SetText('')
        self.Pick8Message.SetFontColor(1.0, 0.8, 0)
        self.Pick8Message.Show()
        self.Board9 = ui.BoardWithTitleBar()
        self.Board9.SetSize(390, 460)
        self.Board9.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board9.AddFlag('movable')
        self.Board9.AddFlag('float')
        self.Board9.SetTitleName('Hack Francoiz')
        self.Board9.SetCloseEvent(self.Board9.Hide)
        self.Board9.Hide()
        self.Pick9Message = ui.TextLine()
        self.Pick9Message.SetParent(self.Board9)
        self.Pick9Message.SetPosition(67, 40)
        self.Pick9Message.SetText('')
        self.Pick9Message.SetFontColor(1.0, 0.8, 0)
        self.Pick9Message.Show()
        self.Board10 = ui.BoardWithTitleBar()
        self.Board10.SetSize(300, 165)
        self.Board10.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board10.AddFlag('movable')
        self.Board10.AddFlag('float')
        self.Board10.SetTitleName('BuffBot - Multihack Francoiz')
        self.Board10.SetCloseEvent(self.Board10.Hide)
        self.Board10.Hide()
        self.Pick10Message = ui.TextLine()
        self.Pick10Message.SetParent(self.Board10)
        self.Pick10Message.SetPosition(67, 40)
        self.Pick10Message.SetText('')
        self.Pick10Message.SetFontColor(1.0, 0.8, 0)
        self.Pick10Message.Show()
        self.Board11 = ui.BoardWithTitleBar()
        self.Board11.SetSize(600, 400)
        self.Board11.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board11.AddFlag('movable')
        self.Board11.AddFlag('float')
        self.Board11.SetTitleName('Librobot - Multihack Francoiz')
        self.Board11.SetCloseEvent(self.Board11.Hide)
        self.Board11.Hide()
        self.Pick11Message = ui.TextLine()
        self.Pick11Message.SetParent(self.Board11)
        self.Pick11Message.SetPosition(67, 40)
        self.Pick11Message.SetText('')
        self.Pick11Message.SetFontColor(1.0, 0.8, 0)
        self.Pick11Message.Show()
        self.Board12 = ui.BoardWithTitleBar()
        self.Board12.SetSize(200, 75)
        self.Board12.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board12.AddFlag('movable')
        self.Board12.AddFlag('float')
        self.Board12.SetTitleName('Detector GM - Multihack Francoiz')
        self.Board12.SetCloseEvent(self.Board12.Hide)
        self.Board12.Hide()
        self.Pick12Message = ui.TextLine()
        self.Pick12Message.SetParent(self.Board12)
        self.Pick12Message.SetPosition(67, 40)
        self.Pick12Message.SetText('')
        self.Pick12Message.SetFontColor(1.0, 0.8, 0)
        self.Pick12Message.Show()
        self.Board13 = ui.BoardWithTitleBar()
        self.Board13.SetSize(200, 120)
        self.Board13.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board13.AddFlag('movable')
        self.Board13.AddFlag('float')
        self.Board13.SetTitleName('Configuracion')
        self.Board13.SetCloseEvent(self.Board13.Hide)
        self.Board13.Hide()
        self.Pick13Message = ui.TextLine()
        self.Pick13Message.SetParent(self.Board13)
        self.Pick13Message.SetPosition(67, 40)
        self.Pick13Message.SetText('')
        self.Pick13Message.SetFontColor(1.0, 0.8, 0)
        self.Pick13Message.Show()
        self.Board14 = ui.BoardWithTitleBar()
        self.Board14.SetSize(250, 200)
        self.Board14.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.Board14.AddFlag('movable')
        self.Board14.AddFlag('float')
        self.Board14.SetTitleName('Mas hacks')
        self.Board14.SetCloseEvent(self.Board14.Hide)
        self.Board14.Hide()
        self.Pick14Message = ui.TextLine()
        self.Pick14Message.SetParent(self.Board14)
        self.Pick14Message.SetPosition(67, 40)
        self.Pick14Message.SetText('Mas hacks - Multihack 1.5')
        self.Pick14Message.SetFontColor(1.0, 0.8, 0)
        self.Pick14Message.Show()
        self.Board15 = ui.BoardWithTitleBar()
        self.Board15.SetSize(390, 465)
        self.Board15.SetPosition(wndMgr.GetScreenWidth() - 600, 80)
        self.Board15.AddFlag('movable')
        self.Board15.AddFlag('float')
        self.Board15.SetTitleName('Hack Francoiz')
        self.Board15.SetCloseEvent(self.Board15.Hide)
        self.Board15.Hide()
        self.Pick15Message = ui.TextLine()
        self.Pick15Message.SetParent(self.Board15)
        self.Pick15Message.SetPosition(67, 40)
        self.Pick15Message.SetText('')
        self.Pick15Message.SetFontColor(1.0, 0.8, 0)
        self.Pick15Message.Show()
        self.Board16 = ui.BoardWithTitleBar()
        self.Board16.SetSize(200, 270)
        self.Board16.SetPosition(wndMgr.GetScreenWidth() - 400, 80)
        self.Board16.AddFlag('movable')
        self.Board16.AddFlag('float')
        self.Board16.SetTitleName('Hack Francoiz')
        self.Board16.SetCloseEvent(self.Board16.Hide)
        self.Board16.Hide()
        self.Pick16Message = ui.TextLine()
        self.Pick16Message.SetParent(self.Board16)
        self.Pick16Message.SetPosition(67, 40)
        self.Pick16Message.SetText('')
        self.Pick16Message.SetFontColor(1.0, 0.8, 0)
        self.Pick16Message.Show()
        self.Board17 = ui.BoardWithTitleBar()
        self.Board17.SetSize(250, 80)
        self.Board17.SetPosition(wndMgr.GetScreenWidth() - 800, 80)
        self.Board17.AddFlag('movable')
        self.Board17.AddFlag('float')
        self.Board17.SetTitleName('Crear Gremio')
        self.Board17.SetCloseEvent(self.Board17.Hide)
        self.Board17.Hide()
        self.Pick17Message = ui.TextLine()
        self.Pick17Message.SetParent(self.Board17)
        self.Pick17Message.SetPosition(67, 40)
        self.Pick17Message.SetText('')
        self.Pick17Message.SetFontColor(1.0, 0.8, 0)
        self.Pick17Message.Show()
        self.ConfiguracionSlotbar = ui.SlotBar()
        self.ConfiguracionSlotbar.SetParent(self.Board13)
        self.ConfiguracionSlotbar.SetSize(30, 18)
        self.ConfiguracionSlotbar.SetPosition(50, 45)
        self.ConfiguracionSlotbar.SetWindowHorizontalAlignCenter()
        self.ConfiguracionSlotbar.Show()
        self.Configuracion = ui.EditLine()
        self.Configuracion.SetParent(self.ConfiguracionSlotbar)
        self.Configuracion.SetSize(30, 17)
        self.Configuracion.SetPosition(8, 2)
        self.Configuracion.SetMax(4)
        self.Configuracion.SetNumberMode()
        self.Configuracion.SetFocus()
        self.Configuracion.SetText('2000')
        self.Configuracion.SetTabEvent(ui.__mem_func__(self.Configuracion.SetFocus))
        self.Configuracion.SetReturnEvent(ui.__mem_func__(self.Configuracion.SetFocus))
        self.Configuracion.Show()
        self.Linea = ui.TextLine()
        self.Linea.SetParent(self.Board8)
        self.Linea.SetDefaultFontName()
        self.Linea.SetPosition(-92, 120)
        self.Linea.SetFeather()
        self.Linea.SetWindowHorizontalAlignCenter()
        self.Linea.SetText('_____________________________________')
        self.Linea.SetFontColor(1.0, 0.8, 0)
        self.Linea.SetOutline()
        self.Linea.Show()
        self.ConfiguracionText = ui.TextLine()
        self.ConfiguracionText.SetParent(self.Board13)
        self.ConfiguracionText.SetDefaultFontName()
        self.ConfiguracionText.SetPosition(-85, 45)
        self.ConfiguracionText.SetFeather()
        self.ConfiguracionText.SetWindowHorizontalAlignCenter()
        self.ConfiguracionText.SetText('Distancia a teletransportar:')
        self.ConfiguracionText.SetOutline()
        self.ConfiguracionText.Show()
        self.SegundosSlotbar = ui.SlotBar()
        self.SegundosSlotbar.SetParent(self.Board11)
        self.SegundosSlotbar.SetSize(30, 18)
        self.SegundosSlotbar.SetPosition(-209, 330)
        self.SegundosSlotbar.SetWindowHorizontalAlignCenter()
        self.SegundosSlotbar.Show()
        self.Segundos = ui.EditLine()
        self.Segundos.SetParent(self.SegundosSlotbar)
        self.Segundos.SetSize(30, 17)
        self.Segundos.SetPosition(8, 2)
        self.Segundos.SetMax(2)
        self.Segundos.SetNumberMode()
        self.Segundos.SetFocus()
        self.Segundos.SetText('0')
        self.Segundos.SetTabEvent(ui.__mem_func__(self.Segundos.SetFocus))
        self.Segundos.SetReturnEvent(ui.__mem_func__(self.Segundos.SetFocus))
        self.Segundos.Show()
        self.MoveSpeedStatsSlotbar = ui.SlotBar()
        self.MoveSpeedStatsSlotbar.SetParent(self.Board3)
        self.MoveSpeedStatsSlotbar.SetSize(30, 18)
        self.MoveSpeedStatsSlotbar.SetPosition(33, 118)
        self.MoveSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
        self.MoveSpeedStatsSlotbar.Show()
        self.MoveSpeedStats = ui.EditLine()
        self.MoveSpeedStats.SetParent(self.MoveSpeedStatsSlotbar)
        self.MoveSpeedStats.SetSize(30, 17)
        self.MoveSpeedStats.SetPosition(10, 2)
        self.MoveSpeedStats.SetMax(3)
        self.MoveSpeedStats.SetNumberMode()
        self.MoveSpeedStats.SetFocus()
        self.MoveSpeedStats.SetText('300')
        self.MoveSpeedStats.Show()
        self.AttackSpeedStatsSlotbar = ui.SlotBar()
        self.AttackSpeedStatsSlotbar.SetParent(self.Board3)
        self.AttackSpeedStatsSlotbar.SetSize(30, 18)
        self.AttackSpeedStatsSlotbar.SetPosition(8, 78)
        self.AttackSpeedStatsSlotbar.SetWindowHorizontalAlignCenter()
        self.AttackSpeedStatsSlotbar.Show()
        self.AttackSpeedStats = ui.EditLine()
        self.AttackSpeedStats.SetParent(self.AttackSpeedStatsSlotbar)
        self.AttackSpeedStats.SetSize(30, 17)
        self.AttackSpeedStats.SetPosition(10, 2)
        self.AttackSpeedStats.SetMax(3)
        self.AttackSpeedStats.SetNumberMode()
        self.AttackSpeedStats.SetFocus()
        self.AttackSpeedStats.SetText('200')
        self.AttackSpeedStats.SetTabEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
        self.AttackSpeedStats.SetReturnEvent(ui.__mem_func__(self.MoveSpeedStats.SetFocus))
        self.AttackSpeedStats.Show()
        self.AutoRedPotLabel = ui.TextLine()
        self.AutoRedPotLabel.SetParent(self.Board1)
        self.AutoRedPotLabel.SetDefaultFontName()
        self.AutoRedPotLabel.SetPosition(-120, 100)
        self.AutoRedPotLabel.SetFeather()
        self.AutoRedPotLabel.SetWindowHorizontalAlignCenter()
        self.AutoRedPotLabel.SetText('Potas Rojas:')
        self.AutoRedPotLabel.SetFontColor(35.0, 0.0, 0.0)
        self.AutoRedPotLabel.SetOutline()
        self.AutoRedPotLabel.Show()
        self.RedPotPercentLabel = ui.TextLine()
        self.RedPotPercentLabel.SetParent(self.Board1)
        self.RedPotPercentLabel.SetDefaultFontName()
        self.RedPotPercentLabel.SetPosition(-22, 99)
        self.RedPotPercentLabel.SetFeather()
        self.RedPotPercentLabel.SetWindowHorizontalAlignCenter()
        self.RedPotPercentLabel.SetText('%')
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
        self.EditLineRedPotting.SetText('90')
        self.EditLineRedPotting.SetFocus()
        self.EditLineRedPotting.Show()
        self.AutoBluePotLabel = ui.TextLine()
        self.AutoBluePotLabel.SetParent(self.Board1)
        self.AutoBluePotLabel.SetDefaultFontName()
        self.AutoBluePotLabel.SetPosition(-120, 130)
        self.AutoBluePotLabel.SetFeather()
        self.AutoBluePotLabel.SetWindowHorizontalAlignCenter()
        self.AutoBluePotLabel.SetText('Potas Azules:')
        self.AutoBluePotLabel.SetFontColor(0.0, 0.0, 1.0)
        self.AutoBluePotLabel.SetOutline()
        self.AutoBluePotLabel.Show()
        self.BluePotPercentLabel = ui.TextLine()
        self.BluePotPercentLabel.SetParent(self.Board1)
        self.BluePotPercentLabel.SetDefaultFontName()
        self.BluePotPercentLabel.SetPosition(-22, 130)
        self.BluePotPercentLabel.SetFeather()
        self.BluePotPercentLabel.SetWindowHorizontalAlignCenter()
        self.BluePotPercentLabel.SetText('%')
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
        self.EditLineBluePotting.SetText('40')
        self.EditLineBluePotting.SetFocus()
        self.EditLineBluePotting.Show()
        self.LevelbotModo0Label = ui.TextLine()
        self.LevelbotModo0Label.SetParent(self.Board1)
        self.LevelbotModo0Label.SetDefaultFontName()
        self.LevelbotModo0Label.SetPosition(-70, 160)
        self.LevelbotModo0Label.SetFeather()
        self.LevelbotModo0Label.SetWindowHorizontalAlignCenter()
        self.LevelbotModo0Label.SetText('Tipo 1:')
        self.LevelbotModo0Label.SetFontColor(1.0, 0.8, 0)
        self.LevelbotModo0Label.SetOutline()
        self.LevelbotModo0Label.Show()
        self.LevelbotModo1Label = ui.TextLine()
        self.LevelbotModo1Label.SetParent(self.Board1)
        self.LevelbotModo1Label.SetDefaultFontName()
        self.LevelbotModo1Label.SetPosition(-20, 160)
        self.LevelbotModo1Label.SetFeather()
        self.LevelbotModo1Label.SetWindowHorizontalAlignCenter()
        self.LevelbotModo1Label.SetText('Tipo 2:')
        self.LevelbotModo1Label.SetFontColor(1.0, 0.8, 0)
        self.LevelbotModo1Label.SetOutline()
        self.LevelbotModo1Label.Show()
        self.LevelbotModo2Label = ui.TextLine()
        self.LevelbotModo2Label.SetParent(self.Board1)
        self.LevelbotModo2Label.SetDefaultFontName()
        self.LevelbotModo2Label.SetPosition(30, 160)
        self.LevelbotModo2Label.SetFeather()
        self.LevelbotModo2Label.SetWindowHorizontalAlignCenter()
        self.LevelbotModo2Label.SetText('Tipo 3:')
        self.LevelbotModo2Label.SetFontColor(1.0, 0.8, 0)
        self.LevelbotModo2Label.SetOutline()
        self.LevelbotModo2Label.Show()
        self.AutoAttackLabel = ui.TextLine()
        self.AutoAttackLabel.SetParent(self.Board1)
        self.AutoAttackLabel.SetDefaultFontName()
        self.AutoAttackLabel.SetPosition(-120, 160)
        self.AutoAttackLabel.SetFeather()
        self.AutoAttackLabel.SetWindowHorizontalAlignCenter()
        self.AutoAttackLabel.SetText('Leveo:')
        self.AutoAttackLabel.SetOutline()
        self.AutoAttackLabel.Show()
        self.AutoPickLabel = ui.TextLine()
        self.AutoPickLabel.SetParent(self.Board1)
        self.AutoPickLabel.SetDefaultFontName()
        self.AutoPickLabel.SetPosition(-122, 190)
        self.AutoPickLabel.SetFeather()
        self.AutoPickLabel.SetWindowHorizontalAlignCenter()
        self.AutoPickLabel.SetText('Auto-Agarre:')
        self.AutoPickLabel.SetOutline()
        self.AutoPickLabel.Show()
        self.AutoRestartLabel = ui.TextLine()
        self.AutoRestartLabel.SetParent(self.Board1)
        self.AutoRestartLabel.SetDefaultFontName()
        self.AutoRestartLabel.SetPosition(-120, 220)
        self.AutoRestartLabel.SetFeather()
        self.AutoRestartLabel.SetWindowHorizontalAlignCenter()
        self.AutoRestartLabel.SetText('Revive aqui:')
        self.AutoRestartLabel.SetOutline()
        self.AutoRestartLabel.Show()
        self.ZoomHackLabel = ui.TextLine()
        self.ZoomHackLabel.SetParent(self.Board2)
        self.ZoomHackLabel.SetDefaultFontName()
        self.ZoomHackLabel.SetPosition(-60, 70)
        self.ZoomHackLabel.SetFeather()
        self.ZoomHackLabel.SetWindowHorizontalAlignCenter()
        self.ZoomHackLabel.SetText('Zoom Hack:')
        self.ZoomHackLabel.SetOutline()
        self.ZoomHackLabel.Show()
        self.NoFogLabel = ui.TextLine()
        self.NoFogLabel.SetParent(self.Board2)
        self.NoFogLabel.SetDefaultFontName()
        self.NoFogLabel.SetPosition(-60, 100)
        self.NoFogLabel.SetFeather()
        self.NoFogLabel.SetWindowHorizontalAlignCenter()
        self.NoFogLabel.SetText('Sin Niebla:')
        self.NoFogLabel.SetOutline()
        self.NoFogLabel.Show()
        self.DayNightLabel = ui.TextLine()
        self.DayNightLabel.SetParent(self.Board2)
        self.DayNightLabel.SetDefaultFontName()
        self.DayNightLabel.SetPosition(-60, 130)
        self.DayNightLabel.SetFeather()
        self.DayNightLabel.SetWindowHorizontalAlignCenter()
        self.DayNightLabel.SetText('Dia/Noche:')
        self.DayNightLabel.SetOutline()
        self.DayNightLabel.Show()
        self.PararcamLabel = ui.TextLine()
        self.PararcamLabel.SetParent(self.Board2)
        self.PararcamLabel.SetDefaultFontName()
        self.PararcamLabel.SetPosition(-60, 190)
        self.PararcamLabel.SetFeather()
        self.PararcamLabel.SetWindowHorizontalAlignCenter()
        self.PararcamLabel.SetText('Parar camara:')
        self.PararcamLabel.SetOutline()
        self.PararcamLabel.Show()
        self.SnowLabel = ui.TextLine()
        self.SnowLabel.SetParent(self.Board2)
        self.SnowLabel.SetDefaultFontName()
        self.SnowLabel.SetPosition(-60, 160)
        self.SnowLabel.SetFeather()
        self.SnowLabel.SetWindowHorizontalAlignCenter()
        self.SnowLabel.SetText('Nieve:')
        self.SnowLabel.SetOutline()
        self.SnowLabel.Show()
        self.AttackSpeedHackHeadline = ui.TextLine()
        self.AttackSpeedHackHeadline.SetParent(self.Board3)
        self.AttackSpeedHackHeadline.SetDefaultFontName()
        self.AttackSpeedHackHeadline.SetPosition(15, 80)
        self.AttackSpeedHackHeadline.SetFeather()
        self.AttackSpeedHackHeadline.SetText('Velocidad de ataque:')
        self.AttackSpeedHackHeadline.SetOutline()
        self.AttackSpeedHackHeadline.Show()
        self.MoveSpeedHackHeadline = ui.TextLine()
        self.MoveSpeedHackHeadline.SetParent(self.Board3)
        self.MoveSpeedHackHeadline.SetDefaultFontName()
        self.MoveSpeedHackHeadline.SetPosition(15, 120)
        self.MoveSpeedHackHeadline.SetFeather()
        self.MoveSpeedHackHeadline.SetText('Velocidad de movimiento:')
        self.MoveSpeedHackHeadline.SetOutline()
        self.MoveSpeedHackHeadline.Show()
        self.CaballouserHeadline = ui.TextLine()
        self.CaballouserHeadline.SetParent(self.Board3)
        self.CaballouserHeadline.SetDefaultFontName()
        self.CaballouserHeadline.SetPosition(15, 160)
        self.CaballouserHeadline.SetFeather()
        self.CaballouserHeadline.SetText('Caballo:')
        self.CaballouserHeadline.SetOutline()
        self.CaballouserHeadline.Show()
        self.CabosLabel = ui.TextLine()
        self.CabosLabel.SetParent(self.Board1)
        self.CabosLabel.SetDefaultFontName()
        self.CabosLabel.SetPosition(-120, 258)
        self.CabosLabel.SetFeather()
        self.CabosLabel.SetWindowHorizontalAlignCenter()
        self.CabosLabel.SetText('Bot de cabos:')
        self.CabosLabel.SetOutline()
        self.CabosLabel.Show()
        self.PoderesLabel = ui.TextLine()
        self.PoderesLabel.SetParent(self.Board1)
        self.PoderesLabel.SetDefaultFontName()
        self.PoderesLabel.SetPosition(-120, 288)
        self.PoderesLabel.SetFeather()
        self.PoderesLabel.SetWindowHorizontalAlignCenter()
        self.PoderesLabel.SetText('Quitar tiempo de habilidades:')
        self.PoderesLabel.SetOutline()
        self.PoderesLabel.Show()
        self.CambiarLabel = ui.TextLine()
        self.CambiarLabel.SetParent(self.Board1)
        self.CambiarLabel.SetDefaultFontName()
        self.CambiarLabel.SetPosition(-120, 317)
        self.CambiarLabel.SetFeather()
        self.CambiarLabel.SetWindowHorizontalAlignCenter()
        self.CambiarLabel.SetText('Cambiar modo de arma:')
        self.CambiarLabel.SetOutline()
        self.CambiarLabel.Show()
        self.CambiarGLabel = ui.TextLine()
        self.CambiarGLabel.SetParent(self.Board1)
        self.CambiarGLabel.SetDefaultFontName()
        self.CambiarGLabel.SetPosition(-120, 347)
        self.CambiarGLabel.SetFeather()
        self.CambiarGLabel.SetWindowHorizontalAlignCenter()
        self.CambiarGLabel.SetText('Modo Guerrero')
        self.CambiarGLabel.SetFontColor(1.0, 0.8, 0)
        self.CambiarGLabel.SetOutline()
        self.CambiarGLabel.Hide()
        self.Modoespada1Label = ui.TextLine()
        self.Modoespada1Label.SetParent(self.Board1)
        self.Modoespada1Label.SetDefaultFontName()
        self.Modoespada1Label.SetPosition(-120, 377)
        self.Modoespada1Label.SetFeather()
        self.Modoespada1Label.SetWindowHorizontalAlignCenter()
        self.Modoespada1Label.SetText('Espada de una mano')
        self.Modoespada1Label.SetOutline()
        self.Modoespada1Label.Hide()
        self.Modoespada2Label = ui.TextLine()
        self.Modoespada2Label.SetParent(self.Board1)
        self.Modoespada2Label.SetDefaultFontName()
        self.Modoespada2Label.SetPosition(-120, 407)
        self.Modoespada2Label.SetFeather()
        self.Modoespada2Label.SetWindowHorizontalAlignCenter()
        self.Modoespada2Label.SetText('Espada dos manos')
        self.Modoespada2Label.SetOutline()
        self.Modoespada2Label.Hide()
        self.CambiarNLabel = ui.TextLine()
        self.CambiarNLabel.SetParent(self.Board1)
        self.CambiarNLabel.SetDefaultFontName()
        self.CambiarNLabel.SetPosition(-120, 437)
        self.CambiarNLabel.SetFeather()
        self.CambiarNLabel.SetWindowHorizontalAlignCenter()
        self.CambiarNLabel.SetText('Modo Ninja')
        self.CambiarNLabel.SetFontColor(1.0, 0.8, 0)
        self.CambiarNLabel.SetOutline()
        self.CambiarNLabel.Hide()
        self.Mododaga1Label = ui.TextLine()
        self.Mododaga1Label.SetParent(self.Board1)
        self.Mododaga1Label.SetDefaultFontName()
        self.Mododaga1Label.SetPosition(-120, 467)
        self.Mododaga1Label.SetFeather()
        self.Mododaga1Label.SetWindowHorizontalAlignCenter()
        self.Mododaga1Label.SetText('Arco')
        self.Mododaga1Label.SetOutline()
        self.Mododaga1Label.Hide()
        self.Mododaga2Label = ui.TextLine()
        self.Mododaga2Label.SetParent(self.Board1)
        self.Mododaga2Label.SetDefaultFontName()
        self.Mododaga2Label.SetPosition(-120, 497)
        self.Mododaga2Label.SetFeather()
        self.Mododaga2Label.SetWindowHorizontalAlignCenter()
        self.Mododaga2Label.SetText('Daga')
        self.Mododaga2Label.SetOutline()
        self.Mododaga2Label.Hide()
        self.CambiarCLabel = ui.TextLine()
        self.CambiarCLabel.SetParent(self.Board1)
        self.CambiarCLabel.SetDefaultFontName()
        self.CambiarCLabel.SetPosition(-120, 527)
        self.CambiarCLabel.SetFeather()
        self.CambiarCLabel.SetWindowHorizontalAlignCenter()
        self.CambiarCLabel.SetText('Modo Chaman')
        self.CambiarCLabel.SetFontColor(1.0, 0.8, 0)
        self.CambiarCLabel.SetOutline()
        self.CambiarCLabel.Hide()
        self.Modochaman1Label = ui.TextLine()
        self.Modochaman1Label.SetParent(self.Board1)
        self.Modochaman1Label.SetDefaultFontName()
        self.Modochaman1Label.SetPosition(-120, 557)
        self.Modochaman1Label.SetFeather()
        self.Modochaman1Label.SetWindowHorizontalAlignCenter()
        self.Modochaman1Label.SetText('Fan')
        self.Modochaman1Label.SetOutline()
        self.Modochaman1Label.Hide()
        self.Modochaman2Label = ui.TextLine()
        self.Modochaman2Label.SetParent(self.Board1)
        self.Modochaman2Label.SetDefaultFontName()
        self.Modochaman2Label.SetPosition(-120, 587)
        self.Modochaman2Label.SetFeather()
        self.Modochaman2Label.SetWindowHorizontalAlignCenter()
        self.Modochaman2Label.SetText('Campana')
        self.Modochaman2Label.SetOutline()
        self.Modochaman2Label.Hide()
        self.CambiargeneralLabel = ui.TextLine()
        self.CambiargeneralLabel.SetParent(self.Board1)
        self.CambiargeneralLabel.SetDefaultFontName()
        self.CambiargeneralLabel.SetPosition(-120, 617)
        self.CambiargeneralLabel.SetFeather()
        self.CambiargeneralLabel.SetWindowHorizontalAlignCenter()
        self.CambiargeneralLabel.SetText('Modo General')
        self.CambiargeneralLabel.SetFontColor(1.0, 0.8, 0)
        self.CambiargeneralLabel.SetOutline()
        self.CambiargeneralLabel.Hide()
        self.ModogeneralLabel = ui.TextLine()
        self.ModogeneralLabel.SetParent(self.Board1)
        self.ModogeneralLabel.SetDefaultFontName()
        self.ModogeneralLabel.SetPosition(-120, 647)
        self.ModogeneralLabel.SetFeather()
        self.ModogeneralLabel.SetWindowHorizontalAlignCenter()
        self.ModogeneralLabel.SetText('General (Sin arma)')
        self.ModogeneralLabel.SetOutline()
        self.ModogeneralLabel.Hide()
        self.CabosSegLabel = ui.TextLine()
        self.CabosSegLabel.SetParent(self.Board1)
        self.CabosSegLabel.SetDefaultFontName()
        self.CabosSegLabel.SetPosition(-12, 258)
        self.CabosSegLabel.SetFeather()
        self.CabosSegLabel.SetWindowHorizontalAlignCenter()
        self.CabosSegLabel.SetText('Segs')
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
        self.TapferkeitsUmhangeDelay.SetMax(2)
        self.TapferkeitsUmhangeDelay.SetNumberMode()
        self.TapferkeitsUmhangeDelay.SetFocus()
        self.TapferkeitsUmhangeDelay.SetText('4')
        self.TapferkeitsUmhangeDelay.Show()
        self.ComboLabel = ui.TextLine()
        self.ComboLabel.SetParent(self.Board4)
        self.ComboLabel.SetDefaultFontName()
        self.ComboLabel.SetPosition(-110, 160)
        self.ComboLabel.SetFeather()
        self.ComboLabel.SetWindowHorizontalAlignCenter()
        self.ComboLabel.SetText('Combo:')
        self.ComboLabel.SetOutline()
        self.ComboLabel.Show()
        self.FantasmaLabel = ui.TextLine()
        self.FantasmaLabel.SetParent(self.Board4)
        self.FantasmaLabel.SetDefaultFontName()
        self.FantasmaLabel.SetPosition(-110, 70)
        self.FantasmaLabel.SetFeather()
        self.FantasmaLabel.SetWindowHorizontalAlignCenter()
        self.FantasmaLabel.SetText('Modo Fantasma:')
        self.FantasmaLabel.SetOutline()
        self.FantasmaLabel.Show()
        self.HerreroLabel = ui.TextLine()
        self.HerreroLabel.SetParent(self.Board4)
        self.HerreroLabel.SetDefaultFontName()
        self.HerreroLabel.SetPosition(-110, 120)
        self.HerreroLabel.SetFeather()
        self.HerreroLabel.SetWindowHorizontalAlignCenter()
        self.HerreroLabel.SetText('Herrero:')
        self.HerreroLabel.SetOutline()
        self.HerreroLabel.Show()
        self.ArmaduraLabel = ui.TextLine()
        self.ArmaduraLabel.SetParent(self.Board4)
        self.ArmaduraLabel.SetDefaultFontName()
        self.ArmaduraLabel.SetPosition(50, 220)
        self.ArmaduraLabel.SetFeather()
        self.ArmaduraLabel.SetWindowHorizontalAlignCenter()
        self.ArmaduraLabel.SetText('Armadura')
        self.ArmaduraLabel.SetOutline()
        self.ArmaduraLabel.Show()
        self.ArmorSlotBar = ui.SlotBar()
        self.ArmorSlotBar.SetParent(self.Board4)
        self.ArmorSlotBar.SetSize(125, 18)
        self.ArmorSlotBar.SetPosition(-30, 220)
        self.ArmorSlotBar.SetWindowHorizontalAlignCenter()
        self.ArmorSlotBar.Show()
        self.ArmorEditLine = ui.EditLine()
        self.ArmorEditLine.SetParent(self.ArmorSlotBar)
        self.ArmorEditLine.SetSize(125, 17)
        self.ArmorEditLine.SetPosition(5, 2)
        self.ArmorEditLine.SetMax(20)
        self.ArmorEditLine.SetText('11299')
        self.ArmorEditLine.SetFocus()
        self.ArmorEditLine.Show()
        self.ArmaLabel = ui.TextLine()
        self.ArmaLabel.SetParent(self.Board4)
        self.ArmaLabel.SetDefaultFontName()
        self.ArmaLabel.SetPosition(50, 250)
        self.ArmaLabel.SetFeather()
        self.ArmaLabel.SetWindowHorizontalAlignCenter()
        self.ArmaLabel.SetText('Arma')
        self.ArmaLabel.SetOutline()
        self.ArmaLabel.Show()
        self.WeaponSlotBar = ui.SlotBar()
        self.WeaponSlotBar.SetParent(self.Board4)
        self.WeaponSlotBar.SetSize(125, 18)
        self.WeaponSlotBar.SetPosition(-30, 250)
        self.WeaponSlotBar.SetWindowHorizontalAlignCenter()
        self.WeaponSlotBar.Show()
        self.WeaponEditLine = ui.EditLine()
        self.WeaponEditLine.SetParent(self.WeaponSlotBar)
        self.WeaponEditLine.SetSize(125, 17)
        self.WeaponEditLine.SetPosition(5, 2)
        self.WeaponEditLine.SetMax(20)
        self.WeaponEditLine.SetText('3229')
        self.WeaponEditLine.SetFocus()
        self.WeaponEditLine.Show()
        self.MobLabel = ui.TextLine()
        self.MobLabel.SetParent(self.Board4)
        self.MobLabel.SetDefaultFontName()
        self.MobLabel.SetPosition(50, 280)
        self.MobLabel.SetFeather()
        self.MobLabel.SetWindowHorizontalAlignCenter()
        self.MobLabel.SetText('Color pelo')
        self.MobLabel.SetOutline()
        self.MobLabel.Show()
        self.HairSlotBar = ui.SlotBar()
        self.HairSlotBar.SetParent(self.Board4)
        self.HairSlotBar.SetSize(125, 18)
        self.HairSlotBar.SetPosition(-30, 280)
        self.HairSlotBar.SetWindowHorizontalAlignCenter()
        self.HairSlotBar.Show()
        self.HairEditLine = ui.EditLine()
        self.HairEditLine.SetParent(self.HairSlotBar)
        self.HairEditLine.SetSize(125, 17)
        self.HairEditLine.SetPosition(5, 2)
        self.HairEditLine.SetMax(1)
        self.HairEditLine.SetText('4')
        self.HairEditLine.SetFocus()
        self.HairEditLine.Show()
        self.ChangeLabel = ui.TextLine()
        self.ChangeLabel.SetParent(self.Board4)
        self.ChangeLabel.SetDefaultFontName()
        self.ChangeLabel.SetPosition(-50, 200)
        self.ChangeLabel.SetFeather()
        self.ChangeLabel.SetWindowHorizontalAlignCenter()
        self.ChangeLabel.SetText('Hack visual')
        self.ChangeLabel.SetFontColor(1.0, 0.8, 0)
        self.ChangeLabel.SetOutline()
        self.ChangeLabel.Show()
        self.TeleportZEditLineSlotBar = ui.SlotBar()
        self.TeleportZEditLineSlotBar.SetParent(self.Board5)
        self.TeleportZEditLineSlotBar.SetSize(43, 18)
        self.TeleportZEditLineSlotBar.SetPosition(-180 + 40 + 120, 135 + 40 * 3 + 1)
        self.TeleportZEditLineSlotBar.SetWindowHorizontalAlignCenter()
        self.TeleportZEditLine = ui.EditLine()
        self.TeleportZEditLine.SetParent(self.TeleportZEditLineSlotBar)
        self.TeleportZEditLine.SetSize(43, 17)
        self.TeleportZEditLine.SetPosition(16, 2)
        self.TeleportZEditLine.SetMax(4)
        self.TeleportZEditLine.SetNumberMode()
        self.TeleportZEditLine.SetFocus()
        self.TeleportZEditLine.SetText('0')
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
        self.TeleportYEditLine.SetText('0')
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
        self.TeleportXEditLine.SetText('0')
        self.TeleportXEditLine.SetTabEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
        self.TeleportXEditLine.SetReturnEvent(ui.__mem_func__(self.TeleportYEditLine.SetFocus))
        self.TeleportXEditLine.Show()
        self.TeleporterLabel = ui.TextLine()
        self.TeleporterLabel.SetParent(self.Board5)
        self.TeleporterLabel.SetDefaultFontName()
        self.TeleporterLabel.SetPosition(-110, 60)
        self.TeleporterLabel.SetFeather()
        self.TeleporterLabel.SetWindowHorizontalAlignCenter()
        self.TeleporterLabel.SetText('Pon las coordenadas del lugar al cual deseas ir')
        self.TeleporterLabel.SetOutline()
        self.TeleporterLabel.Show()
        self.Teleporter1Label = ui.TextLine()
        self.Teleporter1Label.SetParent(self.Board5)
        self.Teleporter1Label.SetDefaultFontName()
        self.Teleporter1Label.SetPosition(-110, 80)
        self.Teleporter1Label.SetFeather()
        self.Teleporter1Label.SetWindowHorizontalAlignCenter()
        self.Teleporter1Label.SetText('Recomendacion.. Procura un lugar no muy lejos..')
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
        self.InputText1.SetText('Multihack By Francoiz..')
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
        self.InputSegundos1.SetText('9999')
        self.InputSegundos1.SetFocus()
        self.InputSegundos1.Show()
        self.CreditosLabel = ui.TextLine()
        self.CreditosLabel.SetParent(self.Board7)
        self.CreditosLabel.SetDefaultFontName()
        self.CreditosLabel.SetPosition(-95, 80)
        self.CreditosLabel.SetFeather()
        self.CreditosLabel.SetWindowHorizontalAlignCenter()
        self.CreditosLabel.SetText('Multihack by Francoiz v1.5')
        self.CreditosLabel.SetFontColor(1.0, 0.8, 0)
        self.CreditosLabel.SetOutline()
        self.CreditosLabel.Show()
        self.Creditos1Label = ui.TextLine()
        self.Creditos1Label.SetParent(self.Board7)
        self.Creditos1Label.SetDefaultFontName()
        self.Creditos1Label.SetPosition(-95, 110)
        self.Creditos1Label.SetFeather()
        self.Creditos1Label.SetWindowHorizontalAlignCenter()
        self.Creditos1Label.SetText('(by Francoiz - 123klo - DaRealFreak)')
        self.Creditos1Label.SetFontColor(1.0, 0.8, 0)
        self.Creditos1Label.SetOutline()
        self.Creditos1Label.Show()
        self.Creditos2Label = ui.TextLine()
        self.Creditos2Label.SetParent(self.Board7)
        self.Creditos2Label.SetPosition(35, 175)
        self.Creditos2Label.SetFeather()
        self.Creditos2Label.SetFontName('STENCIL:32')
        self.Creditos2Label.SetText('Francoiz')
        self.Creditos2Label.SetFontColor(1.0, 0.8, 0)
        self.Creditos2Label.SetOutline()
        self.Creditos2Label.Show()
        self.ChatSpamTitle = ui.TextLine()
        self.ChatSpamTitle.SetParent(self.Board9)
        self.ChatSpamTitle.SetPosition(80, 10)
        self.ChatSpamTitle.SetFeather()
        self.ChatSpamTitle.SetFontName('STENCIL:32')
        self.ChatSpamTitle.SetText('')
        self.ChatSpamTitle.SetFontColor(0.0, 0.7, 1)
        self.ChatSpamTitle.SetOutline()
        self.ChatSpamTitle.Show()
        self.ChatSpamText = ui.TextLine()
        self.ChatSpamText.SetParent(self.Board9)
        self.ChatSpamText.SetDefaultFontName()
        self.ChatSpamText.SetPosition(50, 45)
        self.ChatSpamText.SetFeather()
        self.ChatSpamText.SetText('Texto:')
        self.ChatSpamText.SetFontColor(0.6, 0.7, 1)
        self.ChatSpamText.SetOutline()
        self.ChatSpamText.Show()
        self.ChatTypeText = ui.TextLine()
        self.ChatTypeText.SetParent(self.Board9)
        self.ChatTypeText.SetDefaultFontName()
        self.ChatTypeText.SetPosition(50, 90)
        self.ChatTypeText.SetFeather()
        self.ChatTypeText.SetText('Forma:')
        self.ChatTypeText.SetFontColor(0.6, 0.7, 1)
        self.ChatTypeText.SetOutline()
        self.ChatTypeText.Show()
        self.ChatColourText = ui.TextLine()
        self.ChatColourText.SetParent(self.Board9)
        self.ChatColourText.SetDefaultFontName()
        self.ChatColourText.SetPosition(50, 140)
        self.ChatColourText.SetFeather()
        self.ChatColourText.SetText('Color:')
        self.ChatColourText.SetFontColor(0.6, 0.7, 1)
        self.ChatColourText.SetOutline()
        self.ChatColourText.Show()
        self.Configuration1Text = ui.TextLine()
        self.Configuration1Text.SetParent(self.Board9)
        self.Configuration1Text.SetFontName('Tahoma:14')
        self.Configuration1Text.SetPosition(50, 215)
        self.Configuration1Text.SetFeather()
        self.Configuration1Text.SetText('Configuracion')
        self.Configuration1Text.SetFontColor(0.6, 0.7, 1)
        self.Configuration1Text.SetOutline()
        self.Configuration1Text.Show()
        self.Count1Text = ui.TextLine()
        self.Count1Text.SetParent(self.Board9)
        self.Count1Text.SetDefaultFontName()
        self.Count1Text.SetPosition(50, 235)
        self.Count1Text.SetFeather()
        self.Count1Text.SetText('Cantidad:')
        self.Count1Text.SetFontColor(0.6, 0.7, 1)
        self.Count1Text.SetOutline()
        self.Count1Text.Show()
        self.Delay1Text = ui.TextLine()
        self.Delay1Text.SetParent(self.Board9)
        self.Delay1Text.SetDefaultFontName()
        self.Delay1Text.SetPosition(150, 235)
        self.Delay1Text.SetFeather()
        self.Delay1Text.SetText('Segundos:')
        self.Delay1Text.SetFontColor(0.6, 0.7, 1)
        self.Delay1Text.SetOutline()
        self.Delay1Text.Show()
        self.Error1Text = ui.TextLine()
        self.Error1Text.SetParent(self.Board9)
        self.Error1Text.SetDefaultFontName()
        self.Error1Text.SetPosition(50, 285)
        self.Error1Text.SetFeather()
        self.Error1Text.SetText('Error:')
        self.Error1Text.SetFontColor(0.6, 0.7, 1)
        self.Error1Text.SetOutline()
        self.Error1Text.Show()
        self.Error1Log = ui.TextLine()
        self.Error1Log.SetParent(self.Board9)
        self.Error1Log.SetDefaultFontName()
        self.Error1Log.SetPosition(50, 305)
        self.Error1Log.SetFeather()
        self.Error1Log.SetText('No hay errores')
        self.Error1Log.SetFontColor(1.0, 1.0, 1.0)
        self.Error1Log.SetOutline()
        self.Error1Log.Show()
        self.Error1LogRight = ui.TextLine()
        self.Error1LogRight.SetParent(self.Board9)
        self.Error1LogRight.SetDefaultFontName()
        self.Error1LogRight.SetPosition(230, 305)
        self.Error1LogRight.SetFeather()
        self.Error1LogRight.SetText('')
        self.Error1LogRight.SetFontColor(1.0, 1.0, 1.0)
        self.Error1LogRight.SetOutline()
        self.Error1LogRight.Show()
        self.Error1Log2 = ui.TextLine()
        self.Error1Log2.SetParent(self.Board9)
        self.Error1Log2.SetDefaultFontName()
        self.Error1Log2.SetPosition(50, 325)
        self.Error1Log2.SetFeather()
        self.Error1Log2.SetText('')
        self.Error1Log2.SetFontColor(1.0, 1.0, 1.0)
        self.Error1Log2.SetOutline()
        self.Error1Log2.Show()
        self.Error1Log2Right = ui.TextLine()
        self.Error1Log2Right.SetParent(self.Board9)
        self.Error1Log2Right.SetDefaultFontName()
        self.Error1Log2Right.SetPosition(230, 325)
        self.Error1Log2Right.SetFeather()
        self.Error1Log2Right.SetText('')
        self.Error1Log2Right.SetFontColor(1.0, 1.0, 1.0)
        self.Error1Log2Right.SetOutline()
        self.Error1Log2Right.Show()
        self.Last1ChangeText = ui.TextLine()
        self.Last1ChangeText.SetParent(self.Board9)
        self.Last1ChangeText.SetDefaultFontName()
        self.Last1ChangeText.SetPosition(50, 350)
        self.Last1ChangeText.SetFeather()
        self.Last1ChangeText.SetText('Informacion del bot:')
        self.Last1ChangeText.SetFontColor(0.6, 0.7, 1)
        self.Last1ChangeText.SetOutline()
        self.Last1ChangeText.Show()
        self.Last1Change = ui.TextLine()
        self.Last1Change.SetParent(self.Board9)
        self.Last1Change.SetDefaultFontName()
        self.Last1Change.SetPosition(50, 370)
        self.Last1Change.SetFeather()
        self.Last1Change.SetText('Ninguna')
        self.Last1Change.SetFontColor(1.0, 1.0, 1.0)
        self.Last1Change.SetOutline()
        self.Last1Change.Show()
        self.Creator1Text = ui.TextLine()
        self.Creator1Text.SetParent(self.Board9)
        self.Creator1Text.SetDefaultFontName()
        self.Creator1Text.SetPosition(305, 435)
        self.Creator1Text.SetFeather()
        self.Creator1Text.SetText('Chat Spam')
        self.Creator1Text.SetFontColor(1.0, 0.5, 0.5)
        self.Creator1Text.SetOutline()
        self.Creator1Text.Show()
        self.DelayChatSpamSlotBar = ui.SlotBar()
        self.DelayChatSpamSlotBar.SetParent(self.Board9)
        self.DelayChatSpamSlotBar.SetSize(60, 18)
        self.DelayChatSpamSlotBar.SetPosition(-17, 255)
        self.DelayChatSpamSlotBar.SetWindowHorizontalAlignCenter()
        self.DelayChatSpamSlotBar.Show()
        self.DelayChatSpamEditLine = ui.EditLine()
        self.DelayChatSpamEditLine.SetParent(self.DelayChatSpamSlotBar)
        self.DelayChatSpamEditLine.SetSize(60, 17)
        self.DelayChatSpamEditLine.SetPosition(10, 2)
        self.DelayChatSpamEditLine.SetMax(3)
        self.DelayChatSpamEditLine.SetNumberMode()
        self.DelayChatSpamEditLine.SetFocus()
        self.DelayChatSpamEditLine.SetText('0')
        self.DelayChatSpamEditLine.SetTabEvent(ui.__mem_func__(self.Start1SpamBot))
        self.DelayChatSpamEditLine.SetReturnEvent(ui.__mem_func__(self.Start1SpamBot))
        self.DelayChatSpamEditLine.Show()
        self.CountChatSpamSlotBar = ui.SlotBar()
        self.CountChatSpamSlotBar.SetParent(self.Board9)
        self.CountChatSpamSlotBar.SetSize(60, 18)
        self.CountChatSpamSlotBar.SetPosition(-117, 255)
        self.CountChatSpamSlotBar.SetWindowHorizontalAlignCenter()
        self.CountChatSpamSlotBar.Show()
        self.CountChatSpamEditLine = ui.EditLine()
        self.CountChatSpamEditLine.SetParent(self.CountChatSpamSlotBar)
        self.CountChatSpamEditLine.SetSize(60, 17)
        self.CountChatSpamEditLine.SetPosition(10, 2)
        self.CountChatSpamEditLine.SetMax(5)
        self.CountChatSpamEditLine.SetNumberMode()
        self.CountChatSpamEditLine.SetFocus()
        self.CountChatSpamEditLine.SetText('0')
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
        self.CrearGremioSlotBar = ui.SlotBar()
        self.CrearGremioSlotBar.SetParent(self.Board17)
        self.CrearGremioSlotBar.SetSize(75, 18)
        self.CrearGremioSlotBar.SetPosition(75, 47)
        self.CrearGremioSlotBar.Show()
        self.CrearGremioEditLine = ui.EditLine()
        self.CrearGremioEditLine.SetParent(self.CrearGremioSlotBar)
        self.CrearGremioEditLine.SetSize(75, 17)
        self.CrearGremioEditLine.SetPosition(10, 2)
        self.CrearGremioEditLine.SetMax(12)
        self.CrearGremioEditLine.SetFocus()
        self.CrearGremioEditLine.Show()
        self.PJText = ui.TextLine()
        self.PJText.SetParent(self.Board4)
        self.PJText.SetDefaultFontName()
        self.PJText.SetPosition(20, 360)
        self.PJText.SetFeather()
        self.PJText.SetText('Esconder PJ:')
        self.PJText.SetOutline()
        self.PJText.Show()
        self.CrearGremioText = ui.TextLine()
        self.CrearGremioText.SetParent(self.Board17)
        self.CrearGremioText.SetDefaultFontName()
        self.CrearGremioText.SetPosition(20, 50)
        self.CrearGremioText.SetFeather()
        self.CrearGremioText.SetText('Nombre:')
        self.CrearGremioText.SetOutline()
        self.CrearGremioText.Show()
        self.CopiarText = ui.TextLine()
        self.CopiarText.SetParent(self.Board4)
        self.CopiarText.SetDefaultFontName()
        self.CopiarText.SetPosition(20, 415)
        self.CopiarText.SetFeather()
        self.CopiarText.SetText('Copiar/Pegar:')
        self.CopiarText.SetOutline()
        self.CopiarText.Show()
        self.GmvisualText = ui.TextLine()
        self.GmvisualText.SetParent(self.Board4)
        self.GmvisualText.SetDefaultFontName()
        self.GmvisualText.SetPosition(120, 415)
        self.GmvisualText.SetFeather()
        self.GmvisualText.SetText('Gm Visual:')
        self.GmvisualText.SetOutline()
        self.GmvisualText.Show()
        self.GmText = ui.TextLine()
        self.GmText.SetParent(self.Board12)
        self.GmText.SetDefaultFontName()
        self.GmText.SetPosition(20, 35)
        self.GmText.SetFeather()
        self.GmText.SetText('Detector de GM:')
        self.GmText.SetOutline()
        self.GmText.Show()
        self.TargetName = ui.TextLine()
        self.TargetName.SetParent(self.Board10)
        self.TargetName.SetDefaultFontName()
        self.TargetName.SetPosition(-70, 33)
        self.TargetName.SetFeather()
        self.TargetName.SetWindowHorizontalAlignCenter()
        self.TargetName.SetText('None')
        self.TargetName.SetOutline()
        self.TargetName.Show()
        self.Info = ui.TextLine()
        self.Info.SetParent(self.Board10)
        self.Info.SetDefaultFontName()
        self.Info.SetPosition(-125, 33)
        self.Info.SetFeather()
        self.Info.SetWindowHorizontalAlignCenter()
        self.Info.SetFontColor(1.0, 0.8, 0)
        self.Info.SetText('Seleccion: ')
        self.Info.SetOutline()
        self.Info.Show()
        self.Info3 = ui.TextLine()
        self.Info3.SetParent(self.Board10)
        self.Info3.SetDefaultFontName()
        self.Info3.SetPosition(-125, 70)
        self.Info3.SetFeather()
        self.Info3.SetWindowHorizontalAlignCenter()
        self.Info3.SetFontColor(1.0, 0.8, 0)
        self.Info3.SetText('Segundos:')
        self.Info3.SetOutline()
        self.Info3.Show()
        self.SuraM = ui.TextLine()
        self.SuraM.SetParent(self.Board11)
        self.SuraM.SetDefaultFontName()
        self.SuraM.SetPosition(210, 40)
        self.SuraM.SetFeather()
        self.SuraM.SetWindowHorizontalAlignCenter()
        self.SuraM.SetText('Sura M')
        self.SuraM.SetOutline()
        self.SuraM.Show()
        self.SuraA = ui.TextLine()
        self.SuraA.SetParent(self.Board11)
        self.SuraA.SetDefaultFontName()
        self.SuraA.SetPosition(140, 40)
        self.SuraA.SetFeather()
        self.SuraA.SetWindowHorizontalAlignCenter()
        self.SuraA.SetText('Sura A')
        self.SuraA.SetOutline()
        self.SuraA.Show()
        self.Segs = ui.TextLine()
        self.Segs.SetParent(self.Board11)
        self.Segs.SetDefaultFontName()
        self.Segs.SetPosition(-189, 333)
        self.Segs.SetFeather()
        self.Segs.SetWindowHorizontalAlignCenter()
        self.Segs.SetText('Seg')
        self.Segs.SetOutline()
        self.Segs.Show()
        self.Velocidad = ui.TextLine()
        self.Velocidad.SetParent(self.Board11)
        self.Velocidad.SetDefaultFontName()
        self.Velocidad.SetPosition(-280, 333)
        self.Velocidad.SetFeather()
        self.Velocidad.SetWindowHorizontalAlignCenter()
        self.Velocidad.SetText('Velocidad')
        self.Velocidad.SetOutline()
        self.Velocidad.Show()
        self.Chamandragon = ui.TextLine()
        self.Chamandragon.SetParent(self.Board11)
        self.Chamandragon.SetDefaultFontName()
        self.Chamandragon.SetPosition(70, 40)
        self.Chamandragon.SetFeather()
        self.Chamandragon.SetWindowHorizontalAlignCenter()
        self.Chamandragon.SetText('Chaman D')
        self.Chamandragon.SetOutline()
        self.Chamandragon.Show()
        self.Chamanluz = ui.TextLine()
        self.Chamanluz.SetParent(self.Board11)
        self.Chamanluz.SetDefaultFontName()
        self.Chamanluz.SetPosition(0, 40)
        self.Chamanluz.SetFeather()
        self.Chamanluz.SetWindowHorizontalAlignCenter()
        self.Chamanluz.SetText('Chaman L')
        self.Chamanluz.SetOutline()
        self.Chamanluz.Show()
        self.Guerreromental = ui.TextLine()
        self.Guerreromental.SetParent(self.Board11)
        self.Guerreromental.SetDefaultFontName()
        self.Guerreromental.SetPosition(-74, 40)
        self.Guerreromental.SetFeather()
        self.Guerreromental.SetWindowHorizontalAlignCenter()
        self.Guerreromental.SetText('Guerrero M')
        self.Guerreromental.SetOutline()
        self.Guerreromental.Show()
        self.Guerrerocorporal = ui.TextLine()
        self.Guerrerocorporal.SetParent(self.Board11)
        self.Guerrerocorporal.SetDefaultFontName()
        self.Guerrerocorporal.SetPosition(-144, 40)
        self.Guerrerocorporal.SetFeather()
        self.Guerrerocorporal.SetWindowHorizontalAlignCenter()
        self.Guerrerocorporal.SetText('Guerrero C')
        self.Guerrerocorporal.SetOutline()
        self.Guerrerocorporal.Show()
        self.Ninjaarco = ui.TextLine()
        self.Ninjaarco.SetParent(self.Board11)
        self.Ninjaarco.SetDefaultFontName()
        self.Ninjaarco.SetPosition(-214, 40)
        self.Ninjaarco.SetFeather()
        self.Ninjaarco.SetWindowHorizontalAlignCenter()
        self.Ninjaarco.SetText('Ninja arco')
        self.Ninjaarco.SetOutline()
        self.Ninjaarco.Show()
        self.Ninjahoja = ui.TextLine()
        self.Ninjahoja.SetParent(self.Board11)
        self.Ninjahoja.SetDefaultFontName()
        self.Ninjahoja.SetPosition(-280, 40)
        self.Ninjahoja.SetFeather()
        self.Ninjahoja.SetWindowHorizontalAlignCenter()
        self.Ninjahoja.SetText('Ninja hoja')
        self.Ninjahoja.SetOutline()
        self.Ninjahoja.Show()
        self.InfoDelay = ui.TextLine()
        self.InfoDelay.SetParent(self.Board10)
        self.InfoDelay.SetDefaultFontName()
        self.InfoDelay.SetPosition(-30, 90)
        self.InfoDelay.SetFeather()
        self.InfoDelay.SetWindowHorizontalAlignCenter()
        self.InfoDelay.SetFontColor(1.0, 0.8, 0)
        self.InfoDelay.SetText('0 Segundos')
        self.InfoDelay.SetOutline()
        self.InfoDelay.Show()
        self.WhisperSpamTitle = ui.TextLine()
        self.WhisperSpamTitle.SetParent(self.Board15)
        self.WhisperSpamTitle.SetPosition(60, 10)
        self.WhisperSpamTitle.SetFeather()
        self.WhisperSpamTitle.SetFontName('STENCIL:32')
        self.WhisperSpamTitle.SetText('')
        self.WhisperSpamTitle.SetFontColor(0.0, 0.7, 1)
        self.WhisperSpamTitle.SetOutline()
        self.WhisperSpamTitle.Show()
        self.WhisperSpamText = ui.TextLine()
        self.WhisperSpamText.SetParent(self.Board15)
        self.WhisperSpamText.SetDefaultFontName()
        self.WhisperSpamText.SetPosition(50, 45)
        self.WhisperSpamText.SetFeather()
        self.WhisperSpamText.SetText('Texto:')
        self.WhisperSpamText.SetFontColor(0.6, 0.7, 1)
        self.WhisperSpamText.SetOutline()
        self.WhisperSpamText.Show()
        self.WhisperTypeText = ui.TextLine()
        self.WhisperTypeText.SetParent(self.Board15)
        self.WhisperTypeText.SetDefaultFontName()
        self.WhisperTypeText.SetPosition(50, 90)
        self.WhisperTypeText.SetFeather()
        self.WhisperTypeText.SetText('Forma:')
        self.WhisperTypeText.SetFontColor(0.6, 0.7, 1)
        self.WhisperTypeText.SetOutline()
        self.WhisperTypeText.Show()
        self.WhisperColourText = ui.TextLine()
        self.WhisperColourText.SetParent(self.Board15)
        self.WhisperColourText.SetDefaultFontName()
        self.WhisperColourText.SetPosition(50, 140)
        self.WhisperColourText.SetFeather()
        self.WhisperColourText.SetText('Color:')
        self.WhisperColourText.SetFontColor(0.6, 0.7, 1)
        self.WhisperColourText.SetOutline()
        self.WhisperColourText.Show()
        self.ConfigurationText = ui.TextLine()
        self.ConfigurationText.SetParent(self.Board15)
        self.ConfigurationText.SetFontName('Tahoma:14')
        self.ConfigurationText.SetPosition(50, 225)
        self.ConfigurationText.SetFeather()
        self.ConfigurationText.SetText('Configuracion')
        self.ConfigurationText.SetFontColor(0.6, 0.7, 1)
        self.ConfigurationText.SetOutline()
        self.ConfigurationText.Show()
        self.CountText = ui.TextLine()
        self.CountText.SetParent(self.Board15)
        self.CountText.SetDefaultFontName()
        self.CountText.SetPosition(50, 245)
        self.CountText.SetFeather()
        self.CountText.SetText('Cantidad:')
        self.CountText.SetFontColor(0.6, 0.7, 1)
        self.CountText.SetOutline()
        self.CountText.Show()
        self.DelayText = ui.TextLine()
        self.DelayText.SetParent(self.Board15)
        self.DelayText.SetDefaultFontName()
        self.DelayText.SetPosition(150, 245)
        self.DelayText.SetFeather()
        self.DelayText.SetText('Segundos:')
        self.DelayText.SetFontColor(0.6, 0.7, 1)
        self.DelayText.SetOutline()
        self.DelayText.Show()
        self.PlayernameText = ui.TextLine()
        self.PlayernameText.SetParent(self.Board15)
        self.PlayernameText.SetDefaultFontName()
        self.PlayernameText.SetPosition(240, 245)
        self.PlayernameText.SetFeather()
        self.PlayernameText.SetText('Nombre del PJ:')
        self.PlayernameText.SetFontColor(0.6, 0.7, 1)
        self.PlayernameText.SetOutline()
        self.PlayernameText.Show()
        self.ErrorText = ui.TextLine()
        self.ErrorText.SetParent(self.Board15)
        self.ErrorText.SetDefaultFontName()
        self.ErrorText.SetPosition(50, 295)
        self.ErrorText.SetFeather()
        self.ErrorText.SetText('Error:')
        self.ErrorText.SetFontColor(0.6, 0.7, 1)
        self.ErrorText.SetOutline()
        self.ErrorText.Show()
        self.ErrorLog = ui.TextLine()
        self.ErrorLog.SetParent(self.Board15)
        self.ErrorLog.SetDefaultFontName()
        self.ErrorLog.SetPosition(50, 315)
        self.ErrorLog.SetFeather()
        self.ErrorLog.SetText('No hay errores.')
        self.ErrorLog.SetFontColor(1.0, 1.0, 1.0)
        self.ErrorLog.SetOutline()
        self.ErrorLog.Show()
        self.ErrorLogRight = ui.TextLine()
        self.ErrorLogRight.SetParent(self.Board15)
        self.ErrorLogRight.SetDefaultFontName()
        self.ErrorLogRight.SetPosition(230, 315)
        self.ErrorLogRight.SetFeather()
        self.ErrorLogRight.SetText('')
        self.ErrorLogRight.SetFontColor(1.0, 1.0, 1.0)
        self.ErrorLogRight.SetOutline()
        self.ErrorLogRight.Show()
        self.ErrorLog2 = ui.TextLine()
        self.ErrorLog2.SetParent(self.Board15)
        self.ErrorLog2.SetDefaultFontName()
        self.ErrorLog2.SetPosition(50, 335)
        self.ErrorLog2.SetFeather()
        self.ErrorLog2.SetText('')
        self.ErrorLog2.SetFontColor(1.0, 1.0, 1.0)
        self.ErrorLog2.SetOutline()
        self.ErrorLog2.Show()
        self.ErrorLog2Right = ui.TextLine()
        self.ErrorLog2Right.SetParent(self.Board15)
        self.ErrorLog2Right.SetDefaultFontName()
        self.ErrorLog2Right.SetPosition(230, 335)
        self.ErrorLog2Right.SetFeather()
        self.ErrorLog2Right.SetText('')
        self.ErrorLog2Right.SetFontColor(1.0, 1.0, 1.0)
        self.ErrorLog2Right.SetOutline()
        self.ErrorLog2Right.Show()
        self.LastChangeText = ui.TextLine()
        self.LastChangeText.SetParent(self.Board15)
        self.LastChangeText.SetDefaultFontName()
        self.LastChangeText.SetPosition(50, 360)
        self.LastChangeText.SetFeather()
        self.LastChangeText.SetText('Informacion del bot:')
        self.LastChangeText.SetFontColor(0.6, 0.7, 1)
        self.LastChangeText.SetOutline()
        self.LastChangeText.Show()
        self.LastChange = ui.TextLine()
        self.LastChange.SetParent(self.Board15)
        self.LastChange.SetDefaultFontName()
        self.LastChange.SetPosition(50, 380)
        self.LastChange.SetFeather()
        self.LastChange.SetText('Ninguna')
        self.LastChange.SetFontColor(1.0, 1.0, 1.0)
        self.LastChange.SetOutline()
        self.LastChange.Show()
        self.CreatorText = ui.TextLine()
        self.CreatorText.SetParent(self.Board15)
        self.CreatorText.SetDefaultFontName()
        self.CreatorText.SetPosition(305, 440)
        self.CreatorText.SetFeather()
        self.CreatorText.SetText('SpamBot')
        self.CreatorText.SetFontColor(1.0, 0.5, 0.5)
        self.CreatorText.SetOutline()
        self.CreatorText.Show()
        self.PlayerWhisperSpamSlotBar = ui.SlotBar()
        self.PlayerWhisperSpamSlotBar.SetParent(self.Board15)
        self.PlayerWhisperSpamSlotBar.SetSize(80, 18)
        self.PlayerWhisperSpamSlotBar.SetPosition(83, 265)
        self.PlayerWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
        self.PlayerWhisperSpamSlotBar.Show()
        self.PlayerWhisperSpamEditLine = ui.EditLine()
        self.PlayerWhisperSpamEditLine.SetParent(self.PlayerWhisperSpamSlotBar)
        self.PlayerWhisperSpamEditLine.SetSize(80, 17)
        self.PlayerWhisperSpamEditLine.SetPosition(10, 2)
        self.PlayerWhisperSpamEditLine.SetMax(12)
        self.PlayerWhisperSpamEditLine.SetFocus()
        self.PlayerWhisperSpamEditLine.SetText('')
        self.PlayerWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.StartSpamBot))
        self.PlayerWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.StartSpamBot))
        self.PlayerWhisperSpamEditLine.Show()
        self.DelayWhisperSpamSlotBar = ui.SlotBar()
        self.DelayWhisperSpamSlotBar.SetParent(self.Board15)
        self.DelayWhisperSpamSlotBar.SetSize(60, 18)
        self.DelayWhisperSpamSlotBar.SetPosition(-17, 265)
        self.DelayWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
        self.DelayWhisperSpamSlotBar.Show()
        self.DelayWhisperSpamEditLine = ui.EditLine()
        self.DelayWhisperSpamEditLine.SetParent(self.DelayWhisperSpamSlotBar)
        self.DelayWhisperSpamEditLine.SetSize(60, 17)
        self.DelayWhisperSpamEditLine.SetPosition(10, 2)
        self.DelayWhisperSpamEditLine.SetMax(3)
        self.DelayWhisperSpamEditLine.SetNumberMode()
        self.DelayWhisperSpamEditLine.SetFocus()
        self.DelayWhisperSpamEditLine.SetText('0')
        self.DelayWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.PlayerWhisperSpamEditLine.SetFocus))
        self.DelayWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.PlayerWhisperSpamEditLine.SetFocus))
        self.DelayWhisperSpamEditLine.Show()
        self.CountWhisperSpamSlotBar = ui.SlotBar()
        self.CountWhisperSpamSlotBar.SetParent(self.Board15)
        self.CountWhisperSpamSlotBar.SetSize(60, 18)
        self.CountWhisperSpamSlotBar.SetPosition(-117, 265)
        self.CountWhisperSpamSlotBar.SetWindowHorizontalAlignCenter()
        self.CountWhisperSpamSlotBar.Show()
        self.CountWhisperSpamEditLine = ui.EditLine()
        self.CountWhisperSpamEditLine.SetParent(self.CountWhisperSpamSlotBar)
        self.CountWhisperSpamEditLine.SetSize(60, 17)
        self.CountWhisperSpamEditLine.SetPosition(10, 2)
        self.CountWhisperSpamEditLine.SetMax(5)
        self.CountWhisperSpamEditLine.SetNumberMode()
        self.CountWhisperSpamEditLine.SetFocus()
        self.CountWhisperSpamEditLine.SetText('0')
        self.CountWhisperSpamEditLine.SetTabEvent(ui.__mem_func__(self.DelayWhisperSpamEditLine.SetFocus))
        self.CountWhisperSpamEditLine.SetReturnEvent(ui.__mem_func__(self.DelayWhisperSpamEditLine.SetFocus))
        self.CountWhisperSpamEditLine.Show()
        self.WhisperSpamSlotBar = ui.SlotBar()
        self.WhisperSpamSlotBar.SetParent(self.Board15)
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
        self.Habilidad1SlotBar = ui.SlotBar()
        self.Habilidad1SlotBar.SetParent(self.Board16)
        self.Habilidad1SlotBar.SetSize(30, 18)
        self.Habilidad1SlotBar.SetPosition(60, 50)
        self.Habilidad1SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad1SlotBar.Show()
        self.Habilidad1 = ui.EditLine()
        self.Habilidad1.SetParent(self.Habilidad1SlotBar)
        self.Habilidad1.SetSize(30, 17)
        self.Habilidad1.SetPosition(10, 2)
        self.Habilidad1.SetText('15')
        self.Habilidad1.SetMax(2)
        self.Habilidad1.SetFocus()
        self.Habilidad1.Show()
        self.Habilidad2SlotBar = ui.SlotBar()
        self.Habilidad2SlotBar.SetParent(self.Board16)
        self.Habilidad2SlotBar.SetSize(30, 18)
        self.Habilidad2SlotBar.SetPosition(60, 80)
        self.Habilidad2SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad2SlotBar.Show()
        self.Habilidad2 = ui.EditLine()
        self.Habilidad2.SetParent(self.Habilidad2SlotBar)
        self.Habilidad2.SetSize(30, 17)
        self.Habilidad2.SetText('15')
        self.Habilidad2.SetPosition(10, 2)
        self.Habilidad2.SetMax(2)
        self.Habilidad2.SetFocus()
        self.Habilidad2.Show()
        self.Habilidad3SlotBar = ui.SlotBar()
        self.Habilidad3SlotBar.SetParent(self.Board16)
        self.Habilidad3SlotBar.SetSize(30, 18)
        self.Habilidad3SlotBar.SetPosition(60, 110)
        self.Habilidad3SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad3SlotBar.Show()
        self.Habilidad3 = ui.EditLine()
        self.Habilidad3.SetParent(self.Habilidad3SlotBar)
        self.Habilidad3.SetSize(30, 17)
        self.Habilidad3.SetPosition(10, 2)
        self.Habilidad3.SetText('15')
        self.Habilidad3.SetMax(2)
        self.Habilidad3.SetFocus()
        self.Habilidad3.Show()
        self.Habilidad4SlotBar = ui.SlotBar()
        self.Habilidad4SlotBar.SetParent(self.Board16)
        self.Habilidad4SlotBar.SetSize(30, 18)
        self.Habilidad4SlotBar.SetPosition(60, 140)
        self.Habilidad4SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad4SlotBar.Show()
        self.Habilidad4 = ui.EditLine()
        self.Habilidad4.SetParent(self.Habilidad4SlotBar)
        self.Habilidad4.SetSize(30, 17)
        self.Habilidad4.SetPosition(10, 2)
        self.Habilidad4.SetText('15')
        self.Habilidad4.SetMax(2)
        self.Habilidad4.SetFocus()
        self.Habilidad4.Show()
        self.Habilidad5SlotBar = ui.SlotBar()
        self.Habilidad5SlotBar.SetParent(self.Board16)
        self.Habilidad5SlotBar.SetSize(30, 18)
        self.Habilidad5SlotBar.SetPosition(60, 170)
        self.Habilidad5SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad5SlotBar.Show()
        self.Habilidad5 = ui.EditLine()
        self.Habilidad5.SetParent(self.Habilidad5SlotBar)
        self.Habilidad5.SetSize(30, 17)
        self.Habilidad5.SetPosition(10, 2)
        self.Habilidad5.SetText('15')
        self.Habilidad5.SetMax(2)
        self.Habilidad5.SetFocus()
        self.Habilidad5.Show()
        self.Habilidad6SlotBar = ui.SlotBar()
        self.Habilidad6SlotBar.SetParent(self.Board16)
        self.Habilidad6SlotBar.SetSize(30, 18)
        self.Habilidad6SlotBar.SetPosition(60, 200)
        self.Habilidad6SlotBar.SetWindowHorizontalAlignCenter()
        self.Habilidad6SlotBar.Show()
        self.Habilidad6 = ui.EditLine()
        self.Habilidad6.SetParent(self.Habilidad6SlotBar)
        self.Habilidad6.SetSize(30, 17)
        self.Habilidad6.SetPosition(10, 2)
        self.Habilidad6.SetText('15')
        self.Habilidad6.SetMax(2)
        self.Habilidad6.SetFocus()
        self.Habilidad6.Show()
        self.Habilidad1Texto = ui.TextLine()
        self.Habilidad1Texto.SetParent(self.Board16)
        self.Habilidad1Texto.SetDefaultFontName()
        self.Habilidad1Texto.SetPosition(-80, 53)
        self.Habilidad1Texto.SetFeather()
        self.Habilidad1Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad1Texto.SetText('Habilidad 1:')
        self.Habilidad1Texto.SetOutline()
        self.Habilidad1Texto.Show()
        self.Habilidad2Texto = ui.TextLine()
        self.Habilidad2Texto.SetParent(self.Board16)
        self.Habilidad2Texto.SetDefaultFontName()
        self.Habilidad2Texto.SetPosition(-80, 83)
        self.Habilidad2Texto.SetFeather()
        self.Habilidad2Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad2Texto.SetText('Habilidad 2:')
        self.Habilidad2Texto.SetOutline()
        self.Habilidad2Texto.Show()
        self.Habilidad3Texto = ui.TextLine()
        self.Habilidad3Texto.SetParent(self.Board16)
        self.Habilidad3Texto.SetDefaultFontName()
        self.Habilidad3Texto.SetPosition(-80, 113)
        self.Habilidad3Texto.SetFeather()
        self.Habilidad3Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad3Texto.SetText('Habilidad 3:')
        self.Habilidad3Texto.SetOutline()
        self.Habilidad3Texto.Show()
        self.Habilidad4Texto = ui.TextLine()
        self.Habilidad4Texto.SetParent(self.Board16)
        self.Habilidad4Texto.SetDefaultFontName()
        self.Habilidad4Texto.SetPosition(-80, 143)
        self.Habilidad4Texto.SetFeather()
        self.Habilidad4Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad4Texto.SetText('Habilidad 4:')
        self.Habilidad4Texto.SetOutline()
        self.Habilidad4Texto.Show()
        self.Habilidad5Texto = ui.TextLine()
        self.Habilidad5Texto.SetParent(self.Board16)
        self.Habilidad5Texto.SetDefaultFontName()
        self.Habilidad5Texto.SetPosition(-80, 173)
        self.Habilidad5Texto.SetFeather()
        self.Habilidad5Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad5Texto.SetText('Habilidad 5:')
        self.Habilidad5Texto.SetOutline()
        self.Habilidad5Texto.Show()
        self.Habilidad6Texto = ui.TextLine()
        self.Habilidad6Texto.SetParent(self.Board16)
        self.Habilidad6Texto.SetDefaultFontName()
        self.Habilidad6Texto.SetPosition(-80, 203)
        self.Habilidad6Texto.SetFeather()
        self.Habilidad6Texto.SetWindowHorizontalAlignCenter()
        self.Habilidad6Texto.SetText('Habilidad 6:')
        self.Habilidad6Texto.SetOutline()
        self.Habilidad6Texto.Show()
        self.Tiempo1Texto = ui.TextLine()
        self.Tiempo1Texto.SetParent(self.Board16)
        self.Tiempo1Texto.SetDefaultFontName()
        self.Tiempo1Texto.SetPosition(13, 53)
        self.Tiempo1Texto.SetFeather()
        self.Tiempo1Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo1Texto.SetText('Vel 1:')
        self.Tiempo1Texto.SetOutline()
        self.Tiempo1Texto.Show()
        self.Tiempo2Texto = ui.TextLine()
        self.Tiempo2Texto.SetParent(self.Board16)
        self.Tiempo2Texto.SetDefaultFontName()
        self.Tiempo2Texto.SetPosition(13, 83)
        self.Tiempo2Texto.SetFeather()
        self.Tiempo2Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo2Texto.SetText('Vel 2:')
        self.Tiempo2Texto.SetOutline()
        self.Tiempo2Texto.Show()
        self.Tiempo3Texto = ui.TextLine()
        self.Tiempo3Texto.SetParent(self.Board16)
        self.Tiempo3Texto.SetDefaultFontName()
        self.Tiempo3Texto.SetPosition(13, 113)
        self.Tiempo3Texto.SetFeather()
        self.Tiempo3Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo3Texto.SetText('Vel 3:')
        self.Tiempo3Texto.SetOutline()
        self.Tiempo3Texto.Show()
        self.Tiempo4Texto = ui.TextLine()
        self.Tiempo4Texto.SetParent(self.Board16)
        self.Tiempo4Texto.SetDefaultFontName()
        self.Tiempo4Texto.SetPosition(13, 143)
        self.Tiempo4Texto.SetFeather()
        self.Tiempo4Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo4Texto.SetText('Vel 4:')
        self.Tiempo4Texto.SetOutline()
        self.Tiempo4Texto.Show()
        self.Tiempo5Texto = ui.TextLine()
        self.Tiempo5Texto.SetParent(self.Board16)
        self.Tiempo5Texto.SetDefaultFontName()
        self.Tiempo5Texto.SetPosition(13, 173)
        self.Tiempo5Texto.SetFeather()
        self.Tiempo5Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo5Texto.SetText('Vel 5:')
        self.Tiempo5Texto.SetOutline()
        self.Tiempo5Texto.Show()
        self.Tiempo6Texto = ui.TextLine()
        self.Tiempo6Texto.SetParent(self.Board16)
        self.Tiempo6Texto.SetDefaultFontName()
        self.Tiempo6Texto.SetPosition(13, 203)
        self.Tiempo6Texto.SetFeather()
        self.Tiempo6Texto.SetWindowHorizontalAlignCenter()
        self.Tiempo6Texto.SetText('Vel 6:')
        self.Tiempo6Texto.SetOutline()
        self.Tiempo6Texto.Show()
        self.Habilidad1boton = ui.Button()
        self.Habilidad1boton.SetParent(self.Board16)
        self.Habilidad1boton.SetPosition(78, 53)
        self.Habilidad1boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad1boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad1boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad1boton.SetToolTipText('Activar')
        self.Habilidad1boton.SetEvent(ui.__mem_func__(self.Habilidad1Funcion))
        self.Habilidad1boton.Show()
        self.Habilidad2boton = ui.Button()
        self.Habilidad2boton.SetParent(self.Board16)
        self.Habilidad2boton.SetPosition(78, 83)
        self.Habilidad2boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad2boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad2boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad2boton.SetToolTipText('Activar')
        self.Habilidad2boton.SetEvent(ui.__mem_func__(self.Habilidad2Funcion))
        self.Habilidad2boton.Show()
        self.Habilidad3boton = ui.Button()
        self.Habilidad3boton.SetParent(self.Board16)
        self.Habilidad3boton.SetPosition(78, 113)
        self.Habilidad3boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad3boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad3boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad3boton.SetToolTipText('Activar')
        self.Habilidad3boton.SetEvent(ui.__mem_func__(self.Habilidad3Funcion))
        self.Habilidad3boton.Show()
        self.Habilidad4boton = ui.Button()
        self.Habilidad4boton.SetParent(self.Board16)
        self.Habilidad4boton.SetPosition(78, 143)
        self.Habilidad4boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad4boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad4boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad4boton.SetToolTipText('Activar')
        self.Habilidad4boton.SetEvent(ui.__mem_func__(self.Habilidad4Funcion))
        self.Habilidad4boton.Show()
        self.Habilidad5boton = ui.Button()
        self.Habilidad5boton.SetParent(self.Board16)
        self.Habilidad5boton.SetPosition(78, 173)
        self.Habilidad5boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad5boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad5boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad5boton.SetToolTipText('Activar')
        self.Habilidad5boton.SetEvent(ui.__mem_func__(self.Habilidad5Funcion))
        self.Habilidad5boton.Show()
        self.Habilidad6boton = ui.Button()
        self.Habilidad6boton.SetParent(self.Board16)
        self.Habilidad6boton.SetPosition(78, 203)
        self.Habilidad6boton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.Habilidad6boton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.Habilidad6boton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.Habilidad6boton.SetToolTipText('Activar')
        self.Habilidad6boton.SetEvent(ui.__mem_func__(self.Habilidad6Funcion))
        self.Habilidad6boton.Show()
        self.ColourList = []
        self.WhisperTypeList = []
        x = 55
        i = 0
        for Whispertype in self.WHISPER_MODE:
            WhispertypeButton = ui.Button()
            WhispertypeButton.SetParent(self.Board15)
            WhispertypeButton.SetPosition(x, 110)
            WhispertypeButton.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            WhispertypeButton.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            WhispertypeButton.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            WhispertypeButton.SetText(Whispertype)
            WhispertypeButton.Show()
            Type = self.WHISPER_MODE[i]
            WhispertypeButton.SetEvent(lambda arg=Type: self.UseWhisperType(arg))
            WhispertypeButton.SetEvent(lambda arg=Type: self.UseWhisperType(arg))
            self.WhisperTypeList.append(WhispertypeButton)
            x += 48
            i += 1

        x = 40
        i = 0
        for Colour in self.COLOUR_MODE_NAME2:
            Colour2Button = ui.Button()
            Colour2Button.SetParent(self.Board15)
            Colour2Button.SetPosition(x, 185)
            Colour2Button.SetUpVisual('d:/ymir work/ui/public/small_Button_01.sub')
            Colour2Button.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            Colour2Button.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            Colour2Button.SetText(Colour)
            Colour2Button.Show()
            Type = self.COLOUR_MODE_INDEX2[i]
            Colour2Button.SetEvent(lambda arg=Type: self.UseWhisperColour(arg))
            Colour2Button.SetEvent(lambda arg=Type: self.UseWhisperColour(arg))
            self.ColourList.append(Colour2Button)
            x += 48
            i += 1

        x = 40
        i = 0
        for Colour in self.COLOUR_MODE_NAME:
            ColourButton = ui.Button()
            ColourButton.SetParent(self.Board15)
            ColourButton.SetPosition(x, 160)
            ColourButton.SetUpVisual('d:/ymir work/ui/public/small_Button_01.sub')
            ColourButton.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            ColourButton.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            ColourButton.SetText(Colour)
            ColourButton.Show()
            Type = self.COLOUR_MODE_INDEX[i]
            ColourButton.SetEvent(lambda arg=Type: self.UseWhisperColour(arg))
            ColourButton.SetEvent(lambda arg=Type: self.UseWhisperColour(arg))
            self.ColourList.append(ColourButton)
            x += 48
            i += 1

        self.StartWhisperSpamButton = ui.Button()
        self.StartWhisperSpamButton.SetParent(self.Board15)
        self.StartWhisperSpamButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\start_0.tga')
        self.StartWhisperSpamButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\start_1.tga')
        self.StartWhisperSpamButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\start_2.tga')
        self.StartWhisperSpamButton.SetToolTipText('Activar')
        self.StartWhisperSpamButton.SetPosition(60, 415)
        self.StartWhisperSpamButton.SetEvent(ui.__mem_func__(self.StartSpamBot))
        self.StartWhisperSpamButton.Show()
        self.StopWhisperSpamButton = ui.Button()
        self.StopWhisperSpamButton.SetParent(self.Board15)
        self.StopWhisperSpamButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\stop_0.tga')
        self.StopWhisperSpamButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\stop_1.tga')
        self.StopWhisperSpamButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\stop2.tga')
        self.StopWhisperSpamButton.SetToolTipText('Desactivar')
        self.StopWhisperSpamButton.SetPosition(200, 415)
        self.StopWhisperSpamButton.SetEvent(ui.__mem_func__(self.StopSpamBot))
        self.StopWhisperSpamButton.Show()
        self.CrearGremio01Button = ui.Button()
        self.CrearGremio01Button.SetParent(self.Board17)
        self.CrearGremio01Button.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.CrearGremio01Button.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.CrearGremio01Button.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.CrearGremio01Button.SetToolTipText('Necesitas 300k')
        self.CrearGremio01Button.SetText('Crear')
        self.CrearGremio01Button.SetPosition(167, 47)
        self.CrearGremio01Button.SetEvent(ui.__mem_func__(self.CrearGremio01))
        self.CrearGremio01Button.Show()
        self.velocidad = self.comp.Button(self.Board14, 'Velocidad', '', 30, 60, self.velocidad_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.camara = self.comp.Button(self.Board14, 'Camara', '', 95, 60, self.camara_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.spammbot = self.comp.Button(self.Board14, 'Spamm bot', '', 160, 90, self.spammbot_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.mpcolor = self.comp.Button(self.Board14, 'MP Color', '', 160, 120, self.mpcolor_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.buffbot = self.comp.Button(self.Board14, 'Buffbot', '', 160, 60, self.buffbot_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.botlibros = self.comp.Button(self.Board14, 'Bot de libros', '', 30, 90, self.botlibros_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.detectorgm = self.comp.Button(self.Board14, 'Detector Gm', '', 95, 90, self.detectorgm_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.otroshacks = self.comp.Button(self.Board14, 'Otros hacks', '', 95, 120, self.otroshacks_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.creditos = self.comp.Button(self.Board14, 'Creditos', '', 30, 120, self.creditos_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.salir = self.comp.Button(self.Board14, 'Salir', '', 95, 150, self.salir_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.TirarCHButton = ui.Button()
        self.TirarCHButton.SetParent(self.Board4)
        self.TirarCHButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.TirarCHButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.TirarCHButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.TirarCHButton.SetToolTipText('Funciona en pocos servidores')
        self.TirarCHButton.SetText('CH OFF')
        self.TirarCHButton.SetPosition(115, 450)
        self.TirarCHButton.SetEvent(ui.__mem_func__(self.TirarCH))
        self.TirarCHButton.Show()
        self.CrearGremioButton = ui.Button()
        self.CrearGremioButton.SetParent(self.Board4)
        self.CrearGremioButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.CrearGremioButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.CrearGremioButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.CrearGremioButton.SetToolTipText('Necesitas 300k')
        self.CrearGremioButton.SetText('Crear Gremio')
        self.CrearGremioButton.SetPosition(20, 450)
        self.CrearGremioButton.SetEvent(ui.__mem_func__(self.CrearGremio))
        self.CrearGremioButton.Show()
        self.ActivarDistanciaButton = ui.Button()
        self.ActivarDistanciaButton.SetParent(self.Board13)
        self.ActivarDistanciaButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.ActivarDistanciaButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.ActivarDistanciaButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.ActivarDistanciaButton.SetToolTipText('Cambiar distancia')
        self.ActivarDistanciaButton.SetText('Cambiar')
        self.ActivarDistanciaButton.SetPosition(20, 75)
        self.ActivarDistanciaButton.SetEvent(ui.__mem_func__(self.ActivarDistancia))
        self.ActivarDistanciaButton.Show()
        self.DistanciaButton = ui.Button()
        self.DistanciaButton.SetParent(self.Board8)
        self.DistanciaButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.DistanciaButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.DistanciaButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.DistanciaButton.SetToolTipText('Configuracion de distancia')
        self.DistanciaButton.SetText('Configuracion')
        self.DistanciaButton.SetPosition(120, 150)
        self.DistanciaButton.SetEvent(ui.__mem_func__(self.Board13.Show))
        self.DistanciaButton.Show()
        self.AtrasButton = ui.Button()
        self.AtrasButton.SetParent(self.Board8)
        self.AtrasButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.AtrasButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.AtrasButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.AtrasButton.SetToolTipText('Ir hacia atras')
        self.AtrasButton.SetText('Atras')
        self.AtrasButton.SetPosition(65, 100)
        self.AtrasButton.SetEvent(ui.__mem_func__(self.Atras))
        self.AtrasButton.Show()
        self.AdelanteButton = ui.Button()
        self.AdelanteButton.SetParent(self.Board8)
        self.AdelanteButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.AdelanteButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.AdelanteButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.AdelanteButton.SetToolTipText('Ir hacia adelante')
        self.AdelanteButton.SetText('Adelante')
        self.AdelanteButton.SetPosition(65, 40)
        self.AdelanteButton.SetEvent(ui.__mem_func__(self.Adelante))
        self.AdelanteButton.Show()
        self.DerechaButton = ui.Button()
        self.DerechaButton.SetParent(self.Board8)
        self.DerechaButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.DerechaButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.DerechaButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.DerechaButton.SetToolTipText('Ir hacia la derecha')
        self.DerechaButton.SetText('Derecha')
        self.DerechaButton.SetPosition(125, 70)
        self.DerechaButton.SetEvent(ui.__mem_func__(self.Derecha))
        self.DerechaButton.Show()
        self.IzquierdaButton = ui.Button()
        self.IzquierdaButton.SetParent(self.Board8)
        self.IzquierdaButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.IzquierdaButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.IzquierdaButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.IzquierdaButton.SetToolTipText('Ir hacia la izquierda')
        self.IzquierdaButton.SetText('Izquierda')
        self.IzquierdaButton.SetPosition(10, 70)
        self.IzquierdaButton.SetEvent(ui.__mem_func__(self.Izquierda))
        self.IzquierdaButton.Show()
        self.LibroBot00Button = ui.Button()
        self.LibroBot00Button.SetParent(self.Board11)
        self.LibroBot00Button.SetUpVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
        self.LibroBot00Button.SetOverVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
        self.LibroBot00Button.SetDownVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
        self.LibroBot00Button.SetToolTipText('Activar')
        self.LibroBot00Button.SetPosition(20, 70)
        self.LibroBot00Button.SetEvent(ui.__mem_func__(self.LibroBot00))
        self.LibroBot00Button.Show()
        self.LibroBot01Button = ui.Button()
        self.LibroBot01Button.SetParent(self.Board11)
        self.LibroBot01Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
        self.LibroBot01Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
        self.LibroBot01Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
        self.LibroBot01Button.SetToolTipText('Activar')
        self.LibroBot01Button.SetPosition(20, 110)
        self.LibroBot01Button.SetEvent(ui.__mem_func__(self.LibroBot01))
        self.LibroBot01Button.Show()
        self.LibroBot02Button = ui.Button()
        self.LibroBot02Button.SetParent(self.Board11)
        self.LibroBot02Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
        self.LibroBot02Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
        self.LibroBot02Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
        self.LibroBot02Button.SetToolTipText('Activar')
        self.LibroBot02Button.SetPosition(20, 150)
        self.LibroBot02Button.SetEvent(ui.__mem_func__(self.LibroBot02))
        self.LibroBot02Button.Show()
        self.LibroBot03Button = ui.Button()
        self.LibroBot03Button.SetParent(self.Board11)
        self.LibroBot03Button.SetUpVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
        self.LibroBot03Button.SetOverVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
        self.LibroBot03Button.SetDownVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
        self.LibroBot03Button.SetToolTipText('Activar')
        self.LibroBot03Button.SetPosition(20, 190)
        self.LibroBot03Button.SetEvent(ui.__mem_func__(self.LibroBot03))
        self.LibroBot03Button.Show()
        self.LibroBot04Button = ui.Button()
        self.LibroBot04Button.SetParent(self.Board11)
        self.LibroBot04Button.SetUpVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
        self.LibroBot04Button.SetOverVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
        self.LibroBot04Button.SetDownVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
        self.LibroBot04Button.SetToolTipText('Activar')
        self.LibroBot04Button.SetPosition(20, 230)
        self.LibroBot04Button.SetEvent(ui.__mem_func__(self.LibroBot04))
        self.LibroBot04Button.Show()
        self.LibroBot05Button = ui.Button()
        self.LibroBot05Button.SetParent(self.Board11)
        self.LibroBot05Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
        self.LibroBot05Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
        self.LibroBot05Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
        self.LibroBot05Button.SetToolTipText('Activar')
        self.LibroBot05Button.SetPosition(20, 270)
        self.LibroBot05Button.SetEvent(ui.__mem_func__(self.LibroBot05))
        self.LibroBot05Button.Show()
        self.LibroBot10Button = ui.Button()
        self.LibroBot10Button.SetParent(self.Board11)
        self.LibroBot10Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
        self.LibroBot10Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
        self.LibroBot10Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
        self.LibroBot10Button.SetToolTipText('Activar')
        self.LibroBot10Button.SetPosition(90, 70)
        self.LibroBot10Button.SetEvent(ui.__mem_func__(self.LibroBot10))
        self.LibroBot10Button.Show()
        self.LibroBot11Button = ui.Button()
        self.LibroBot11Button.SetParent(self.Board11)
        self.LibroBot11Button.SetUpVisual('pack\\Botones\\Habilidades\\LLuviadeflechas00.tga')
        self.LibroBot11Button.SetOverVisual('pack\\Botones\\Habilidades\\LLuviadeflechas00.tga')
        self.LibroBot11Button.SetDownVisual('pack\\Botones\\Habilidades\\LLuviadeflechas00.tga')
        self.LibroBot11Button.SetToolTipText('Activar')
        self.LibroBot11Button.SetPosition(90, 110)
        self.LibroBot11Button.SetEvent(ui.__mem_func__(self.LibroBot11))
        self.LibroBot11Button.Show()
        self.LibroBot12Button = ui.Button()
        self.LibroBot12Button.SetParent(self.Board11)
        self.LibroBot12Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
        self.LibroBot12Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
        self.LibroBot12Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
        self.LibroBot12Button.SetToolTipText('Activar')
        self.LibroBot12Button.SetPosition(90, 150)
        self.LibroBot12Button.SetEvent(ui.__mem_func__(self.LibroBot12))
        self.LibroBot12Button.Show()
        self.LibroBot13Button = ui.Button()
        self.LibroBot13Button.SetParent(self.Board11)
        self.LibroBot13Button.SetUpVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
        self.LibroBot13Button.SetOverVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
        self.LibroBot13Button.SetDownVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
        self.LibroBot13Button.SetToolTipText('Activar')
        self.LibroBot13Button.SetPosition(90, 190)
        self.LibroBot13Button.SetEvent(ui.__mem_func__(self.LibroBot13))
        self.LibroBot13Button.Show()
        self.LibroBot14Button = ui.Button()
        self.LibroBot14Button.SetParent(self.Board11)
        self.LibroBot14Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
        self.LibroBot14Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
        self.LibroBot14Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
        self.LibroBot14Button.SetToolTipText('Activar')
        self.LibroBot14Button.SetPosition(90, 230)
        self.LibroBot14Button.SetEvent(ui.__mem_func__(self.LibroBot14))
        self.LibroBot14Button.Show()
        self.LibroBot15Button = ui.Button()
        self.LibroBot15Button.SetParent(self.Board11)
        self.LibroBot15Button.SetUpVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
        self.LibroBot15Button.SetOverVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
        self.LibroBot15Button.SetDownVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
        self.LibroBot15Button.SetToolTipText('Activar')
        self.LibroBot15Button.SetPosition(90, 270)
        self.LibroBot15Button.SetEvent(ui.__mem_func__(self.LibroBot15))
        self.LibroBot15Button.Show()
        self.LibroBot20Button = ui.Button()
        self.LibroBot20Button.SetParent(self.Board11)
        self.LibroBot20Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
        self.LibroBot20Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
        self.LibroBot20Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
        self.LibroBot20Button.SetToolTipText('Activar')
        self.LibroBot20Button.SetPosition(160, 70)
        self.LibroBot20Button.SetEvent(ui.__mem_func__(self.LibroBot20))
        self.LibroBot20Button.Show()
        self.LibroBot21Button = ui.Button()
        self.LibroBot21Button.SetParent(self.Board11)
        self.LibroBot21Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
        self.LibroBot21Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
        self.LibroBot21Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
        self.LibroBot21Button.SetToolTipText('Activar')
        self.LibroBot21Button.SetPosition(160, 110)
        self.LibroBot21Button.SetEvent(ui.__mem_func__(self.LibroBot21))
        self.LibroBot21Button.Show()
        self.LibroBot22Button = ui.Button()
        self.LibroBot22Button.SetParent(self.Board11)
        self.LibroBot22Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
        self.LibroBot22Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
        self.LibroBot22Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
        self.LibroBot22Button.SetToolTipText('Activar')
        self.LibroBot22Button.SetPosition(160, 150)
        self.LibroBot22Button.SetEvent(ui.__mem_func__(self.LibroBot22))
        self.LibroBot22Button.Show()
        self.LibroBot23Button = ui.Button()
        self.LibroBot23Button.SetParent(self.Board11)
        self.LibroBot23Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
        self.LibroBot23Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
        self.LibroBot23Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
        self.LibroBot23Button.SetToolTipText('Activar')
        self.LibroBot23Button.SetPosition(160, 190)
        self.LibroBot23Button.SetEvent(ui.__mem_func__(self.LibroBot23))
        self.LibroBot23Button.Show()
        self.LibroBot24Button = ui.Button()
        self.LibroBot24Button.SetParent(self.Board11)
        self.LibroBot24Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
        self.LibroBot24Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
        self.LibroBot24Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
        self.LibroBot24Button.SetToolTipText('Activar')
        self.LibroBot24Button.SetPosition(160, 230)
        self.LibroBot24Button.SetEvent(ui.__mem_func__(self.LibroBot24))
        self.LibroBot24Button.Show()
        self.LibroBot25Button = ui.Button()
        self.LibroBot25Button.SetParent(self.Board11)
        self.LibroBot25Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
        self.LibroBot25Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
        self.LibroBot25Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
        self.LibroBot25Button.SetToolTipText('Activar')
        self.LibroBot25Button.SetPosition(160, 270)
        self.LibroBot25Button.SetEvent(ui.__mem_func__(self.LibroBot25))
        self.LibroBot25Button.Show()
        self.LibroBot30Button = ui.Button()
        self.LibroBot30Button.SetParent(self.Board11)
        self.LibroBot30Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
        self.LibroBot30Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
        self.LibroBot30Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
        self.LibroBot30Button.SetToolTipText('Activar')
        self.LibroBot30Button.SetPosition(230, 70)
        self.LibroBot30Button.SetEvent(ui.__mem_func__(self.LibroBot30))
        self.LibroBot30Button.Show()
        self.LibroBot31Button = ui.Button()
        self.LibroBot31Button.SetParent(self.Board11)
        self.LibroBot31Button.SetUpVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
        self.LibroBot31Button.SetOverVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
        self.LibroBot31Button.SetDownVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
        self.LibroBot31Button.SetToolTipText('Activar')
        self.LibroBot31Button.SetPosition(230, 110)
        self.LibroBot31Button.SetEvent(ui.__mem_func__(self.LibroBot31))
        self.LibroBot31Button.Show()
        self.LibroBot32Button = ui.Button()
        self.LibroBot32Button.SetParent(self.Board11)
        self.LibroBot32Button.SetUpVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
        self.LibroBot32Button.SetOverVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
        self.LibroBot32Button.SetDownVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
        self.LibroBot32Button.SetToolTipText('Activar')
        self.LibroBot32Button.SetPosition(230, 150)
        self.LibroBot32Button.SetEvent(ui.__mem_func__(self.LibroBot32))
        self.LibroBot32Button.Show()
        self.LibroBot33Button = ui.Button()
        self.LibroBot33Button.SetParent(self.Board11)
        self.LibroBot33Button.SetUpVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
        self.LibroBot33Button.SetOverVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
        self.LibroBot33Button.SetDownVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
        self.LibroBot33Button.SetToolTipText('Activar')
        self.LibroBot33Button.SetPosition(230, 190)
        self.LibroBot33Button.SetEvent(ui.__mem_func__(self.LibroBot33))
        self.LibroBot33Button.Show()
        self.LibroBot34Button = ui.Button()
        self.LibroBot34Button.SetParent(self.Board11)
        self.LibroBot34Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
        self.LibroBot34Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
        self.LibroBot34Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
        self.LibroBot34Button.SetToolTipText('Activar')
        self.LibroBot34Button.SetPosition(230, 230)
        self.LibroBot34Button.SetEvent(ui.__mem_func__(self.LibroBot34))
        self.LibroBot34Button.Show()
        self.LibroBot35Button = ui.Button()
        self.LibroBot35Button.SetParent(self.Board11)
        self.LibroBot35Button.SetUpVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
        self.LibroBot35Button.SetOverVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
        self.LibroBot35Button.SetDownVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
        self.LibroBot35Button.SetToolTipText('Activar')
        self.LibroBot35Button.SetPosition(230, 270)
        self.LibroBot35Button.SetEvent(ui.__mem_func__(self.LibroBot35))
        self.LibroBot35Button.Show()
        self.LibroBot40Button = ui.Button()
        self.LibroBot40Button.SetParent(self.Board11)
        self.LibroBot40Button.SetUpVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
        self.LibroBot40Button.SetOverVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
        self.LibroBot40Button.SetDownVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
        self.LibroBot40Button.SetToolTipText('Activar')
        self.LibroBot40Button.SetPosition(300, 70)
        self.LibroBot40Button.SetEvent(ui.__mem_func__(self.LibroBot40))
        self.LibroBot40Button.Show()
        self.LibroBot41Button = ui.Button()
        self.LibroBot41Button.SetParent(self.Board11)
        self.LibroBot41Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
        self.LibroBot41Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
        self.LibroBot41Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
        self.LibroBot41Button.SetToolTipText('Activar')
        self.LibroBot41Button.SetPosition(300, 110)
        self.LibroBot41Button.SetEvent(ui.__mem_func__(self.LibroBot41))
        self.LibroBot41Button.Show()
        self.LibroBot42Button = ui.Button()
        self.LibroBot42Button.SetParent(self.Board11)
        self.LibroBot42Button.SetUpVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
        self.LibroBot42Button.SetOverVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
        self.LibroBot42Button.SetDownVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
        self.LibroBot42Button.SetToolTipText('Activar')
        self.LibroBot42Button.SetPosition(300, 150)
        self.LibroBot42Button.SetEvent(ui.__mem_func__(self.LibroBot42))
        self.LibroBot42Button.Show()
        self.LibroBot43Button = ui.Button()
        self.LibroBot43Button.SetParent(self.Board11)
        self.LibroBot43Button.SetUpVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
        self.LibroBot43Button.SetOverVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
        self.LibroBot43Button.SetDownVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
        self.LibroBot43Button.SetToolTipText('Activar')
        self.LibroBot43Button.SetPosition(300, 190)
        self.LibroBot43Button.SetEvent(ui.__mem_func__(self.LibroBot43))
        self.LibroBot43Button.Show()
        self.LibroBot44Button = ui.Button()
        self.LibroBot44Button.SetParent(self.Board11)
        self.LibroBot44Button.SetUpVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
        self.LibroBot44Button.SetOverVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
        self.LibroBot44Button.SetDownVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
        self.LibroBot44Button.SetToolTipText('Activar')
        self.LibroBot44Button.SetPosition(300, 230)
        self.LibroBot44Button.SetEvent(ui.__mem_func__(self.LibroBot44))
        self.LibroBot44Button.Show()
        self.LibroBot45Button = ui.Button()
        self.LibroBot45Button.SetParent(self.Board11)
        self.LibroBot45Button.SetUpVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
        self.LibroBot45Button.SetOverVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
        self.LibroBot45Button.SetDownVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
        self.LibroBot45Button.SetToolTipText('Activar')
        self.LibroBot45Button.SetPosition(300, 270)
        self.LibroBot45Button.SetEvent(ui.__mem_func__(self.LibroBot45))
        self.LibroBot45Button.Show()
        self.LibroBot50Button = ui.Button()
        self.LibroBot50Button.SetParent(self.Board11)
        self.LibroBot50Button.SetUpVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
        self.LibroBot50Button.SetOverVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
        self.LibroBot50Button.SetDownVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
        self.LibroBot50Button.SetToolTipText('Activar')
        self.LibroBot50Button.SetPosition(370, 70)
        self.LibroBot50Button.SetEvent(ui.__mem_func__(self.LibroBot50))
        self.LibroBot50Button.Show()
        self.LibroBot51Button = ui.Button()
        self.LibroBot51Button.SetParent(self.Board11)
        self.LibroBot51Button.SetUpVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
        self.LibroBot51Button.SetOverVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
        self.LibroBot51Button.SetDownVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
        self.LibroBot51Button.SetToolTipText('Activar')
        self.LibroBot51Button.SetPosition(370, 110)
        self.LibroBot51Button.SetEvent(ui.__mem_func__(self.LibroBot51))
        self.LibroBot51Button.Show()
        self.LibroBot52Button = ui.Button()
        self.LibroBot52Button.SetParent(self.Board11)
        self.LibroBot52Button.SetUpVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
        self.LibroBot52Button.SetOverVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
        self.LibroBot52Button.SetDownVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
        self.LibroBot52Button.SetToolTipText('Activar')
        self.LibroBot52Button.SetPosition(370, 150)
        self.LibroBot52Button.SetEvent(ui.__mem_func__(self.LibroBot52))
        self.LibroBot52Button.Show()
        self.LibroBot53Button = ui.Button()
        self.LibroBot53Button.SetParent(self.Board11)
        self.LibroBot53Button.SetUpVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
        self.LibroBot53Button.SetOverVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
        self.LibroBot53Button.SetDownVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
        self.LibroBot53Button.SetToolTipText('Activar')
        self.LibroBot53Button.SetPosition(370, 190)
        self.LibroBot53Button.SetEvent(ui.__mem_func__(self.LibroBot53))
        self.LibroBot53Button.Show()
        self.LibroBot54Button = ui.Button()
        self.LibroBot54Button.SetParent(self.Board11)
        self.LibroBot54Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
        self.LibroBot54Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
        self.LibroBot54Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
        self.LibroBot54Button.SetToolTipText('Activar')
        self.LibroBot54Button.SetPosition(370, 230)
        self.LibroBot54Button.SetEvent(ui.__mem_func__(self.LibroBot54))
        self.LibroBot54Button.Show()
        self.LibroBot55Button = ui.Button()
        self.LibroBot55Button.SetParent(self.Board11)
        self.LibroBot55Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
        self.LibroBot55Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
        self.LibroBot55Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
        self.LibroBot55Button.SetToolTipText('Activar')
        self.LibroBot55Button.SetPosition(370, 270)
        self.LibroBot55Button.SetEvent(ui.__mem_func__(self.LibroBot55))
        self.LibroBot55Button.Show()
        self.LibroBot60Button = ui.Button()
        self.LibroBot60Button.SetParent(self.Board11)
        self.LibroBot60Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
        self.LibroBot60Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
        self.LibroBot60Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
        self.LibroBot60Button.SetToolTipText('Activar')
        self.LibroBot60Button.SetPosition(440, 70)
        self.LibroBot60Button.SetEvent(ui.__mem_func__(self.LibroBot60))
        self.LibroBot60Button.Show()
        self.LibroBot61Button = ui.Button()
        self.LibroBot61Button.SetParent(self.Board11)
        self.LibroBot61Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
        self.LibroBot61Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
        self.LibroBot61Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
        self.LibroBot61Button.SetToolTipText('Activar')
        self.LibroBot61Button.SetPosition(440, 110)
        self.LibroBot61Button.SetEvent(ui.__mem_func__(self.LibroBot61))
        self.LibroBot61Button.Show()
        self.LibroBot62Button = ui.Button()
        self.LibroBot62Button.SetParent(self.Board11)
        self.LibroBot62Button.SetUpVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
        self.LibroBot62Button.SetOverVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
        self.LibroBot62Button.SetDownVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
        self.LibroBot62Button.SetToolTipText('Activar')
        self.LibroBot62Button.SetPosition(440, 150)
        self.LibroBot62Button.SetEvent(ui.__mem_func__(self.LibroBot62))
        self.LibroBot62Button.Show()
        self.LibroBot63Button = ui.Button()
        self.LibroBot63Button.SetParent(self.Board11)
        self.LibroBot63Button.SetUpVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
        self.LibroBot63Button.SetOverVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
        self.LibroBot63Button.SetDownVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
        self.LibroBot63Button.SetToolTipText('Activar')
        self.LibroBot63Button.SetPosition(440, 190)
        self.LibroBot63Button.SetEvent(ui.__mem_func__(self.LibroBot63))
        self.LibroBot63Button.Show()
        self.LibroBot64Button = ui.Button()
        self.LibroBot64Button.SetParent(self.Board11)
        self.LibroBot64Button.SetUpVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
        self.LibroBot64Button.SetOverVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
        self.LibroBot64Button.SetDownVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
        self.LibroBot64Button.SetToolTipText('Activar')
        self.LibroBot64Button.SetPosition(440, 230)
        self.LibroBot64Button.SetEvent(ui.__mem_func__(self.LibroBot64))
        self.LibroBot64Button.Show()
        self.LibroBot65Button = ui.Button()
        self.LibroBot65Button.SetParent(self.Board11)
        self.LibroBot65Button.SetUpVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
        self.LibroBot65Button.SetOverVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
        self.LibroBot65Button.SetDownVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
        self.LibroBot65Button.SetToolTipText('Activar')
        self.LibroBot65Button.SetPosition(440, 270)
        self.LibroBot65Button.SetEvent(ui.__mem_func__(self.LibroBot65))
        self.LibroBot65Button.Show()
        self.LibroBot70Button = ui.Button()
        self.LibroBot70Button.SetParent(self.Board11)
        self.LibroBot70Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
        self.LibroBot70Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
        self.LibroBot70Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
        self.LibroBot70Button.SetToolTipText('Activar')
        self.LibroBot70Button.SetPosition(510, 70)
        self.LibroBot70Button.SetEvent(ui.__mem_func__(self.LibroBot70))
        self.LibroBot70Button.Show()
        self.LibroBot71Button = ui.Button()
        self.LibroBot71Button.SetParent(self.Board11)
        self.LibroBot71Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
        self.LibroBot71Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
        self.LibroBot71Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
        self.LibroBot71Button.SetToolTipText('Activar')
        self.LibroBot71Button.SetPosition(510, 110)
        self.LibroBot71Button.SetEvent(ui.__mem_func__(self.LibroBot71))
        self.LibroBot71Button.Show()
        self.LibroBot72Button = ui.Button()
        self.LibroBot72Button.SetParent(self.Board11)
        self.LibroBot72Button.SetUpVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
        self.LibroBot72Button.SetOverVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
        self.LibroBot72Button.SetDownVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
        self.LibroBot72Button.SetToolTipText('Activar')
        self.LibroBot72Button.SetPosition(510, 150)
        self.LibroBot72Button.SetEvent(ui.__mem_func__(self.LibroBot72))
        self.LibroBot72Button.Show()
        self.LibroBot73Button = ui.Button()
        self.LibroBot73Button.SetParent(self.Board11)
        self.LibroBot73Button.SetUpVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
        self.LibroBot73Button.SetOverVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
        self.LibroBot73Button.SetDownVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
        self.LibroBot73Button.SetToolTipText('Activar')
        self.LibroBot73Button.SetPosition(510, 190)
        self.LibroBot73Button.SetEvent(ui.__mem_func__(self.LibroBot73))
        self.LibroBot73Button.Show()
        self.LibroBot74Button = ui.Button()
        self.LibroBot74Button.SetParent(self.Board11)
        self.LibroBot74Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
        self.LibroBot74Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
        self.LibroBot74Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
        self.LibroBot74Button.SetToolTipText('Activar')
        self.LibroBot74Button.SetPosition(510, 230)
        self.LibroBot74Button.SetEvent(ui.__mem_func__(self.LibroBot74))
        self.LibroBot74Button.Show()
        self.LibroBot75Button = ui.Button()
        self.LibroBot75Button.SetParent(self.Board11)
        self.LibroBot75Button.SetUpVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
        self.LibroBot75Button.SetOverVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
        self.LibroBot75Button.SetDownVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
        self.LibroBot75Button.SetToolTipText('Activar')
        self.LibroBot75Button.SetPosition(510, 270)
        self.LibroBot75Button.SetEvent(ui.__mem_func__(self.LibroBot75))
        self.LibroBot75Button.Show()
        self.BuffBotStartButton = ui.Button()
        self.BuffBotStartButton.SetParent(self.Board10)
        self.BuffBotStartButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\stop_0.tga')
        self.BuffBotStartButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\stop_1.tga')
        self.BuffBotStartButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\stop2.tga')
        self.BuffBotStartButton.SetToolTipText('Activar')
        self.BuffBotStartButton.SetPosition(120, 120)
        self.BuffBotStartButton.SetEvent(ui.__mem_func__(self.StartBuffbot))
        self.BuffBotStartButton.Show()
        self.DelaySlide = ui.SliderBar()
        self.DelaySlide.SetParent(self.Board10)
        self.DelaySlide.SetPosition(75, 70)
        self.DelaySlide.SetEvent(ui.__mem_func__(self.SlideDelay))
        self.DelaySlide.Show()
        self.GmvisualButton = ui.Button()
        self.GmvisualButton.SetParent(self.Board4)
        self.GmvisualButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.GmvisualButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.GmvisualButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.GmvisualButton.SetToolTipText('Activar')
        self.GmvisualButton.SetPosition(168, 415)
        self.GmvisualButton.SetEvent(ui.__mem_func__(self.Gmvisual))
        self.GmvisualButton.Show()
        self.CopiarButton = ui.Button()
        self.CopiarButton.SetParent(self.Board4)
        self.CopiarButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.CopiarButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.CopiarButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.CopiarButton.SetToolTipText('Activar')
        self.CopiarButton.SetPosition(88, 415)
        self.CopiarButton.SetEvent(ui.__mem_func__(self.Copiar))
        self.CopiarButton.Show()
        self.PJButton = ui.Button()
        self.PJButton.SetParent(self.Board4)
        self.PJButton.SetUpVisual('pack\\Botones\\Stealth_0.tga')
        self.PJButton.SetOverVisual('pack\\Botones\\Stealth_0.tga')
        self.PJButton.SetDownVisual('pack\\Botones\\Stealth_01.tga')
        self.PJButton.SetToolTipText('Activar')
        self.PJButton.SetPosition(84, 355)
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
            ChattypeButton.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            ChattypeButton.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            ChattypeButton.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            ChattypeButton.SetText(Chattype)
            ChattypeButton.Show()
            Type = self.CHAT_MODE_INDEX[i]
            ChattypeButton.SetEvent(lambda arg=Type: self.UseChatType(arg))
            ChattypeButton.SetEvent(lambda arg=Type: self.UseChatType(arg))
            self.ChatTypeList.append(ChattypeButton)
            x += 48
            i += 1

        x = 40
        i = 0
        for Colour in self.COLOUR1_MODE_NAME:
            Colour1Button = ui.Button()
            Colour1Button.SetParent(self.Board9)
            Colour1Button.SetPosition(x, 160)
            Colour1Button.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            Colour1Button.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            Colour1Button.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            Colour1Button.SetText(Colour)
            Colour1Button.Show()
            Type = self.COLOUR1_MODE_INDEX[i]
            Colour1Button.SetEvent(lambda arg=Type: self.UseChatColour(arg))
            Colour1Button.SetEvent(lambda arg=Type: self.UseChatColour(arg))
            self.Colour1List.append(Colour1Button)
            x += 48
            i += 1

        x = 40
        i = 0
        for Colour in self.COLOUR1_MODE_NAME2:
            Colour12Button = ui.Button()
            Colour12Button.SetParent(self.Board9)
            Colour12Button.SetPosition(x, 185)
            Colour12Button.SetUpVisual('d:/ymir work/ui/public/small_button_01.sub')
            Colour12Button.SetOverVisual('d:/ymir work/ui/public/small_button_02.sub')
            Colour12Button.SetDownVisual('d:/ymir work/ui/public/small_button_03.sub')
            Colour12Button.SetText(Colour)
            Colour12Button.Show()
            Type = self.COLOUR1_MODE_INDEX2[i]
            Colour12Button.SetEvent(lambda arg=Type: self.UseChatColour(arg))
            Colour12Button.SetEvent(lambda arg=Type: self.UseChatColour(arg))
            self.ColourList.append(Colour12Button)
            x += 48
            i += 1

        self.StartChatSpamButton = ui.Button()
        self.StartChatSpamButton.SetParent(self.Board9)
        self.StartChatSpamButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\start_0.tga')
        self.StartChatSpamButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\start_1.tga')
        self.StartChatSpamButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\start_2.tga')
        self.StartChatSpamButton.SetToolTipText('Activar')
        self.StartChatSpamButton.SetPosition(60, 405)
        self.StartChatSpamButton.SetEvent(ui.__mem_func__(self.Start1SpamBot))
        self.StartChatSpamButton.Show()
        self.StopChatSpamButton = ui.Button()
        self.StopChatSpamButton.SetParent(self.Board9)
        self.StopChatSpamButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\stop_0.tga')
        self.StopChatSpamButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\stop_1.tga')
        self.StopChatSpamButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\stop2.tga')
        self.StopChatSpamButton.SetToolTipText('Desactivar')
        self.StopChatSpamButton.SetPosition(200, 405)
        self.StopChatSpamButton.SetEvent(ui.__mem_func__(self.Stop1SpamBot))
        self.StopChatSpamButton.Show()
        self.DetectorGMSButton = ui.Button()
        self.DetectorGMSButton.SetParent(self.Board12)
        self.DetectorGMSButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.DetectorGMSButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.DetectorGMSButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.DetectorGMSButton.SetToolTipText("Detector de GM's")
        self.DetectorGMSButton.SetText('Activar')
        self.DetectorGMSButton.SetPosition(100, 35)
        self.DetectorGMSButton.SetEvent(ui.__mem_func__(self.GMDetector))
        self.DetectorGMSButton.Show()
        self.PaginawebButton = ui.Button()
        self.PaginawebButton.SetParent(self.Board7)
        self.PaginawebButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.PaginawebButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.PaginawebButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.PaginawebButton.SetToolTipText('francoiz.net/')
        self.PaginawebButton.SetText('Pagina web')
        self.PaginawebButton.SetPosition(148, 145)
        self.PaginawebButton.SetEvent(ui.__mem_func__(self.Paginaweb))
        self.PaginawebButton.Show()
        self.CreditosfrancoizButton = ui.Button()
        self.CreditosfrancoizButton.SetParent(self.Board7)
        self.CreditosfrancoizButton.SetUpVisual('pack\\Botones\\yt_1.tga')
        self.CreditosfrancoizButton.SetOverVisual('pack\\Botones\\yt_0.tga')
        self.CreditosfrancoizButton.SetDownVisual('pack\\Botones\\yt_1.tga')
        self.CreditosfrancoizButton.SetToolTipText('Canal Francoiz')
        self.CreditosfrancoizButton.SetPosition(96, 140)
        self.CreditosfrancoizButton.SetEvent(ui.__mem_func__(self.Creditosfrancoiz))
        self.CreditosfrancoizButton.Show()
        self.SpamfrancoizButton = ui.Button()
        self.SpamfrancoizButton.SetParent(self.Board7)
        self.SpamfrancoizButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\start_0.tga')
        self.SpamfrancoizButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\start_1.tga')
        self.SpamfrancoizButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\start_2.tga')
        self.SpamfrancoizButton.SetToolTipText('Spamm Francoiz')
        self.SpamfrancoizButton.SetPosition(35, 140)
        self.SpamfrancoizButton.SetEvent(ui.__mem_func__(self.Spamfrancoiz))
        self.SpamfrancoizButton.Show()
        self.TeleportButton = ui.Button()
        self.TeleportButton.SetParent(self.Board5)
        self.TeleportButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.TeleportButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.TeleportButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.TeleportButton.SetText('Teleporter')
        self.TeleportButton.SetPosition(10, 100)
        self.TeleportButton.SetEvent(ui.__mem_func__(self.TeleportToCoordinates))
        self.TeleportButton.Show()
        self.ChangeButton = ui.Button()
        self.ChangeButton.SetParent(self.Board4)
        self.ChangeButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.ChangeButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.ChangeButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.ChangeButton.SetText('Generar')
        self.ChangeButton.SetPosition(80, 310)
        self.ChangeButton.SetEvent(ui.__mem_func__(self.EqChange))
        self.ChangeButton.SetToolTipText('')
        self.ChangeButton.Show()
        self.HerreroButton = ui.Button()
        self.HerreroButton.SetParent(self.Board4)
        self.HerreroButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.HerreroButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.HerreroButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.HerreroButton.SetText('Mejorar')
        self.HerreroButton.SetPosition(61, 117)
        self.HerreroButton.SetEvent(ui.__mem_func__(self.RefineOneTime))
        self.HerreroButton.SetToolTipText('')
        self.HerreroButton.Show()
        self.FantasmaButton = ui.Button()
        self.FantasmaButton.SetParent(self.Board4)
        self.FantasmaButton.SetUpVisual('pack\\Botones\\gmod_0.tga')
        self.FantasmaButton.SetOverVisual('pack\\Botones\\gmod_1.tga')
        self.FantasmaButton.SetDownVisual('pack\\Botones\\gmod_0.tga')
        self.FantasmaButton.SetToolTipText('Activar')
        self.FantasmaButton.SetPosition(100, 60)
        self.FantasmaButton.SetEvent(ui.__mem_func__(self.GhostMod))
        self.FantasmaButton.Show()
        self.ComboTypeButton = ui.Button()
        self.ComboTypeButton.SetParent(self.Board4)
        self.ComboTypeButton.SetPosition(60, 160)
        self.ComboTypeButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ComboTypeButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ComboTypeButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ComboTypeButton.SetEvent(ui.__mem_func__(self.Combo))
        self.ComboTypeButton.SetToolTipText('Activar')
        self.ComboTypeButton.Show()
        self.CabosButton = ui.Button()
        self.CabosButton.SetParent(self.Board1)
        self.CabosButton.SetUpVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
        self.CabosButton.SetOverVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
        self.CabosButton.SetDownVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
        self.CabosButton.SetToolTipText('Activar')
        self.CabosButton.SetPosition(150, 250)
        self.CabosButton.SetEvent(ui.__mem_func__(self.SetTapferkeitsUmhange))
        self.CabosButton.Show()
        self.poderesButton = ui.Button()
        self.poderesButton.SetParent(self.Board1)
        self.poderesButton.SetPosition(157, 287)
        self.poderesButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.poderesButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.poderesButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.poderesButton.SetEvent(ui.__mem_func__(self.Habilidad))
        self.poderesButton.SetToolTipText('Activar')
        self.poderesButton.Show()
        self.CaballofuncionButton = ui.Button()
        self.CaballofuncionButton.SetParent(self.Board3)
        self.CaballofuncionButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.CaballofuncionButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.CaballofuncionButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.CaballofuncionButton.SetToolTipText('Activar')
        self.CaballofuncionButton.SetPosition(60, 158)
        self.CaballofuncionButton.SetEvent(ui.__mem_func__(self.Caballofuncion))
        self.CaballofuncionButton.Show()
        self.AttackSpeedStatusButton = ui.Button()
        self.AttackSpeedStatusButton.SetParent(self.Board3)
        self.AttackSpeedStatusButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.AttackSpeedStatusButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.AttackSpeedStatusButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.AttackSpeedStatusButton.SetToolTipText('Activar')
        self.AttackSpeedStatusButton.SetPosition(155, 77)
        self.AttackSpeedStatusButton.SetEvent(ui.__mem_func__(self.AttackSpeedStatus))
        self.AttackSpeedStatusButton.Show()
        self.MoveSpeedStatusButton = ui.Button()
        self.MoveSpeedStatusButton.SetParent(self.Board3)
        self.MoveSpeedStatusButton.SetUpVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
        self.MoveSpeedStatusButton.SetOverVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
        self.MoveSpeedStatusButton.SetDownVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
        self.MoveSpeedStatusButton.SetToolTipText('Activar')
        self.MoveSpeedStatusButton.SetPosition(184, 113)
        self.MoveSpeedStatusButton.SetEvent(ui.__mem_func__(self.MoveSpeedStatus))
        self.MoveSpeedStatusButton.Show()
        self.AutoRedPotButton = ui.Button()
        self.AutoRedPotButton.SetParent(self.Board1)
        self.AutoRedPotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
        self.AutoRedPotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
        self.AutoRedPotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
        self.AutoRedPotButton.SetToolTipText('Activar')
        self.AutoRedPotButton.SetPosition(138, 91)
        self.AutoRedPotButton.SetEvent(ui.__mem_func__(self.AutoRedPot))
        self.AutoRedPotButton.Show()
        self.AutoBluePotButton = ui.Button()
        self.AutoBluePotButton.SetParent(self.Board1)
        self.AutoBluePotButton.SetPosition(138, 124)
        self.AutoBluePotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
        self.AutoBluePotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
        self.AutoBluePotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
        self.AutoBluePotButton.SetToolTipText('Activar')
        self.AutoBluePotButton.SetEvent(ui.__mem_func__(self.AutoBluePot))
        self.AutoBluePotButton.Show()
        self.LevelbotModo1Button = ui.Button()
        self.LevelbotModo1Button.SetParent(self.Board1)
        self.LevelbotModo1Button.SetPosition(147, 160)
        self.LevelbotModo1Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.LevelbotModo1Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.LevelbotModo1Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.LevelbotModo1Button.SetToolTipText('Activar')
        self.LevelbotModo1Button.SetEvent(ui.__mem_func__(self.LevelbotModo1))
        self.LevelbotModo1Button.Show()
        self.LevelbotModo2Button = ui.Button()
        self.LevelbotModo2Button.SetParent(self.Board1)
        self.LevelbotModo2Button.SetPosition(197, 160)
        self.LevelbotModo2Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.LevelbotModo2Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.LevelbotModo2Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.LevelbotModo2Button.SetToolTipText('Activar')
        self.LevelbotModo2Button.SetEvent(ui.__mem_func__(self.LevelbotModo2))
        self.LevelbotModo2Button.Show()
        self.LevelbotModo0Button = ui.Button()
        self.LevelbotModo0Button.SetParent(self.Board1)
        self.LevelbotModo0Button.SetPosition(97, 160)
        self.LevelbotModo0Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.LevelbotModo0Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.LevelbotModo0Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.LevelbotModo0Button.SetToolTipText('Activar')
        self.LevelbotModo0Button.SetEvent(ui.__mem_func__(self.LevelbotModo0))
        self.LevelbotModo0Button.Show()
        self.AutoPickupButton = ui.Button()
        self.AutoPickupButton.SetParent(self.Board1)
        self.AutoPickupButton.SetPosition(77, 190)
        self.AutoPickupButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.AutoPickupButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.AutoPickupButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.AutoPickupButton.SetToolTipText('Activar')
        self.AutoPickupButton.SetEvent(ui.__mem_func__(self.AutoPickup))
        self.AutoPickupButton.Show()
        self.AutoRestartButton = ui.Button()
        self.AutoRestartButton.SetParent(self.Board1)
        self.AutoRestartButton.SetPosition(75, 219)
        self.AutoRestartButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.AutoRestartButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.AutoRestartButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.AutoRestartButton.SetToolTipText('Activar')
        self.AutoRestartButton.SetEvent(ui.__mem_func__(self.AutoRestart))
        self.AutoRestartButton.Show()
        self.CambiararmaButton = ui.Button()
        self.CambiararmaButton.SetParent(self.Board1)
        self.CambiararmaButton.SetPosition(131, 317)
        self.CambiararmaButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.CambiararmaButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.CambiararmaButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.CambiararmaButton.SetToolTipText('Activar')
        self.CambiararmaButton.SetEvent(ui.__mem_func__(self.Cambiar))
        self.CambiararmaButton.Show()
        self.ModoEspada1Button = ui.Button()
        self.ModoEspada1Button.SetParent(self.Board1)
        self.ModoEspada1Button.SetPosition(117, 377)
        self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoEspada1Button.SetToolTipText('Activar')
        self.ModoEspada1Button.SetEvent(ui.__mem_func__(self.Modoespada1))
        self.ModoEspada1Button.Hide()
        self.ModoEspada2Button = ui.Button()
        self.ModoEspada2Button.SetParent(self.Board1)
        self.ModoEspada2Button.SetPosition(113, 407)
        self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoEspada2Button.SetToolTipText('Activar')
        self.ModoEspada2Button.SetEvent(ui.__mem_func__(self.Modoespada2))
        self.ModoEspada2Button.Hide()
        self.ModoDaga1Button = ui.Button()
        self.ModoDaga1Button.SetParent(self.Board1)
        self.ModoDaga1Button.SetPosition(47, 467)
        self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoDaga1Button.SetToolTipText('Activar')
        self.ModoDaga1Button.SetEvent(ui.__mem_func__(self.ModoDaga1))
        self.ModoDaga1Button.Hide()
        self.ModoDaga2Button = ui.Button()
        self.ModoDaga2Button.SetParent(self.Board1)
        self.ModoDaga2Button.SetPosition(48, 497)
        self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoDaga2Button.SetToolTipText('Activar')
        self.ModoDaga2Button.SetEvent(ui.__mem_func__(self.ModoDaga2))
        self.ModoDaga2Button.Hide()
        self.ModoChaman1Button = ui.Button()
        self.ModoChaman1Button.SetParent(self.Board1)
        self.ModoChaman1Button.SetPosition(40, 557)
        self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoChaman1Button.SetToolTipText('Activar')
        self.ModoChaman1Button.SetEvent(ui.__mem_func__(self.ModoChaman1))
        self.ModoChaman1Button.Hide()
        self.ModoChaman2Button = ui.Button()
        self.ModoChaman2Button.SetParent(self.Board1)
        self.ModoChaman2Button.SetPosition(62, 587)
        self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoChaman2Button.SetToolTipText('Activar')
        self.ModoChaman2Button.SetEvent(ui.__mem_func__(self.ModoChaman2))
        self.ModoChaman2Button.Hide()
        self.ModoGeneralButton = ui.Button()
        self.ModoGeneralButton.SetParent(self.Board1)
        self.ModoGeneralButton.SetPosition(103, 647)
        self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ModoGeneralButton.SetToolTipText('Activar')
        self.ModoGeneralButton.SetEvent(ui.__mem_func__(self.ModoGeneral))
        self.ModoGeneralButton.Hide()
        self.ZoomHackButton = ui.Button()
        self.ZoomHackButton.SetParent(self.Board2)
        self.ZoomHackButton.SetPosition(77, 69)
        self.ZoomHackButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.ZoomHackButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.ZoomHackButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.ZoomHackButton.SetToolTipText('Activar')
        self.ZoomHackButton.SetEvent(ui.__mem_func__(self.ZoomHack))
        self.ZoomHackButton.Show()
        self.NoFogButton = ui.Button()
        self.NoFogButton.SetParent(self.Board2)
        self.NoFogButton.SetPosition(75, 99)
        self.NoFogButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.NoFogButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.NoFogButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.NoFogButton.SetToolTipText('Activar')
        self.NoFogButton.SetEvent(ui.__mem_func__(self.NoFog))
        self.NoFogButton.Show()
        self.DayNightButton = ui.Button()
        self.DayNightButton.SetParent(self.Board2)
        self.DayNightButton.SetPosition(75, 129)
        self.DayNightButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.DayNightButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.DayNightButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.DayNightButton.SetToolTipText('Activar')
        self.DayNightButton.SetEvent(ui.__mem_func__(self.DayNight))
        self.DayNightButton.Show()
        self.PararcamButton = ui.Button()
        self.PararcamButton.SetParent(self.Board2)
        self.PararcamButton.SetPosition(85, 189)
        self.PararcamButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.PararcamButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.PararcamButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.PararcamButton.SetToolTipText('Activar')
        self.PararcamButton.SetEvent(ui.__mem_func__(self.Pararcam))
        self.PararcamButton.Show()
        self.SnowButton = ui.Button()
        self.SnowButton.SetParent(self.Board2)
        self.SnowButton.SetPosition(53, 159)
        self.SnowButton.SetUpVisual('pack\\Botones\\off_0.tga')
        self.SnowButton.SetOverVisual('pack\\Botones\\off_1.tga')
        self.SnowButton.SetDownVisual('pack\\Botones\\off_2.tga')
        self.SnowButton.SetToolTipText('Activar')
        self.SnowButton.SetEvent(ui.__mem_func__(self.EnableSnow))
        self.SnowButton.Show()

    def FaceButton(self):
        global TeleporterButton
        global HabilidadesButton
        global TeleporterText
        global Teleporter3Text
        global SalirText
        global SalirButton
        global MasButton
        global MasText
        global HabilidadesText
        global Leveo1Button
        global Teleporter3Button
        global Leveo1Text
        Leveo1Button = ui.Button()
        Leveo1Button.SetText('')
        Leveo1Button.SetPosition(wndMgr.GetScreenWidth() - 100, 220)
        Leveo1Button.SetSize(88, 21)
        Leveo1Button.SetEvent(self.Board1.Show)
        Leveo1Button.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        Leveo1Button.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        Leveo1Button.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        Leveo1Button.Show()
        Leveo1Text = ui.TextLine()
        Leveo1Text.SetParent(Leveo1Button)
        Leveo1Text.SetVerticalAlignCenter()
        Leveo1Text.SetHorizontalAlignCenter()
        Leveo1Text.SetPosition(43, 10)
        Leveo1Text.SetText('Leveo Bot')
        Leveo1Text.Show()
        HabilidadesButton = ui.Button()
        HabilidadesButton.SetText('')
        HabilidadesButton.SetPosition(wndMgr.GetScreenWidth() - 100, 250)
        HabilidadesButton.SetSize(88, 21)
        HabilidadesButton.SetEvent(self.Board16.Show)
        HabilidadesButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        HabilidadesButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        HabilidadesButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        HabilidadesButton.Show()
        HabilidadesText = ui.TextLine()
        HabilidadesText.SetParent(HabilidadesButton)
        HabilidadesText.SetVerticalAlignCenter()
        HabilidadesText.SetHorizontalAlignCenter()
        HabilidadesText.SetPosition(43, 10)
        HabilidadesText.SetText('Habilidades')
        HabilidadesText.Show()
        TeleporterButton = ui.Button()
        TeleporterButton.SetText('')
        TeleporterButton.SetPosition(wndMgr.GetScreenWidth() - 100, 280)
        TeleporterButton.SetSize(88, 21)
        TeleporterButton.SetEvent(self.Board5.Show)
        TeleporterButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        TeleporterButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        TeleporterButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        TeleporterButton.Show()
        TeleporterText = ui.TextLine()
        TeleporterText.SetParent(TeleporterButton)
        TeleporterText.SetVerticalAlignCenter()
        TeleporterText.SetHorizontalAlignCenter()
        TeleporterText.SetPosition(43, 10)
        TeleporterText.SetText('Teleporter 1')
        TeleporterText.Show()
        Teleporter3Button = ui.Button()
        Teleporter3Button.SetText('')
        Teleporter3Button.SetPosition(wndMgr.GetScreenWidth() - 100, 340)
        Teleporter3Button.SetSize(88, 21)
        Teleporter3Button.SetEvent(self.Board8.Show)
        Teleporter3Button.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        Teleporter3Button.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        Teleporter3Button.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        Teleporter3Button.Show()
        Teleporter3Text = ui.TextLine()
        Teleporter3Text.SetParent(Teleporter3Button)
        Teleporter3Text.SetVerticalAlignCenter()
        Teleporter3Text.SetHorizontalAlignCenter()
        Teleporter3Text.SetPosition(43, 10)
        Teleporter3Text.SetText('Teleporter 3')
        Teleporter3Text.Show()
        SalirButton = ui.Button()
        SalirButton.SetText('')
        SalirButton.SetPosition(wndMgr.GetScreenWidth() - 100, 490)
        SalirButton.SetSize(88, 21)
        SalirButton.SetEvent(ui.__mem_func__(self.Salir))
        SalirButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        SalirButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        SalirButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        SalirButton.Show()
        SalirText = ui.TextLine()
        SalirText.SetParent(SalirButton)
        SalirText.SetVerticalAlignCenter()
        SalirText.SetHorizontalAlignCenter()
        SalirText.SetPosition(43, 10)
        SalirText.SetText('Salir')
        SalirText.Show()
        MasButton = ui.Button()
        MasButton.SetText('')
        MasButton.SetPosition(wndMgr.GetScreenWidth() - 100, 460)
        MasButton.SetSize(88, 21)
        MasButton.SetEvent(self.Board14.Show)
        MasButton.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        MasButton.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        MasButton.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        MasButton.Show()
        MasText = ui.TextLine()
        MasText.SetParent(MasButton)
        MasText.SetVerticalAlignCenter()
        MasText.SetHorizontalAlignCenter()
        MasText.SetPosition(43, 10)
        MasText.SetText('Mas hacks')
        MasText.Show()

    def SendGoldDown(self):
        net.SendGoldDropPacketNew(500)

    def OpenInv(self):
        ToggleInventoryWindow()

    def Habilidad1Funcion(self):
        global Habilidad1V
        if Habilidad1V == 0:
            Habilidad1V = 1
            self.Habilidad1boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad1boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad1boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad1boton.SetToolTipText('Desactivar')
            self.ActivarHab1()
        else:
            Habilidad1V = 0
            self.Habilidad1boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad1boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad1boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad1boton.SetToolTipText('Activar')
            self.DesactivarHab1()

    def ActivarHab1(self):
        global LevelbotModo2
        global LevelbotModo1
        global LevelbotModo0
        TiempoHabilidad1 = self.Habilidad1.GetText()
        self.SegundosHab1 = WaitingDialog()
        self.SegundosHab1.Open(int(TiempoHabilidad1))
        self.SegundosHab1.SAFE_SetTimeOverEvent(self.ActivarHab1)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(1)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(1)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(1)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab1(self):
        TiempoHabilidad1 = self.Habilidad1.GetText()
        self.SegundosHab1 = WaitingDialog()
        self.SegundosHab1.Open(int(999999999999999999999))
        self.SegundosHab1.SAFE_SetTimeOverEvent(self.DesactivarHab1)

    def Habilidad2Funcion(self):
        global Habilidad2V
        if Habilidad2V == 0:
            Habilidad2V = 1
            self.Habilidad2boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad2boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad2boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad2boton.SetToolTipText('Desactivar')
            self.ActivarHab2()
        else:
            Habilidad2V = 0
            self.Habilidad2boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad2boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad2boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad2boton.SetToolTipText('Activar')
            self.DesactivarHab2()

    def ActivarHab2(self):
        TiempoHabilidad2 = self.Habilidad2.GetText()
        self.SegundosHab2 = WaitingDialog()
        self.SegundosHab2.Open(int(TiempoHabilidad2))
        self.SegundosHab2.SAFE_SetTimeOverEvent(self.ActivarHab2)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(2)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(2)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(2)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab2(self):
        TiempoHabilidad2 = self.Habilidad2.GetText()
        self.SegundosHab2 = WaitingDialog()
        self.SegundosHab2.Open(int(999999999999999999999))
        self.SegundosHab2.SAFE_SetTimeOverEvent(self.DesactivarHab2)

    def Habilidad3Funcion(self):
        global Habilidad3V
        if Habilidad3V == 0:
            Habilidad3V = 1
            self.Habilidad3boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad3boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad3boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad3boton.SetToolTipText('Desactivar')
            self.ActivarHab3()
        else:
            Habilidad3V = 0
            self.Habilidad3boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad3boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad3boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad3boton.SetToolTipText('Activar')
            self.DesactivarHab3()

    def ActivarHab3(self):
        TiempoHabilidad3 = self.Habilidad3.GetText()
        self.SegundosHab3 = WaitingDialog()
        self.SegundosHab3.Open(int(TiempoHabilidad3))
        self.SegundosHab3.SAFE_SetTimeOverEvent(self.ActivarHab3)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(3)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(3)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(3)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab3(self):
        TiempoHabilidad3 = self.Habilidad3.GetText()
        self.SegundosHab3 = WaitingDialog()
        self.SegundosHab3.Open(int(999999999999999999999))
        self.SegundosHab3.SAFE_SetTimeOverEvent(self.DesactivarHab3)

    def Habilidad4Funcion(self):
        global Habilidad4V
        if Habilidad4V == 0:
            Habilidad4V = 1
            self.Habilidad4boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad4boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad4boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad4boton.SetToolTipText('Desactivar')
            self.ActivarHab4()
        else:
            Habilidad4V = 0
            self.Habilidad4boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad4boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad4boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad4boton.SetToolTipText('Activar')
            self.DesactivarHab4()

    def ActivarHab4(self):
        TiempoHabilidad4 = self.Habilidad4.GetText()
        self.SegundosHab4 = WaitingDialog()
        self.SegundosHab4.Open(int(TiempoHabilidad4))
        self.SegundosHab4.SAFE_SetTimeOverEvent(self.ActivarHab4)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(4)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(4)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(4)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab4(self):
        TiempoHabilidad4 = self.Habilidad4.GetText()
        self.SegundosHab4 = WaitingDialog()
        self.SegundosHab4.Open(int(999999999999999999999))
        self.SegundosHab4.SAFE_SetTimeOverEvent(self.DesactivarHab4)

    def Habilidad5Funcion(self):
        global Habilidad5V
        if Habilidad5V == 0:
            Habilidad5V = 1
            self.Habilidad5boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad5boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad5boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad5boton.SetToolTipText('Desactivar')
            self.ActivarHab5()
        else:
            Habilidad5V = 0
            self.Habilidad5boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad5boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad5boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad5boton.SetToolTipText('Activar')
            self.DesactivarHab5()

    def ActivarHab5(self):
        TiempoHabilidad5 = self.Habilidad5.GetText()
        self.SegundosHab5 = WaitingDialog()
        self.SegundosHab5.Open(int(TiempoHabilidad5))
        self.SegundosHab5.SAFE_SetTimeOverEvent(self.ActivarHab5)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(5)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(5)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(5)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab5(self):
        TiempoHabilidad5 = self.Habilidad5.GetText()
        self.SegundosHab5 = WaitingDialog()
        self.SegundosHab5.Open(int(999999999999999999999))
        self.SegundosHab5.SAFE_SetTimeOverEvent(self.DesactivarHab5)

    def Habilidad6Funcion(self):
        global Habilidad6V
        if Habilidad6V == 0:
            Habilidad6V = 1
            self.Habilidad6boton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.Habilidad6boton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.Habilidad6boton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.Habilidad6boton.SetToolTipText('Desactivar')
            self.ActivarHab6()
        else:
            Habilidad6V = 0
            self.Habilidad6boton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.Habilidad6boton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.Habilidad6boton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.Habilidad6boton.SetToolTipText('Activar')
            self.DesactivarHab6()

    def ActivarHab6(self):
        TiempoHabilidad6 = self.Habilidad6.GetText()
        self.SegundosHab6 = WaitingDialog()
        self.SegundosHab6.Open(int(TiempoHabilidad6))
        self.SegundosHab6.SAFE_SetTimeOverEvent(self.ActivarHab6)
        if LevelbotModo0 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(6)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo1 == 1:
            if LevelbotModo0 == 0:
                if LevelbotModo2 == 0:
                    player.ClickSkillSlot(6)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        if LevelbotModo2 == 1:
            if LevelbotModo1 == 0:
                if LevelbotModo0 == 0:
                    player.ClickSkillSlot(6)
                else:
                    chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
            else:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha producido un error.')
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Se ha activado la habilidad correctamente. Esta comenzara una vez que se active el bot de leveo.')

    def DesactivarHab6(self):
        TiempoHabilidad6 = self.Habilidad6.GetText()
        self.SegundosHab6 = WaitingDialog()
        self.SegundosHab6.Open(int(999999999999999999999))
        self.SegundosHab6.SAFE_SetTimeOverEvent(self.DesactivarHab6)

    def UseWhisperType(self, mode):
        global WHISPER_TYPE
        self.LastChange.SetText('Forma elegida: ' + str(mode))
        WHISPER_TYPE = mode

    def UseWhisperColour(self, colour):
        global WhisperColour
        WhisperColour = str(colour)
        if WhisperColour.find(str(self.COLOUR_MODE_INDEX[0])) != -1:
            WhisperType = str(self.COLOUR_MODE_NAME[0])
        else:
            if WhisperColour.find(str(self.COLOUR_MODE_INDEX[1])) != -1:
                WhisperType = str(self.COLOUR_MODE_NAME[1])
            else:
                if WhisperColour.find(str(self.COLOUR_MODE_INDEX[2])) != -1:
                    WhisperType = str(self.COLOUR_MODE_NAME[2])
                else:
                    if WhisperColour.find(str(self.COLOUR_MODE_INDEX[3])) != -1:
                        WhisperType = str(self.COLOUR_MODE_NAME[3])
                    else:
                        if WhisperColour.find(str(self.COLOUR_MODE_INDEX[4])) != -1:
                            WhisperType = str(self.COLOUR_MODE_NAME[4])
                        else:
                            if WhisperColour.find(str(self.COLOUR_MODE_INDEX[6])) != -1:
                                WhisperType = str(self.COLOUR_MODE_NAME[6])
                            else:
                                WhisperType = WhisperColour
        self.LastChange.SetText('Color elegido: ' + str(WhisperType))
        if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[0])) != -1:
            WhisperType = str(self.COLOUR_MODE_NAME2[0])
        else:
            if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[1])) != -1:
                WhisperType = str(self.COLOUR_MODE_NAME2[1])
            else:
                if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[2])) != -1:
                    WhisperType = str(self.COLOUR_MODE_NAME2[2])
                else:
                    if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[3])) != -1:
                        WhisperType = str(self.COLOUR_MODE_NAME2[3])
                    else:
                        if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[4])) != -1:
                            WhisperType = str(self.COLOUR_MODE_NAME2[4])
                        else:
                            if WhisperColour.find(str(self.COLOUR_MODE_INDEX2[6])) != -1:
                                WhisperType = str(self.COLOUR_MODE_NAME2[6])
                            else:
                                WhisperType = WhisperColour
        self.LastChange.SetText('Color elegido: ' + str(WhisperType))

    def StopSpamBot(self):
        global WhisperCount
        global WhisperActivity
        WhisperActivity = 'Pause'
        WhisperCount = 0
        self.LastChange.SetText('SpamBot parado')

    def StartSpamBot(self):
        global WhisperAmount
        global WhisperDelay
        global WhisperActivity
        self.SetVIDRange()
        self.ErrorLog.SetText('No hay errores')
        self.ErrorLogRight.SetText('')
        self.ErrorLog2.SetText('')
        self.ErrorLog2Right.SetText('')
        if int(WhisperCount) != 0:
            Message = str(self.ERROR_MESSAGE_INDEX[0])
            self.ErrorLog.SetText(str(Message))
        if WHISPER_TYPE == '':
            Message = str(self.ERROR_MESSAGE_INDEX[1])
            if self.ErrorLog.GetText() != 'keiner':
                self.ErrorLog2.SetText(str(Message))
            else:
                self.ErrorLog.SetText(str(Message))
        else:
            if WHISPER_TYPE == 'PJ' and str(self.PlayerWhisperSpamEditLine.GetText()) == '':
                Message = str(self.ERROR_MESSAGE_INDEX[6])
                if self.ErrorLog.GetText() != 'keiner':
                    if self.ErrorLog2.GetText() != '':
                        self.ErrorLogRight.SetText(str(Message))
                    else:
                        self.ErrorLog2.SetText(str(Message))
                else:
                    self.ErrorLog.SetText(str(Message))
        if WhisperColour == '':
            Message = str(self.ERROR_MESSAGE_INDEX[2])
            if self.ErrorLog.GetText() != 'No hay errores':
                if self.ErrorLog2.GetText() != '':
                    self.ErrorLogRight.SetText(str(Message))
                else:
                    self.ErrorLog2.SetText(str(Message))
            else:
                self.ErrorLog.SetText(str(Message))
        if str(self.WhisperSpamEditLine.GetText()) == '':
            Message = str(self.ERROR_MESSAGE_INDEX[3])
            if self.ErrorLog.GetText() != 'No hay errores':
                if self.ErrorLog2.GetText() != '':
                    if self.ErrorLogRight.GetText() != '':
                        self.ErrorLog2Right.SetText(str(Message))
                    else:
                        self.ErrorLogRight.SetText(str(Message))
                else:
                    self.ErrorLog2.SetText(str(Message))
            else:
                self.ErrorLog.SetText(str(Message))
        if str(self.DelayWhisperSpamEditLine.GetText()) == '':
            if WHISPER_TYPE != 6:
                Message = str(self.ERROR_MESSAGE_INDEX[4])
                if self.ErrorLog.GetText() != 'No hay errores':
                    if self.ErrorLog2.GetText() != '':
                        if self.ErrorLogRight.GetText() != '':
                            self.ErrorLog2Right.SetText(str(Message))
                        else:
                            self.ErrorLogRight.SetText(str(Message))
                    else:
                        self.ErrorLog2.SetText(str(Message))
                else:
                    self.ErrorLog.SetText(str(Message))
        if int(self.CountWhisperSpamEditLine.GetText()) <= 0 or str(self.CountWhisperSpamEditLine.GetText()) == '':
            Message = str(self.ERROR_MESSAGE_INDEX[5])
            if self.ErrorLog.GetText() != 'No hay errores':
                if self.ErrorLog2.GetText() != '':
                    if self.ErrorLogRight.GetText() != '':
                        self.ErrorLog2Right.SetText(str(Message))
                    else:
                        self.ErrorLogRight.SetText(str(Message))
                else:
                    self.ErrorLog2.SetText(str(Message))
            else:
                self.ErrorLog.SetText(str(Message))
        if WHISPER_TYPE != '' and (int(self.CountWhisperSpamEditLine.GetText()) > 0 or str(self.CountWhisperSpamEditLine.GetText()) == '') and str(self.DelayWhisperSpamEditLine.GetText()) != '' and WhisperColour != '' and int(WhisperCount) == 0:
            WhisperDelay = int(self.DelayWhisperSpamEditLine.GetText())
            WhisperAmount = int(self.CountWhisperSpamEditLine.GetText())
            self.LastChange.SetText('El spamBot ha comenzado!')
            WhisperActivity = 'Spam'
            self.WhisperSpam()

    def WhisperSpam(self):
        global WhisperCount
        global ScanEnd
        global ScanStart
        if int(WhisperAmount) > int(WhisperCount):
            if WhisperColour != 'Random':
                if WhisperActivity == 'Spam':
                    if str(WHISPER_TYPE) == 'PJ':
                        net.SendWhisperPacket(str(self.PlayerWhisperSpamEditLine.GetText()), str(WhisperColour) + str(self.WhisperSpamEditLine.GetText()))
                        self.LastChange.SetText('Canditdad elegida: ' + str(WhisperCount))
                    else:
                        if str(WHISPER_TYPE) == 'Todos':
                            for i in xrange(ScanStart, ScanEnd):
                                Player = chr.GetNameByVID(i)
                                Race = chr.GetInstanceType(i)
                                PlayerName = player.GetName()
                                if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != 'None' and str(Player) != '' and str(Player) != str(PlayerName):
                                    net.SendWhisperPacket(str(Player), str(WhisperColour) + str(self.WhisperSpamEditLine.GetText()))
                                    self.LastChange.SetText('Cantidad elegida: ' + str(WhisperCount))

            else:
                if WhisperColour == 'Random':
                    if WhisperActivity == 'Spam':
                        if str(WHISPER_TYPE) == 'PJ':
                            net.SendWhisperPacket(str(self.PlayerWhisperSpamEditLine.GetText()), '|c' + str(self.random_color()) + '|H|h ' + str(self.WhisperSpamEditLine.GetText()))
                            self.LastChange.SetText('Cantidad elegida: ' + str(WhisperCount))
                        else:
                            if str(WHISPER_TYPE) == 'Todos':
                                for i in xrange(ScanStart, ScanEnd):
                                    Player = chr.GetNameByVID(i)
                                    Race = chr.GetInstanceType(i)
                                    PlayerName = player.GetName()
                                    if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != 'None' and str(Player) != '' and str(Player) != str(PlayerName):
                                        net.SendWhisperPacket(str(Player), '|c' + str(self.random_color()) + '|H|h ' + str(self.WhisperSpamEditLine.GetText()))
                                        self.LastChange.SetText('Cantidad elegida: ' + str(WhisperCount))

            if WhisperActivity == 'Spam':
                WhisperCount += 1
                self.WaitingDelay = WaitingDialog()
                self.WaitingDelay.Open(float(WhisperDelay))
                self.WaitingDelay.SAFE_SetTimeOverEvent(self.WhisperSpam)
        else:
            WhisperCount = 0
            self.LastChange.SetText('El spamBot ha finalizado con exito')

    def random_color(self):
        COLOR_RANGE = (50, 255)
        rgb = list()
        for c in range(0, 4):
            rgb.append(app.GetRandom(COLOR_RANGE[0], COLOR_RANGE[1]))

        return ('').join([ hex(c)[2:].upper() for c in rgb ])

    def SetVIDRange(self):
        global ScanEnd
        global ScanStart
        for i in range(500, 3000000):
            Player = chr.GetNameByVID(i)
            Race = chr.GetInstanceType(i)
            if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != 'None' and str(Player) != '':
                ScanStart = int(i - 500)
                ScanEnd = int(i + 50000)
                break

    def velocidad_func(self):
        self.Board3.Show()

    def camara_func(self):
        self.Board2.Show()

    def spammbot_func(self):
        self.Board9.Show()

    def mpcolor_func(self):
        self.Board15.Show()

    def buffbot_func(self):
        self.Board10.Show()

    def botlibros_func(self):
        self.Board11.Show()

    def detectorgm_func(self):
        self.Board12.Show()

    def otroshacks_func(self):
        self.Board4.Show()

    def creditos_func(self):
        self.Board7.Show()

    def salir_func(self):
        app.Exit()

    def TirarCH(self):
        Codigo01 = '/dice -2147483648 2147483647'
        Codigo02 = '/war gremio -200000000'
        Codigo03 = '/war gremio -1111111'
        net.SendChatPacket(Codigo01, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(Codigo02, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(Codigo03, chat.CHAT_TYPE_TALKING)

    def CrearGremio01(self):
        Gremio = self.CrearGremioEditLine.GetText()
        net.SendAnswerMakeGuildPacket(Gremio)

    def CrearGremio(self):
        self.Board17.Show()

    def ActivarDistancia(self):
        Distancia = self.Configuracion.GetText()
        if 500 >= int(Distancia):
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'La distancia que usted ha escojido es muy poca. Escoja una mayor a 500.')
            self.Configuracion.SetText('500')
        else:
            if 2500 <= int(Distancia):
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'La distancia que usted ha escojido es demasiada. Escoja una menor a 2500.')
                self.Configuracion.SetText('2500')

    def Atras(self):
        Distancia = self.Configuracion.GetText()
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Usted se ha movido hacia atras, para cambiar la distancia vaya a configuracion.')
        x, y, z = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) + int(Distancia), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def Adelante(self):
        Distancia = self.Configuracion.GetText()
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Usted se ha movido hacia adelante, para cambiar la distancia vaya a configuracion.')
        x, y, z = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) - int(Distancia), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def Izquierda(self):
        Distancia = self.Configuracion.GetText()
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Usted se ha movido hacia la izquierda, para cambiar la distancia vaya a configuracion.')
        x, y, z = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) - int(Distancia), int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def Derecha(self):
        Distancia = self.Configuracion.GetText()
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Usted se ha movido hacia la derecha, para cambiar la distancia vaya a configuracion.')
        x, y, z = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) + int(Distancia), int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def GM(self):
        global CheckGM
        global LevelbotModo1
        global LevelbotModo0
        global LevelbotModo2
        if CheckGM == 1:
            VidList = self.GetVidList()
            for vid in VidList:
                Instance = chr.GetInstanceType(vid)
                if Instance == chr.INSTANCE_TYPE_PLAYER and chr.GetNameByVID(vid) != 'None' and (chr.IsGameMaster(vid) or chr.GetNameByVID(vid)[0] == '['):
                    LevelbotModo0 = 1
                    LevelbotModo1 = 1
                    LevelbotModo2 = 1
                    self.LevelbotModo0()
                    self.LevelbotModo1()
                    self.LevelbotModo2()
                    chat.AppendChat(1, 'GameMaster: ' + str(chr.GetNameByVID(vid)) + ' te ha visto, el level bot a parado.')
                    break

    def GetVidList(self):
        return VidList

    def CheckGameMaster(self):
        return self.CheckGM

    def GMDetector(self):
        global CheckGM
        if CheckGM == 0:
            CheckGM = 1
            self.DetectorGMSButton.SetText('Desactivar')
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'El detector de gms ha sido activado')
            self.GM()
        else:
            CheckGM = 0
            self.DetectorGMSButton.SetText('Activar')
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'El detector de gms ha sido desactivado')

    def Pesca(self):
        app.RunPythonFile('Hack.py')

    def Cambiar(self):
        global Modoespada
        if Modoespada == 0:
            Modoespada = 1
            self.ModoEspada1Button.Show()
            self.ModoEspada2Button.Show()
            self.ModoDaga1Button.Show()
            self.ModoDaga2Button.Show()
            self.ModoChaman1Button.Show()
            self.ModoChaman2Button.Show()
            self.ModoGeneralButton.Show()
            self.CambiarGLabel.Show()
            self.CambiarNLabel.Show()
            self.CambiarCLabel.Show()
            self.CambiargeneralLabel.Show()
            self.Modoespada1Label.Show()
            self.Modoespada2Label.Show()
            self.Mododaga1Label.Show()
            self.Mododaga2Label.Show()
            self.Modochaman1Label.Show()
            self.Modochaman2Label.Show()
            self.ModogeneralLabel.Show()
            self.Board1.SetSize(272, 700)
            self.CambiararmaButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.CambiararmaButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.CambiararmaButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.CambiararmaButton.SetToolTipText('Desactivar')
        else:
            Modoespada = 0
            self.ModoEspada1Button.Hide()
            self.ModoEspada2Button.Hide()
            self.ModoDaga1Button.Hide()
            self.ModoDaga2Button.Hide()
            self.ModoChaman1Button.Hide()
            self.ModoChaman2Button.Hide()
            self.ModoGeneralButton.Hide()
            self.CambiarGLabel.Hide()
            self.CambiarNLabel.Hide()
            self.CambiarCLabel.Hide()
            self.CambiargeneralLabel.Hide()
            self.Modoespada1Label.Hide()
            self.Modoespada2Label.Hide()
            self.Mododaga1Label.Hide()
            self.Mododaga2Label.Hide()
            self.Modochaman1Label.Hide()
            self.Modochaman2Label.Hide()
            self.ModogeneralLabel.Hide()
            self.Board1.SetSize(272, 370)
            self.CambiararmaButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.CambiararmaButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.CambiararmaButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.CambiararmaButton.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')

    def Modoespada1(self):
        global Modoespada1
        if Modoespada1 == 0:
            Modoespada1 = 1
            Modoespada2 = 0
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoEspada1Button.SetToolTipText('Desactivar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)
        else:
            Modoespada1 = 1
            Modoespada2 = 0
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoEspada1Button.SetToolTipText('Desactivar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)

    def Modoespada2(self):
        global Modoespada2
        if Modoespada2 == 0:
            Modoespada2 = 1
            Modoespada1 = 0
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoEspada2Button.SetToolTipText('Desactivar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)
        else:
            Modoespada2 = 1
            Modoespada1 = 0
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoEspada2Button.SetToolTipText('Desactivar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)

    def ModoDaga1(self):
        global ModoDaga1
        if ModoDaga1 == 0:
            ModoDaga1 = 1
            ModoDaga2 = 0
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoDaga1Button.SetToolTipText('Desactivar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_BOW)
        else:
            ModoDaga1 = 1
            ModoDaga2 = 0
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoDaga1Button.SetToolTipText('Desactivar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_BOW)

    def ModoDaga2(self):
        global ModoDaga2
        if ModoDaga2 == 0:
            ModoDaga2 = 1
            ModoDaga1 = 0
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoDaga2Button.SetToolTipText('Desactivar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_DUALHAND_SWORD)
        else:
            ModoDaga2 = 1
            ModoDaga1 = 0
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoDaga2Button.SetToolTipText('Desactivar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_DUALHAND_SWORD)

    def ModoChaman1(self):
        global ModoChaman1
        if ModoChaman1 == 0:
            ModoChaman1 = 1
            ModoChaman2 = 0
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoChaman1Button.SetToolTipText('Desactivar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_FAN)
        else:
            ModoChaman1 = 1
            ModoChaman2 = 0
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoChaman1Button.SetToolTipText('Desactivar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_FAN)

    def ModoChaman2(self):
        global ModoChaman2
        if ModoChaman2 == 0:
            ModoChaman2 = 1
            ModoChaman1 = 0
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoChaman2Button.SetToolTipText('Desactivar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_BELL)
        else:
            ModoChaman2 = 1
            ModoChaman1 = 0
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoChaman2Button.SetToolTipText('Desactivar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoGeneralButton.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_BELL)

    def ModoGeneral(self):
        global ModoGeneral
        if ModoGeneral == 0:
            ModoGeneral = 1
            ModoGeneral = 0
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoGeneralButton.SetToolTipText('Desactivar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_GENERAL)
        else:
            ModoGeneral = 1
            ModoGeneral = 0
            self.ModoGeneralButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ModoGeneralButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ModoGeneralButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ModoGeneralButton.SetToolTipText('Desactivar')
            self.ModoEspada1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada1Button.SetToolTipText('Activar')
            self.ModoEspada2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoEspada2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoEspada2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoEspada2Button.SetToolTipText('Activar')
            self.ModoDaga1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga1Button.SetToolTipText('Activar')
            self.ModoDaga2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoDaga2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoDaga2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoDaga2Button.SetToolTipText('Activar')
            self.ModoChaman1Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman1Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman1Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman1Button.SetToolTipText('Activar')
            self.ModoChaman2Button.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ModoChaman2Button.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ModoChaman2Button.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ModoChaman2Button.SetToolTipText('Activar')
            chr.SetMotionMode(chr.MOTION_MODE_GENERAL)

    def Habilidad(self):
        global Habilidades
        if Habilidades == 0:
            Habilidades = 1
            self.poderesButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.poderesButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.poderesButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.poderesButton.SetToolTipText('Desactivar')
            player.ToggleCoolTime()
        else:
            Habilidades = 0
            self.poderesButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.poderesButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.poderesButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.poderesButton.SetToolTipText('Activar')
            player.ToggleCoolTime()

    def Salir(self):
        app.Exit()

    def LibroBot00(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot00Button.SetUpVisual('pack\\Botones\\Habilidades\\Ambush01.tga')
            self.LibroBot00Button.SetOverVisual('pack\\Botones\\Habilidades\\Ambush01.tga')
            self.LibroBot00Button.SetDownVisual('pack\\Botones\\Habilidades\\Ambush01.tga')
            self.LibroBot00Button.SetToolTipText('Desactivar')
            self.LibroBotItem1()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot00Button.SetUpVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
            self.LibroBot00Button.SetOverVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
            self.LibroBot00Button.SetDownVisual('pack\\Botones\\Habilidades\\Ambush00.tga')
            self.LibroBot00Button.SetToolTipText('Activar')

    def LibroBot01(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot01Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataquerapido01.tga')
            self.LibroBot01Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataquerapido01.tga')
            self.LibroBot01Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataquerapido01.tga')
            self.LibroBot01Button.SetToolTipText('Desactivar')
            self.LibroBotItem4()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot01Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
            self.LibroBot01Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
            self.LibroBot01Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataquerapido00.tga')
            self.LibroBot01Button.SetToolTipText('Activar')

    def LibroBot02(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot02Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagarodante01.tga')
            self.LibroBot02Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagarodante01.tga')
            self.LibroBot02Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagarodante01.tga')
            self.LibroBot02Button.SetToolTipText('Desactivar')
            self.LibroBotItem7()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot02Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
            self.LibroBot02Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
            self.LibroBot02Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagarodante00.tga')
            self.LibroBot02Button.SetToolTipText('Activar')

    def LibroBot03(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot03Button.SetUpVisual('pack\\Botones\\Habilidades\\Stealth01.tga')
            self.LibroBot03Button.SetOverVisual('pack\\Botones\\Habilidades\\Stealth01.tga')
            self.LibroBot03Button.SetDownVisual('pack\\Botones\\Habilidades\\Stealth01.tga')
            self.LibroBot03Button.SetToolTipText('Desactivar')
            self.LibroBotItem10()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot03Button.SetUpVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
            self.LibroBot03Button.SetOverVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
            self.LibroBot03Button.SetDownVisual('pack\\Botones\\Habilidades\\Stealth00.tga')
            self.LibroBot03Button.SetToolTipText('Activar')

    def LibroBot04(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot04Button.SetUpVisual('pack\\Botones\\Habilidades\\Nubetoxica01.tga')
            self.LibroBot04Button.SetOverVisual('pack\\Botones\\Habilidades\\Nubetoxica01.tga')
            self.LibroBot04Button.SetDownVisual('pack\\Botones\\Habilidades\\Nubetoxica01.tga')
            self.LibroBot04Button.SetToolTipText('Desactivar')
            self.LibroBotItem13()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot04Button.SetUpVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
            self.LibroBot04Button.SetOverVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
            self.LibroBot04Button.SetDownVisual('pack\\Botones\\Habilidades\\Nubetoxica00.tga')
            self.LibroBot04Button.SetToolTipText('Activar')

    def LibroBot05(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot05Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagaletal01.tga')
            self.LibroBot05Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagaletal01.tga')
            self.LibroBot05Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagaletal01.tga')
            self.LibroBot05Button.SetToolTipText('Desactivar')
            self.LibroBotItem16()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot05Button.SetUpVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
            self.LibroBot05Button.SetOverVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
            self.LibroBot05Button.SetDownVisual('pack\\Botones\\Habilidades\\Dagaletal00.tga')
            self.LibroBot05Button.SetToolTipText('Activar')

    def LibroBot10(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot10Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparorepetido01.tga')
            self.LibroBot10Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparorepetido01.tga')
            self.LibroBot10Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparorepetido01.tga')
            self.LibroBot10Button.SetToolTipText('Desactivar')
            self.LibroBotItem19()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot10Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
            self.LibroBot10Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
            self.LibroBot10Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparorepetido00.tga')
            self.LibroBot10Button.SetToolTipText('Activar')

    def LibroBot11(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot11Button.SetUpVisual('pack\\Botones\\Habilidades\\Lluviadeflechas01.tga')
            self.LibroBot11Button.SetOverVisual('pack\\Botones\\Habilidades\\Lluviadeflechas01.tga')
            self.LibroBot11Button.SetDownVisual('pack\\Botones\\Habilidades\\Lluviadeflechas01.tga')
            self.LibroBot11Button.SetToolTipText('Desactivar')
            self.LibroBotItem22()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot11Button.SetUpVisual('pack\\Botones\\Habilidades\\Lluviadeflechas00.tga')
            self.LibroBot11Button.SetOverVisual('pack\\Botones\\Habilidades\\Lluviadeflechas00.tga')
            self.LibroBot11Button.SetDownVisual('pack\\Botones\\Habilidades\\Lluviadeflechas00.tga')
            self.LibroBot11Button.SetToolTipText('Activar')

    def LibroBot12(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot12Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechadefuego01.tga')
            self.LibroBot12Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechadefuego01.tga')
            self.LibroBot12Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechadefuego01.tga')
            self.LibroBot12Button.SetToolTipText('Desactivar')
            self.LibroBotItem25()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot12Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
            self.LibroBot12Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
            self.LibroBot12Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechadefuego00.tga')
            self.LibroBot12Button.SetToolTipText('Activar')

    def LibroBot13(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot13Button.SetUpVisual('pack\\Botones\\Habilidades\\Caminopluma01.tga')
            self.LibroBot13Button.SetOverVisual('pack\\Botones\\Habilidades\\Caminopluma01.tga')
            self.LibroBot13Button.SetDownVisual('pack\\Botones\\Habilidades\\Caminopluma01.tga')
            self.LibroBot13Button.SetToolTipText('Desactivar')
            self.LibroBotItem28()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot13Button.SetUpVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
            self.LibroBot13Button.SetOverVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
            self.LibroBot13Button.SetDownVisual('pack\\Botones\\Habilidades\\Caminopluma00.tga')
            self.LibroBot13Button.SetToolTipText('Activar')

    def LibroBot14(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot14Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechavenenosa01.tga')
            self.LibroBot14Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechavenenosa01.tga')
            self.LibroBot14Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechavenenosa01.tga')
            self.LibroBot14Button.SetToolTipText('Desactivar')
            self.LibroBotItem31()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot14Button.SetUpVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
            self.LibroBot14Button.SetOverVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
            self.LibroBot14Button.SetDownVisual('pack\\Botones\\Habilidades\\Flechavenenosa00.tga')
            self.LibroBot14Button.SetToolTipText('Activar')

    def LibroBot15(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot15Button.SetUpVisual('pack\\Botones\\Habilidades\\Berrinche01.tga')
            self.LibroBot15Button.SetOverVisual('pack\\Botones\\Habilidades\\Berrinche01.tga')
            self.LibroBot15Button.SetDownVisual('pack\\Botones\\Habilidades\\Berrinche01.tga')
            self.LibroBot15Button.SetToolTipText('Desactivar')
            self.LibroBotItem34()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot15Button.SetUpVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
            self.LibroBot15Button.SetOverVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
            self.LibroBot15Button.SetDownVisual('pack\\Botones\\Habilidades\\Berrinche00.tga')
            self.LibroBot15Button.SetToolTipText('Activar')

    def LibroBot20(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot20Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras001.tga')
            self.LibroBot20Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras001.tga')
            self.LibroBot20Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras001.tga')
            self.LibroBot20Button.SetToolTipText('Desactivar')
            self.LibroBotItem37()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot20Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
            self.LibroBot20Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
            self.LibroBot20Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Cortetresmaneras000.tga')
            self.LibroBot20Button.SetToolTipText('Activar')

    def LibroBot21(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot21Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada001.tga')
            self.LibroBot21Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada001.tga')
            self.LibroBot21Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada001.tga')
            self.LibroBot21Button.SetToolTipText('Desactivar')
            self.LibroBotItem40()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot21Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
            self.LibroBot21Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
            self.LibroBot21Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Girodeespada000.tga')
            self.LibroBot21Button.SetToolTipText('Activar')

    def LibroBot22(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot22Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada001.tga')
            self.LibroBot22Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada001.tga')
            self.LibroBot22Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada001.tga')
            self.LibroBot22Button.SetToolTipText('Desactivar')
            self.LibroBotItem43()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot22Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
            self.LibroBot22Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
            self.LibroBot22Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Rociada000.tga')
            self.LibroBot22Button.SetToolTipText('Activar')

    def LibroBot23(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot23Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada001.tga')
            self.LibroBot23Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada001.tga')
            self.LibroBot23Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada001.tga')
            self.LibroBot23Button.SetToolTipText('Desactivar')
            self.LibroBotItem46()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot23Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
            self.LibroBot23Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
            self.LibroBot23Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Auradeespada000.tga')
            self.LibroBot23Button.SetToolTipText('Activar')

    def LibroBot24(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot24Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk001.tga')
            self.LibroBot24Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk001.tga')
            self.LibroBot24Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk001.tga')
            self.LibroBot24Button.SetToolTipText('Desactivar')
            self.LibroBotItem49()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot24Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
            self.LibroBot24Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
            self.LibroBot24Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Berserk000.tga')
            self.LibroBot24Button.SetToolTipText('Activar')

    def LibroBot25(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot25Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal01.tga')
            self.LibroBot25Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal01.tga')
            self.LibroBot25Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal01.tga')
            self.LibroBot25Button.SetToolTipText('Desactivar')
            self.LibroBotItem52()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot25Button.SetUpVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
            self.LibroBot25Button.SetOverVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
            self.LibroBot25Button.SetDownVisual('pack\\Botones\\Habilidades\\Guerrero\\Golpemortal00.tga')
            self.LibroBot25Button.SetToolTipText('Activar')

    def LibroBot30(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot30Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpe01.tga')
            self.LibroBot30Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpe01.tga')
            self.LibroBot30Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpe01.tga')
            self.LibroBot30Button.SetToolTipText('Desactivar')
            self.LibroBotItem55()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot30Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
            self.LibroBot30Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
            self.LibroBot30Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpe00.tga')
            self.LibroBot30Button.SetToolTipText('Activar')

    def LibroBot31(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot31Button.SetUpVisual('pack\\Botones\\Habilidades\\Pulsoespiritual01.tga')
            self.LibroBot31Button.SetOverVisual('pack\\Botones\\Habilidades\\Pulsoespiritual01.tga')
            self.LibroBot31Button.SetDownVisual('pack\\Botones\\Habilidades\\Pulsoespiritual01.tga')
            self.LibroBot31Button.SetToolTipText('Desactivar')
            self.LibroBotItem58()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot31Button.SetUpVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
            self.LibroBot31Button.SetOverVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
            self.LibroBot31Button.SetDownVisual('pack\\Botones\\Habilidades\\Pulsoespiritual00.tga')
            self.LibroBot31Button.SetToolTipText('Activar')

    def LibroBot32(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot32Button.SetUpVisual('pack\\Botones\\Habilidades\\Tocon01.tga')
            self.LibroBot32Button.SetOverVisual('pack\\Botones\\Habilidades\\Tocon01.tga')
            self.LibroBot32Button.SetDownVisual('pack\\Botones\\Habilidades\\Tocon01.tga')
            self.LibroBot32Button.SetToolTipText('Desactivar')
            self.LibroBotItem61()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot32Button.SetUpVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
            self.LibroBot32Button.SetOverVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
            self.LibroBot32Button.SetDownVisual('pack\\Botones\\Habilidades\\Tocon00.tga')
            self.LibroBot32Button.SetToolTipText('Activar')

    def LibroBot33(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot33Button.SetUpVisual('pack\\Botones\\Habilidades\\Cuerpofuerte01.tga')
            self.LibroBot33Button.SetOverVisual('pack\\Botones\\Habilidades\\Cuerpofuerte01.tga')
            self.LibroBot33Button.SetDownVisual('pack\\Botones\\Habilidades\\Cuerpofuerte01.tga')
            self.LibroBot33Button.SetToolTipText('Desactivar')
            self.LibroBotItem64()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot33Button.SetUpVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
            self.LibroBot33Button.SetOverVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
            self.LibroBot33Button.SetDownVisual('pack\\Botones\\Habilidades\\Cuerpofuerte00.tga')
            self.LibroBot33Button.SetToolTipText('Activar')

    def LibroBot34(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot34Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedeespada01.tga')
            self.LibroBot34Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedeespada01.tga')
            self.LibroBot34Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedeespada01.tga')
            self.LibroBot34Button.SetToolTipText('Desactivar')
            self.LibroBotItem67()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot34Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
            self.LibroBot34Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
            self.LibroBot34Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedeespada00.tga')
            self.LibroBot34Button.SetToolTipText('Activar')

    def LibroBot35(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot35Button.SetUpVisual('pack\\Botones\\Habilidades\\Relampagomortal01.tga')
            self.LibroBot35Button.SetOverVisual('pack\\Botones\\Habilidades\\Relampagomortal01.tga')
            self.LibroBot35Button.SetDownVisual('pack\\Botones\\Habilidades\\Relampagomortal01.tga')
            self.LibroBot35Button.SetToolTipText('Desactivar')
            self.LibroBotItem70()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot35Button.SetUpVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
            self.LibroBot35Button.SetOverVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
            self.LibroBot35Button.SetDownVisual('pack\\Botones\\Habilidades\\Relampagomortal00.tga')
            self.LibroBot35Button.SetToolTipText('Activar')

    def LibroBot40(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot40Button.SetUpVisual('pack\\Botones\\Habilidades\\Talismanvolador01.tga')
            self.LibroBot40Button.SetOverVisual('pack\\Botones\\Habilidades\\Talismanvolador01.tga')
            self.LibroBot40Button.SetDownVisual('pack\\Botones\\Habilidades\\Talismanvolador01.tga')
            self.LibroBot40Button.SetToolTipText('Desactivar')
            self.LibroBotItem73()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot40Button.SetUpVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
            self.LibroBot40Button.SetOverVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
            self.LibroBot40Button.SetDownVisual('pack\\Botones\\Habilidades\\Talismanvolador00.tga')
            self.LibroBot40Button.SetToolTipText('Activar')

    def LibroBot41(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot41Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparodeldragon01.tga')
            self.LibroBot41Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparodeldragon01.tga')
            self.LibroBot41Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparodeldragon01.tga')
            self.LibroBot41Button.SetToolTipText('Desactivar')
            self.LibroBotItem76()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot41Button.SetUpVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
            self.LibroBot41Button.SetOverVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
            self.LibroBot41Button.SetDownVisual('pack\\Botones\\Habilidades\\Disparodeldragon00.tga')
            self.LibroBot41Button.SetToolTipText('Activar')

    def LibroBot42(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot42Button.SetUpVisual('pack\\Botones\\Habilidades\\Rugidodeldragon01.tga')
            self.LibroBot42Button.SetOverVisual('pack\\Botones\\Habilidades\\Rugidodeldragon01.tga')
            self.LibroBot42Button.SetDownVisual('pack\\Botones\\Habilidades\\Rugidodeldragon01.tga')
            self.LibroBot42Button.SetToolTipText('Desactivar')
            self.LibroBotItem79()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot42Button.SetUpVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
            self.LibroBot42Button.SetOverVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
            self.LibroBot42Button.SetDownVisual('pack\\Botones\\Habilidades\\Rugidodeldragon00.tga')
            self.LibroBot42Button.SetToolTipText('Activar')

    def LibroBot43(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot43Button.SetUpVisual('pack\\Botones\\Habilidades\\Bendicion01.tga')
            self.LibroBot43Button.SetOverVisual('pack\\Botones\\Habilidades\\Bendicion01.tga')
            self.LibroBot43Button.SetDownVisual('pack\\Botones\\Habilidades\\Bendicion01.tga')
            self.LibroBot43Button.SetToolTipText('Desactivar')
            self.LibroBotItem82()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot43Button.SetUpVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
            self.LibroBot43Button.SetOverVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
            self.LibroBot43Button.SetDownVisual('pack\\Botones\\Habilidades\\Bendicion00.tga')
            self.LibroBot43Button.SetToolTipText('Activar')

    def LibroBot44(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot44Button.SetUpVisual('pack\\Botones\\Habilidades\\Reflectar01.tga')
            self.LibroBot44Button.SetOverVisual('pack\\Botones\\Habilidades\\Reflectar01.tga')
            self.LibroBot44Button.SetDownVisual('pack\\Botones\\Habilidades\\Reflectar01.tga')
            self.LibroBot44Button.SetToolTipText('Desactivar')
            self.LibroBotItem85()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot44Button.SetUpVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
            self.LibroBot44Button.SetOverVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
            self.LibroBot44Button.SetDownVisual('pack\\Botones\\Habilidades\\Reflectar00.tga')
            self.LibroBot44Button.SetToolTipText('Activar')

    def LibroBot45(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot45Button.SetUpVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon01.tga')
            self.LibroBot45Button.SetOverVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon01.tga')
            self.LibroBot45Button.SetDownVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon01.tga')
            self.LibroBot45Button.SetToolTipText('Desactivar')
            self.LibroBotItem88()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot45Button.SetUpVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
            self.LibroBot45Button.SetOverVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
            self.LibroBot45Button.SetDownVisual('pack\\Botones\\Habilidades\\Fuerzadeldragon00.tga')
            self.LibroBot45Button.SetToolTipText('Activar')

    def LibroBot50(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot50Button.SetUpVisual('pack\\Botones\\Habilidades\\Tirorelampago01.tga')
            self.LibroBot50Button.SetOverVisual('pack\\Botones\\Habilidades\\Tirorelampago01.tga')
            self.LibroBot50Button.SetDownVisual('pack\\Botones\\Habilidades\\Tirorelampago01.tga')
            self.LibroBot50Button.SetToolTipText('Desactivar')
            self.LibroBotItem91()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot50Button.SetUpVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
            self.LibroBot50Button.SetOverVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
            self.LibroBot50Button.SetDownVisual('pack\\Botones\\Habilidades\\Tirorelampago00.tga')
            self.LibroBot50Button.SetToolTipText('Activar')

    def LibroBot51(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot51Button.SetUpVisual('pack\\Botones\\Habilidades\\Llamadorelampago01.tga')
            self.LibroBot51Button.SetOverVisual('pack\\Botones\\Habilidades\\Llamadorelampago01.tga')
            self.LibroBot51Button.SetDownVisual('pack\\Botones\\Habilidades\\Llamadorelampago01.tga')
            self.LibroBot51Button.SetToolTipText('Desactivar')
            self.LibroBotItem94()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot51Button.SetUpVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
            self.LibroBot51Button.SetOverVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
            self.LibroBot51Button.SetDownVisual('pack\\Botones\\Habilidades\\Llamadarelampago00.tga')
            self.LibroBot51Button.SetToolTipText('Activar')

    def LibroBot52(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot52Button.SetUpVisual('pack\\Botones\\Habilidades\\Garrarelampago01.tga')
            self.LibroBot52Button.SetOverVisual('pack\\Botones\\Habilidades\\Garrarelampago01.tga')
            self.LibroBot52Button.SetDownVisual('pack\\Botones\\Habilidades\\Garrarelampago01.tga')
            self.LibroBot52Button.SetToolTipText('Desactivar')
            self.LibroBotItem97()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot52Button.SetUpVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
            self.LibroBot52Button.SetOverVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
            self.LibroBot52Button.SetDownVisual('pack\\Botones\\Habilidades\\Garrarelampago00.tga')
            self.LibroBot52Button.SetToolTipText('Activar')

    def LibroBot53(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot53Button.SetUpVisual('pack\\Botones\\Habilidades\\Curacion01.tga')
            self.LibroBot53Button.SetOverVisual('pack\\Botones\\Habilidades\\Curacion01.tga')
            self.LibroBot53Button.SetDownVisual('pack\\Botones\\Habilidades\\Curacion01.tga')
            self.LibroBot53Button.SetToolTipText('Desactivar')
            self.LibroBotItem100()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot53Button.SetUpVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
            self.LibroBot53Button.SetOverVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
            self.LibroBot53Button.SetDownVisual('pack\\Botones\\Habilidades\\Curacion00.tga')
            self.LibroBot53Button.SetToolTipText('Activar')

    def LibroBot54(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot54Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinos01.tga')
            self.LibroBot54Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinos01.tga')
            self.LibroBot54Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinos01.tga')
            self.LibroBot54Button.SetToolTipText('Desactivar')
            self.LibroBotItem103()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot54Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
            self.LibroBot54Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
            self.LibroBot54Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinos00.tga')
            self.LibroBot54Button.SetToolTipText('Activar')

    def LibroBot55(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot55Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataque01.tga')
            self.LibroBot55Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataque01.tga')
            self.LibroBot55Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataque01.tga')
            self.LibroBot55Button.SetToolTipText('Desactivar')
            self.LibroBotItem106()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot55Button.SetUpVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
            self.LibroBot55Button.SetOverVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
            self.LibroBot55Button.SetDownVisual('pack\\Botones\\Habilidades\\Ataque00.tga')
            self.LibroBot55Button.SetToolTipText('Activar')

    def LibroBot60(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot60Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpededo01.tga')
            self.LibroBot60Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpededo01.tga')
            self.LibroBot60Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpededo01.tga')
            self.LibroBot60Button.SetToolTipText('Desactivar')
            self.LibroBotItem109()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot60Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
            self.LibroBot60Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
            self.LibroBot60Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpededo00.tga')
            self.LibroBot60Button.SetToolTipText('Activar')

    def LibroBot61(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot61Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinodragon01.tga')
            self.LibroBot61Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinodragon01.tga')
            self.LibroBot61Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinodragon01.tga')
            self.LibroBot61Button.SetToolTipText('Desactivar')
            self.LibroBotItem112()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot61Button.SetUpVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
            self.LibroBot61Button.SetOverVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
            self.LibroBot61Button.SetDownVisual('pack\\Botones\\Habilidades\\Remolinodragon00.tga')
            self.LibroBot61Button.SetToolTipText('Activar')

    def LibroBot62(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot62Button.SetUpVisual('pack\\Botones\\Habilidades\\Hojaencantada01.tga')
            self.LibroBot62Button.SetOverVisual('pack\\Botones\\Habilidades\\Hojaencantada01.tga')
            self.LibroBot62Button.SetDownVisual('pack\\Botones\\Habilidades\\Hojaencantada01.tga')
            self.LibroBot62Button.SetToolTipText('Desactivar')
            self.LibroBotItem115()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot62Button.SetUpVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
            self.LibroBot62Button.SetOverVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
            self.LibroBot62Button.SetDownVisual('pack\\Botones\\Habilidades\\Hojaencantada00.tga')
            self.LibroBot62Button.SetToolTipText('Activar')

    def LibroBot63(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot63Button.SetUpVisual('pack\\Botones\\Habilidades\\Miedo01.tga')
            self.LibroBot63Button.SetOverVisual('pack\\Botones\\Habilidades\\Miedo01.tga')
            self.LibroBot63Button.SetDownVisual('pack\\Botones\\Habilidades\\Miedo01.tga')
            self.LibroBot63Button.SetToolTipText('Desactivar')
            self.LibroBotItem118()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot63Button.SetUpVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
            self.LibroBot63Button.SetOverVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
            self.LibroBot63Button.SetDownVisual('pack\\Botones\\Habilidades\\Miedo00.tga')
            self.LibroBot63Button.SetToolTipText('Activar')

    def LibroBot64(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot64Button.SetUpVisual('pack\\Botones\\Habilidades\\Armaduraencantada01.tga')
            self.LibroBot64Button.SetOverVisual('pack\\Botones\\Habilidades\\Armaduraencantada01.tga')
            self.LibroBot64Button.SetDownVisual('pack\\Botones\\Habilidades\\Armaduraencantada01.tga')
            self.LibroBot64Button.SetToolTipText('Desactivar')
            self.LibroBotItem121()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot64Button.SetUpVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
            self.LibroBot64Button.SetOverVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
            self.LibroBot64Button.SetDownVisual('pack\\Botones\\Habilidades\\Armaduraencantada00.tga')
            self.LibroBot64Button.SetToolTipText('Activar')

    def LibroBot65(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot65Button.SetUpVisual('pack\\Botones\\Habilidades\\Dispar01.tga')
            self.LibroBot65Button.SetOverVisual('pack\\Botones\\Habilidades\\Dispar01.tga')
            self.LibroBot65Button.SetDownVisual('pack\\Botones\\Habilidades\\Dispar01.tga')
            self.LibroBot65Button.SetToolTipText('Desactivar')
            self.LibroBotItem124()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot65Button.SetUpVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
            self.LibroBot65Button.SetOverVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
            self.LibroBot65Button.SetDownVisual('pack\\Botones\\Habilidades\\Dispar00.tga')
            self.LibroBot65Button.SetToolTipText('Activar')

    def LibroBot70(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot70Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeoscuro01.tga')
            self.LibroBot70Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeoscuro01.tga')
            self.LibroBot70Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeoscuro01.tga')
            self.LibroBot70Button.SetToolTipText('Desactivar')
            self.LibroBotItem127()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot70Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
            self.LibroBot70Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
            self.LibroBot70Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeoscuro00.tga')
            self.LibroBot70Button.SetToolTipText('Activar')

    def LibroBot71(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot71Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedellama01.tga')
            self.LibroBot71Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedellama01.tga')
            self.LibroBot71Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedellama01.tga')
            self.LibroBot71Button.SetToolTipText('Desactivar')
            self.LibroBotItem130()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot71Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
            self.LibroBot71Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
            self.LibroBot71Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpedellama00.tga')
            self.LibroBot71Button.SetToolTipText('Activar')

    def LibroBot72(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot72Button.SetUpVisual('pack\\Botones\\Habilidades\\Espiritudelallama01.tga')
            self.LibroBot72Button.SetOverVisual('pack\\Botones\\Habilidades\\Espiritudelallama01.tga')
            self.LibroBot72Button.SetDownVisual('pack\\Botones\\Habilidades\\Espiritudelallama01.tga')
            self.LibroBot72Button.SetToolTipText('Desactivar')
            self.LibroBotItem133()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot72Button.SetUpVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
            self.LibroBot72Button.SetOverVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
            self.LibroBot72Button.SetDownVisual('pack\\Botones\\Habilidades\\Espiritudelallama00.tga')
            self.LibroBot72Button.SetToolTipText('Activar')

    def LibroBot73(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot73Button.SetUpVisual('pack\\Botones\\Habilidades\\Proteccionoscura01.tga')
            self.LibroBot73Button.SetOverVisual('pack\\Botones\\Habilidades\\Proteccionoscura01.tga')
            self.LibroBot73Button.SetDownVisual('pack\\Botones\\Habilidades\\Proteccionoscura01.tga')
            self.LibroBot73Button.SetToolTipText('Desactivar')
            self.LibroBotItem136()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot73Button.SetUpVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
            self.LibroBot73Button.SetOverVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
            self.LibroBot73Button.SetDownVisual('pack\\Botones\\Habilidades\\Proteccionoscura00.tga')
            self.LibroBot73Button.SetToolTipText('Activar')

    def LibroBot74(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot74Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeespiritual01.tga')
            self.LibroBot74Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeespiritual01.tga')
            self.LibroBot74Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeespiritual01.tga')
            self.LibroBot74Button.SetToolTipText('Desactivar')
            self.LibroBotItem139()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot74Button.SetUpVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
            self.LibroBot74Button.SetOverVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
            self.LibroBot74Button.SetDownVisual('pack\\Botones\\Habilidades\\Golpeespiritual00.tga')
            self.LibroBot74Button.SetToolTipText('Activar')

    def LibroBot75(self):
        global LibroBot
        if LibroBot == 0:
            LibroBot = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot75Button.SetUpVisual('pack\\Botones\\Habilidades\\Orbeoscuro01.tga')
            self.LibroBot75Button.SetOverVisual('pack\\Botones\\Habilidades\\Orbeoscuro01.tga')
            self.LibroBot75Button.SetDownVisual('pack\\Botones\\Habilidades\\Orbeoscuro01.tga')
            self.LibroBot75Button.SetToolTipText('Desactivar')
            self.LibroBotItem142()
        else:
            LibroBot = 0
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.LibroBot75Button.SetUpVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
            self.LibroBot75Button.SetOverVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
            self.LibroBot75Button.SetDownVisual('pack\\Botones\\Habilidades\\Orbeoscuro00.tga')
            self.LibroBot75Button.SetToolTipText('Activar')

    def LibroBotItem144(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem143)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem143(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem142)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem142(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50481:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem144)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem141(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem140)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem140(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem139)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem139(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50480:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem141)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem138(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem137)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem137(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem136)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem136(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50479:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem138)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem135(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem134)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem134(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem133)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem133(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50478:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem135)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem132(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem131)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem131(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem130)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem130(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50477:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem132)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem129(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem128)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem128(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem127)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem127(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50476:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem129)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem126(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem125)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem125(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem124)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem124(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50466:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem126)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem123(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem122)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem122(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem121)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem121(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50465:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem123)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem120(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem119)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem119(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem118)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem118(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50464:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem120)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem117(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem116)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem116(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem115)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem115(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50463:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem117)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem114(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem113)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem113(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem112)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem112(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50462:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem114)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem111(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem110)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem110(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem109)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem109(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50461:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem111)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem108(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem107)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem107(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem106)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem106(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50511:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem108)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem105(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem104)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem104(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem103)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem103(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50510:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem105)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem102(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem101)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem101(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem100)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem100(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50509:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem102)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem99(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem98)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem98(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem97)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem97(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50508:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem99)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem96(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem95)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem95(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem94)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem94(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50507:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem96)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem93(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem92)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem92(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem91)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem91(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50506:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem93)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem90(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem89)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem89(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem88)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem88(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50496:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem90)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem87(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem86)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem86(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem85)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem85(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50495:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem87)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem84(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem83)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem83(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem82)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem82(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50494:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem84)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem81(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem80)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem80(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem79)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem79(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50493:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem81)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem78(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem77)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem77(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem76)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem76(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50492:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem78)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem75(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem74)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem74(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem73)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem73(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50491:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem75)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem72(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem71)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem71(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem70)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem70(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50421:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem72)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem69(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem68)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem68(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem67)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem67(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50420:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem69)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem66(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem65)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem65(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem64)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem64(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50419:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem66)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem63(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem62)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem62(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem61)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem61(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50418:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem63)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem60(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem59)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem59(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem58)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem58(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50417:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem60)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem57(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem56)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem56(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem55)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem55(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50416:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem57)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem54(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem53)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem53(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem52)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem52(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50405:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem54)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem51(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem50)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem50(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem49)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem49(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50405:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem51)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem48(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem47)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem47(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem46)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem46(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50404:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem48)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem45(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem44)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem44(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem43)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem43(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50403:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem45)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem42(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem41)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem41(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem40)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem40(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50402:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem42)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem39(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem38)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem38(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem37)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem37(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50401:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem39)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem36(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem35)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem35(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem34)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem34(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50451:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem36)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem33(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem32)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem32(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem31)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem31(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50450:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem33)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem30(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem29)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem29(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem28)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem28(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50449:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem30)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem27(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem26)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem26(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem25)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem25(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50448:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem27)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem24(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem23)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem23(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem22)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem22(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50447:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem24)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem21(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem20)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem20(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem19)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem19(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50446:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem21)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem18(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem17)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem17(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem16)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem16(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50436:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem18)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem15(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem14)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem14(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem13)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem13(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50435:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem15)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem12(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem11)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem11(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem10)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem10(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50434:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem12)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem9(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem8)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem8(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem7)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem7(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50433:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem9)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem6(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem5)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem5(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem4)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem4(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50432:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem6)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem3(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71094:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem2)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem2(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 71001:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem1)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def LibroBotItem1(self):
        if LibroBot != 0:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 50431:
                    Segundoslibro = self.Segundos.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(Segundoslibro))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.LibroBotItem3)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def StartBuffbot(self):
        global Buffbotstarten
        self.Teleport2Target()
        if Buffbotstarten == 0:
            self.BuffBotStartButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\start_0.tga')
            self.BuffBotStartButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\start_1.tga')
            self.BuffBotStartButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\start_2.tga')
            self.BuffBotStartButton.SetToolTipText('Desactivar')
            Buffbotstarten = 1
            self.MakeBuff()
        else:
            self.BuffBotStartButton.SetUpVisual('pack\\Botones\\Botones onoff\\Img\\stop_0.tga')
            self.BuffBotStartButton.SetOverVisual('pack\\Botones\\Botones onoff\\Img\\stop_1.tga')
            self.BuffBotStartButton.SetDownVisual('pack\\Botones\\Botones onoff\\Img\\stop2.tga')
            self.BuffBotStartButton.SetToolTipText('Activar')
            Buffbotstarten = 0

    def SlideDelay(self):
        global waitingdelay
        waitingdelay = int(self.DelaySlide.GetSliderPos() * 100)
        self.InfoDelay.SetText(str(waitingdelay) + ' Segundos')

    def MakeBuff(self):
        global xBuff
        if Buffbotstarten == 0:
            return
        if xBuff == 4:
            xBuff = 1
            self.WaitingDelay = WaitingDialog()
            self.WaitingDelay.Open(int(waitingdelay))
            self.WaitingDelay.SAFE_SetTimeOverEvent(self.MakeBuff)
            return
        SkillSlotID = xBuff + 3
        player.ClickSkillSlot(SkillSlotID)
        xBuff += 1
        self.BuffDelay = WaitingDialog()
        self.BuffDelay.Open(3.5)
        self.BuffDelay.SAFE_SetTimeOverEvent(self.MakeBuff)

    def Teleport2Target(self):
        vid = player.GetTargetVID()
        TargetX, TargetY, TargetZ = chr.GetPixelPosition(int(vid))
        Distance = player.GetCharacterDistance(int(vid))
        if Distance >= 100:
            chr.SetPixelPosition(int(TargetX), int(TargetY) - 10)
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    def OnUpdate(self):
        vid = player.GetTargetVID()
        name = chr.GetNameByVID(vid)
        self.TargetName.SetText(name)
        self.TargetName.Show()
        if Buffbotstarten != 0:
            self.Teleport2Target()

    def Copiar(self):
        global Copiar
        if Copiar == 0:
            Copiar = 1
            self.CopiarButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.CopiarButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.CopiarButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.CopiarButton.SetToolTipText('Desactivar')
            constInfo.CONSOLE_ENABLE = TRUE
            self.consoleEnable = TRUE
            app.EnableSpecialCameraMode()
            ui.EnablePaste(TRUE)
        else:
            Copiar = 0
            self.CopiarButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.CopiarButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.CopiarButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.CopiarButton.SetToolTipText('Activar')
            constInfo.CONSOLE_ENABLE = FALSE
            self.consoleEnable = FALSE
            app.EnableSpecialCameraMode()
            ui.EnablePaste(FALSE)

    def Gmvisual(self):
        global Gmvisual
        if Gmvisual == 0:
            Gmvisual = 1
            self.GmvisualButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.GmvisualButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.GmvisualButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.GmvisualButton.SetToolTipText('Desactivar')
            name = chr.GetName()
            name = name.replace('[GM]', '')
            namegm = '[GM]' + name
            chrmgr.SetAffect(-1, 0, 1)
            chr.SetNameString(namegm)
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'El efecto de GM Visual ha sido activado.')
            namegm = namegm.replace('[GM]', '')
        else:
            Gmvisual = 0
            self.GmvisualButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.GmvisualButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.GmvisualButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.GmvisualButton.SetToolTipText('Activar')
            name = chr.GetName()
            name = name.replace('[GM]', '')
            chrmgr.SetAffect(-1, 0, 0)
            chr.SetNameString(name)
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'El efecto de GM visual ha sido desactivado.')

    def PJ(self):
        global Pj
        if Pj == 0:
            Pj = 1
            self.PJButton.SetUpVisual('pack\\Botones\\Stealth_01.tga')
            self.PJButton.SetOverVisual('pack\\Botones\\Stealth_01.tga')
            self.PJButton.SetDownVisual('pack\\Botones\\Stealth_0.tga')
            self.PJButton.SetToolTipText('Desactivar')
            player.HidePlayer()
        else:
            Pj = 0
            self.PJButton.SetUpVisual('pack\\Botones\\Stealth_0.tga')
            self.PJButton.SetOverVisual('pack\\Botones\\Stealth_0.tga')
            self.PJButton.SetDownVisual('pack\\Botones\\Stealth_01.tga')
            self.PJButton.SetToolTipText('Activar')
            player.ShowPlayer()

    def UseChatType(self, mode):
        global CHAT_TYPE
        if mode != 'Random':
            CHAT_TYPE = mode
        else:
            Rnd = int(app.GetRandom(0, 3))
            CHAT_TYPE = self.CHAT_MODE_INDEX[int(Rnd)]
        if int(CHAT_TYPE) == 3:
            ChatType = 1
        else:
            if int(CHAT_TYPE) == 4:
                ChatType = 2
            else:
                if int(CHAT_TYPE) == 6:
                    ChatType = 3
                else:
                    ChatType = int(CHAT_TYPE)
        self.Last1Change.SetText('Forma elegida: ' + str(self.CHAT_MODE_NAME[int(ChatType)]))

    def UseChatColour(self, colour):
        global ChatColour
        ChatColour = str(colour)
        if ChatColour.find(str(self.COLOUR1_MODE_INDEX[0])) != -1:
            ChatType = str(self.COLOUR1_MODE_NAME[0])
        else:
            if ChatColour.find(str(self.COLOUR1_MODE_INDEX[1])) != -1:
                ChatType = str(self.COLOUR1_MODE_NAME[1])
            else:
                if ChatColour.find(str(self.COLOUR1_MODE_INDEX[2])) != -1:
                    ChatType = str(self.COLOUR1_MODE_NAME[2])
                else:
                    if ChatColour.find(str(self.COLOUR1_MODE_INDEX[3])) != -1:
                        ChatType = str(self.COLOUR1_MODE_NAME[3])
                    else:
                        if ChatColour.find(str(self.COLOUR1_MODE_INDEX[4])) != -1:
                            ChatType = str(self.COLOUR1_MODE_NAME[4])
                        else:
                            if ChatColour.find(str(self.COLOUR1_MODE_INDEX[6])) != -1:
                                ChatType = str(self.COLOUR1_MODE_NAME[6])
                            else:
                                ChatType = ChatColour
        self.Last1Change.SetText('Color elegido: ' + str(ChatType))
        if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[0])) != -1:
            ChatType = str(self.COLOUR1_MODE_NAME2[0])
        else:
            if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[1])) != -1:
                ChatType = str(self.COLOUR1_MODE_NAME2[1])
            else:
                if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[2])) != -1:
                    ChatType = str(self.COLOUR1_MODE_NAME2[2])
                else:
                    if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[3])) != -1:
                        ChatType = str(self.COLOUR1_MODE_NAME2[3])
                    else:
                        if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[4])) != -1:
                            ChatType = str(self.COLOUR1_MODE_NAME2[4])
                        else:
                            if ChatColour.find(str(self.COLOUR1_MODE_INDEX2[6])) != -1:
                                ChatType = str(self.COLOUR1_MODE_NAME2[6])
                            else:
                                ChatType = ChatColour
        self.Last1Change.SetText('Color elegido: ' + str(ChatType))

    def Stop1SpamBot(self):
        global Activity
        global Count
        Activity = 'Pause'
        Count = 0
        self.Last1Change.SetText('El spamm bot Ha sido parado')

    def Start1SpamBot(self):
        global Activity
        global Amount
        global Delay
        self.Error1Log.SetText('No hay errores')
        self.Error1LogRight.SetText('')
        self.Error1Log2.SetText('')
        self.Error1Log2Right.SetText('')
        State = 'Allow'
        if int(Count) != 0:
            Message = str(self.ERROR1_MESSAGE_INDEX[0])
            self.Error1Log.SetText(str(Message))
        if CHAT_TYPE == '':
            Message = str(self.ERROR1_MESSAGE_INDEX[1])
            if self.Error1Log.GetText() != 'No hay errores':
                self.Error1Log2.SetText(str(Message))
            else:
                self.Error1Log.SetText(str(Message))
        if ChatColour == '':
            Message = str(self.ERROR1_MESSAGE_INDEX[2])
            if self.Error1Log.GetText() != 'keiner':
                if self.Error1Log2.GetText() != '':
                    self.Error1LogRight.SetText(str(Message))
                else:
                    self.Error1Log2.SetText(str(Message))
            else:
                self.Error1Log.SetText(str(Message))
        if str(self.ChatSpamEditLine.GetText()) == '':
            Message = str(self.ERROR1_MESSAGE_INDEX[3])
            if self.Error1Log.GetText() != 'No hay errores':
                if self.Error1Log2.GetText() != '':
                    if self.Error1LogRight.GetText() != '':
                        self.Error1Log2Right.SetText(str(Message))
                    else:
                        self.Error1LogRight.SetText(str(Message))
                else:
                    self.Error1Log2.SetText(str(Message))
            else:
                self.Error1Log.SetText(str(Message))
        if CHAT_TYPE == 6 and int(self.DelayChatSpamEditLine.GetText()) < 15:
            Message = str(self.ERROR1_MESSAGE_INDEX[6])
            State = 'Banned'
            if self.Error1Log.GetText() != 'No hay errores':
                if self.Error1Log2.GetText() != '':
                    if self.Error1LogRight.GetText() != '':
                        self.Error1Log2Right.SetText(str(Message))
                    else:
                        self.Error1LogRight.SetText(str(Message))
                else:
                    self.Error1Log2.SetText(str(Message))
            else:
                self.Error1Log.SetText(str(Message))
        if str(self.DelayChatSpamEditLine.GetText()) == '':
            if CHAT_TYPE != 6:
                Message = str(self.ERROR1_MESSAGE_INDEX[4])
                if self.Error1Log.GetText() != 'No hay errores':
                    if self.Error1Log2.GetText() != '':
                        if self.Error1LogRight.GetText() != '':
                            self.Error1Log2Right.SetText(str(Message))
                        else:
                            self.Error1LogRight.SetText(str(Message))
                    else:
                        self.Error1Log2.SetText(str(Message))
                else:
                    self.Error1Log.SetText(str(Message))
        if int(self.CountChatSpamEditLine.GetText()) <= 0 or str(self.CountChatSpamEditLine.GetText()) == '':
            Message = str(self.ERROR1_MESSAGE_INDEX[5])
            if self.Error1Log.GetText() != 'No hay errores':
                if self.Error1Log2.GetText() != '':
                    if self.Error1LogRight.GetText() != '':
                        self.Error1Log2Right.SetText(str(Message))
                    else:
                        self.Error1LogRight.SetText(str(Message))
                else:
                    self.Error1Log2.SetText(str(Message))
            else:
                self.Error1Log.SetText(str(Message))
        if CHAT_TYPE != '' and (int(self.CountChatSpamEditLine.GetText()) > 0 or str(self.CountChatSpamEditLine.GetText()) == '') and str(self.DelayChatSpamEditLine.GetText()) != '' and ChatColour != '' and int(Count) == 0 and State == 'Allow':
            Delay = int(self.DelayChatSpamEditLine.GetText())
            Amount = int(self.CountChatSpamEditLine.GetText())
            self.Last1Change.SetText('El SpamBot Chat ha comenzado!')
            Activity = 'Spam'
            self.Spam()

    def Spam(self):
        global Count
        if int(Amount) > int(Count):
            if ChatColour != 'Random':
                if Activity == 'Spam':
                    net.SendChatPacket(str(ChatColour) + str(self.ChatSpamEditLine.GetText()), CHAT_TYPE)
                    self.Last1Change.SetText('Cantidad: ' + str(Count))
            else:
                if ChatColour == 'Random':
                    if Activity == 'Spam':
                        net.SendChatPacket('|c' + str(self.random1_color()) + '|H|h ' + str(self.ChatSpamEditLine.GetText()), CHAT_TYPE)
                        self.Last1Change.SetText('Cantidad: ' + str(Count))
            if Activity == 'Spam':
                Count += 1
                self.WaitingDelay = WaitingDialog()
                self.WaitingDelay.Open(float(Delay))
                self.WaitingDelay.SAFE_SetTimeOverEvent(self.Spam)
        else:
            Count = 0
            self.Last1Change.SetText('El spamBot Chat ha finalizado con exito..')

    def random1_color(self):
        COLOR_RANGE = (50, 255)
        rgb = list()
        for c in range(0, 4):
            rgb.append(app.GetRandom(COLOR_RANGE[0], COLOR_RANGE[1]))

        return ('').join([ hex(c)[2:].upper() for c in rgb ])

    def SetVIDRange(self):
        global ScanEnd
        global ScanStart
        for i in range(500, 3000000):
            Player = chr.GetNameByVID(i)
            Race = chr.GetInstanceType(i)
            if chr.INSTANCE_TYPE_PLAYER == Race and str(Player) != 'None' and str(Player) != '':
                ScanStart = int(i - 500)
                ScanEnd = int(i + 50000)
                break

    def Paginaweb(self):
        os.system('start http://www.francoiz.net/')

    def Creditosfrancoiz(self):
        os.system('start http://www.youtube.com/user/xFrancoizx')

    def Spamfrancoiz(self):
        chattext = self.InputText1.GetText()
        chatSegundos = self.InputSegundos1.GetText()
        net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(chattext, chat.CHAT_TYPE_TALKING)
        net.SendChatPacket(chattext, chat.WHISPER_TYPE_GM)
        net.SendChatPacket(chattext, chat.CHAT_TYPE_SHOUT)
        self.dela = WaitingDialog()
        self.dela.Open(int(chatSegundos))
        self.dela.SAFE_SetTimeOverEvent(self.NormalSpam)

    def TeleportToCoordinates(self):
        global teleport_mode
        global telestep
        x_coordinate = self.TeleportXEditLine.GetText()
        y_coordinate = self.TeleportYEditLine.GetText()
        z_coordinate = self.TeleportZEditLine.GetText()
        x_coordinate = int(x_coordinate) * 100
        y_coordinate = int(y_coordinate) * 100
        z_coordinate = int(z_coordinate) * 100
        ax, ay, az = player.GetMainCharacterPosition()
        teleport_mode = 1
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax) - 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax) + 2000, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax), int(ay) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                if telestep > 10:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax), int(ay) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                if telestep > 7:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, 'Por favor espere 5 segundos..')
                    return
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 2000)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                ax, ay, az = player.GetMainCharacterPosition()
                telestep = telestep + 1

            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        teleport_mode = 0

    def EqChange(self):
        ArmorValue = self.ArmorEditLine.GetText()
        WeaponValue = self.WeaponEditLine.GetText()
        HairValue = self.HairEditLine.GetText()
        if ArmorValue == '':
            chat.AppendChat(chat.CHAT_TYPE_INFO, 'Debes colocar algun numero')
        if WeaponValue == '':
            chat.AppendChat(chat.CHAT_TYPE_INFO, 'Debes colocar algun numero')
        if HairValue == '':
            chat.AppendChat(chat.CHAT_TYPE_INFO, 'Debes colocar algun numero')
        else:
            chr.ChangeShape(int(ArmorValue))
            chr.SetWeapon(int(WeaponValue))
            chr.ChangeHair(int(HairValue))
            chr.Refresh()

    def Combo(self):
        global Combo
        if Combo == 0:
            Combo = 1
            self.ComboTypeButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ComboTypeButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ComboTypeButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ComboTypeButton.SetToolTipText('Desactivar')
            chr.testSetComboType(2)
        else:
            Combo = 0
            self.ComboTypeButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ComboTypeButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ComboTypeButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ComboTypeButton.SetToolTipText('Activar')
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
        global AutoRedPot
        global AutoBluePot
        if AutoRedPot == 1 or AutoBluePot == 1:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Antes de despertar en modo fantasma, desactive los autopoteos.')
        else:
            chr.Revive()

    def SetTapferkeitsUmhange(self):
        global TapferkeitsUmhange
        if TapferkeitsUmhange == '':
            TapferkeitsUmhange = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.CabosButton.SetUpVisual('pack\\Botones\\Otros\\Img\\cabos_on.tga')
            self.CabosButton.SetOverVisual('pack\\Botones\\Otros\\Img\\cabos_on.tga')
            self.CabosButton.SetDownVisual('pack\\Botones\\Otros\\Img\\cabos_on.tga')
            self.CabosButton.SetToolTipText('Desactivar')
            self.UseTapferkeitsUmhange()
        else:
            TapferkeitsUmhange = ''
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            self.CabosButton.SetUpVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
            self.CabosButton.SetOverVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
            self.CabosButton.SetDownVisual('pack\\Botones\\Otros\\Img\\cabos_off.tga')
            self.CabosButton.SetToolTipText('Activar')

    def UseTapferkeitsUmhange(self):
        if TapferkeitsUmhange != '':
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                ItemValue = player.GetItemIndex(i)
                if ItemValue == 70038:
                    TapferkeitsUmhangeWaitingDelay = self.TapferkeitsUmhangeDelay.GetText()
                    net.SendItemUsePacket(i)
                    self.TapferkeitsUmhangDelay = WaitingDialog()
                    self.TapferkeitsUmhangDelay.Open(int(TapferkeitsUmhangeWaitingDelay))
                    self.TapferkeitsUmhangDelay.SAFE_SetTimeOverEvent(self.UseTapferkeitsUmhange)
                    break

        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def Caballofuncion(self):
        global MoveSpeedHack
        global Caballo
        if Caballo == '':
            Caballo = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, 'El caballo ha sido activado, por favor quitate o ponte la armadura.')
            if Caballo == 1:
                chr.MountHorse()
                self.MoveSpeedFix = WaitingDialog()
                self.MoveSpeedFix.Open(3.0)
                self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.Caballovelocidad1)
                self.CaballofuncionButton.SetUpVisual('pack\\Botones\\on_0.tga')
                self.CaballofuncionButton.SetOverVisual('pack\\Botones\\on_1.tga')
                self.CaballofuncionButton.SetDownVisual('pack\\Botones\\on_2.tga')
                self.CaballofuncionButton.SetToolTipText('Desactivar')
        else:
            Caballo = ''
            if MoveSpeedHack == 1:
                chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Si usted tiene activado el hack de velocidad, por favor desactivelo y luego intente desactivar el caballo nuevamente..')
                Caballo = 1
            else:
                chat.AppendChat(chat.CHAT_TYPE_INFO, 'Muevase en cualquier direccin y el caballo se desaparecer en 5 segundos, por favor espere.')
                chr.MountHorse(int(player.GetStatus(player.MOVING_SPEED)))
                self.CaballofuncionButton.SetUpVisual('pack\\Botones\\off_0.tga')
                self.CaballofuncionButton.SetOverVisual('pack\\Botones\\off_1.tga')
                self.CaballofuncionButton.SetDownVisual('pack\\Botones\\off_2.tga')
                self.CaballofuncionButton.SetToolTipText('Activar')

    def Caballovelocidad1(self):
        chr.MountHorse(int(player.GetStatus(player.MOVING_SPEED)))
        self.Caballovelocidad2()

    def Caballovelocidad2(self):
        if Caballo != '':
            chr.MountHorse()
            self.MoveSpeedFix = WaitingDialog()
            self.MoveSpeedFix.Open(3.0)
            self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.Caballovelocidad1)

    def AttackSpeedStatus(self):
        global AttackSpeedHack
        CurrentAttackSpeedHack = self.AttackSpeedStats.GetText()
        if AttackSpeedHack == '':
            AttackSpeedHack = 1
            chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            chr.SetAttackSpeed(int(CurrentAttackSpeedHack))
            self.AttackSpeedStatusButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.AttackSpeedStatusButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.AttackSpeedStatusButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.AttackSpeedStatusButton.SetToolTipText('Desactivar')
        else:
            if int(CurrentAttackSpeedHack) < 0.01:
                chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            else:
                if int(CurrentAttackSpeedHack) > 0.01:
                    AttackSpeedHack = ''
                    chat.AppendChat(chat.CHAT_TYPE_INFO, '')
                    chr.SetAttackSpeed(int(player.GetStatus(player.ATT_SPEED)))
                    self.AttackSpeedStatusButton.SetUpVisual('pack\\Botones\\off_0.tga')
                    self.AttackSpeedStatusButton.SetOverVisual('pack\\Botones\\off_1.tga')
                    self.AttackSpeedStatusButton.SetDownVisual('pack\\Botones\\off_2.tga')
                    self.AttackSpeedStatusButton.SetToolTipText('Activar')
                else:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def MoveSpeedStatus(self):
        global MoveSpeedHack
        CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
        if MoveSpeedHack == '':
            MoveSpeedHack = 1
            chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
            self.MoveSpeedStatusButton.SetUpVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
            self.MoveSpeedStatusButton.SetOverVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
            self.MoveSpeedStatusButton.SetDownVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
            self.MoveSpeedStatusButton.SetToolTipText('Desactivar')
            if int(CurrentMoveSpeedHack) > 100:
                self.MoveSpeedFix = WaitingDialog()
                self.MoveSpeedFix.Open(0.9)
                self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)
                self.MoveSpeedStatusButton.SetUpVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
                self.MoveSpeedStatusButton.SetOverVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
                self.MoveSpeedStatusButton.SetDownVisual('pack\\Botones\\Otros\\Img\\walkspeed_on.tga')
                self.MoveSpeedStatusButton.SetToolTipText('Desactivar')
        else:
            if int(CurrentMoveSpeedHack) < 0.01:
                chat.AppendChat(chat.CHAT_TYPE_INFO, '')
            else:
                if int(CurrentMoveSpeedHack) > 0.01:
                    MoveSpeedHack = ''
                    chat.AppendChat(chat.CHAT_TYPE_INFO, '')
                    chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
                    self.MoveSpeedStatusButton.SetUpVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
                    self.MoveSpeedStatusButton.SetOverVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
                    self.MoveSpeedStatusButton.SetDownVisual('pack\\Botones\\Otros\\Img\\walkspeed_off.tga')
                    self.MoveSpeedStatusButton.SetToolTipText('Activar')
                else:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, '')

    def MoveSpeedHackFixLoop1(self):
        chr.SetMoveSpeed(int(player.GetStatus(player.MOVING_SPEED)))
        self.MoveSpeedHackFixLoop2()

    def MoveSpeedHackFixLoop2(self):
        if MoveSpeedHack != '':
            CurrentMoveSpeedHack = self.MoveSpeedStats.GetText()
            chr.SetMoveSpeed(int(CurrentMoveSpeedHack))
            self.MoveSpeedFix = WaitingDialog()
            self.MoveSpeedFix.Open(0.9)
            self.MoveSpeedFix.SAFE_SetTimeOverEvent(self.MoveSpeedHackFixLoop1)

    def ZoomHack(self):
        global ZoomHack
        if ZoomHack == 0:
            ZoomHack = 1
            self.ZoomHackButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.ZoomHackButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.ZoomHackButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.ZoomHackButton.SetToolTipText('Desactivar')
            app.SetCameraMaxDistance(100000)
        else:
            ZoomHack = 0
            self.ZoomHackButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.ZoomHackButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.ZoomHackButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.ZoomHackButton.SetToolTipText('Activar')
            app.SetCameraMaxDistance(2500)

    def NoFog(self):
        global NoFog
        if NoFog == 0:
            NoFog = 1
            self.NoFogButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.NoFogButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.NoFogButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.NoFogButton.SetToolTipText('Desactivar')
            app.SetMinFog(900000)
        else:
            NoFog = 0
            self.NoFogButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.NoFogButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.NoFogButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.NoFogButton.SetToolTipText('Activar')
            app.SetMinFog(2500)

    def DayNight(self):
        global DayNight
        if DayNight == 0:
            DayNight = 1
            self.DayNightButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.DayNightButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.DayNightButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.DayNightButton.SetToolTipText('Desactivar')
            background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
            background.SetEnvironmentData(1)
        else:
            DayNight = 0
            self.DayNightButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.DayNightButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.DayNightButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.DayNightButton.SetToolTipText('Activar')
            background.SetEnvironmentData(0)

    def Pararcam(self):
        global Pararcam
        if Pararcam == 0:
            Pararcam = 1
            self.PararcamButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.PararcamButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.PararcamButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.PararcamButton.SetToolTipText('Desactivar')
            x, y, z = player.GetMainCharacterPosition()
            app.SetCameraSetting(int(x), int(-y), int(z), 3000, 0, 30)
        else:
            Pararcam = 0
            self.PararcamButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.PararcamButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.PararcamButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.PararcamButton.SetToolTipText('Activar')
            app.SetDefaultCamera()

    def EnableSnow(self):
        global EnableSnow
        if EnableSnow == 0:
            EnableSnow = 1
            self.SnowButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.SnowButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.SnowButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.SnowButton.SetToolTipText('Desactivar')
            background.EnableSnow(1)
        else:
            EnableSnow = 0
            self.SnowButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.SnowButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.SnowButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.SnowButton.SetToolTipText('Activar')
            background.EnableSnow(0)

    def AutoRedPot(self):
        global AutoRedPot
        if AutoRedPot == 0:
            AutoRedPot = 1
            self.AutoRedPotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potared_on.tga')
            self.AutoRedPotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potared_on.tga')
            self.AutoRedPotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potared_on.tga')
            self.AutoRedPotButton.SetToolTipText('Desactivar')
            self.EnableRedAutoPotting()
        else:
            AutoRedPot = 0
            self.AutoRedPotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
            self.AutoRedPotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
            self.AutoRedPotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potared_off.tga')
            self.AutoRedPotButton.SetToolTipText('Activar')
            self.DisableRedAutoPotting()

    def EnableRedAutoPotting(self):
        MaxTP = player.GetStatus(player.MAX_HP)
        ActualTP = player.GetStatus(player.HP)
        RedPercentValue = self.EditLineRedPotting.GetText()
        if float(ActualTP) / float(MaxTP) * 100 < int(RedPercentValue):
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                RedPott = player.GetItemIndex(i)
                if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
                    net.SendItemUsePacket(i)
                    break

        self.delay1 = WaitingDialog()
        self.delay1.Open(float(0.1))
        self.delay1.SAFE_SetTimeOverEvent(self.EnableRedAutoPotting)

    def DisableRedAutoPotting(self):
        for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
            RedPott = player.GetItemIndex(i)
            if RedPott == 27001 or RedPott == 27002 or RedPott == 27003:
                net.SendItemUsePacket(i)
                break

        self.delay1 = WaitingDialog()
        self.delay1.Open(int(999999999999999999999))
        self.delay1.SAFE_SetTimeOverEvent(self.DisableRedAutoPotting)

    def AutoBluePot(self):
        global AutoBluePot
        if AutoBluePot == 0:
            AutoBluePot = 1
            self.AutoBluePotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potablue_on.tga')
            self.AutoBluePotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potablue_on.tga')
            self.AutoBluePotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potablue_on.tga')
            self.AutoBluePotButton.SetToolTipText('Desactivar')
            self.EnableBlueAutoPotting()
        else:
            AutoBluePot = 0
            self.AutoBluePotButton.SetUpVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
            self.AutoBluePotButton.SetOverVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
            self.AutoBluePotButton.SetDownVisual('pack\\Botones\\Otros\\Img\\potablue_off.tga')
            self.AutoBluePotButton.SetToolTipText('Activar')
            self.DisableBlueAutoPotting()

    def EnableBlueAutoPotting(self):
        MaxSP = player.GetStatus(player.MAX_SP)
        ActualSP = player.GetStatus(player.SP)
        BluePercentValue = self.EditLineBluePotting.GetText()
        if float(ActualSP) / float(MaxSP) * 100 < int(BluePercentValue):
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                BluePott = player.GetItemIndex(i)
                if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
                    net.SendItemUsePacket(i)
                    break

        self.delay2 = WaitingDialog()
        self.delay2.Open(float(0.1))
        self.delay2.SAFE_SetTimeOverEvent(self.EnableBlueAutoPotting)

    def DisableBlueAutoPotting(self):
        for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
            BluePott = player.GetItemIndex(i)
            if BluePott == 27004 or BluePott == 27005 or BluePott == 27006:
                break

        self.delay2 = WaitingDialog()
        self.delay2.Open(int(999999999999999999999))
        self.delay2.SAFE_SetTimeOverEvent(self.DisableBlueAutoPotting)

    def LevelbotSolucion(self):
        pass

    def LevelbotModo2(self):
        global LevelbotModo2
        global LevelbotModo1
        global LevelbotModo0
        if LevelbotModo0 == 0 and LevelbotModo1 == 0:
            if LevelbotModo2 == 0:
                LevelbotModo2 = 1
                LevelbotModo1 = 0
                LevelbotModo0 = 0
                self.LevelbotModo2Button.SetUpVisual('pack\\Botones\\on_0.tga')
                self.LevelbotModo2Button.SetOverVisual('pack\\Botones\\on_1.tga')
                self.LevelbotModo2Button.SetDownVisual('pack\\Botones\\on_2.tga')
                self.LevelbotModo1Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo1Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo1Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo0Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo0Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo0Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo0Button.SetToolTipText('Activar')
                self.LevelbotModo1Button.SetToolTipText('Activar')
                self.LevelbotModo2Button.SetToolTipText('Desactivar')
                self.ActivarLevelbotModo2()
                self.DesactivarLevelbotModo1()
                self.DesactivarLevelbotModo0()
                self.LevelbotSolucion()
                if Habilidad1V == 1:
                    player.ClickSkillSlot(1)
                if Habilidad2V == 1:
                    player.ClickSkillSlot(2)
                if Habilidad3V == 1:
                    player.ClickSkillSlot(3)
                if Habilidad4V == 1:
                    player.ClickSkillSlot(4)
                if Habilidad5V == 1:
                    player.ClickSkillSlot(5)
                if Habilidad6V == 1:
                    player.ClickSkillSlot(6)
            else:
                LevelbotModo2 = 0
                self.LevelbotModo2Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo2Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo2Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo2Button.SetToolTipText('Activar')
                self.DesactivarLevelbotModo2()
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Primero desactiva los otros tipos de leveo.')

    def ActivarLevelbotModo2(self):
        player.SetAttackKeyState(TRUE)
        self.Levelbotmodo2Tiempo = WaitingDialog()
        self.Levelbotmodo2Tiempo.Open(float(0.1))
        self.Levelbotmodo2Tiempo.SAFE_SetTimeOverEvent(self.ActivarLevelbotModo2)

    def DesactivarLevelbotModo2(self):
        player.SetAttackKeyState(FALSE)
        self.Levelbotmodo2Tiempo = WaitingDialog()
        self.Levelbotmodo2Tiempo.Open(int(99999999999999999))
        self.Levelbotmodo2Tiempo.SAFE_SetTimeOverEvent(self.DesactivarLevelbotModo2)

    def LevelbotModo0(self):
        global LevelbotModo2
        global LevelbotModo1
        global LevelbotModo0
        if LevelbotModo1 == 0 and LevelbotModo2 == 0:
            if LevelbotModo0 == 0:
                LevelbotModo0 = 1
                LevelbotModo1 = 0
                LevelbotModo2 = 0
                self.LevelbotModo0Button.SetUpVisual('pack\\Botones\\on_0.tga')
                self.LevelbotModo0Button.SetOverVisual('pack\\Botones\\on_1.tga')
                self.LevelbotModo0Button.SetDownVisual('pack\\Botones\\on_2.tga')
                self.LevelbotModo1Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo1Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo1Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo2Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo2Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo2Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo2Button.SetToolTipText('Activar')
                self.LevelbotModo1Button.SetToolTipText('Activar')
                self.LevelbotModo0Button.SetToolTipText('Desactivar')
                self.ActivarLevelbotModo0()
                self.DesactivarLevelbotModo1()
                self.DesactivarLevelbotModo2()
                self.LevelbotSolucion()
                if Habilidad1V == 1:
                    player.ClickSkillSlot(1)
                if Habilidad2V == 1:
                    player.ClickSkillSlot(2)
                if Habilidad3V == 1:
                    player.ClickSkillSlot(3)
                if Habilidad4V == 1:
                    player.ClickSkillSlot(4)
                if Habilidad5V == 1:
                    player.ClickSkillSlot(5)
                if Habilidad6V == 1:
                    player.ClickSkillSlot(6)
            else:
                LevelbotModo0 = 0
                self.LevelbotModo0Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo0Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo0Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo0Button.SetToolTipText('Activar')
                self.DesactivarLevelbotModo0()
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Primero desactiva los otros tipos de leveo.')

    def ActivarLevelbotModo0(self):
        DirectionModo0 = app.GetRandom(0, 7)
        player.SetAttackKeyState(TRUE)
        chr.SetDirection(DirectionModo0)
        self.Levelbotmodo0Tiempo = WaitingDialog()
        self.Levelbotmodo0Tiempo.Open(float(0.1))
        self.Levelbotmodo0Tiempo.SAFE_SetTimeOverEvent(self.ActivarLevelbotModo0)

    def DesactivarLevelbotModo0(self):
        player.SetAttackKeyState(FALSE)
        self.Levelbotmodo0Tiempo = WaitingDialog()
        self.Levelbotmodo0Tiempo.Open(int(99999999999999999))
        self.Levelbotmodo0Tiempo.SAFE_SetTimeOverEvent(self.DesactivarLevelbotModo0)

    def LevelbotModo1(self):
        global LevelbotModo2
        global LevelbotModo1
        global LevelbotModo0
        if LevelbotModo0 == 0 and LevelbotModo2 == 0:
            if LevelbotModo1 == 0:
                LevelbotModo1 = 1
                LevelbotModo0 = 0
                LevelbotModo2 = 0
                self.LevelbotModo1Button.SetUpVisual('pack\\Botones\\on_0.tga')
                self.LevelbotModo1Button.SetOverVisual('pack\\Botones\\on_1.tga')
                self.LevelbotModo1Button.SetDownVisual('pack\\Botones\\on_2.tga')
                self.LevelbotModo0Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo0Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo0Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo2Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo2Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo2Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo2Button.SetToolTipText('Activar')
                self.LevelbotModo0Button.SetToolTipText('Activar')
                self.LevelbotModo1Button.SetToolTipText('Desactivar')
                self.ActivarLevelbotModo1()
                self.DesactivarLevelbotModo0()
                self.DesactivarLevelbotModo2()
                self.LevelbotSolucion()
                if Habilidad1V == 1:
                    player.ClickSkillSlot(1)
                if Habilidad2V == 1:
                    player.ClickSkillSlot(2)
                if Habilidad3V == 1:
                    player.ClickSkillSlot(3)
                if Habilidad4V == 1:
                    player.ClickSkillSlot(4)
                if Habilidad5V == 1:
                    player.ClickSkillSlot(5)
                if Habilidad6V == 1:
                    player.ClickSkillSlot(6)
            else:
                LevelbotModo1 = 0
                self.LevelbotModo1Button.SetUpVisual('pack\\Botones\\off_0.tga')
                self.LevelbotModo1Button.SetOverVisual('pack\\Botones\\off_1.tga')
                self.LevelbotModo1Button.SetDownVisual('pack\\Botones\\off_2.tga')
                self.LevelbotModo1Button.SetToolTipText('Activar')
                self.DesactivarLevelbotModo1()
        else:
            chat.AppendChat(chat.CHAT_TYPE_NOTICE, 'Primero desactiva los otros tipos de leveo.')

    def ActivarLevelbotModo1(self):
        DirectionModo1 = app.GetRandom(0, 7)
        player.SetAttackKeyState(TRUE)
        chr.SetDirection(DirectionModo1)
        self.Levelbotmodo1Tiempo = WaitingDialog()
        self.Levelbotmodo1Tiempo.Open(int(1.0))
        self.Levelbotmodo1Tiempo.SAFE_SetTimeOverEvent(self.ActivarLevelbotModo1)

    def DesactivarLevelbotModo1(self):
        player.SetAttackKeyState(FALSE)
        self.Levelbotmodo1Tiempo = WaitingDialog()
        self.Levelbotmodo1Tiempo.Open(int(99999999999999999))
        self.Levelbotmodo1Tiempo.SAFE_SetTimeOverEvent(self.DesactivarLevelbotModo1)

    def AutoPickup(self):
        global AutoPickup
        if AutoPickup == 0:
            AutoPickup = 1
            self.AutoPickupButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.AutoPickupButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.AutoPickupButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.AutoPickupButton.SetToolTipText('Desactivar')
            self.EnableAutoPickup()
        else:
            AutoPickup = 0
            self.AutoPickupButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.AutoPickupButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.AutoPickupButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.AutoPickupButton.SetToolTipText('Activar')
            self.DisableAutoPickup()

    def EnableAutoPickup(self):
        net.SendItemPickUpPacket()
        self.delay4 = WaitingDialog()
        self.delay4.Open(int(0.5))
        self.delay4.SAFE_SetTimeOverEvent(self.EnableAutoPickup)

    def DisableAutoPickup(self):
        player.PickCloseItem()
        self.delay4 = WaitingDialog()
        self.delay4.Open(int(999999999999999999999999999999))
        self.delay4.SAFE_SetTimeOverEvent(self.DisableAutoPickup)

    def AutoRestart(self):
        global AutoRestart
        if AutoRestart == 0:
            AutoRestart = 1
            self.AutoRestartButton.SetUpVisual('pack\\Botones\\on_0.tga')
            self.AutoRestartButton.SetOverVisual('pack\\Botones\\on_1.tga')
            self.AutoRestartButton.SetDownVisual('pack\\Botones\\on_2.tga')
            self.AutoRestartButton.SetToolTipText('Desactivar')
            self.EnableRestart()
        else:
            AutoRestart = 0
            self.AutoRestartButton.SetUpVisual('pack\\Botones\\off_0.tga')
            self.AutoRestartButton.SetOverVisual('pack\\Botones\\off_1.tga')
            self.AutoRestartButton.SetDownVisual('pack\\Botones\\off_2.tga')
            self.AutoRestartButton.SetToolTipText('Activar')
            self.DisableRestart()

    def EnableRestart(self):
        net.SendChatPacket('/restart_here')
        self.delay5 = WaitingDialog()
        self.delay5.Open(int(2.5))
        self.delay5.SAFE_SetTimeOverEvent(self.EnableRestart)


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
        return


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
StartDialog.Hide()