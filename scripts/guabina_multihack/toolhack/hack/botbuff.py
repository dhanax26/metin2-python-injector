global Mobber_ID, Poty, Poty_1_ID, Poty_1_Icon, Poty_2_ID, Poty_2_Icon, Otwieraczx, Otwieracz_ID, Otwieracz_ID1, Otwieracz_ID2, Otwieracz_ID3, Otwieracz_ID4, Otwieracz_ID5, Dopalaczx, Dopalacz_ID1, Dopalacz_ID2, Dopalacz_ID3, Dopalacz_ID4, Dopalacz_ID5, Dopalacz_ID6, Dopalacz_ID7, Dopalacz_ID8, Dopalacz_ID9, Dopalacz_ID10, Dopalacz_ID11, Dopalacz_ID12, Dopalacz_ID13, Dopalacz_ID14, Dopalacz_ID15, Dopalacz_ID16, Dopalacz_ID17, Dopalacz_ID18, Dopalacz_ID19, Dopalacz_ID20, Dopalacz_ID21, Dopalacz_ID22, Dopalacz_ID23, Dopalacz_ID24, Dopalacz_ID25, Dopalacz_ID26, Dopalacz_ID27, Dopalacz_ID28, SlotUlepszania, telestep, teleport_mode
exec 'import sys'
# import app
b = sys.modules.keys()
for i in range(len(b)):
    h = b[i]
    r = 0
    for g in range(len(h)):
        if h[g] != '.':
            r = r + 1
            if r == len(h):
                a = dir(__import__(b[i]))
                for y in range(len(a)):
                    if a[y] == 'GetMainCharacterIndex':
                        playerm = b[i]
                    
                    if a[y] == 'GetNameByVID':
                        chrm = b[i]
                    
                    if a[y] == 'SendChatPacket':
                        netm = b[i]
                    
                
            
        
    

huj = 'import '
exec huj + chrm + ' as chr'

try:
    import playerm2g2 as player
    chr.GetPixelPosition = player.GetMainCharacterPosition
except:
    exec huj + playerm + ' as player'


try:
    import m2netm2g as net
except:
    exec huj + netm + ' as net'

import ui
import dbg
import app
import wndMgr
import chat
import chr
import time
import background
import os
import chrmgr
import item
import textTail
import shop
import mouseModule
import grp
import uiToolTip
import nonplayer
import systemSetting
import constInfo
from uitooltip import ItemToolTip
Mobber_ID = 0
Poty = 0
Poty_1_ID = 0
Poty_1_Icon = 0
Poty_2_ID = 0
Poty_2_Icon = 0
Otwieraczx = 0
Otwieracz_ID = 0
Otwieracz_ID1 = 0
Otwieracz_ID2 = 0
Otwieracz_ID3 = 0
Otwieracz_ID4 = 0
Otwieracz_ID5 = 0
Dopalaczx = 0
Dopalacz_ID1 = 0
Dopalacz_ID2 = 0
Dopalacz_ID3 = 0
Dopalacz_ID4 = 0
Dopalacz_ID5 = 0
Dopalacz_ID6 = 0
Dopalacz_ID7 = 0
Dopalacz_ID8 = 0
Dopalacz_ID9 = 0
Dopalacz_ID10 = 0
Dopalacz_ID11 = 0
Dopalacz_ID12 = 0
Dopalacz_ID13 = 0
Dopalacz_ID14 = 0
Dopalacz_ID15 = 0
Dopalacz_ID16 = 0
Dopalacz_ID17 = 0
Dopalacz_ID18 = 0
Dopalacz_ID19 = 0
Dopalacz_ID20 = 0
Dopalacz_ID21 = 0
Dopalacz_ID22 = 0
Dopalacz_ID23 = 0
Dopalacz_ID24 = 0
Dopalacz_ID25 = 0
Dopalacz_ID26 = 0
Dopalacz_ID27 = 0
Dopalacz_ID28 = 0
SlotUlepszania = 0
kostiumidx = 0
telestep = 0
teleport_mode = 0
Spambotp1 = [
    '|cffFFFFFF|H|hNormal',
    '|cffff0000|H|hCzerwony',
    '|cff00FF00|H|hZielony',
    '|cffFFFF00|H|hZolty',
    '|cffFF1493|H|hRozowy',
    '|cff800000|H|hBrazowy',
    '|cffffcc00|H|hZloty',
    '|cff800080|H|hFiolotowy',
    '|cff0000FF|H|hNiebieski',
    '|cff00FFFF|H|hBlekitny']
bosy = (192, 193, 191, 194, 394, 591, 534, 533, 691, 2191, 1901, 791, 1304, 2307, 2206, 2091)

class Dialog1(ui.Window):
    
    def __init__(self):
        ui.Window.__init__(self)
        self.BuildWindow()

    
    def __del__(self):
        ui.Window.__del__(self)

    
    def BuildWindow(self):
        self.Board1 = ui.Bar()
        self.Board1.SetSize(320, 230)
        self.Board1.SetCenterPosition()
        self.Board1.AddFlag('movable')
        self.Board1.AddFlag('float')
        self.Board1.SetColor(grp.GenerateColor(0.0, 0.0, 0.0, 0.0))
        self.Board1.Show()
        self.Boarddod = ui.Board()
        self.Boarddod.SetParent(self.Board1)
        self.Boarddod.SetSize(120, 205)
        self.Boarddod.SetPosition(200, 20)
        self.Boarddod.Show()
        self.Board = ui.BoardWithTitleBar()
        self.Board.SetParent(self.Board1)
        self.Board.SetSize(210, 235)
        self.Board.SetPosition(0, 0)
        self.Board.SetTitleName('Eternal 1337 by dhanax26')
        self.Board.SetCloseEvent(self.Close)
        self.Board.Show()
        self.WykrywaczOkno = ui.BoardWithTitleBar()
        self.WykrywaczOkno.SetSize(220, 210)
        self.WykrywaczOkno.SetCenterPosition()
        self.WykrywaczOkno.AddFlag('movable')
        self.WykrywaczOkno.AddFlag('float')
        self.WykrywaczOkno.SetTitleName('Metin Detector')
        self.WykrywaczOkno.SetCloseEvent(self.CloseWykr)
        self.WykrywaczOkno.Hide()
        self.DopalaczeOknoBoard = ui.BoardWithTitleBar()
        self.DopalaczeOknoBoard.SetSize(280, 245)
        self.DopalaczeOknoBoard.SetCenterPosition()
        self.DopalaczeOknoBoard.AddFlag('movable')
        self.DopalaczeOknoBoard.AddFlag('float')
        self.DopalaczeOknoBoard.SetTitleName('Almejas')
        self.DopalaczeOknoBoard.SetCloseEvent(self.CloseDopy)
        self.DopalaczeOknoBoard.Hide()
        self.Spambotboard = ui.BoardWithTitleBar()
        self.Spambotboard.SetSize(437, 208)
        self.Spambotboard.SetCenterPosition()
        self.Spambotboard.AddFlag('movable')
        self.Spambotboard.AddFlag('float')
        self.Spambotboard.SetTitleName('Spambot')
        self.Spambotboard.SetCloseEvent(self.Spambotclose)
        self.Spambotboard.Hide()
        self.Ustawieniao = ui.BoardWithTitleBar()
        self.Ustawieniao.SetSize(500, 230)
        self.Ustawieniao.SetCenterPosition()
        self.Ustawieniao.AddFlag('movable')
        self.Ustawieniao.AddFlag('float')
        self.Ustawieniao.SetTitleName('Ajustes')
        self.Ustawieniao.SetCloseEvent(self.Ustawieniaoclose)
        self.Ustawieniao.Hide()
        self.Typstr = ui.BoardWithTitleBar()
        self.Typstr.SetSize(150, 250)
        self.Typstr.SetCenterPosition()
        self.Typstr.AddFlag('movable')
        self.Typstr.AddFlag('float')
        self.Typstr.SetTitleName('Tipo de Golpes')
        self.Typstr.SetCloseEvent(self.Typstrclose)
        self.Typstr.Hide()
        self.UlepszBoard = ui.BoardWithTitleBar()
        self.UlepszBoard.SetSize(175, 146)
        self.UlepszBoard.SetCenterPosition()
        self.UlepszBoard.AddFlag('movable')
        self.UlepszBoard.AddFlag('float')
        self.UlepszBoard.SetTitleName('Subir Objetos')
        self.UlepszBoard.SetCloseEvent(self.CloseUlepsz)
        self.UlepszBoard.Hide()
        self.Pogoda = ui.BoardWithTitleBar()
        self.Pogoda.SetSize(120, 190)
        self.Pogoda.SetCenterPosition()
        self.Pogoda.AddFlag('movable')
        self.Pogoda.AddFlag('float')
        self.Pogoda.SetTitleName('Tiempo')
        self.Pogoda.SetCloseEvent(self.ClosePogoda)
        self.Pogoda.Hide()
        self.WizualnyBoard = ui.BoardWithTitleBar()
        self.WizualnyBoard.SetSize(439, 308)
        self.WizualnyBoard.SetCenterPosition()
        self.WizualnyBoard.AddFlag('movable')
        self.WizualnyBoard.AddFlag('float')
        self.WizualnyBoard.SetTitleName('Cambio Visual')
        self.WizualnyBoard.SetCloseEvent(self.CloseWizualnyBoard)
        self.WizualnyBoard.Hide()
        self.AutoSkileBoard = ui.BoardWithTitleBar()
        self.AutoSkileBoard.SetSize(260, 270)
        self.AutoSkileBoard.SetCenterPosition()
        self.AutoSkileBoard.AddFlag('movable')
        self.AutoSkileBoard.AddFlag('float')
        self.AutoSkileBoard.SetTitleName('Bot de Habilidades')
        self.AutoSkileBoard.SetCloseEvent(self.AutoSkileClose)
        self.AutoSkileBoard.Hide()
        self._Dialog1__BuildKeyDict()
        self.comp = Component()
        self.Poty = ui.ToggleButton()
        self.Poty.SetParent(self.Board)
        self.Poty.SetPosition(110, 55)
        self.Poty.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        self.Poty.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        self.Poty.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        self.Poty.SetToggleDownEvent(ui.__mem_func__(self.Potyfunc))
        self.Poty.SetToggleUpEvent(ui.__mem_func__(self.Potyfunc))
        self.Poty.SetText('Auto Potas')
        self.Poty.Show()
        self.Spambotp = self.comp.ComboBox(self.Spambotboard, 'Color', 20, 160, 70)
        for Spambotp in Spambotp1:
            self.Spambotp.InsertItem(1, str(Spambotp))
        
        self.Zoom = self.comp.Button(self.Pogoda, 'Zoom', '', 15, 80, self.Zoom_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Dzien = self.comp.Button(self.Pogoda, 'Dia', '', 15, 30, self.Dzien_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ghost = self.comp.Button(self.Pogoda, 'Fantasma', '', 15, 130, self.Ghost_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Noc = self.comp.Button(self.Pogoda, 'Noche', '', 15, 55, self.Noc_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Gora = self.comp.Button(self.Board, 'Arriba', '', 134, 135, self.Gora_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.Lewo = self.comp.Button(self.Board, 'Izquierda', '', 113, 155, self.Lewo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.Prawo = self.comp.Button(self.Board, 'Derecha', '', 155, 155, self.Prawo_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.Dol = self.comp.Button(self.Board, 'Abajo', '', 134, 175, self.Dol_func, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.WykrywaczMetinow = self.comp.Button(self.Boarddod, 'Jefes', '', 15, 30, self.WykrywaczMetinow_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Dopalaczestr = self.comp.Button(self.Boarddod, 'Abre Almejas', '', 15, 50, self.Dopalaczestr_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Spambot = self.comp.Button(self.Boarddod, 'Spam Bot', '', 15, 70, self.Spambot_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ustawienia = self.comp.Button(self.Boarddod, 'Ajustes', '', 15, 90, self.Ustawienia_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypBicia = self.comp.Button(self.Boarddod, 'Tipo de Golpes', '', 15, 110, self.TypBicia_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ulepszanie = self.comp.Button(self.Boarddod, 'Subir Objetos', '', 15, 130, self.Ulepszanie_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Pogodastr = self.comp.Button(self.Boarddod, 'Tiempo', '', 15, 150, self.Pogoda_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Wizualniestr = self.comp.Button(self.Boarddod, 'Cambio Visual', '', 15, 170, self.Wizual_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.AutoSkilestr = self.comp.Button(self.Boarddod, 'Auto Hab', '', 15, 10, self.Autoskile_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Tpdokordow = self.comp.Button(self.Board, 'Teletrasportar', '', 15, 200, self.Tpdokordow_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zamknijgre = self.comp.Button(self.Board, 'Cerrar Juego', '', 110, 200, self.Zamknijgre_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.AutoAtak = self.comp.ToggleButton(self.Board, 'Auto Atacar', '', 15, 30, lambda arg = 'off': self.AutoAtak_func(arg), lambda arg = 'on': self.AutoAtak_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Pickup = self.comp.ToggleButton(self.Board, 'Recoger Cosas', '', 15, 55, lambda arg = 'off': self.Pickup_func(arg), lambda arg = 'on': self.Pickup_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Mobberek = self.comp.ToggleButton(self.Board, 'Cabos', '', 110, 30, lambda arg = 'off': self.Mobber_func(arg), lambda arg = 'on': self.Mobber_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Dopalacze = self.comp.ToggleButton(self.Board, 'Almejas', '', 15, 80, lambda arg = 'off': self.Dopalacze_func(arg), lambda arg = 'on': self.Dopalacze_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Snieg = self.comp.ToggleButton(self.Pogoda, 'Nieve', '', 15, 105, lambda arg = 'off': self.Snieg_func(arg), lambda arg = 'on': self.Snieg_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Kamera = self.comp.ToggleButton(self.Pogoda, 'Parar camara', '', 15, 155, lambda arg = 'off': self.Kamera_func(arg), lambda arg = 'on': self.Kamera_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Combo = self.comp.ToggleButton(self.Board, 'Combo', '', 15, 105, lambda arg = 'off': self.Combo_func(arg), lambda arg = 'on': self.Combo_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Otwieracz = self.comp.ToggleButton(self.Board, 'Activar Rocios', '', 110, 105, lambda arg = 'off': self.Otwieracz_func(arg), lambda arg = 'on': self.Otwieracz_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.AutoWstawanie = self.comp.ToggleButton(self.Board, 'Auto Revivir', '', 110, 80, lambda arg = 'off': self.AutoWstawanie_func(arg), lambda arg = 'on': self.AutoWstawanie_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.WykrywaczGM = self.comp.ToggleButton(self.Board, 'Detector GM', '', 15, 130, lambda arg = 'off': self.WykrywaczGM_func(arg), lambda arg = 'on': self.WykrywaczGM_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        (self.slotbar_Xin, self.Xin) = self.comp.EditLine(self.Board, '', 62, 156, 30, 15, 4)
        (self.slotbar_Yin, self.Yin) = self.comp.EditLine(self.Board, '', 62, 177, 30, 15, 4)
        self.Podajx = self.comp.TextLine(self.Board, 'Ir a:', 15, 157, self.comp.RGB(255, 255, 0))
        self.Podajy = self.comp.TextLine(self.Board, 'Ir a x:', 15, 177, self.comp.RGB(255, 255, 0))
        self.SzukajMetinow = self.comp.ToggleButton(self.WykrywaczOkno, 'Caminar al Metin', '', 15, 159, lambda arg = 'off': self.SzukajMetinow_func(arg), lambda arg = 'on': self.SzukajMetinow_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Tpdometina = self.comp.ToggleButton(self.WykrywaczOkno, 'Teletrasportar al Metin', '', 15, 178, lambda arg = 'off': self.Tpdometina_func(arg), lambda arg = 'on': self.Tpdometina_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.SzukajBossow = self.comp.ToggleButton(self.WykrywaczOkno, 'Caminar al Jefe', '', 115, 159, lambda arg = 'off': self.SzukajBossow_func(arg), lambda arg = 'on': self.SzukajBossow_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TpdoBossa = self.comp.ToggleButton(self.WykrywaczOkno, 'Teletrasportar al Jefe', '', 115, 178, lambda arg = 'off': self.TpdoBossa_func(arg), lambda arg = 'on': self.TpdoBossa_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Nazwabossa = self.comp.TextLine(self.WykrywaczOkno, 'Nombre del Jefe:', 19, 41, self.comp.RGB(255, 255, 0))
        self.Pozycjabossax = self.comp.TextLine(self.WykrywaczOkno, 'Posicion del Jefe:', 18, 59, self.comp.RGB(255, 255, 0))
        self.Pozycjabossay = self.comp.TextLine(self.WykrywaczOkno, 'Posicion del Jefe2:', 18, 77, self.comp.RGB(255, 255, 0))
        self.Nazwametina = self.comp.TextLine(self.WykrywaczOkno, 'Nombre del Metin:', 19, 105, self.comp.RGB(255, 255, 0))
        self.Pozycjametinax = self.comp.TextLine(self.WykrywaczOkno, 'Posicion del Metin:', 18, 123, self.comp.RGB(255, 255, 0))
        self.Pozycjametinay = self.comp.TextLine(self.WykrywaczOkno, 'Posicion del Metin2:', 18, 141, self.comp.RGB(255, 255, 0))
        self.dsds = self.comp.ThinBoard(self.DopalaczeOknoBoard, FALSE, 10, 33, 260, 160, FALSE)
        self.usundopybtn = self.comp.Button(self.DopalaczeOknoBoard, ' ', '', 157, 217, self.usundopy, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        (self.slotbar_Coiledopyin, self.Coiledopyin) = self.comp.EditLine(self.DopalaczeOknoBoard, '10', 209, 198, 25, 15, 3)
        self.Coiledopy = self.comp.TextLine(self.DopalaczeOknoBoard, 'Cada cuantos minutos', 12, 198, self.comp.RGB(0, 255, 0))
        self.usundopytxt = self.comp.TextLine(self.DopalaczeOknoBoard, 'Usar Rocios o Almejas.', 12, 215, self.comp.RGB(0, 255, 0))
        self.Tyl = self.comp.ThinBoard(self.Spambotboard, FALSE, 13, 32, 410, 109, FALSE)
        self.Spambtn = self.comp.ToggleButton(self.Spambotboard, 'Normal', '', 190, 158, lambda arg = 'off': self.Spambtn_func(arg), lambda arg = 'on': self.Spambtn_func(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Spambtn1 = self.comp.ToggleButton(self.Spambotboard, 'Llamar', '', 96, 158, lambda arg = 'off': self.Spambtn_func1(arg), lambda arg = 'on': self.Spambtn_func1(arg), 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        (self.slotbar_Tekstin, self.Tekstin) = self.comp.EditLine(self.Spambotboard, 'Escribe un texto...', 25, 45, 385, 75, 37500)
        (self.slotbar_Coilespamtxtin, self.Coilespamtxtin) = self.comp.EditLine(self.Spambotboard, '15', 359, 160, 25, 15, 3)
        self.Coilespambotin = self.comp.TextLine(self.Spambotboard, 'Cada cuanto enviar (s)?', 292, 160, self.comp.RGB(0, 255, 255))
        self.tylmobber = self.comp.ThinBoard(self.Ustawieniao, FALSE, 35, 55, 70, 70, FALSE)
        self.tylpotki = self.comp.ThinBoard(self.Ustawieniao, FALSE, 180, 55, 90, 70, FALSE)
        self.tylotwiwracz = self.comp.ThinBoard(self.Ustawieniao, FALSE, 320, 55, 160, 100, FALSE)
        (self.slotbar_Potyhpczas, self.Potyhpczas) = self.comp.EditLine(self.Ustawieniao, '90', 215, 150, 20, 15, 2)
        (self.slotbar_Potympczas, self.Potympczas) = self.comp.EditLine(self.Ustawieniao, '90', 215, 190, 20, 15, 2)
        (self.slotbar_Peleczas, self.Peleczas) = self.comp.EditLine(self.Ustawieniao, '5', 57.5, 145, 25, 15, 3)
        (self.slotbar_Dopyczas, self.Dopyczas) = self.comp.EditLine(self.Ustawieniao, '0.1', 385, 180, 30, 15, 4)
        self.coilepele = self.comp.TextLine(self.Ustawieniao, 'Cada cuanto usar  (s)', 25, 130, self.comp.RGB(56, 142, 48))
        self.coilepelezepele = self.comp.TextLine(self.Ustawieniao, 'Cabos', 50, 35, self.comp.RGB(255, 255, 255))
        self.coiledopy1 = self.comp.TextLine(self.Ustawieniao, 'Cada cuanto activar (s)', 355, 160, self.comp.RGB(56, 142, 48))
        self.coiledopy1zedopy = self.comp.TextLine(self.Ustawieniao, 'Rocios y Otros', 370, 35, self.comp.RGB(255, 255, 255))
        self.odilepotympzepoty = self.comp.TextLine(self.Ustawieniao, 'Pociones', 210, 35, self.comp.RGB(255, 255, 255))
        self.odilepotymp = self.comp.TextLine(self.Ustawieniao, 'Cada cuanto % de tu HP usar una Pota Azul', 155, 170, self.comp.RGB(0, 0, 255))
        self.odilepotyhp = self.comp.TextLine(self.Ustawieniao, 'Cada cuanto % de tu HP usar una Pota Roja', 155, 130, self.comp.RGB(255, 0, 0))
        self.TypJednor = self.comp.Button(self.Typstr, 'Espada', '', 30, 35, self.TypJednor_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypDwu = self.comp.Button(self.Typstr, 'Lanza', '', 30, 60, self.TypDwu_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypSztylety = self.comp.Button(self.Typstr, 'Dagas', '', 30, 85, self.TypSztylety_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypLuk = self.comp.Button(self.Typstr, 'Flechas', '', 30, 110, self.TypLuk_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypDzwon = self.comp.Button(self.Typstr, 'Campana', '', 30, 135, self.TypDzwon_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypWachlarz = self.comp.Button(self.Typstr, 'Fan', '', 30, 160, self.TypWachlarz_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypWedka = self.comp.Button(self.Typstr, 'Ca\xf1a', '', 30, 185, self.TypWedka_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.TypPiesc = self.comp.Button(self.Typstr, 'Pu\xf1os', '', 30, 210, self.TypPiesc_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ulepsz = self.comp.Button(self.UlepszBoard, 'Subir', '', 65, 80, self.Ulepsz_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        (self.slotbar_Oileulepszycin, self.Oileulepszycin) = self.comp.EditLine(self.UlepszBoard, '9', 145, 45, 15, 15, 1)
        self.Oiletxt = self.comp.TextLine(self.UlepszBoard, 'Subir a +:', 65, 45, self.comp.RGB(0, 650, 650))
        self.Zmienlv = self.comp.Button(self.WizualnyBoard, 'Subir Nivel', '', 15, 82, self.Zmienlv_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zmienzbr = self.comp.Button(self.WizualnyBoard, 'Cambiar Armor', '', 15, 104, self.Zmienzbr_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zmienbrn = self.comp.Button(self.WizualnyBoard, 'Cambiar Arma', '', 15, 126, self.Zmienbrn_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Sprawdz = self.comp.Button(self.WizualnyBoard, 'Comprobar', '', 10, 270, self.Sprawdz_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Aura = self.comp.Button(self.WizualnyBoard, 'Usar Aura', '', 230, 60, self.Aura_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ostrze = self.comp.Button(self.WizualnyBoard, 'Usar Hoja', '', 230, 82, self.Ostrze_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Strach = self.comp.Button(self.WizualnyBoard, 'Usar Miedo', '', 230, 104, self.Strach_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zbroja = self.comp.Button(self.WizualnyBoard, 'Usar Armadura', '', 230, 126, self.Zbroja_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Blogo = self.comp.Button(self.WizualnyBoard, 'Usar Bendicion', '', 230, 148, self.Blogo_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Pomoc = self.comp.Button(self.WizualnyBoard, 'Usar Proteccion', '', 330, 60, self.Pomoc_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Odbicie = self.comp.Button(self.WizualnyBoard, 'Usar Disipar', '', 330, 82, self.Odbicie_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zwiekszenie = self.comp.Button(self.WizualnyBoard, 'Usar ...', '', 330, 192, self.Zwiekszenie_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Silne = self.comp.Button(self.WizualnyBoard, 'Usar Cuerpo', '', 330, 126, self.Silne_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Ochronka = self.comp.Button(self.WizualnyBoard, 'Usar Criticos', '', 230, 170, self.Ochronka_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Duch = self.comp.Button(self.WizualnyBoard, 'Usar Llama', '', 330, 148, self.Duch_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Krycie = self.comp.Button(self.WizualnyBoard, 'Usar Opacidad', '', 330, 170, self.Krycie_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Rozpro = self.comp.Button(self.WizualnyBoard, 'Usar Miedo', '', 230, 192, self.Rozpro_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Trucie = self.comp.Button(self.WizualnyBoard, 'Usar Veneno', '', 330, 104, self.Trucie_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Powstan = self.comp.Button(self.WizualnyBoard, 'Revivir', '', 330, 214, self.Powstan_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Zgin = self.comp.Button(self.WizualnyBoard, 'Matarse', '', 230, 214, self.Zgin_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.Nick = self.comp.Button(self.WizualnyBoard, 'Cambiar Nick', '', 15, 60, self.Nick_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.GM = self.comp.Button(self.WizualnyBoard, 'Signo de GM', '', 14, 148, self.GM_funcw, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        (self.slotbar_Nickin, self.Nickin) = self.comp.EditLine(self.WizualnyBoard, 'this is a test!', 105, 61, 110, 15, 20)
        (self.slotbar_Lvlin, self.Lvlin) = self.comp.EditLine(self.WizualnyBoard, '99', 105, 83, 30, 15, 4)
        (self.slotbar_Bronin, self.Bronin) = self.comp.EditLine(self.WizualnyBoard, '189', 105, 129, 40, 15, 6)
        (self.slotbar_Zbrin, self.Zbrin) = self.comp.EditLine(self.WizualnyBoard, '11971', 105, 106, 40, 15, 6)
        self.Zmianainfo = self.comp.TextLine(self.WizualnyBoard, '~Esto es cambio visual solo tu puedes verlo~', 85, 35, self.comp.RGB(255, 0, 255))
        self.Zmianainfo1 = self.comp.TextLine(self.WizualnyBoard, 'Armadura', 15, 166, self.comp.RGB(255, 0, 255))
        self.Zmianainfo2 = self.comp.TextLine(self.WizualnyBoard, 'Arma', 65, 166, self.comp.RGB(255, 0, 255))
        self.ZbrImg = self.comp.ExpandedImage(self.WizualnyBoard, 15, 180, '')
        self.BronImg = self.comp.ExpandedImage(self.WizualnyBoard, 60, 180, '')
        self.WojM = self.comp.Button(self.WizualnyBoard, 'War M', '', 105, 148, self.WojM_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.WojK = self.comp.Button(self.WizualnyBoard, 'War F', '', 165, 148, self.WojK_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.SuraK = self.comp.Button(self.WizualnyBoard, 'Sura F', '', 165, 170, self.SuraK_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.SuraM = self.comp.Button(self.WizualnyBoard, 'Sura M', '', 105, 170, self.SuraM_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.NinjaM = self.comp.Button(self.WizualnyBoard, 'Ninja M', '', 105, 192, self.NinjaM_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.NinjaK = self.comp.Button(self.WizualnyBoard, 'Ninja F', '', 165, 192, self.NinjaK_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.SzamanK = self.comp.Button(self.WizualnyBoard, 'Chaman F', '', 165, 214, self.SzamanK_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.SzamanM = self.comp.Button(self.WizualnyBoard, 'Chaman M', '', 105, 214, self.SzamanM_func, 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.UstawRace = self.comp.Button(self.WizualnyBoard, 'Juego de Carreras', '', 340, 276, self.UstawRace_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        self.SprawdzRace = self.comp.Button(self.WizualnyBoard, 'Control de la Raza', '', 340, 250, self.SprawdzRace_func, 'd:/ymir work/ui/public/large_button_01.sub', 'd:/ymir work/ui/public/large_button_02.sub', 'd:/ymir work/ui/public/large_button_03.sub')
        (self.slotbar_Racein, self.Racein) = self.comp.EditLine(self.WizualnyBoard, '20016', 276, 276, 60, 15, 10)
        self.Sprawdztxt = self.comp.TextLine(self.WizualnyBoard, '', 115, 250, self.comp.RGB(650, 255, 650))
        self.Podajracetxt = self.comp.TextLine(self.WizualnyBoard, ':', 205, 276, self.comp.RGB(650, 255, 650))
        self.Racer = self.comp.TextLine(self.WizualnyBoard, ':', 115, 276, self.comp.RGB(650, 255, 650))
        self.Aurax = self.comp.ToggleButton(self.AutoSkileBoard, 'Aura', '', 60, 85, lambda arg = 'off': self.Aura_func(arg), lambda arg = 'on': self.Aura_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Berekx = self.comp.ToggleButton(self.AutoSkileBoard, 'Bersek', '', 122, 85, lambda arg = 'off': self.Berek_func(arg), lambda arg = 'on': self.Berek_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Silnex = self.comp.ToggleButton(self.AutoSkileBoard, 'Cuerpo', '', 60, 115, lambda arg = 'off': self.Silne_func(arg), lambda arg = 'on': self.Silne_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Ostrzex = self.comp.ToggleButton(self.AutoSkileBoard, 'Hoja', '', 60, 145, lambda arg = 'off': self.Ostrze_func(arg), lambda arg = 'on': self.Ostrze_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Strachx = self.comp.ToggleButton(self.AutoSkileBoard, 'Miedo', '', 122, 145, lambda arg = 'off': self.Strach_func(arg), lambda arg = 'on': self.Strach_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Zbrojax = self.comp.ToggleButton(self.AutoSkileBoard, 'Armadura', '', 182, 145, lambda arg = 'off': self.Zbroja_func(arg), lambda arg = 'on': self.Zbroja_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Ochronkax = self.comp.ToggleButton(self.AutoSkileBoard, 'Proteccion', '', 60, 175, lambda arg = 'off': self.Ochronka_func(arg), lambda arg = 'on': self.Ochronka_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Duchx = self.comp.ToggleButton(self.AutoSkileBoard, 'Espiritu', '', 122, 175, lambda arg = 'off': self.Duch_func(arg), lambda arg = 'on': self.Duch_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Atakx = self.comp.ToggleButton(self.AutoSkileBoard, 'Ataque', '', 60, 205, lambda arg = 'off': self.Atak_func(arg), lambda arg = 'on': self.Atak_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Zwinnoscx = self.comp.ToggleButton(self.AutoSkileBoard, 'Curacion', '', 122, 205, lambda arg = 'off': self.Zwinnosc_func(arg), lambda arg = 'on': self.Zwinnosc_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Blogox = self.comp.ToggleButton(self.AutoSkileBoard, 'Dragon', '', 60, 235, lambda arg = 'off': self.Blogo_func(arg), lambda arg = 'on': self.Blogo_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Pomocx = self.comp.ToggleButton(self.AutoSkileBoard, 'Reflectar', '', 122, 235, lambda arg = 'off': self.Pomoc_func(arg), lambda arg = 'on': self.Pomoc_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        self.Odbiciex = self.comp.ToggleButton(self.AutoSkileBoard, 'Bendicion', '', 182, 235, lambda arg = 'off': self.Odbicie_func(arg), lambda arg = 'on': self.Odbicie_func(arg), 'd:/ymir work/ui/public/middle_button_01.sub', 'd:/ymir work/ui/public/middle_button_02.sub', 'd:/ymir work/ui/public/middle_button_03.sub')
        (self.slotbar_Skill1czas, self.Skill1czas) = self.comp.EditLine(self.AutoSkileBoard, '120', 92, 60, 25, 15, 3)
        (self.slotbar_Skill2czas, self.Skill2czas) = self.comp.EditLine(self.AutoSkileBoard, '83', 152, 60, 25, 15, 3)
        (self.slotbar_Skill3czas, self.Skill3czas) = self.comp.EditLine(self.AutoSkileBoard, '45', 212, 60, 25, 15, 3)
        self.coileskile = self.comp.TextLine(self.AutoSkileBoard, 'Usar Habilidads cada:', 100, 40, self.comp.RGB(158, 62, 114))
        self.Skill1 = self.comp.TextLine(self.AutoSkileBoard, 'Hab 1', 60, 60, self.comp.RGB(158, 255, 114))
        self.Skill2 = self.comp.TextLine(self.AutoSkileBoard, 'Hab 2', 120, 60, self.comp.RGB(0, 102, 255))
        self.Skill3 = self.comp.TextLine(self.AutoSkileBoard, 'Hab 3', 180, 60, self.comp.RGB(190, 33, 255))
        self.Body = self.comp.TextLine(self.AutoSkileBoard, 'Corporal', 15, 85, self.comp.RGB(142, 0, 64))
        self.mental = self.comp.TextLine(self.AutoSkileBoard, 'Mental', 15, 115, self.comp.RGB(142, 0, 64))
        self.WP = self.comp.TextLine(self.AutoSkileBoard, 'Espejo', 15, 145, self.comp.RGB(142, 0, 64))
        self.BM = self.comp.TextLine(self.AutoSkileBoard, 'Magia Negra', 15, 175, self.comp.RGB(142, 0, 64))
        self.Healer = self.comp.TextLine(self.AutoSkileBoard, 'Curador', 15, 205, self.comp.RGB(142, 0, 64))
        self.Smok = self.comp.TextLine(self.AutoSkileBoard, 'Dragon', 15, 235, self.comp.RGB(142, 0, 64))
        self.DopalaczSlot1 = ui.ExpandedImageBox()
        self.DopalaczSlot1.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot1.SetPosition(20, 40)
        self.DopalaczSlot1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot1.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc1()
        self.DopalaczSlot1.Show()
        self.DopalaczSlotIcon1 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon1.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon1.SetPosition(20, 40)
        self.DopalaczSlotIcon1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon1.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc1()
        self.DopalaczSlotIcon1.Show()
        self.DopalaczSlot2 = ui.ExpandedImageBox()
        self.DopalaczSlot2.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot2.SetPosition(55, 40)
        self.DopalaczSlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot2.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc2()
        self.DopalaczSlot2.Show()
        self.DopalaczSlotIcon2 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon2.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon2.SetPosition(55, 40)
        self.DopalaczSlotIcon2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon2.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc2()
        self.DopalaczSlotIcon2.Show()
        self.DopalaczSlot3 = ui.ExpandedImageBox()
        self.DopalaczSlot3.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot3.SetPosition(90, 40)
        self.DopalaczSlot3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot3.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc3()
        self.DopalaczSlot3.Show()
        self.DopalaczSlotIcon3 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon3.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon3.SetPosition(90, 40)
        self.DopalaczSlotIcon3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon3.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc3()
        self.DopalaczSlotIcon3.Show()
        self.DopalaczSlot4 = ui.ExpandedImageBox()
        self.DopalaczSlot4.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot4.SetPosition(125, 40)
        self.DopalaczSlot4.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot4.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc4()
        self.DopalaczSlot4.Show()
        self.DopalaczSlotIcon4 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon4.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon4.SetPosition(125, 40)
        self.DopalaczSlotIcon4.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon4.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc4()
        self.DopalaczSlotIcon4.Show()
        self.DopalaczSlot5 = ui.ExpandedImageBox()
        self.DopalaczSlot5.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot5.SetPosition(160, 40)
        self.DopalaczSlot5.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot5.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc5()
        self.DopalaczSlot5.Show()
        self.DopalaczSlotIcon5 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon5.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon5.SetPosition(160, 40)
        self.DopalaczSlotIcon5.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon5.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc5()
        self.DopalaczSlotIcon5.Show()
        self.DopalaczSlot6 = ui.ExpandedImageBox()
        self.DopalaczSlot6.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot6.SetPosition(195, 40)
        self.DopalaczSlot6.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot6.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc6()
        self.DopalaczSlot6.Show()
        self.DopalaczSlotIcon6 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon6.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon6.SetPosition(195, 40)
        self.DopalaczSlotIcon6.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon6.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc6()
        self.DopalaczSlotIcon6.Show()
        self.DopalaczSlot7 = ui.ExpandedImageBox()
        self.DopalaczSlot7.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot7.SetPosition(230, 40)
        self.DopalaczSlot7.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot7.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc7()
        self.DopalaczSlot7.Show()
        self.DopalaczSlotIcon7 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon7.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon7.SetPosition(230, 40)
        self.DopalaczSlotIcon7.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon7.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc7()
        self.DopalaczSlotIcon7.Show()
        self.DopalaczSlot8 = ui.ExpandedImageBox()
        self.DopalaczSlot8.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot8.SetPosition(20, 75)
        self.DopalaczSlot8.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot8.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc8()
        self.DopalaczSlot8.Show()
        self.DopalaczSlotIcon8 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon8.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon8.SetPosition(20, 75)
        self.DopalaczSlotIcon8.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon8.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc8()
        self.DopalaczSlotIcon8.Show()
        self.DopalaczSlot9 = ui.ExpandedImageBox()
        self.DopalaczSlot9.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot9.SetPosition(55, 75)
        self.DopalaczSlot9.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot9.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc9()
        self.DopalaczSlot9.Show()
        self.DopalaczSlotIcon9 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon9.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon9.SetPosition(55, 75)
        self.DopalaczSlotIcon9.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon9.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc9()
        self.DopalaczSlotIcon9.Show()
        self.DopalaczSlot10 = ui.ExpandedImageBox()
        self.DopalaczSlot10.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot10.SetPosition(90, 75)
        self.DopalaczSlot10.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot10.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc10()
        self.DopalaczSlot10.Show()
        self.DopalaczSlotIcon10 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon10.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon10.SetPosition(90, 75)
        self.DopalaczSlotIcon10.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon10.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc10()
        self.DopalaczSlotIcon10.Show()
        self.DopalaczSlot11 = ui.ExpandedImageBox()
        self.DopalaczSlot11.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot11.SetPosition(125, 75)
        self.DopalaczSlot11.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot11.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc11()
        self.DopalaczSlot11.Show()
        self.DopalaczSlotIcon11 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon11.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon11.SetPosition(125, 75)
        self.DopalaczSlotIcon11.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon11.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc11()
        self.DopalaczSlotIcon11.Show()
        self.DopalaczSlot12 = ui.ExpandedImageBox()
        self.DopalaczSlot12.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot12.SetPosition(160, 75)
        self.DopalaczSlot12.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot12.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc12()
        self.DopalaczSlot12.Show()
        self.DopalaczSlotIcon12 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon12.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon12.SetPosition(160, 75)
        self.DopalaczSlotIcon12.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon12.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc12()
        self.DopalaczSlotIcon12.Show()
        self.DopalaczSlot13 = ui.ExpandedImageBox()
        self.DopalaczSlot13.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot13.SetPosition(195, 75)
        self.DopalaczSlot13.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot13.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc13()
        self.DopalaczSlot13.Show()
        self.DopalaczSlotIcon13 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon13.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon13.SetPosition(195, 75)
        self.DopalaczSlotIcon13.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon13.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc13()
        self.DopalaczSlotIcon13.Show()
        self.DopalaczSlot14 = ui.ExpandedImageBox()
        self.DopalaczSlot14.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot14.SetPosition(230, 75)
        self.DopalaczSlot14.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot14.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc14()
        self.DopalaczSlot14.Show()
        self.DopalaczSlotIcon14 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon14.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon14.SetPosition(195, 75)
        self.DopalaczSlotIcon14.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon14.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc14()
        self.DopalaczSlotIcon14.Show()
        self.DopalaczSlot15 = ui.ExpandedImageBox()
        self.DopalaczSlot15.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot15.SetPosition(20, 110)
        self.DopalaczSlot15.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot15.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc15()
        self.DopalaczSlot15.Show()
        self.DopalaczSlotIcon15 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon15.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon15.SetPosition(20, 110)
        self.DopalaczSlotIcon15.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon15.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc15()
        self.DopalaczSlotIcon15.Show()
        self.DopalaczSlot16 = ui.ExpandedImageBox()
        self.DopalaczSlot16.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot16.SetPosition(55, 110)
        self.DopalaczSlot16.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot16.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc16()
        self.DopalaczSlot16.Show()
        self.DopalaczSlotIcon16 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon16.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon16.SetPosition(55, 110)
        self.DopalaczSlotIcon16.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon16.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc16()
        self.DopalaczSlotIcon16.Show()
        self.DopalaczSlot17 = ui.ExpandedImageBox()
        self.DopalaczSlot17.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot17.SetPosition(90, 110)
        self.DopalaczSlot17.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot17.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc17()
        self.DopalaczSlot17.Show()
        self.DopalaczSlotIcon17 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon17.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon17.SetPosition(90, 110)
        self.DopalaczSlotIcon17.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon17.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc17()
        self.DopalaczSlotIcon17.Show()
        self.DopalaczSlot18 = ui.ExpandedImageBox()
        self.DopalaczSlot18.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot18.SetPosition(125, 110)
        self.DopalaczSlot18.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot18.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc18()
        self.DopalaczSlot18.Show()
        self.DopalaczSlotIcon18 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon18.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon18.SetPosition(125, 110)
        self.DopalaczSlotIcon18.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon18.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc18()
        self.DopalaczSlotIcon18.Show()
        self.DopalaczSlot19 = ui.ExpandedImageBox()
        self.DopalaczSlot19.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot19.SetPosition(160, 110)
        self.DopalaczSlot19.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot19.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc19()
        self.DopalaczSlot19.Show()
        self.DopalaczSlotIcon19 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon19.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon19.SetPosition(160, 110)
        self.DopalaczSlotIcon19.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon19.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc19()
        self.DopalaczSlotIcon19.Show()
        self.DopalaczSlot20 = ui.ExpandedImageBox()
        self.DopalaczSlot20.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot20.SetPosition(195, 110)
        self.DopalaczSlot20.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot20.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc20()
        self.DopalaczSlot20.Show()
        self.DopalaczSlotIcon20 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon20.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon20.SetPosition(195, 110)
        self.DopalaczSlotIcon20.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon20.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc20()
        self.DopalaczSlotIcon20.Show()
        self.DopalaczSlot21 = ui.ExpandedImageBox()
        self.DopalaczSlot21.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot21.SetPosition(230, 110)
        self.DopalaczSlot21.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot21.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc21()
        self.DopalaczSlot21.Show()
        self.DopalaczSlotIcon21 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon21.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon21.SetPosition(230, 110)
        self.DopalaczSlotIcon21.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon21.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc21()
        self.DopalaczSlotIcon21.Show()
        self.DopalaczSlot22 = ui.ExpandedImageBox()
        self.DopalaczSlot22.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot22.SetPosition(20, 145)
        self.DopalaczSlot22.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot22.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc22()
        self.DopalaczSlot22.Show()
        self.DopalaczSlotIcon22 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon22.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon22.SetPosition(20, 145)
        self.DopalaczSlotIcon22.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon22.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc22()
        self.DopalaczSlotIcon22.Show()
        self.DopalaczSlot23 = ui.ExpandedImageBox()
        self.DopalaczSlot23.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot23.SetPosition(55, 145)
        self.DopalaczSlot23.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot23.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc23()
        self.DopalaczSlot23.Show()
        self.DopalaczSlotIcon23 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon23.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon23.SetPosition(55, 145)
        self.DopalaczSlotIcon23.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon23.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc23()
        self.DopalaczSlotIcon23.Show()
        self.DopalaczSlot24 = ui.ExpandedImageBox()
        self.DopalaczSlot24.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot24.SetPosition(90, 145)
        self.DopalaczSlot24.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot24.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc24()
        self.DopalaczSlot24.Show()
        self.DopalaczSlotIcon24 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon24.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon24.SetPosition(90, 145)
        self.DopalaczSlotIcon24.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon24.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc24()
        self.DopalaczSlotIcon24.Show()
        self.DopalaczSlot25 = ui.ExpandedImageBox()
        self.DopalaczSlot25.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot25.SetPosition(125, 145)
        self.DopalaczSlot25.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot25.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc25()
        self.DopalaczSlot25.Show()
        self.DopalaczSlotIcon25 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon25.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon25.SetPosition(125, 145)
        self.DopalaczSlotIcon25.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon25.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc25()
        self.DopalaczSlotIcon25.Show()
        self.DopalaczSlot26 = ui.ExpandedImageBox()
        self.DopalaczSlot26.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot26.SetPosition(160, 145)
        self.DopalaczSlot26.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot26.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc26()
        self.DopalaczSlot26.Show()
        self.DopalaczSlotIcon26 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon26.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon26.SetPosition(160, 145)
        self.DopalaczSlotIcon26.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon26.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc26()
        self.DopalaczSlotIcon26.Show()
        self.DopalaczSlot27 = ui.ExpandedImageBox()
        self.DopalaczSlot27.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot27.SetPosition(195, 145)
        self.DopalaczSlot27.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot27.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc27()
        self.DopalaczSlot27.Show()
        self.DopalaczSlotIcon27 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon27.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon27.SetPosition(195, 145)
        self.DopalaczSlotIcon27.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon27.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc27()
        self.DopalaczSlotIcon27.Show()
        self.DopalaczSlot28 = ui.ExpandedImageBox()
        self.DopalaczSlot28.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlot28.SetPosition(230, 145)
        self.DopalaczSlot28.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlot28.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc28()
        self.DopalaczSlot28.Show()
        self.DopalaczSlotIcon28 = ui.ExpandedImageBox()
        self.DopalaczSlotIcon28.SetParent(self.DopalaczeOknoBoard)
        self.DopalaczSlotIcon28.SetPosition(230, 145)
        self.DopalaczSlotIcon28.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.DopalaczSlotIcon28.OnMouseLeftButtonUp = lambda : self.DopalaczeSlotFunc28()
        self.DopalaczSlotIcon28.Show()
        self.MobberSlot = ui.ExpandedImageBox()
        self.MobberSlot.SetParent(self.Ustawieniao)
        self.MobberSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.MobberSlot.OnMouseLeftButtonUp = lambda : self.MobberSlotFunc()
        self.MobberSlot.SetPosition(54, 75)
        self.MobberSlot.Show()
        self.MobberSlotIcon = ui.ExpandedImageBox()
        self.MobberSlotIcon.SetParent(self.Ustawieniao)
        self.MobberSlotIcon.SetPosition(54, 75)
        self.MobberSlotIcon.LoadImage('')
        
        self.MobberSlotIcon.OnMouseLeftButtonUp = lambda : self.MobberSlotFunc()
        self.MobberSlotIcon.Show()
        self.PotySlot = ui.ExpandedImageBox()
        self.PotySlot.SetParent(self.Ustawieniao)
        self.PotySlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.PotySlot.OnMouseLeftButtonUp = lambda : self.Set_Poty_1_ID()
        self.PotySlot.SetPosition(190, 75)
        self.PotySlot.Show()
        self.PotySlot2 = ui.ExpandedImageBox()
        self.PotySlot2.SetParent(self.Ustawieniao)
        self.PotySlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.PotySlot2.OnMouseLeftButtonUp = lambda : self.Set_Poty_2_ID()
        self.PotySlot2.SetPosition(225, 75)
        self.PotySlot2.Show()
        self.PotySlotIcon = ui.ExpandedImageBox()
        self.PotySlotIcon.SetParent(self.Ustawieniao)
        self.PotySlotIcon.SetPosition(190, 75)
        self.PotySlotIcon.LoadImage('')
        
        self.PotySlotIcon.OnMouseLeftButtonUp = lambda : self.Set_Poty_1_ID()
        self.PotySlotIcon.Show()
        self.PotySlotIcon2 = ui.ExpandedImageBox()
        self.PotySlotIcon2.SetParent(self.Ustawieniao)
        self.PotySlotIcon2.SetPosition(225, 75)
        self.PotySlotIcon2.LoadImage('')
        
        self.PotySlotIcon2.OnMouseLeftButtonUp = lambda : self.Set_Poty_2_ID()
        self.PotySlotIcon2.Show()
        self.OtwieraczSlot = ui.ExpandedImageBox()
        self.OtwieraczSlot.SetParent(self.Ustawieniao)
        self.OtwieraczSlot.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc()
        self.OtwieraczSlot.SetPosition(350, 70)
        self.OtwieraczSlot.Show()
        self.OtwieraczSlot1 = ui.ExpandedImageBox()
        self.OtwieraczSlot1.SetParent(self.Ustawieniao)
        self.OtwieraczSlot1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot1.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc1()
        self.OtwieraczSlot1.SetPosition(385, 70)
        self.OtwieraczSlot1.Show()
        self.OtwieraczSlot2 = ui.ExpandedImageBox()
        self.OtwieraczSlot2.SetParent(self.Ustawieniao)
        self.OtwieraczSlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot2.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc2()
        self.OtwieraczSlot2.SetPosition(420, 70)
        self.OtwieraczSlot2.Show()
        self.OtwieraczSlot3 = ui.ExpandedImageBox()
        self.OtwieraczSlot3.SetParent(self.Ustawieniao)
        self.OtwieraczSlot3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot3.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc3()
        self.OtwieraczSlot3.SetPosition(350, 105)
        self.OtwieraczSlot3.Show()
        self.OtwieraczSlot4 = ui.ExpandedImageBox()
        self.OtwieraczSlot4.SetParent(self.Ustawieniao)
        self.OtwieraczSlot4.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot4.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc4()
        self.OtwieraczSlot4.SetPosition(385, 105)
        self.OtwieraczSlot4.Show()
        self.OtwieraczSlot5 = ui.ExpandedImageBox()
        self.OtwieraczSlot5.SetParent(self.Ustawieniao)
        self.OtwieraczSlot5.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.OtwieraczSlot5.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc5()
        self.OtwieraczSlot5.SetPosition(420, 105)
        self.OtwieraczSlot5.Show()
        self.OtwieraczSlotIcon = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon.SetPosition(350, 70)
        self.OtwieraczSlotIcon.LoadImage('')
        
        self.OtwieraczSlotIcon.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc()
        self.OtwieraczSlotIcon.Show()
        self.OtwieraczSlotIcon1 = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon1.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon1.SetPosition(385, 70)
        self.OtwieraczSlotIcon1.LoadImage('')
        
        self.OtwieraczSlotIcon1.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc1()
        self.OtwieraczSlotIcon1.Show()
        self.OtwieraczSlotIcon2 = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon2.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon2.SetPosition(420, 70)
        self.OtwieraczSlotIcon2.LoadImage('')
        
        self.OtwieraczSlotIcon2.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc2()
        self.OtwieraczSlotIcon2.Show()
        self.OtwieraczSlotIcon3 = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon3.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon3.SetPosition(350, 105)
        self.OtwieraczSlotIcon3.LoadImage('')
        
        self.OtwieraczSlotIcon3.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc3()
        self.OtwieraczSlotIcon3.Show()
        self.OtwieraczSlotIcon4 = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon4.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon4.SetPosition(385, 105)
        self.OtwieraczSlotIcon4.LoadImage('')
        
        self.OtwieraczSlotIcon4.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc4()
        self.OtwieraczSlotIcon4.Show()
        self.OtwieraczSlotIcon5 = ui.ExpandedImageBox()
        self.OtwieraczSlotIcon5.SetParent(self.Ustawieniao)
        self.OtwieraczSlotIcon5.SetPosition(420, 105)
        self.OtwieraczSlotIcon5.LoadImage('')
        
        self.OtwieraczSlotIcon5.OnMouseLeftButtonUp = lambda : self.OtwieraczSlotFunc5()
        self.OtwieraczSlotIcon5.Show()
        self.UlepszanieSlot1 = ui.ExpandedImageBox()
        self.UlepszanieSlot1.SetParent(self.UlepszBoard)
        self.UlepszanieSlot1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.UlepszanieSlot1.OnMouseLeftButtonUp = lambda : self.Ulepsz_Item()
        self.UlepszanieSlot1.SetPosition(15, 30)
        self.UlepszanieSlot1.Show()
        self.UlepszanieSlot2 = ui.ExpandedImageBox()
        self.UlepszanieSlot2.SetParent(self.UlepszBoard)
        self.UlepszanieSlot2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.UlepszanieSlot2.OnMouseLeftButtonUp = lambda : self.Ulepsz_Item()
        self.UlepszanieSlot2.SetPosition(15, 62)
        self.UlepszanieSlot2.Show()
        self.UlepszanieSlot3 = ui.ExpandedImageBox()
        self.UlepszanieSlot3.SetParent(self.UlepszBoard)
        self.UlepszanieSlot3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        
        self.UlepszanieSlot3.OnMouseLeftButtonUp = lambda : self.Ulepsz_Item()
        self.UlepszanieSlot3.SetPosition(15, 94)
        self.UlepszanieSlot3.Show()
        self.UlepszanieSlotIcon = ui.ExpandedImageBox()
        self.UlepszanieSlotIcon.SetParent(self.UlepszBoard)
        self.UlepszanieSlotIcon.SetPosition(15, 30)
        self.UlepszanieSlotIcon.LoadImage('')
        
        self.UlepszanieSlotIcon.OnMouseLeftButtonUp = lambda : self.Ulepsz_Item()
        self.UlepszanieSlotIcon.Show()

    
    def Zoom_func(self):
        app.SetCameraMaxDistance(50000)

    
    def Dzien_func(self):
        background.SetEnvironmentData(0)

    
    def Noc_func(self):
        background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
        background.SetEnvironmentData(1)

    
    def Gora_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) - 500, int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    
    def Lewo_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) - 500, int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    
    def Prawo_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) + 500, int(y), int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    
    def Dol_func(self):
        myVid = player.GetMainCharacterIndex()
        chr.SelectInstance(myVid)
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) + 500, int(z))
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    
    def WykrywaczMetinow_func(self):
        self.OpenWindowWykr()

    
    def Dopalaczestr_func(self):
        self.OpenWindowDopy()

    
    def Spambot_func(self):
        self.OpenWindowSpam()

    
    def Ustawienia_func(self):
        self.OpenWindowUstawieniao()

    
    def TypBicia_func(self):
        self.OpenWindowTypbicia()

    
    def Ulepszanie_func(self):
        self.OpenWindowUlepsz()

    
    def Pogoda_func(self):
        self.OpenWindowPogoda()

    
    def Wizual_func(self):
        self.OpenWindowWizualnyBoard()

    
    def Autoskile_func(self):
        self.AutoSkileWindow()

    
    def TypJednor_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)

    
    def TypDwu_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)

    
    def TypSztylety_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_DUALHAND_SWORD)

    
    def TypLuk_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_BOW)

    
    def TypDzwon_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_BELL)

    
    def TypWachlarz_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_FAN)

    
    def TypWedka_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_FISHING)

    
    def TypPiesc_func(self):
        chr.SetMotionMode(chr.MOTION_MODE_GENERAL)

    
    def Tpdokordow_func(self):
        global teleport_mode, telestep, teleport_mode
        x_coordinate = self.Xin.GetText()
        y_coordinate = self.Yin.GetText()
        x_coordinate = int(x_coordinate) * 100
        y_coordinate = int(y_coordinate) * 100
        z_coordinate = int(1) * 100
        (ax, ay, az) = player.GetMainCharacterPosition()
        teleport_mode = 1
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) - 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) + 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        teleport_mode = 0

    
    def Zamknijgre_func(self):
        app.Exit()

    
    def AutoAtak_func(self, arg):
        if arg == 'on':
            self.AutoAttackStartFunc()
        elif arg == 'off':
            self.AutoAttackStopFunc()
        

    
    def AutoAttackStartFunc(self):
        self.AutoAttackx = XX()
        self.AutoAttackx.XX1(1)
        self.AutoAttackx.XX2(self.AutoAttackStartFunc)
        player.SetAttackKeyState(TRUE)
        chr.SelectInstance(player.GetMainCharacterIndex)
        chr.SetDirection(app.GetRandom(0, 0))

    
    def AutoAttackStopFunc(self):
        self.AutoAttackx = XX()
        self.AutoAttackx.XX1(50000000)
        self.AutoAttackx.XX2(self.AutoAttackStopFunc)
        player.SetAttackKeyState(FALSE)

    
    def Potyfunc(self):
        global Poty
        if Poty == 0:
            Poty = 1
            self.PotyStartFunc()
        else:
            Poty = 0
            self.PotyStopFunc()

    
    def PotyStartFunc(self):
        if Poty == 1:
            Potyt = self.Potyhpczas.GetText()
        
        maxhp = player.GetStatus(player.MAX_HP)
        aktualnehp = player.GetStatus(player.HP)
        if (float(aktualnehp) / float(maxhp)) * 100 < int(float(Potyt)):
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                CzerwonePotki = player.GetItemIndex(i)
                if CzerwonePotki == int(Poty_1_ID):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Poty == 1:
            Potyt1 = self.Potympczas.GetText()
        
        maxmp = player.GetStatus(player.MAX_SP)
        aktualnemp = player.GetStatus(player.SP)
        if (float(aktualnemp) / float(maxmp)) * 100 < int(float(Potyt1)):
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                NiebieskiePotki = player.GetItemIndex(i)
                if NiebieskiePotki == int(Poty_2_ID):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        self.Potyx = XX()
        self.Potyx.XX1(float(0.5000000000000001))
        self.Potyx.XX2(self.PotyStartFunc)

    
    def PotyStopFunc(self):
        self.Potyx = XX()
        self.Potyx.XX1(float(0x16345785D89FFFFL))
        self.Potyx.XX2(self.PotyStopFunc)

    
    def Pickup_func(self, arg):
        if arg == 'on':
            self.PickUpStartFunc()
        elif arg == 'off':
            self.PickUpStopFunc()
        

    
    def PickUpStartFunc(self):
        self.PickUp = XX()
        self.PickUp.XX1(0.001)
        self.PickUp.XX2(self.PickUpStartFunc)
        player.PickCloseItem()

    
    def PickUpStopFunc(self):
        self.PickUp = XX()
        self.PickUp.XX1(50000000)
        self.PickUp.XX2(self.PickUpStopFunc)

    
    def Mobber_func(self, arg):
        if arg == 'on':
            self.MobberStartFunc()
        elif arg == 'off':
            self.MobberStopFunc()
        

    
    def MobberStartFunc(self):
        mobbert = self.Peleczas.GetText()
        self.Mobber = XX()
        self.Mobber.XX1(float(mobbert))
        self.Mobber.XX2(self.MobberStartFunc)
        for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
            Mobberitemx = player.GetItemIndex(i)
            if Mobberitemx == int(Mobber_ID):
                net.SendItemUsePacket(i)
                break
            
        

    
    def MobberStopFunc(self):
        self.Mobber = XX()
        self.Mobber.XX1(50000000)
        self.Mobber.XX2(self.MobberStopFunc)

    
    def Dopalacze_func(self, arg):
        if arg == 'on':
            self.DopalaczStartFunc()
        elif arg == 'off':
            self.DopalaczStopFunc()
        

    
    def DopalaczStartFunc(self):
        global Dopalaczx
        Dopalaczx = 1
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz1_ID = player.GetItemIndex(i)
                if Dopalacz1_ID == int(Dopalacz_ID1):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz2_ID = player.GetItemIndex(i)
                if Dopalacz2_ID == int(Dopalacz_ID2):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz3_ID = player.GetItemIndex(i)
                if Dopalacz3_ID == int(Dopalacz_ID3):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz4_ID = player.GetItemIndex(i)
                if Dopalacz4_ID == int(Dopalacz_ID4):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz5_ID = player.GetItemIndex(i)
                if Dopalacz5_ID == int(Dopalacz_ID5):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz6_ID = player.GetItemIndex(i)
                if Dopalacz6_ID == int(Dopalacz_ID6):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz7_ID = player.GetItemIndex(i)
                if Dopalacz7_ID == int(Dopalacz_ID7):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz8_ID = player.GetItemIndex(i)
                if Dopalacz8_ID == int(Dopalacz_ID8):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz9_ID = player.GetItemIndex(i)
                if Dopalacz9_ID == int(Dopalacz_ID9):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz10_ID = player.GetItemIndex(i)
                if Dopalacz10_ID == int(Dopalacz_ID10):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz11_ID = player.GetItemIndex(i)
                if Dopalacz11_ID == int(Dopalacz_ID11):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz12_ID = player.GetItemIndex(i)
                if Dopalacz12_ID == int(Dopalacz_ID12):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz13_ID = player.GetItemIndex(i)
                if Dopalacz13_ID == int(Dopalacz_ID13):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz14_ID = player.GetItemIndex(i)
                if Dopalacz14_ID == int(Dopalacz_ID14):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz15_ID = player.GetItemIndex(i)
                if Dopalacz15_ID == int(Dopalacz_ID15):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz16_ID = player.GetItemIndex(i)
                if Dopalacz16_ID == int(Dopalacz_ID16):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz17_ID = player.GetItemIndex(i)
                if Dopalacz17_ID == int(Dopalacz_ID17):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz18_ID = player.GetItemIndex(i)
                if Dopalacz18_ID == int(Dopalacz_ID18):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz19_ID = player.GetItemIndex(i)
                if Dopalacz19_ID == int(Dopalacz_ID19):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz20_ID = player.GetItemIndex(i)
                if Dopalacz20_ID == int(Dopalacz_ID20):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz21_ID = player.GetItemIndex(i)
                if Dopalacz21_ID == int(Dopalacz_ID21):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz22_ID = player.GetItemIndex(i)
                if Dopalacz22_ID == int(Dopalacz_ID22):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz23_ID = player.GetItemIndex(i)
                if Dopalacz23_ID == int(Dopalacz_ID23):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz24_ID = player.GetItemIndex(i)
                if Dopalacz24_ID == int(Dopalacz_ID24):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz25_ID = player.GetItemIndex(i)
                if Dopalacz25_ID == int(Dopalacz_ID25):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz26_ID = player.GetItemIndex(i)
                if Dopalacz26_ID == int(Dopalacz_ID26):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz27_ID = player.GetItemIndex(i)
                if Dopalacz27_ID == int(Dopalacz_ID27):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Dopalaczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Dopalacz28_ID = player.GetItemIndex(i)
                if Dopalacz28_ID == int(Dopalacz_ID28):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        Otwieraczt = self.coiledopy1.GetText()
        self.Delay_Dopalacz = XX()
        self.Delay_Dopalacz.XX1(float(Otwieraczt * 60))
        self.Delay_Dopalacz.XX2(self.DopalaczStartFunc)

    
    def DopalaczStopFunc(self):
        self.Delay_Dopalacz = XX()
        self.Delay_Dopalacz.XX1(float(0x16345785D89FFFFL))
        self.Delay_Dopalacz.XX2(self.DopalaczStopFunc)

    
    def DopalaczeSlotFunc1(self):
        global Dopalacz_ID1
        if mouseModule.mouseController.isAttached():
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID1 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.DopalaczSlotIcon1.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def DopalaczeSlotFunc2(self):
        global Dopalacz_ID2
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID2 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon2.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc3(self):
        global Dopalacz_ID3
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID3 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon3.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc4(self):
        global Dopalacz_ID4
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID4 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon4.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc5(self):
        global Dopalacz_ID5
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID5 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon5.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc6(self):
        global Dopalacz_ID6
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID6 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon6.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc7(self):
        global Dopalacz_ID7
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID7 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon7.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc8(self):
        global Dopalacz_ID8
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID8 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon8.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc9(self):
        global Dopalacz_ID9
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID9 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon9.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc10(self):
        global Dopalacz_ID10
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID10 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon10.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc11(self):
        global Dopalacz_ID11
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID11 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon11.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc12(self):
        global Dopalacz_ID12
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID12 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon12.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc13(self):
        global Dopalacz_ID13
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID13 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon13.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc14(self):
        global Dopalacz_ID14
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID14 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon14.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc15(self):
        global Dopalacz_ID15
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID15 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon15.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc16(self):
        global Dopalacz_ID16
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID16 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon16.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc17(self):
        global Dopalacz_ID17
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID17 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon17.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc18(self):
        global Dopalacz_ID18
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID18 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon18.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc19(self):
        global Dopalacz_ID19
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID19 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon19.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc20(self):
        global Dopalacz_ID20
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID20 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon20.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc21(self):
        global Dopalacz_ID21
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID21 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon21.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc22(self):
        global Dopalacz_ID22
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID22 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon22.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc23(self):
        global Dopalacz_ID23
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID23 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon23.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc24(self):
        global Dopalacz_ID24
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID24 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon24.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc25(self):
        global Dopalacz_ID25
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID25 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon25.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc26(self):
        global Dopalacz_ID26
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID26 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon26.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc27(self):
        global Dopalacz_ID27
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID27 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon27.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def DopalaczeSlotFunc28(self):
        global Dopalacz_ID28
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Dopalacz_ID28 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
            item.SelectItem(int(attachedSlotVnum))
            self.DopalaczSlotIcon28.LoadImage(str(item.GetIconImageFileName()))
            mouseModule.mouseController.DeattachObject()
        

    
    def Ghost_func(self):
        chr.Revive()

    
    def Kamera_func(self, arg):
        if arg == 'on':
            (x, y, z) = player.GetMainCharacterPosition()
            app.SetCameraSetting(int(x), int(-y), int(z), 5000, 10, 30)
        elif arg == 'off':
            app.SetDefaultCamera()
        

    
    def Snieg_func(self, arg):
        if arg == 'on':
            background.EnableSnow(1)
        elif arg == 'off':
            background.EnableSnow(0)
        

    
    def Combo_func(self, arg):
        if arg == 'on':
            chr.testSetComboType(2)
        elif arg == 'off':
            chr.testSetComboType(0)
        

    
    def Otwieracz_func(self, arg):
        if arg == 'on':
            self.OtwieraczStartFunc()
        elif arg == 'off':
            self.OtwieraczStopFunc()
        

    
    def OtwieraczStartFunc(self):
        global Otwieraczx
        Otwieraczx = 1
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz1_ID = player.GetItemIndex(i)
                if Otwieracz1_ID == int(Otwieracz_ID):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz2_ID = player.GetItemIndex(i)
                if Otwieracz2_ID == int(Otwieracz_ID1):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz3_ID = player.GetItemIndex(i)
                if Otwieracz3_ID == int(Otwieracz_ID2):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz4_ID = player.GetItemIndex(i)
                if Otwieracz4_ID == int(Otwieracz_ID3):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz5_ID = player.GetItemIndex(i)
                if Otwieracz5_ID == int(Otwieracz_ID4):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        if Otwieraczx == 1:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 5):
                Otwieracz6_ID = player.GetItemIndex(i)
                if Otwieracz6_ID == int(Otwieracz_ID5):
                    net.SendItemUsePacket(i)
                    break
                
            
        
        Otwieraczt = self.Dopyczas.GetText()
        self.Delay_Otwieracz = XX()
        self.Delay_Otwieracz.XX1(float(Otwieraczt))
        self.Delay_Otwieracz.XX2(self.OtwieraczStartFunc)

    
    def OtwieraczStopFunc(self):
        self.Delay_Otwieracz = XX()
        self.Delay_Otwieracz.XX1(float(0x16345785D89FFFFL))
        self.Delay_Otwieracz.XX2(self.OtwieraczStopFunc)

    
    def AutoWstawanie_func(self, arg):
        if arg == 'on':
            self.Autowstawaniestart()
        elif arg == 'off':
            self.Autowstawaniestop()
        

    
    def Autowstawaniestart(self):
        self.awfunc = XX()
        self.awfunc.XX1(5.0)
        self.awfunc.XX2(self.Autowstawaniestart)
        maxhp = player.GetStatus(player.MAX_HP)
        aktualnehp = player.GetStatus(player.HP)
        if (float(aktualnehp) / float(maxhp)) * 100 < int(0):
            player.SetAttackKeyState(FALSE)
            net.SendChatPacket('/restart_here')
        

    
    def Autowstawaniestop(self):
        self.awfunc = XX()
        self.awfunc.XX1(50000000.0)
        self.awfunc.XX2(self.Autowstawaniestop)

    
    def WykrywaczGM_func(self, arg):
        if arg == 'on':
            self.WykrywaczgmStartFunc()
        elif arg == 'off':
            self.WykrywaczgmStopFunc()
        

    
    def WykrywaczgmStartFunc(self):
        self.Wykrywaczgm = XX()
        self.Wykrywaczgm.XX1(10.0)
        self.Wykrywaczgm.XX2(self.WykrywaczgmStartFunc)
        x = player.GetMainCharacterIndex()
        for i in xrange(x - 50000, x + 50000):
            if chr.IsGameMaster(i):
                Pozycja = player.GetMainCharacterPosition(i)
                Nazwa = chr.GetNameByVID(i)
                (x, y, z) = chr.GetPixelPosition(i)
                dbg.LogBox(str(Nazwa) + '  x:' + str(x / 100) + '  y:' + str(y / 100))
            
        

    
    def WykrywaczgmStopFunc(self):
        self.Wykrywaczgm = XX()
        self.Wykrywaczgm.XX1(50000000.0)
        self.Wykrywaczgm.XX2(self.WykrywaczgmStopFunc)

    
    def SzukajMetinow_func(self, arg):
        if arg == 'on':
            self.WykrywaczMetinowFuncStart()
        elif arg == 'off':
            self.WykrywaczMetinowFuncStop()
        

    
    def WykrywaczMetinowFuncStart(self):
        b = 0
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(5)
        self.Wykrywaczmetinow.XX2(self.WykrywaczMetinowFuncStart)
        o = player.GetMainCharacterIndex()
        for i in xrange(o - 500000, o + 50000):
            Odleglosc = player.GetCharacterDistance(i)
            if Odleglosc > 2:
                Typ = chr.GetInstanceType(i)
                if Typ == 2:
                    imie = chr.GetNameByVID(i)
                    chr.SelectInstance(i)
                    (x, y, z) = chr.GetPixelPosition(i)
                    yt = player.GetMainCharacterPosition()
                    chat.AppendChat(chat.BOARD_STATE_LOG, 'Nazwa Metina:  ' + str(imie) + '  x:' + str(x / 100) + '  y:' + str(y / 100))
                
            
        
        self.Pozycjaxtext = ui.TextLine()
        self.Pozycjaxtext.SetParent(self.WykrywaczOkno)
        self.Pozycjaxtext.SetDefaultFontName()
        self.Pozycjaxtext.SetPosition(120, 123)
        self.Pozycjaxtext.SetFeather()
        self.Pozycjaxtext.SetText(str(x / 100))
        self.Pozycjaxtext.SetOutline()
        self.Pozycjaxtext.Show()
        self.Pozycjaytext = ui.TextLine()
        self.Pozycjaytext.SetParent(self.WykrywaczOkno)
        self.Pozycjaytext.SetDefaultFontName()
        self.Pozycjaytext.SetPosition(120, 141)
        self.Pozycjaytext.SetFeather()
        self.Pozycjaytext.SetText(str(y / 100))
        self.Pozycjaytext.SetOutline()
        self.Pozycjaytext.Show()
        self.Nazwametinatext = ui.TextLine()
        self.Nazwametinatext.SetParent(self.WykrywaczOkno)
        self.Nazwametinatext.SetDefaultFontName()
        self.Nazwametinatext.SetPosition(105, 105)
        self.Nazwametinatext.SetFeather()
        self.Nazwametinatext.SetText(str(imie))
        self.Nazwametinatext.SetOutline()
        self.Nazwametinatext.Show()

    
    def WykrywaczMetinowFuncStop(self):
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(50000000.0)
        self.Wykrywaczmetinow.XX2(self.WykrywaczMetinowFuncStop)

    
    def SzukajBossow_func(self, arg):
        if arg == 'on':
            self.WykrywaczBossowFuncStart()
        elif arg == 'off':
            self.WykrywaczBossowFuncStop()
        

    
    def WykrywaczBossowFuncStart(self):
        b = 0
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(5)
        self.Wykrywaczmetinow.XX2(self.WykrywaczBossowFuncStart)
        o = player.GetMainCharacterIndex()
        for i in xrange(o - 500000, o + 50000):
            Odleglosc = player.GetCharacterDistance(i)
            if Odleglosc > 0:
                Typ = chr.GetInstanceType(i)
                if Typ == 0:
                    chr.SelectInstance(i)
                    Race = chr.GetRace(i)
                    for k in bosy:
                        if Race == k:
                            imie = chr.GetNameByVID(i)
                            chr.SelectInstance(i)
                            (x, y, z) = chr.GetPixelPosition(i)
                            yt = player.GetMainCharacterPosition()
                            chat.AppendChat(chat.BOARD_STATE_LOG, 'Nazwa Bossa:  ' + str(imie) + '  x:' + str(x / 100) + '  y:' + str(y / 100))
                        
                    
                
            
        
        self.Pozycjaxtext = ui.TextLine()
        self.Pozycjaxtext.SetParent(self.WykrywaczOkno)
        self.Pozycjaxtext.SetDefaultFontName()
        self.Pozycjaxtext.SetPosition(120, 59)
        self.Pozycjaxtext.SetFeather()
        self.Pozycjaxtext.SetText(str(x / 100))
        self.Pozycjaxtext.SetOutline()
        self.Pozycjaxtext.Show()
        self.Pozycjaytext = ui.TextLine()
        self.Pozycjaytext.SetParent(self.WykrywaczOkno)
        self.Pozycjaytext.SetDefaultFontName()
        self.Pozycjaytext.SetPosition(120, 77)
        self.Pozycjaytext.SetFeather()
        self.Pozycjaytext.SetText(str(y / 100))
        self.Pozycjaytext.SetOutline()
        self.Pozycjaytext.Show()
        self.Nazwametinatext = ui.TextLine()
        self.Nazwametinatext.SetParent(self.WykrywaczOkno)
        self.Nazwametinatext.SetDefaultFontName()
        self.Nazwametinatext.SetPosition(105, 41)
        self.Nazwametinatext.SetFeather()
        self.Nazwametinatext.SetText(str(imie))
        self.Nazwametinatext.SetOutline()
        self.Nazwametinatext.Show()

    
    def WykrywaczBossowFuncStop(self):
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(50000000.0)
        self.Wykrywaczmetinow.XX2(self.WykrywaczBossowFuncStop)

    
    def Tpdometina_func(self, arg):
        if arg == 'on':
            self.WykrywaczMetinowFuncStartx()
            self.Debug()
        elif arg == 'off':
            self.WykrywaczMetinowFuncStopx()
            self.Debug()
        

    
    def WykrywaczMetinowFuncStartx(self):
        global teleport_mode, telestep, teleport_mode
        b = 0
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(10)
        self.Wykrywaczmetinow.XX2(self.WykrywaczMetinowFuncStartx)
        o = player.GetMainCharacterIndex()
        for i in xrange(o - 500000, o + 50000):
            Odleglosc = player.GetCharacterDistance(i)
            if Odleglosc > 0:
                Typ = chr.GetInstanceType(i)
                if Typ == 2:
                    chr.SelectInstance(i)
                    (x, y, z) = chr.GetPixelPosition(i)
                    break
                
            
        
        x_coordinate = x
        y_coordinate = y
        x_coordinate = int(x_coordinate)
        y_coordinate = int(y_coordinate)
        z_coordinate = int(1) * 100
        (ax, ay, az) = player.GetMainCharacterPosition()
        teleport_mode = 1
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) - 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) + 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        teleport_mode = 0
        self.Debug()

    
    def WykrywaczMetinowFuncStopx(self):
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(50000000.0)
        self.Wykrywaczmetinow.XX2(self.WykrywaczMetinowFuncStopx)

    
    def TpdoBossa_func(self, arg):
        if arg == 'on':
            self.WykrywaczBossowFuncStartx()
        elif arg == 'off':
            self.WykrywaczBossowFuncStopx()
        

    
    def WykrywaczBossowFuncStartx(self):
        global teleport_mode, telestep, teleport_mode
        b = 0
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(10)
        self.Wykrywaczmetinow.XX2(self.WykrywaczBossowFuncStartx)
        o = player.GetMainCharacterIndex()
        for i in xrange(o - 500000, o + 50000):
            Odleglosc = player.GetCharacterDistance(i)
            if Odleglosc > 0:
                Typ = chr.GetInstanceType(i)
                if Typ == 0:
                    chr.SelectInstance(i)
                    Race = chr.GetRace(i)
                    for k in bosy:
                        if Race == k:
                            chr.SelectInstance(i)
                            (x, y, z) = chr.GetPixelPosition(i)
                            break
                        
                    
                
            
        
        x_coordinate = x
        y_coordinate = y
        x_coordinate = int(x_coordinate)
        y_coordinate = int(y_coordinate)
        z_coordinate = int(1) * 100
        (ax, ay, az) = player.GetMainCharacterPosition()
        teleport_mode = 1
        if int(x_coordinate) < int(ax):
            while int(x_coordinate) < int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) - 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(x_coordinate) > int(ax):
            while int(x_coordinate) > int(ax):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax) + 500, int(ay))
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(x_coordinate), int(ay))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) < int(ay):
            while int(y_coordinate) < int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(y_coordinate) > int(ay):
            while int(y_coordinate) > int(ay):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(y_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) < int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) < int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) - 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        if int(z_coordinate) > int(az) and int(z_coordinate) != 0:
            while int(z_coordinate) > int(az):
                myVid = player.GetMainCharacterIndex()
                chr.SelectInstance(myVid)
                chr.SetPixelPosition(int(ax), int(ay), int(az) + 500)
                player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
                player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
                (ax, ay, az) = player.GetMainCharacterPosition()
                telestep = telestep + 1
            myVid = player.GetMainCharacterIndex()
            chr.SelectInstance(myVid)
            chr.SetPixelPosition(int(ax), int(ay), int(z_coordinate))
            player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
            player.SetSingleDIKKeyState(app.DIK_UP, FALSE)
        
        teleport_mode = 0
        self.Debug()

    
    def WykrywaczBossowFuncStopx(self):
        self.Wykrywaczmetinow = XX()
        self.Wykrywaczmetinow.XX1(50000000.0)
        self.Wykrywaczmetinow.XX2(self.WykrywaczBossowFuncStopx)

    
    def Debug(self):
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)

    
    def usundopy(self):
        global Dopalacz_ID1, Dopalacz_ID2, Dopalacz_ID3, Dopalacz_ID4, Dopalacz_ID5, Dopalacz_ID6, Dopalacz_ID7, Dopalacz_ID8, Dopalacz_ID9, Dopalacz_ID10, Dopalacz_ID11, Dopalacz_ID12, Dopalacz_ID13, Dopalacz_ID14, Dopalacz_ID15, Dopalacz_ID16, Dopalacz_ID17, Dopalacz_ID18, Dopalacz_ID19, Dopalacz_ID20, Dopalacz_ID21, Dopalacz_ID22, Dopalacz_ID23, Dopalacz_ID24, Dopalacz_ID25
        Dopalacz_ID1 = 0
        Dopalacz_ID2 = 0
        Dopalacz_ID3 = 0
        Dopalacz_ID4 = 0
        Dopalacz_ID5 = 0
        Dopalacz_ID6 = 0
        Dopalacz_ID7 = 0
        Dopalacz_ID8 = 0
        Dopalacz_ID9 = 0
        Dopalacz_ID10 = 0
        Dopalacz_ID11 = 0
        Dopalacz_ID12 = 0
        Dopalacz_ID13 = 0
        Dopalacz_ID14 = 0
        Dopalacz_ID15 = 0
        Dopalacz_ID16 = 0
        Dopalacz_ID17 = 0
        Dopalacz_ID18 = 0
        Dopalacz_ID19 = 0
        Dopalacz_ID20 = 0
        Dopalacz_ID21 = 0
        Dopalacz_ID22 = 0
        Dopalacz_ID23 = 0
        Dopalacz_ID24 = 0
        Dopalacz_ID25 = 0
        self.DopalaczSlotIcon1.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon2.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon3.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon4.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon5.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon6.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon7.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon8.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon9.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon10.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon11.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon12.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon13.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon14.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon15.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon16.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon17.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon18.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon19.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon20.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon21.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon22.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon23.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon24.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')
        self.DopalaczSlotIcon25.LoadImage('d:/ymir work/ui/public/Slot_Base.sub')

    
    def Spamboton(self):
        if self.Spambotp.GetCurrentText() == '|cff00FF00|H|hZielony':
            net.SendChatPacket('|cff00FF00|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cffff0000|H|hCzerwony':
            net.SendChatPacket('|cffff0000|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cffFFFFFF|H|hNormal':
            net.SendChatPacket(self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cffFFFF00|H|hZolty':
            net.SendChatPacket('|cffFFFF00|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cffFF1493|H|hRozowy':
            net.SendChatPacket('|cffFF1493|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cff800000|H|hBrazowy':
            net.SendChatPacket('|cff800000|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cffffcc00|H|hZloty':
            net.SendChatPacket('|cffffcc00|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cff800080|H|hFiolotowy':
            net.SendChatPacket('|cff800080|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cff0000FF|H|hNiebieski':
            net.SendChatPacket('|cff0000FF|H|h' + self.Tekstin.GetText())
        
        if self.Spambotp.GetCurrentText() == '|cff00FFFF|H|hBlekitny':
            net.SendChatPacket('|cff00FFFF|H|h' + self.Tekstin.GetText())
        
        self.Spambotk = XX()
        self.Spambotk.XX1(float(self.Coilespamtxtin.GetText()))
        self.Spambotk.XX2(self.Spamboton)

    
    def Spambotoff(self):
        self.Spambotk = XX()
        self.Spambotk.XX1(float(0x9184E729FFFL))
        self.Spambotk.XX2(self.Spambotoff)

    
    def Spamboton1(self):
        if self.Spambotp.GetCurrentText() == '|cff00FF00|H|hZielony':
            net.SendChatPacket('|cff00FF00|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cffff0000|H|hCzerwony':
            net.SendChatPacket('|cffff0000|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cffFFFFFF|H|hNormal':
            net.SendChatPacket(self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cffFFFF00|H|hZolty':
            net.SendChatPacket('|cffFFFF00|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cffFF1493|H|hRozowy':
            net.SendChatPacket('|cffFF1493|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cff800000|H|hBrazowy':
            net.SendChatPacket('|cff800000|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cffffcc00|H|hZloty':
            net.SendChatPacket('|cffffcc00|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cff800080|H|hFiolotowy':
            net.SendChatPacket('|cff800080|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cff0000FF|H|hNiebieski':
            net.SendChatPacket('|cff0000FF|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        if self.Spambotp.GetCurrentText() == '|cff00FFFF|H|hBlekitny':
            net.SendChatPacket('|cff00FFFF|H|h' + self.Tekstin.GetText(), chat.CHAT_TYPE_SHOUT)
        
        self.Spambotk = XX()
        self.Spambotk.XX1(float(self.Coilespamtxtin.GetText()))
        self.Spambotk.XX2(self.Spamboton1)

    
    def Spambotoff1(self):
        self.Spambotk = XX()
        self.Spambotk.XX1(float(0x9184E729FFFL))
        self.Spambotk.XX2(self.Spambotoff1)

    
    def Spambtn_func(self, arg):
        if arg == 'on':
            self.Spamboton()
        elif arg == 'off':
            self.Spambotoff()
        

    
    def Spambtn_func1(self, arg):
        if arg == 'on':
            self.Spamboton1()
        elif arg == 'off':
            self.Spambotoff1()
        

    
    def Zmienlv_func(self):
        player.SetStatus(player.LEVEL, int(self.Lvlin.GetText()))

    
    def Zmienzbr_func(self):
        chr.ChangeShape(int(self.Zbrin.GetText()))
        chr.Refresh()

    
    def Zmienbrn_func(self):
        chr.SetWeapon(int(self.Bronin.GetText()))
        chr.Refresh()

    
    def Sprawdz_func(self):
        item.SelectItem(int(self.Bronin.GetText()))
        self.BronImg.LoadImage(str(item.GetIconImageFileName()))
        item.SelectItem(int(self.Zbrin.GetText()))
        self.ZbrImg.LoadImage(str(item.GetIconImageFileName()))

    
    def Aura_funcw(self):
        chrmgr.SetAffect(-1, 15, 1)

    
    def Ostrze_funcw(self):
        chrmgr.SetAffect(-1, 19, 1)

    
    def Strach_funcw(self):
        chrmgr.SetAffect(-1, 20, 1)

    
    def Zbroja_funcw(self):
        chrmgr.SetAffect(-1, 21, 1)

    
    def Blogo_funcw(self):
        chrmgr.SetAffect(-1, 22, 1)

    
    def Pomoc_funcw(self):
        chrmgr.SetAffect(-1, 29, 1)

    
    def Odbicie_funcw(self):
        chrmgr.SetAffect(-1, 23, 1)

    
    def Zwiekszenie_funcw(self):
        chrmgr.SetAffect(-1, 30, 1)

    
    def Silne_funcw(self):
        chrmgr.SetAffect(-1, 16, 1)

    
    def Ochronka_funcw(self):
        chrmgr.SetAffect(-1, 25, 1)

    
    def Duch_funcw(self):
        chrmgr.SetAffect(-1, 26, 1)

    
    def Krycie_funcw(self):
        chrmgr.SetAffect(-1, 18, 1)

    
    def Rozpro_funcw(self):
        chrmgr.SetAffect(-1, 32, 1)

    
    def Trucie_funcw(self):
        chrmgr.SetAffect(-1, 3, 1)

    
    def Powstan_funcw(self):
        chr.Revive()

    
    def Zgin_funcw(self):
        chr.Die()

    
    def Nick_funcw(self):
        chr.SetNameString(str(self.Nickin.GetText()))

    
    def GM_funcw(self):
        chrmgr.SetAffect(-1, 0, 1)

    
    def WojM_func(self):
        chr.SetRace(int(0))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def WojK_func(self):
        chr.SetRace(int(4))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def SuraK_func(self):
        chr.SetRace(int(6))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def SuraM_func(self):
        chr.SetRace(int(2))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def NinjaM_func(self):
        chr.SetRace(int(5))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def NinjaK_func(self):
        chr.SetRace(int(1))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def SzamanK_func(self):
        chr.SetRace(int(3))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def SzamanM_func(self):
        chr.SetRace(int(7))
        chr.ChangeShape(int(self.Zbrin.GetText()))

    
    def UstawRace_func(self):
        chr.SetRace(int(self.Racein.GetText()))
        chr.Refresh()

    
    def SprawdzRace_func(self):
        i = player.GetTargetVID()
        chr.SelectInstance(i)
        race = chr.GetRace(i)
        self.Racer1 = self.comp.TextLine(self.WizualnyBoard, 'Race:' + str(int(race)), 115, 276, self.comp.RGB(250, 255, 650))

    
    def Ulepsz_func(self):
        a = int(self.Oileulepszycin.GetText())
        b = int(0)
        if a == 1:
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 2:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 3:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 4:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 5:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 6:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 7:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 8:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        
        if a == 9:
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
            net.SendRefinePacket(SlotUlepszania, b)
        

    
    def Aura_func(self, arg):
        if arg == 'on':
            self.AuraBuff()
        elif arg == 'off':
            self.AuraBuffof()
        

    
    def Berek_func(self, arg):
        if arg == 'on':
            self.BerekBuff()
        elif arg == 'off':
            self.BerekBuffof()
        

    
    def Silne_func(self, arg):
        if arg == 'on':
            self.SilneBuff()
        elif arg == 'off':
            self.SilneBuffof()
        

    
    def Ostrze_func(self, arg):
        if arg == 'on':
            self.OstrzeBuff()
        elif arg == 'off':
            self.OstrzeBuffof()
        

    
    def Strach_func(self, arg):
        if arg == 'on':
            self.StrachBuff()
        elif arg == 'off':
            self.StrachBuffof()
        

    
    def Zbroja_func(self, arg):
        if arg == 'on':
            self.ZbrojaBuff()
        elif arg == 'off':
            self.ZbrojaBuffof()
        

    
    def Ochronka_func(self, arg):
        if arg == 'on':
            self.OchronkaBuff()
        elif arg == 'off':
            self.OchronkaBuffof()
        

    
    def Duch_func(self, arg):
        if arg == 'on':
            self.DuchBuff()
        elif arg == 'off':
            self.DuchBuffof()
        

    
    def Atak_func(self, arg):
        if arg == 'on':
            self.AtakBuff()
        elif arg == 'off':
            self.AtakBuffof()
        

    
    def Zwinnosc_func(self, arg):
        if arg == 'on':
            self.ZwinnoscBuff()
        elif arg == 'off':
            self.ZwinnoscBuffof()
        

    
    def Blogo_func(self, arg):
        if arg == 'on':
            self.BlogoBuff()
        elif arg == 'off':
            self.BlogoBuffof()
        

    
    def Pomoc_func(self, arg):
        if arg == 'on':
            self.PomocBuff()
        elif arg == 'off':
            self.PomocBuffof()
        

    
    def Odbicie_func(self, arg):
        if arg == 'on':
            self.OdbicieBuff()
        elif arg == 'off':
            self.OdbicieBuffof()
        

    
    def horse(self):
        net.SendChatPacket('/ride')

    
    def Skil3(self):
        player.ClickSkillSlot(3)

    
    def Skil4(self):
        player.ClickSkillSlot(4)

    
    def Skil5(self):
        player.ClickSkillSlot(5)

    
    def Skil6(self):
        player.ClickSkillSlot(6)

    
    def AuraBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Aura0 = XX()
        self.Aura0.XX1(1)
        self.Aura0.XX2(self.Skil4)
        self.Aura1 = XX()
        self.Aura1.XX1(1.5)
        self.Aura1.XX2(self.horse)
        self.Aura2 = XX()
        self.Aura2.XX1(int(self.Skill1czas.GetText()))
        self.Aura2.XX2(self.AuraBuff)

    
    def AuraBuffof(self):
        self.Aura2 = XX()
        self.Aura2.XX1(int(0x9184E729FFFL))
        self.Aura2.XX2(self.AuraBuffof)

    
    def BerekBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Berek0 = XX()
        self.Berek0.XX1(1)
        self.Berek0.XX2(self.Skil3)
        self.Berek1 = XX()
        self.Berek1.XX1(1.5)
        self.Berek1.XX2(self.horse)
        self.Berek2 = XX()
        self.Berek2.XX1(int(self.Skill2czas.GetText()))
        self.Berek2.XX2(self.BerekBuff)

    
    def BerekBuffof(self):
        self.Berek2 = XX()
        self.Berek2.XX1(int(0x174876E7FFL))
        self.Berek2.XX2(self.BerekBuffof)

    
    def SilneBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Silne0 = XX()
        self.Silne0.XX1(1)
        self.Silne0.XX2(self.Skil4)
        self.Silne2 = XX()
        self.Silne2.XX1(1.5)
        self.Silne2.XX2(self.horse)
        self.Silne3 = XX()
        self.Silne3.XX1(int(self.Skill1czas.GetText()))
        self.Silne3.XX2(self.SilneBuff)

    
    def SilneBuffof(self):
        self.Silne3 = XX()
        self.Silne3.XX1(int(0x174876E7FFL))
        self.Silne3.XX2(self.SilneBuffof)

    
    def OstrzeBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Ostrze0 = XX()
        self.Ostrze0.XX1(1)
        self.Ostrze0.XX2(self.Skil3)
        self.Ostrze1 = XX()
        self.Ostrze1.XX1(1.5)
        self.Ostrze1.XX2(self.horse)
        self.Ostrze2 = XX()
        self.Ostrze2.XX1(int(self.Skill1czas.GetText()))
        self.Ostrze2.XX2(self.OstrzeBuff)

    
    def OstrzeBuffof(self):
        self.Ostrze2 = XX()
        self.Ostrze2.XX1(int(0x174876E7FFL))
        self.Ostrze2.XX2(self.OstrzeBuffof)

    
    def StrachBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Strach0 = XX()
        self.Strach0.XX1(1)
        self.Strach0.XX2(self.Skil4)
        self.Strach1 = XX()
        self.Strach1.XX1(1.5)
        self.Strach1.XX2(self.horse)
        self.Strach2 = XX()
        self.Strach2.XX1(int(self.Skill2czas.GetText()))
        self.Strach2.XX2(self.StrachBuff)

    
    def StrachBuffof(self):
        self.Strach2 = XX()
        self.Strach2.XX1(int(0x174876E7FFL))
        self.Strach2.XX2(self.StrachBuffof)

    
    def ZbrojaBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Zbroja0 = XX()
        self.Zbroja0.XX1(1)
        self.Zbroja0.XX2(self.Skil5)
        self.Zbroja1 = XX()
        self.Zbroja1.XX1(1.5)
        self.Zbroja1.XX2(self.horse)
        self.Zbroja2 = XX()
        self.Zbroja2.XX1(int(self.Skill3czas.GetText()))
        self.Zbroja2.XX2(self.ZbrojaBuff)

    
    def ZbrojaBuffof(self):
        self.Zbroja2 = XX()
        self.Zbroja2.XX1(int(0x2540BE3FFL))
        self.Zbroja2.XX2(self.ZbrojaBuffof)

    
    def OchronkaBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Ochronka0 = XX()
        self.Ochronka0.XX1(1)
        self.Ochronka0.XX2(self.Skil4)
        self.Ochronka1 = XX()
        self.Ochronka1.XX1(1.5)
        self.Ochronka1.XX2(self.horse)
        self.Ochronka2 = XX()
        self.Ochronka2.XX1(int(self.Skill1czas.GetText()))
        self.Ochronka2.XX2(self.OchronkaBuff)

    
    def OchronkaBuffof(self):
        self.Ochronka2 = XX()
        self.Ochronka2.XX1(int(999999999))
        self.Ochronka2.XX2(self.OchronkaBuffof)

    
    def DuchBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Duch0 = XX()
        self.Duch0.XX1(1)
        self.Duch0.XX2(self.Skil3)
        self.Duch1 = XX()
        self.Duch1.XX1(1.5)
        self.Duch1.XX2(self.horse)
        self.Duch2 = XX()
        self.Duch2.XX1(int(self.Skill2czas.GetText()))
        self.Duch2.XX2(self.DuchBuff)

    
    def DuchBuffof(self):
        self.Duch2 = XX()
        self.Duch2.XX1(int(99999999))
        self.Duch2.XX2(self.DuchBuffof)

    
    def AtakBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Atak0 = XX()
        self.Atak0.XX1(1)
        self.Atak0.XX2(self.Skil6)
        self.Atak1 = XX()
        self.Atak1.XX1(1.5)
        self.Atak1.XX2(self.horse)
        self.Atak2 = XX()
        self.Atak2.XX1(int(self.Skill1czas.GetText()))
        self.Atak2.XX2(self.AtakBuff)

    
    def AtakBuffof(self):
        self.Atak2 = XX()
        self.Atak2.XX1(int(999999999))
        self.Atak2.XX2(self.AtakBuffof)

    
    def ZwinnoscBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Zwinnosc0 = XX()
        self.Zwinnosc0.XX1(1)
        self.Zwinnosc0.XX2(self.Skil5)
        self.Zwinnosc1 = XX()
        self.Zwinnosc1.XX1(1.5)
        self.Zwinnosc1.XX2(self.horse)
        self.Zwinnosc2 = XX()
        self.Zwinnosc2.XX1(int(self.Skill2czas.GetText()))
        self.Zwinnosc2.XX2(self.ZwinnoscBuff)

    
    def ZwinnoscBuffof(self):
        self.Zwinnosc2 = XX()
        self.Zwinnosc2.XX1(int(0x38D7EA4C67FFFL))
        self.Zwinnosc2.XX2(self.ZwinnoscBuffof)

    
    def BlogoBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Blogo0 = XX()
        self.Blogo0.XX1(1)
        self.Blogo0.XX2(self.Skil4)
        self.Blogo1 = XX()
        self.Blogo1.XX1(1.5)
        self.Blogo1.XX2(self.horse)
        self.Blogo2 = XX()
        self.Blogo2.XX1(int(self.Skill1czas.GetText()))
        self.Blogo2.XX2(self.BlogoBuff)

    
    def BlogoBuffof(self):
        self.Blogo2 = XX()
        self.Blogo2.XX1(int(9999999))
        self.Blogo2.XX2(self.BlogoBuffof)

    
    def PomocBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Pomoc0 = XX()
        self.Pomoc0.XX1(1)
        self.Pomoc0.XX2(self.Skil6)
        self.Pomoc1 = XX()
        self.Pomoc1.XX1(1.5)
        self.Pomoc1.XX2(self.horse)
        self.Pomoc2 = XX()
        self.Pomoc2.XX1(int(self.Skill2czas.GetText()))
        self.Pomoc2.XX2(self.PomocBuff)

    
    def PomocBuffof(self):
        self.Pomoc2 = XX()
        self.Pomoc2.XX1(int(999999999))
        self.Pomoc2.XX2(self.PomocBuffof)

    
    def OdbicieBuff(self):
        if player.IsMountingHorse():
            net.SendChatPacket('/unmount')
        
        self.Odbicie0 = XX()
        self.Odbicie0.XX1(1)
        self.Odbicie0.XX2(self.Skil5)
        self.Odbicie1 = XX()
        self.Odbicie1.XX1(1.5)
        self.Odbicie1.XX2(self.horse)
        self.Odbicie2 = XX()
        self.Odbicie2.XX1(int(self.Skill3czas.GetText()))
        self.Odbicie2.XX2(self.OdbicieBuff)

    
    def OdbicieBuffof(self):
        self.Odbicie2 = XX()
        self.Odbicie2.XX1(int(99999999))
        self.Odbicie2.XX2(self.OdbicieBuffof)

    
    def MobberSlotFunc(self):
        global Mobber_ID
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Mobber_ID = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.MobberSlotIcon.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def Set_Poty_1_ID(self):
        global Poty_1_ID
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Poty_1_ID = mouseModule.mouseController.GetAttachedItemIndex()
        
        item.SelectItem(attachedSlotVnum)
        item.SelectItem(int(attachedSlotVnum))
        self.PotySlotIcon.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def Set_Poty_2_ID(self):
        global Poty_2_ID
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Poty_2_ID = mouseModule.mouseController.GetAttachedItemIndex()
        
        item.SelectItem(attachedSlotVnum)
        item.SelectItem(int(attachedSlotVnum))
        self.PotySlotIcon2.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc(self):
        global Otwieracz_ID
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc1(self):
        global Otwieracz_ID1
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID1 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon1.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc2(self):
        global Otwieracz_ID2
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID2 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon2.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc3(self):
        global Otwieracz_ID3
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID3 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon3.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc4(self):
        global Otwieracz_ID4
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID4 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon4.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def OtwieraczSlotFunc5(self):
        global Otwieracz_ID5
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            Otwieracz_ID5 = mouseModule.mouseController.GetAttachedItemIndex()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.OtwieraczSlotIcon5.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def Ulepsz_Item(self):
        global SlotUlepszania
        if mouseModule.mouseController.isAttached():
            attachedSlotType = mouseModule.mouseController.GetAttachedType()
            attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
            attachedSlotVnum = mouseModule.mouseController.GetAttachedItemIndex()
            SlotUlepszania = mouseModule.mouseController.GetAttachedSlotNumber()
            item.SelectItem(attachedSlotVnum)
        
        item.SelectItem(int(attachedSlotVnum))
        self.UlepszanieSlotIcon.LoadImage(str(item.GetIconImageFileName()))
        mouseModule.mouseController.DeattachObject()

    
    def _Dialog1__BuildKeyDict(self):
        onPressKeyDict = { }
        
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

    
    def OpenWindowWykr(self):
        if self.WykrywaczOkno.IsShow():
            self.WykrywaczOkno.Hide()
        else:
            self.WykrywaczOkno.Show()

    
    def OpenWindowDopy(self):
        if self.DopalaczeOknoBoard.IsShow():
            self.DopalaczeOknoBoard.Hide()
        else:
            self.DopalaczeOknoBoard.Show()

    
    def OpenWindowSpam(self):
        if self.Spambotboard.IsShow():
            self.Spambotboard.Hide()
        else:
            self.Spambotboard.Show()

    
    def OpenWindowUstawieniao(self):
        if self.Ustawieniao.IsShow():
            self.Ustawieniao.Hide()
        else:
            self.Ustawieniao.Show()

    
    def OpenWindowTypbicia(self):
        if self.Typstr.IsShow():
            self.Typstr.Hide()
        else:
            self.Typstr.Show()

    
    def OpenWindowUlepsz(self):
        if self.UlepszBoard.IsShow():
            self.UlepszBoard.Hide()
        else:
            self.UlepszBoard.Show()

    
    def OpenWindowPogoda(self):
        if self.Pogoda.IsShow():
            self.Pogoda.Hide()
        else:
            self.Pogoda.Show()

    
    def OpenWindowWizualnyBoard(self):
        if self.WizualnyBoard.IsShow():
            self.WizualnyBoard.Hide()
        else:
            self.WizualnyBoard.Show()

    
    def AutoSkileWindow(self):
        if self.AutoSkileBoard.IsShow():
            self.AutoSkileBoard.Show()
        else:
            self.AutoSkileBoard.Show()

    
    def Close(self):
        self.Board1.Hide()

    
    def CloseWykr(self):
        self.WykrywaczOkno.Hide()

    
    def CloseDopy(self):
        self.DopalaczeOknoBoard.Hide()

    
    def Spambotclose(self):
        self.Spambotboard.Hide()

    
    def Ustawieniaoclose(self):
        self.Ustawieniao.Hide()

    
    def Typstrclose(self):
        self.Typstr.Hide()

    
    def CloseUlepsz(self):
        self.UlepszBoard.Hide()

    
    def ClosePogoda(self):
        self.Pogoda.Hide()

    
    def CloseWizualnyBoard(self):
        self.WizualnyBoard.Hide()

    
    def AutoSkileClose(self):
        self.AutoSkileBoard.Hide()



class XX(ui.ScriptWindow):
    
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        
        self.eventTimeOver = lambda *arg: None
        
        self.eventExit = lambda *arg: None

    
    def __del__(self):
        ui.ScriptWindow.__del__(self)

    
    def XX1(self, waitTime):
        curTime = time.clock()
        self.endTime = curTime + waitTime
        self.Show()

    
    def Close(self):
        self.Hide()

    
    def Destroy(self):
        self.Hide()

    
    def XX2(self, event):
        self.eventTimeOver = ui.__mem_func__(event)

    
    def SAFE_SetExitEvent(self, event):
        self.eventExit = ui.__mem_func__(event)

    
    def OnUpdate(self):
        lastTime = max(0, self.endTime - time.clock())
        if 0 == lastTime:
            self.Close()
            self.eventTimeOver()
        else:
            return None



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
        return (SlotBar, Value)

    
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

    
    def GetCurrentText(self):
        return self.textLine.GetText()

    
    def OnSelectItem(self, index, name):
        self.SetCurrentItem(name)
        self.CloseListBox()
        self.event()

    ui.ComboBox.GetCurrentText = GetCurrentText
    ui.ComboBox.OnSelectItem = OnSelectItem

Okno = Dialog1()
btns = ui.Button()
btns.SetPosition(5, 5)
btns.SetEvent(Okno.Board1.Show)
btns.SetUpVisual('d:/ymir work/ui/public/close_button_01.sub')
btns.SetOverVisual('d:/ymir work/ui/public/close_button_02.sub')
btns.SetDownVisual('d:/ymir work/ui/public/close_button_03.sub')
btns.Show()
