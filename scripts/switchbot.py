import os, app, dbg, grp, item, background, chr, chrmgr, player, snd, chat, textTail, snd, net, effect, chat, item, net, player, snd, locale, shop, ui, uiTip, wndMgr
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

class EfsunBotuIrcRest(ui.ThinBoard):

    def __init__(self):
        ui.ThinBoard.__init__(self)
        self.YukleEfsunBotuIrcRest()
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '#Editado :$')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '#Editado :$')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '#Editado :$')
        chat.AppendChat(chat.CHAT_TYPE_NOTICE, '#Editado :$')

    def __del__(self):
        ui.ThinBoard.__del__(self)

    def Destroy(self):
        self.Hide()
        return TRUE

    def EfsunNKoduIrcRest(self):
        global ENesneKoduIrcRest
        for i in xrange(player.INVENTORY_PAGE_SIZE * 2):
            itemIndex = player.GetItemIndex(i)
            item.SelectItem(itemIndex)
            ItemValue = player.GetItemIndex(i)
            if item.IsAntiFlag(74112) and item.IsFlag(8196) and item.GetItemSubType() == 18:
                ENesneKoduIrcRest = int(ItemValue)
                break
            else:
                if str(item.GetItemName()) == '|cFF00FF00|H|hBilinmeyen Hata, Hata Kodu : 01C':
                    ENesneKoduIrcRest = int(ItemValue)
                    break

    def YukleEfsunBotuIrcRest(self):
        if str("xxx").find('IrcRest') != -1:
            return
        self.Board = ui.Board()
        self.Board.SetPosition(0, 0)
        self.Board.SetSize(440, 220)
        self.Board.Show()
        self.Board.AddFlag('movable')
        self.Board.AddFlag('float')
        self.LoadTextLines()
        self.FaceButton()
        self.LoadButtons()
        self.LoadEditLines()
        self.EfsunNKoduIrcRest()
        self.BoardMessage = uiTip.BigBoard()

    def LoadEditLines(self):
        self.cRe35SlotBar = ui.SlotBar()
        self.cRe35SlotBar.SetParent(self.Board)
        self.cRe35SlotBar.SetSize(29, 14)
        self.cRe35SlotBar.SetPosition(172, 110)
        self.cRe35SlotBar.SetWindowHorizontalAlignCenter()
        self.cRe35SlotBar.Hide()
        self.Slotbar = ui.EditLine()
        self.Slotbar.SetParent(self.cRe35SlotBar)
        self.Slotbar.SetSize(29, 18)
        self.Slotbar.SetPosition(6, 0)
        self.Slotbar.SetMax(2)
        self.Slotbar.SetNumberMode()
        self.Slotbar.SetText('0')
        self.Slotbar.SetTabEvent(ui.__mem_func__(self.StartSwitchBot))
        self.Slotbar.SetReturnEvent(ui.__mem_func__(self.StartSwitchBot))
        self.Slotbar.Hide()
        self.cRe35EfsunD5SlotBar = ui.SlotBar()
        self.cRe35EfsunD5SlotBar.SetParent(self.Board)
        self.cRe35EfsunD5SlotBar.SetSize(29, 14)
        self.cRe35EfsunD5SlotBar.SetPosition(120, 183)
        self.cRe35EfsunD5SlotBar.Show()
        self.cRe35ED5 = ui.EditLine()
        self.cRe35ED5.SetParent(self.cRe35EfsunD5SlotBar)
        self.cRe35ED5.SetSize(29, 18)
        self.cRe35ED5.SetPosition(6, 0)
        self.cRe35ED5.SetMax(4)
        self.cRe35ED5.SetNumberMode()
        self.cRe35ED5.SetText('0')
        self.cRe35ED5.SetTabEvent(ui.__mem_func__(self.Slotbar.SetFocus))
        self.cRe35ED5.SetReturnEvent(ui.__mem_func__(self.Slotbar.SetFocus))
        self.cRe35ED5.Show()
        self.cRe35EfsunD4SlotBar = ui.SlotBar()
        self.cRe35EfsunD4SlotBar.SetParent(self.Board)
        self.cRe35EfsunD4SlotBar.SetSize(29, 14)
        self.cRe35EfsunD4SlotBar.SetPosition(120, 148)
        self.cRe35EfsunD4SlotBar.Show()
        self.cRe35ED4 = ui.EditLine()
        self.cRe35ED4.SetParent(self.cRe35EfsunD4SlotBar)
        self.cRe35ED4.SetSize(29, 18)
        self.cRe35ED4.SetPosition(6, 0)
        self.cRe35ED4.SetMax(4)
        self.cRe35ED4.SetNumberMode()
        self.cRe35ED4.SetFocus()
        self.cRe35ED4.SetText('0')
        self.cRe35ED4.SetTabEvent(ui.__mem_func__(self.cRe35ED5.SetFocus))
        self.cRe35ED4.SetReturnEvent(ui.__mem_func__(self.cRe35ED5.SetFocus))
        self.cRe35ED4.Show()
        self.cRe35EfsunD3SlotBar = ui.SlotBar()
        self.cRe35EfsunD3SlotBar.SetParent(self.Board)
        self.cRe35EfsunD3SlotBar.SetSize(29, 14)
        self.cRe35EfsunD3SlotBar.SetPosition(120, 113)
        self.cRe35EfsunD3SlotBar.Show()
        self.cRe35ED3 = ui.EditLine()
        self.cRe35ED3.SetParent(self.cRe35EfsunD3SlotBar)
        self.cRe35ED3.SetSize(29, 18)
        self.cRe35ED3.SetPosition(6, 0)
        self.cRe35ED3.SetMax(4)
        self.cRe35ED3.SetNumberMode()
        self.cRe35ED3.SetText('0')
        self.cRe35ED3.SetTabEvent(ui.__mem_func__(self.cRe35ED4.SetFocus))
        self.cRe35ED3.SetReturnEvent(ui.__mem_func__(self.cRe35ED4.SetFocus))
        self.cRe35ED3.Show()
        self.cRe35EfsunD2SlotBar = ui.SlotBar()
        self.cRe35EfsunD2SlotBar.SetParent(self.Board)
        self.cRe35EfsunD2SlotBar.SetSize(29, 14)
        self.cRe35EfsunD2SlotBar.SetPosition(120, 78)
        self.cRe35EfsunD2SlotBar.Show()
        self.cRe35ED2 = ui.EditLine()
        self.cRe35ED2.SetParent(self.cRe35EfsunD2SlotBar)
        self.cRe35ED2.SetSize(29, 18)
        self.cRe35ED2.SetPosition(6, 0)
        self.cRe35ED2.SetMax(4)
        self.cRe35ED2.SetNumberMode()
        self.cRe35ED2.SetText('0')
        self.cRe35ED2.SetTabEvent(ui.__mem_func__(self.cRe35ED3.SetFocus))
        self.cRe35ED2.SetReturnEvent(ui.__mem_func__(self.cRe35ED3.SetFocus))
        self.cRe35ED2.Show()
        self.cRe35EfsunD1SlotBar = ui.SlotBar()
        self.cRe35EfsunD1SlotBar.SetParent(self.Board)
        self.cRe35EfsunD1SlotBar.SetSize(29, 14)
        self.cRe35EfsunD1SlotBar.SetPosition(120, 43)
        self.cRe35EfsunD1SlotBar.Show()
        self.cRe35ED1 = ui.EditLine()
        self.cRe35ED1.SetParent(self.cRe35EfsunD1SlotBar)
        self.cRe35ED1.SetSize(29, 18)
        self.cRe35ED1.SetPosition(6, 0)
        self.cRe35ED1.SetMax(4)
        self.cRe35ED1.SetNumberMode()
        self.cRe35ED1.SetText('0')
        self.cRe35ED1.SetFocus()
        self.cRe35ED1.SetTabEvent(ui.__mem_func__(self.cRe35ED2.SetFocus))
        self.cRe35ED1.SetReturnEvent(ui.__mem_func__(self.cRe35ED2.SetFocus))
        self.cRe35ED1.Show()
        self.segundosSlotBar = ui.SlotBar()
        self.segundosSlotBar.SetParent(self.Board)
        self.segundosSlotBar.SetSize(29, 14)
        self.segundosSlotBar.SetPosition(230, 195)
        self.segundosSlotBar.Show()
        self.segundos = ui.EditLine()
        self.segundos.SetParent(self.segundosSlotBar)
        self.segundos.SetSize(29, 18)
        self.segundos.SetPosition(6, 0)
        self.segundos.SetMax(2)
        self.segundos.SetNumberMode()
        self.segundos.SetText('1')
        self.segundos.SetFocus()
        self.segundos.SetTabEvent(ui.__mem_func__(self.cRe35ED2.SetFocus))
        self.segundos.SetReturnEvent(ui.__mem_func__(self.cRe35ED2.SetFocus))
        self.segundos.Show()

    def FaceButton(self):
        global Boton01Button
        global Boton01Text
        Boton01Button = ui.Button()
        Boton01Button.SetText('')
        Boton01Button.SetPosition(wndMgr.GetScreenWidth() - 100, 190)
        Boton01Button.SetSize(88, 21)
        Boton01Button.SetEvent(ui.__mem_func__(self.Boton01))
        Boton01Button.SetUpVisual('d:/ymir work/ui/public/large_button_01.sub')
        Boton01Button.SetOverVisual('d:/ymir work/ui/public/large_button_02.sub')
        Boton01Button.SetDownVisual('d:/ymir work/ui/public/large_button_03.sub')
        Boton01Button.Hide()
        Boton01Text = ui.TextLine()
        Boton01Text.SetParent(Boton01Button)
        Boton01Text.SetVerticalAlignCenter()
        Boton01Text.SetHorizontalAlignCenter()
        Boton01Text.SetPosition(43, 10)
        Boton01Text.SetText('Bot de bonus')
        Boton01Text.Hide()

    def LoadButtons(self):
        self.cRe35Kapat = ui.Button()
        self.cRe35Kapat.SetParent(self.Board)
        self.cRe35Kapat.SetPosition(399, 10)
        self.cRe35Kapat.SetUpVisual('d:/ymir work/ui/public/close_button_01.sub')
        self.cRe35Kapat.SetOverVisual('d:/ymir work/ui/public/close_button_02.sub')
        self.cRe35Kapat.SetDownVisual('d:/ymir work/ui/public/close_button_03.sub')
        self.cRe35Kapat.SetToolTipText(locale.UI_CLOSE, 0, -23)
        self.cRe35Kapat.SetEvent(ui.__mem_func__(self.Close))
        self.cRe35Kapat.Show()
        self.minimizar = ui.Button()
        self.minimizar.SetParent(self.Board)
        self.minimizar.SetPosition(380, 10)
        self.minimizar.SetUpVisual('d:/ymir work/ui/public/minimize_button_01.sub')
        self.minimizar.SetOverVisual('d:/ymir work/ui/public/minimize_button_02.sub')
        self.minimizar.SetDownVisual('d:/ymir work/ui/public/minimize_button_03.sub')
        self.minimizar.SetToolTipText('Minimizar')
        self.minimizar.SetEvent(ui.__mem_func__(self.Minimizar))
        self.minimizar.Show()
        self.DegercRe35Efsun01 = ui.Button()
        self.DegercRe35Efsun01.SetParent(self.Board)
        self.DegercRe35Efsun01.SetPosition(15, 40)
        self.DegercRe35Efsun01.SetUpVisual('d:/ymir work/ui/public/middle_Button_01.sub')
        self.DegercRe35Efsun01.SetOverVisual('d:/ymir work/ui/public/middle_Button_02.sub')
        self.DegercRe35Efsun01.SetDownVisual('d:/ymir work/ui/public/middle_Button_03.sub')
        self.DegercRe35Efsun01.SetText('1-Bonus')
        self.DegercRe35Efsun01.SetEvent(ui.__mem_func__(self.__Wish_1_Option))
        self.DegercRe35Efsun01.Show()
        self.DegercRe35Efsun02 = ui.Button()
        self.DegercRe35Efsun02.SetParent(self.Board)
        self.DegercRe35Efsun02.SetPosition(15, 75)
        self.DegercRe35Efsun02.SetUpVisual('d:/ymir work/ui/public/middle_Button_01.sub')
        self.DegercRe35Efsun02.SetOverVisual('d:/ymir work/ui/public/middle_Button_02.sub')
        self.DegercRe35Efsun02.SetDownVisual('d:/ymir work/ui/public/middle_Button_03.sub')
        self.DegercRe35Efsun02.SetText('2-Bonus')
        self.DegercRe35Efsun02.SetEvent(ui.__mem_func__(self.__Wish_2_Option))
        self.DegercRe35Efsun02.Show()
        self.DegercRe35Efsun03 = ui.Button()
        self.DegercRe35Efsun03.SetParent(self.Board)
        self.DegercRe35Efsun03.SetPosition(15, 110)
        self.DegercRe35Efsun03.SetUpVisual('d:/ymir work/ui/public/middle_Button_01.sub')
        self.DegercRe35Efsun03.SetOverVisual('d:/ymir work/ui/public/middle_Button_02.sub')
        self.DegercRe35Efsun03.SetDownVisual('d:/ymir work/ui/public/middle_Button_03.sub')
        self.DegercRe35Efsun03.SetText('3-Bonus')
        self.DegercRe35Efsun03.SetEvent(ui.__mem_func__(self.__Wish_3_Option))
        self.DegercRe35Efsun03.Show()
        self.DegercRe35Efsun04 = ui.Button()
        self.DegercRe35Efsun04.SetParent(self.Board)
        self.DegercRe35Efsun04.SetPosition(15, 145)
        self.DegercRe35Efsun04.SetUpVisual('d:/ymir work/ui/public/middle_Button_01.sub')
        self.DegercRe35Efsun04.SetOverVisual('d:/ymir work/ui/public/middle_Button_02.sub')
        self.DegercRe35Efsun04.SetDownVisual('d:/ymir work/ui/public/middle_Button_03.sub')
        self.DegercRe35Efsun04.SetText('4-Bonus')
        self.DegercRe35Efsun04.SetEvent(ui.__mem_func__(self.__Wish_4_Option))
        self.DegercRe35Efsun04.Show()
        self.DegercRe35Efsun05 = ui.Button()
        self.DegercRe35Efsun05.SetParent(self.Board)
        self.DegercRe35Efsun05.SetPosition(15, 180)
        self.DegercRe35Efsun05.SetUpVisual('d:/ymir work/ui/public/middle_Button_01.sub')
        self.DegercRe35Efsun05.SetOverVisual('d:/ymir work/ui/public/middle_Button_02.sub')
        self.DegercRe35Efsun05.SetDownVisual('d:/ymir work/ui/public/middle_Button_03.sub')
        self.DegercRe35Efsun05.SetText('5-Bonus')
        self.DegercRe35Efsun05.SetEvent(ui.__mem_func__(self.__Wish_5_Option))
        self.DegercRe35Efsun05.Show()
        self.cRe35EfsunResetButton = ui.Button()
        self.cRe35EfsunResetButton.SetParent(self.Board)
        self.cRe35EfsunResetButton.SetPosition(160, 160)
        self.cRe35EfsunResetButton.SetUpVisual('d:/ymir work/ui/public/Large_Button_01.sub')
        self.cRe35EfsunResetButton.SetOverVisual('d:/ymir work/ui/public/Large_Button_02.sub')
        self.cRe35EfsunResetButton.SetDownVisual('d:/ymir work/ui/public/Large_Button_03.sub')
        self.cRe35EfsunResetButton.SetText('Limpiar tabla')
        self.cRe35EfsunResetButton.SetEvent(ui.__mem_func__(self.__cRe35EfsunReset))
        self.cRe35EfsunResetButton.Show()
        self.cRe35BotuDurdur = ui.Button()
        self.cRe35BotuDurdur.SetParent(self.Board)
        self.cRe35BotuDurdur.SetPosition(305, 125)
        self.cRe35BotuDurdur.SetUpVisual('d:/ymir work/ui/public/Large_Button_01.sub')
        self.cRe35BotuDurdur.SetOverVisual('d:/ymir work/ui/public/Large_Button_02.sub')
        self.cRe35BotuDurdur.SetDownVisual('d:/ymir work/ui/public/Large_Button_03.sub')
        self.cRe35BotuDurdur.SetEvent(ui.__mem_func__(self.__BreakSwitching))
        self.cRe35BotuDurdur.SetText('Parar Bot')
        self.cRe35BotuDurdur.Show()
        self.cRe35BotuBaslat = ui.Button()
        self.cRe35BotuBaslat.SetParent(self.Board)
        self.cRe35BotuBaslat.SetPosition(305, 100)
        self.cRe35BotuBaslat.SetUpVisual('d:/ymir work/ui/public/Large_Button_01.sub')
        self.cRe35BotuBaslat.SetOverVisual('d:/ymir work/ui/public/Large_Button_02.sub')
        self.cRe35BotuBaslat.SetDownVisual('d:/ymir work/ui/public/Large_Button_03.sub')
        self.cRe35BotuBaslat.SetEvent(ui.__mem_func__(self.StartSwitchBot))
        self.cRe35BotuBaslat.SetText('Comenzar Bot')
        self.cRe35BotuBaslat.Show()

    def LoadTextLines(self):
        self.segundost = ui.TextLine()
        self.segundost.SetParent(self.Board)
        self.segundost.SetDefaultFontName()
        self.segundost.SetPosition(180, 195)
        self.segundost.SetFeather()
        self.segundost.SetText('Velocidad:')
        self.segundost.SetOutline()
        self.segundost.Show()
        self.cRe35Baslik = ui.TextLine()
        self.cRe35Baslik.SetParent(self.Board)
        self.cRe35Baslik.SetDefaultFontName()
        self.cRe35Baslik.SetPosition(135, 15)
        self.cRe35Baslik.SetFeather()
        self.cRe35Baslik.SetText('|cFFFFCC00|H|h #Editado :$')
        self.cRe35Baslik.SetOutline()
        self.cRe35Baslik.Show()
        self.cRe35Baslik2 = ui.TextLine()
        self.cRe35Baslik2.SetParent(self.Board)
        self.cRe35Baslik2.SetDefaultFontName()
        self.cRe35Baslik2.SetPosition(310, 155)
        self.cRe35Baslik2.SetFeather()
        self.cRe35Baslik2.SetText('#Editado :$')
        self.cRe35Baslik2.SetOutline()
        self.cRe35Baslik2.Show()
        self.cRe35Baslik21 = ui.TextLine()
        self.cRe35Baslik21.SetParent(self.Board)
        self.cRe35Baslik21.SetDefaultFontName()
        self.cRe35Baslik21.SetPosition(310, 175)
        self.cRe35Baslik21.SetFeather()
        self.cRe35Baslik21.SetText('#Editado :$')
        self.cRe35Baslik21.SetOutline()
        self.cRe35Baslik21.Show()
        self.cRe35IslemGecmisi = ui.TextLine()
        self.cRe35IslemGecmisi.SetParent(self.Board)
        self.cRe35IslemGecmisi.SetDefaultFontName()
        self.cRe35IslemGecmisi.SetPosition(305, 42)
        self.cRe35IslemGecmisi.SetFeather()
        self.cRe35IslemGecmisi.SetText('|cFFFFCC00|H|hAyuda:')
        self.cRe35IslemGecmisi.SetOutline()
        self.cRe35IslemGecmisi.Show()
        self.cRe35IslemGecmisiYaz = ui.TextLine()
        self.cRe35IslemGecmisiYaz.SetParent(self.Board)
        self.cRe35IslemGecmisiYaz.SetDefaultFontName()
        self.cRe35IslemGecmisiYaz.SetPosition(305, 65)
        self.cRe35IslemGecmisiYaz.SetFeather()
        self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
        self.cRe35IslemGecmisiYaz.SetOutline()
        self.cRe35IslemGecmisiYaz.Show()
        self.cRe35EfsunD1Text = ui.TextLine()
        self.cRe35EfsunD1Text.SetParent(self.Board)
        self.cRe35EfsunD1Text.SetPosition(90, 43)
        self.cRe35EfsunD1Text.SetFeather()
        self.cRe35EfsunD1Text.SetDefaultFontName()
        self.cRe35EfsunD1Text.SetText('Cant:')
        self.cRe35EfsunD1Text.SetOutline()
        self.cRe35EfsunD1Text.Show()
        self.cRe35EfsunD2Text = ui.TextLine()
        self.cRe35EfsunD2Text.SetParent(self.Board)
        self.cRe35EfsunD2Text.SetPosition(90, 78)
        self.cRe35EfsunD2Text.SetFeather()
        self.cRe35EfsunD2Text.SetDefaultFontName()
        self.cRe35EfsunD2Text.SetText('Cant:')
        self.cRe35EfsunD2Text.SetOutline()
        self.cRe35EfsunD2Text.Show()
        self.cRe35EfsunD3Text = ui.TextLine()
        self.cRe35EfsunD3Text.SetParent(self.Board)
        self.cRe35EfsunD3Text.SetPosition(90, 113)
        self.cRe35EfsunD3Text.SetFeather()
        self.cRe35EfsunD3Text.SetDefaultFontName()
        self.cRe35EfsunD3Text.SetText('Cant:')
        self.cRe35EfsunD3Text.SetOutline()
        self.cRe35EfsunD3Text.Show()
        self.cRe35EfsunD4Text = ui.TextLine()
        self.cRe35EfsunD4Text.SetParent(self.Board)
        self.cRe35EfsunD4Text.SetPosition(90, 148)
        self.cRe35EfsunD4Text.SetFeather()
        self.cRe35EfsunD4Text.SetDefaultFontName()
        self.cRe35EfsunD4Text.SetText('Cant:')
        self.cRe35EfsunD4Text.SetOutline()
        self.cRe35EfsunD4Text.Show()
        self.cRe35EfsunD5Text = ui.TextLine()
        self.cRe35EfsunD5Text.SetParent(self.Board)
        self.cRe35EfsunD5Text.SetPosition(90, 183)
        self.cRe35EfsunD5Text.SetFeather()
        self.cRe35EfsunD5Text.SetDefaultFontName()
        self.cRe35EfsunD5Text.SetText('Cant:')
        self.cRe35EfsunD5Text.SetOutline()
        self.cRe35EfsunD5Text.Show()
        self.BonuscRe35Baslik = ui.TextLine()
        self.BonuscRe35Baslik.SetParent(self.Board)
        self.BonuscRe35Baslik.SetDefaultFontName()
        self.BonuscRe35Baslik.SetPosition(165, 42)
        self.BonuscRe35Baslik.SetFeather()
        self.BonuscRe35Baslik.SetText('Tabla de bonus:')
        self.BonuscRe35Baslik.SetOutline()
        self.BonuscRe35Baslik.Show()
        self.cRe35Efsun1Attr = ui.TextLine()
        self.cRe35Efsun1Attr.SetParent(self.Board)
        self.cRe35Efsun1Attr.SetDefaultFontName()
        self.cRe35Efsun1Attr.SetPosition(165, 65 + 13 * 0)
        self.cRe35Efsun1Attr.SetFeather()
        self.cRe35Efsun1Attr.SetText('Bonus')
        self.cRe35Efsun1Attr.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun1Attr.SetOutline()
        self.cRe35Efsun1Attr.Show()
        self.cRe35Efsun1Var = ui.TextLine()
        self.cRe35Efsun1Var.SetParent(self.Board)
        self.cRe35Efsun1Var.SetDefaultFontName()
        self.cRe35Efsun1Var.SetPosition(270, 65 + 13 * 0)
        self.cRe35Efsun1Var.SetFeather()
        self.cRe35Efsun1Var.SetText('0')
        self.cRe35Efsun1Var.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun1Var.SetOutline()
        self.cRe35Efsun1Var.Show()
        self.cRe35Efsun2Attr = ui.TextLine()
        self.cRe35Efsun2Attr.SetParent(self.Board)
        self.cRe35Efsun2Attr.SetDefaultFontName()
        self.cRe35Efsun2Attr.SetPosition(165, 70 + 13 * 1)
        self.cRe35Efsun2Attr.SetFeather()
        self.cRe35Efsun2Attr.SetText('Bonus')
        self.cRe35Efsun2Attr.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun2Attr.SetOutline()
        self.cRe35Efsun2Attr.Show()
        self.cRe35Efsun2Var = ui.TextLine()
        self.cRe35Efsun2Var.SetParent(self.Board)
        self.cRe35Efsun2Var.SetDefaultFontName()
        self.cRe35Efsun2Var.SetPosition(270, 70 + 13 * 1)
        self.cRe35Efsun2Var.SetFeather()
        self.cRe35Efsun2Var.SetText('0')
        self.cRe35Efsun2Var.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun2Var.SetOutline()
        self.cRe35Efsun2Var.Show()
        self.cRe35Efsun3Attr = ui.TextLine()
        self.cRe35Efsun3Attr.SetParent(self.Board)
        self.cRe35Efsun3Attr.SetDefaultFontName()
        self.cRe35Efsun3Attr.SetPosition(165, 75 + 13 * 2)
        self.cRe35Efsun3Attr.SetFeather()
        self.cRe35Efsun3Attr.SetText('Bonus')
        self.cRe35Efsun3Attr.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun3Attr.SetOutline()
        self.cRe35Efsun3Attr.Show()
        self.cRe35Efsun3Var = ui.TextLine()
        self.cRe35Efsun3Var.SetParent(self.Board)
        self.cRe35Efsun3Var.SetDefaultFontName()
        self.cRe35Efsun3Var.SetPosition(270, 75 + 13 * 2)
        self.cRe35Efsun3Var.SetFeather()
        self.cRe35Efsun3Var.SetText('0')
        self.cRe35Efsun3Var.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun3Var.SetOutline()
        self.cRe35Efsun3Var.Show()
        self.cRe35Efsun4Attr = ui.TextLine()
        self.cRe35Efsun4Attr.SetParent(self.Board)
        self.cRe35Efsun4Attr.SetDefaultFontName()
        self.cRe35Efsun4Attr.SetPosition(165, 80 + 13 * 3)
        self.cRe35Efsun4Attr.SetFeather()
        self.cRe35Efsun4Attr.SetText('Bonus')
        self.cRe35Efsun4Attr.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun4Attr.SetOutline()
        self.cRe35Efsun4Attr.Show()
        self.cRe35Efsun4Var = ui.TextLine()
        self.cRe35Efsun4Var.SetParent(self.Board)
        self.cRe35Efsun4Var.SetDefaultFontName()
        self.cRe35Efsun4Var.SetPosition(270, 80 + 13 * 3)
        self.cRe35Efsun4Var.SetFeather()
        self.cRe35Efsun4Var.SetText('0')
        self.cRe35Efsun4Var.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun4Var.SetOutline()
        self.cRe35Efsun4Var.Show()
        self.cRe35Efsun5Attr = ui.TextLine()
        self.cRe35Efsun5Attr.SetParent(self.Board)
        self.cRe35Efsun5Attr.SetDefaultFontName()
        self.cRe35Efsun5Attr.SetPosition(165, 85 + 13 * 4)
        self.cRe35Efsun5Attr.SetFeather()
        self.cRe35Efsun5Attr.SetText('Bonus')
        self.cRe35Efsun5Attr.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun5Attr.SetOutline()
        self.cRe35Efsun5Attr.Show()
        self.cRe35Efsun5Var = ui.TextLine()
        self.cRe35Efsun5Var.SetParent(self.Board)
        self.cRe35Efsun5Var.SetDefaultFontName()
        self.cRe35Efsun5Var.SetPosition(270, 85 + 13 * 4)
        self.cRe35Efsun5Var.SetFeather()
        self.cRe35Efsun5Var.SetText('0')
        self.cRe35Efsun5Var.SetFontColor(1.0, 1.0, 1.0)
        self.cRe35Efsun5Var.SetOutline()
        self.cRe35Efsun5Var.Show()

    def __BreakSwitching(self):
        global EfsunSButonIrcRest
        if EfsunSButonIrcRest == 1:
            self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
            chat.AppendChat(chat.CHAT_TYPE_INFO, 'El bot ha sido parado!')
            EfsunSButonIrcRest = 0

    def StartSwitchBot(self):
        global EfsunSButonIrcRest
        EfsunSButonIrcRest = 1
        self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
        chat.AppendChat(chat.CHAT_TYPE_INFO, 'El bot ha comenzado!')
        self.cRe35BotuDurdur.SetText('Parar bot')
        self.__Switchtingdialog()

    def __Switchtingdialog(self):
        global cRe35Efsun4
        global EfsunSButonIrcRest
        global cRe35Efsun2
        global cRe35Efsun0
        global cRe35Efsun1
        global cRe35Efsun3
        Slot = self.Slotbar.GetText()
        val0, bon0 = player.GetItemAttribute(int(Slot), 0)
        val1, bon1 = player.GetItemAttribute(int(Slot), 1)
        val2, bon2 = player.GetItemAttribute(int(Slot), 2)
        val3, bon3 = player.GetItemAttribute(int(Slot), 3)
        val4, bon4 = player.GetItemAttribute(int(Slot), 4)
        Switchvalue = ENesneKoduIrcRest
        Search0 = self.cRe35ED1.GetText()
        Search1 = self.cRe35ED2.GetText()
        Search2 = self.cRe35ED3.GetText()
        Search3 = self.cRe35ED4.GetText()
        Search4 = self.cRe35ED5.GetText()
        DELAY_SEC = self.segundos.GetText()
        if EfsunSButonIrcRest == 1:
            if int(cRe35Efsun1) == 0 and (val0 == int(cRe35Efsun0) and bon0 >= int(Search0) or val1 == int(cRe35Efsun0) and bon1 >= int(Search0) or val2 == int(cRe35Efsun0) and bon2 >= int(Search0) or val3 == int(cRe35Efsun0) and bon3 >= int(Search0) or val4 == int(cRe35Efsun0) and bon4 >= int(Search0)):
                self.BoardMessage.SetTip('#Editado :$')
                self.BoardMessage.SetTop()
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
                EfsunSButonIrcRest = 0
            if int(cRe35Efsun2) == 0 and (val0 == int(cRe35Efsun0) and bon0 >= int(Search0) or val1 == int(cRe35Efsun0) and bon1 >= int(Search0) or val2 == int(cRe35Efsun0) and bon2 >= int(Search0) or val3 == int(cRe35Efsun0) and bon3 >= int(Search0) or val4 == int(cRe35Efsun0) and bon4 >= int(Search0)) and (val0 == int(cRe35Efsun1) and bon0 >= int(Search1) or val1 == int(cRe35Efsun1) and bon1 >= int(Search1) or val2 == int(cRe35Efsun1) and bon2 >= int(Search1) or val3 == int(cRe35Efsun1) and bon3 >= int(Search1) or val4 == int(cRe35Efsun1) and bon4 >= int(Search1)):
                self.BoardMessage.SetTip('#Editado :$')
                self.BoardMessage.SetTop()
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
                EfsunSButonIrcRest = 0
            if int(cRe35Efsun3) == 0 and (val0 == int(cRe35Efsun0) and bon0 >= int(Search0) or val1 == int(cRe35Efsun0) and bon1 >= int(Search0) or val2 == int(cRe35Efsun0) and bon2 >= int(Search0) or val3 == int(cRe35Efsun0) and bon3 >= int(Search0) or val4 == int(cRe35Efsun0) and bon4 >= int(Search0)) and (val0 == int(cRe35Efsun1) and bon0 >= int(Search1) or val1 == int(cRe35Efsun1) and bon1 >= int(Search1) or val2 == int(cRe35Efsun1) and bon2 >= int(Search1) or val3 == int(cRe35Efsun1) and bon3 >= int(Search1) or val4 == int(cRe35Efsun1) and bon4 >= int(Search1)) and (val0 == int(cRe35Efsun2) and bon0 >= int(Search2) or val1 == int(cRe35Efsun2) and bon1 >= int(Search2) or val2 == int(cRe35Efsun2) and bon2 >= int(Search2) or val3 == int(cRe35Efsun2) and bon3 >= int(Search2) or val4 == int(cRe35Efsun2) and bon4 >= int(Search2)):
                self.BoardMessage.SetTip('#Editado :$')
                self.BoardMessage.SetTop()
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
                EfsunSButonIrcRest = 0
            if int(cRe35Efsun4) == 0 and (val0 == int(cRe35Efsun0) and bon0 >= int(Search0) or val1 == int(cRe35Efsun0) and bon1 >= int(Search0) or val2 == int(cRe35Efsun0) and bon2 >= int(Search0) or val3 == int(cRe35Efsun0) and bon3 >= int(Search0) or val4 == int(cRe35Efsun0) and bon4 >= int(Search0)) and (val0 == int(cRe35Efsun1) and bon0 >= int(Search1) or val1 == int(cRe35Efsun1) and bon1 >= int(Search1) or val2 == int(cRe35Efsun1) and bon2 >= int(Search1) or val3 == int(cRe35Efsun1) and bon3 >= int(Search1) or val4 == int(cRe35Efsun1) and bon4 >= int(Search1)) and (val0 == int(cRe35Efsun2) and bon0 >= int(Search2) or val1 == int(cRe35Efsun2) and bon1 >= int(Search2) or val2 == int(cRe35Efsun2) and bon2 >= int(Search2) or val3 == int(cRe35Efsun2) and bon3 >= int(Search2) or val4 == int(cRe35Efsun2) and bon4 >= int(Search2)) and (val0 == int(cRe35Efsun3) and bon0 >= int(Search3) or val1 == int(cRe35Efsun3) and bon1 >= int(Search3) or val2 == int(cRe35Efsun3) and bon2 >= int(Search3) or val3 == int(cRe35Efsun3) and bon3 >= int(Search3) or val4 == int(cRe35Efsun3) and bon4 >= int(Search3)):
                self.BoardMessage.SetTip('#Editado :$')
                self.BoardMessage.SetTop()
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
                EfsunSButonIrcRest = 0
            if int(cRe35Efsun4) != 0 and (val0 == int(cRe35Efsun0) and bon0 >= int(Search0) or val1 == int(cRe35Efsun0) and bon1 >= int(Search0) or val2 == int(cRe35Efsun0) and bon2 >= int(Search0) or val3 == int(cRe35Efsun0) and bon3 >= int(Search0) or val4 == int(cRe35Efsun0) and bon4 >= int(Search0)) and (val0 == int(cRe35Efsun1) and bon0 >= int(Search1) or val1 == int(cRe35Efsun1) and bon1 >= int(Search1) or val2 == int(cRe35Efsun1) and bon2 >= int(Search1) or val3 == int(cRe35Efsun1) and bon3 >= int(Search1) or val4 == int(cRe35Efsun1) and bon4 >= int(Search1)) and (val0 == int(cRe35Efsun2) and bon0 >= int(Search2) or val1 == int(cRe35Efsun2) and bon1 >= int(Search2) or val2 == int(cRe35Efsun2) and bon2 >= int(Search2) or val3 == int(cRe35Efsun2) and bon3 >= int(Search2) or val4 == int(cRe35Efsun2) and bon4 >= int(Search2)) and (val0 == int(cRe35Efsun3) and bon0 >= int(Search3) or val1 == int(cRe35Efsun3) and bon1 >= int(Search3) or val2 == int(cRe35Efsun3) and bon2 >= int(Search3) or val3 == int(cRe35Efsun3) and bon3 >= int(Search3) or val4 == int(cRe35Efsun3) and bon4 >= int(Search3)) and (val0 == int(cRe35Efsun4) and bon0 >= int(Search4) or val1 == int(cRe35Efsun4) and bon1 >= int(Search4) or val2 == int(cRe35Efsun4) and bon2 >= int(Search4) or val3 == int(cRe35Efsun4) and bon3 >= int(Search4) or val4 == int(cRe35Efsun4) and bon4 >= int(Search4)):
                self.BoardMessage.SetTip('#Editado :$')
                self.BoardMessage.SetTop()
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
                EfsunSButonIrcRest = 0
            if cRe35Efsun0 == 0:
                EfsunSButonIrcRest = 0
                self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
            self.WaitingDelay = WaitingDialog()
            self.WaitingDelay.Open(float(DELAY_SEC))
            self.WaitingDelay.SAFE_SetTimeOverEvent(self.__Switchtingdialog)
            for eachSlot in xrange(player.INVENTORY_PAGE_SIZE * 2):
                itemVNum = player.GetItemIndex(eachSlot)
                if itemVNum == int(Switchvalue):
                    net.SendItemUseToItemPacket(eachSlot, int(Slot))
                    break

            if player.GetItemCountByVnum(int(Switchvalue)) <= 1:
                for eachSlot in xrange(shop.SHOP_SLOT_COUNT):
                    getShopItemID = shop.GetItemID(eachSlot)
                    if getShopItemID == int(Switchvalue) and not itemVNum == int(Switchvalue):
                        net.SendShopBuyPacket(eachSlot)

    def __cRe35EfsunReset(self):
        global cRe35Efsun4
        global cRe35Efsun2
        global cRe35Efsun0
        global cRe35Efsun1
        global cRe35Efsun3
        cRe35Efsun0 = 0
        cRe35Efsun1 = 0
        cRe35Efsun2 = 0
        cRe35Efsun3 = 0
        cRe35Efsun4 = 0
        self.cRe35ED1.SetText('0')
        self.cRe35ED2.SetText('0')
        self.cRe35ED3.SetText('0')
        self.cRe35ED4.SetText('0')
        self.cRe35ED5.SetText('0')
        self.cRe35Efsun1Attr.SetText('Bonus')
        self.cRe35Efsun2Attr.SetText('Bonus')
        self.cRe35Efsun3Attr.SetText('Bonus')
        self.cRe35Efsun4Attr.SetText('Bonus')
        self.cRe35Efsun5Attr.SetText('Bonus')
        self.cRe35IslemGecmisiYaz.SetText('Tener la tienda abierta')
        chat.AppendChat(chat.CHAT_TYPE_INFO, 'Se ha limiado la tabla correctamente')

    def __Wish_1_Option(self):
        global cRe35Bot0
        cRe35Bot0 = 1
        self.BonusListBox = FileListDialog()

    def __Wish_2_Option(self):
        global cRe35Bot1
        cRe35Bot1 = 1
        self.BonusListBox = FileListDialog()

    def __Wish_3_Option(self):
        global cRe35Bot2
        cRe35Bot2 = 1
        self.BonusListBox = FileListDialog()

    def __Wish_4_Option(self):
        global cRe35Bot3
        cRe35Bot3 = 1
        self.BonusListBox = FileListDialog()

    def __Wish_5_Option(self):
        global cRe35Bot4
        cRe35Bot4 = 1
        self.BonusListBox = FileListDialog()

    def OnUpdate(self):
        if self.cRe35Efsun1Attr.GetText() != str(BonusListe[int(cRe35Efsun0)]) and int(cRe35Efsun0) != 0:
            self.cRe35Efsun1Attr.SetText(str(BonusListe[int(cRe35Efsun0)]))
        else:
            if self.cRe35Efsun1Attr.GetText() != '' and int(cRe35Efsun0) == 0:
                self.cRe35Efsun1Attr.SetText('Bonus')
        if self.cRe35Efsun2Attr.GetText() != str(BonusListe[int(cRe35Efsun1)]) and int(cRe35Efsun1) != 0:
            self.cRe35Efsun2Attr.SetText(str(BonusListe[int(cRe35Efsun1)]))
        else:
            if self.cRe35Efsun2Attr.GetText() != '' and int(cRe35Efsun1) == 0:
                self.cRe35Efsun2Attr.SetText('Bonus')
        if self.cRe35Efsun3Attr.GetText() != str(BonusListe[int(cRe35Efsun2)]) and int(cRe35Efsun2) != 0:
            self.cRe35Efsun3Attr.SetText(str(BonusListe[int(cRe35Efsun2)]))
        else:
            if self.cRe35Efsun3Attr.GetText() != '' and int(cRe35Efsun2) == 0:
                self.cRe35Efsun3Attr.SetText('Bonus')
        if self.cRe35Efsun4Attr.GetText() != str(BonusListe[int(cRe35Efsun3)]) and int(cRe35Efsun3) != 0:
            self.cRe35Efsun4Attr.SetText(str(BonusListe[int(cRe35Efsun3)]))
        else:
            if self.cRe35Efsun4Attr.GetText() != '' and int(cRe35Efsun3) == 0:
                self.cRe35Efsun4Attr.SetText('Bonus')
        if self.cRe35Efsun5Attr.GetText() != str(BonusListe[int(cRe35Efsun4)]) and int(cRe35Efsun4) != 0:
            self.cRe35Efsun5Attr.SetText(str(BonusListe[int(cRe35Efsun4)]))
        else:
            if self.cRe35Efsun5Attr.GetText() != '' and int(cRe35Efsun4) == 0:
                self.cRe35Efsun5Attr.SetText('Bonus')
        if self.cRe35Efsun1Var.GetText() != self.cRe35ED1.GetText():
            self.cRe35Efsun1Var.SetText(str(self.cRe35ED1.GetText()))
        if self.cRe35Efsun2Var.GetText() != self.cRe35ED2.GetText():
            self.cRe35Efsun2Var.SetText(str(self.cRe35ED2.GetText()))
        if self.cRe35Efsun3Var.GetText() != self.cRe35ED3.GetText():
            self.cRe35Efsun3Var.SetText(str(self.cRe35ED3.GetText()))
        if self.cRe35Efsun4Var.GetText() != self.cRe35ED4.GetText():
            self.cRe35Efsun4Var.SetText(str(self.cRe35ED4.GetText()))
        if self.cRe35Efsun5Var.GetText() != self.cRe35ED5.GetText():
            self.cRe35Efsun5Var.SetText(str(self.cRe35ED5.GetText()))

    def Show(self):
        ui.ThinBoard.Show(self)

    def Boton01(self):
        self.Board.Show()
        Boton01Button.Hide()
        Boton01Text.Hide()

    def Minimizar(self):
        self.Board.Hide()
        Boton01Button.Show()
        Boton01Text.Show()

    def Close(self):
        self.Board.Hide()
        return TRUE

    def OnPressEscapeKey(self):
        self.Hide()
        return TRUE


BonusListe = ('', 'Maxima HP', 'Maxima SP', 'Vitalidad', 'Inteligencia', 'Fuerza', 'Destreza', 'Velocidad de ataque', 'Velocidad de movimiento', 'Velocidad de hechizo', 'Regeneracion de hp', 'Regeneracion de sp', 'Probabilidad de envenenamiento', 'Probabilidad de desmayo (Apagon)', 'Probabilidad de retardo', 'Probabilidad de golpes criticos', 'Probabilidad de penetracion', 'Fuerza contra mediohumanos', 'Fuerza contra animales', 'Fuerza contra orcos', 'Fuerza contra misticos', 'Fuerza contra nomuerto', 'Fuerza contra demonios', 'El dao sera absorbido por HP', 'El dao sera absorbido por SP', '-----', '-----', 'Probabilidad de bloquear golpes cuerpo a cuerpo', 'Probabilidad de evitar flecha', 'Defensa a espada', 'Defensa a espada de dos manos', 'Defensa a daga', 'Defensa a campana', 'Defensa a fan', 'Resistencia a flechas', 'Recistencia a fuego', 'Recistencia a relampago', 'Recistencia a magia', 'Recistencia a viento', 'Probabilidad de reflectar golpes cuerpo a cuerpo', '-----', 'Recistencia Veneno', 'Probabilidad de regeneracion sp', 'Probablidad de bonus exp', 'Probabilidad de caer doble de yang', 'Probabilidad de caer doble de objetos', '-----', 'Probabilidad de regeneracion hpP', 'Defensa a apagon', 'Defensa a retardo',
 '-----', '-', 'Valor de ataque', '-----',
 '-----', '-----', '-----', '-----', '-----', 'Fuerza contra guerrero', 'Fuerza contra Ninja', 'Fuerza contra Sura', 'Fuerza contra Chaman', 'Fuerza contra monstruos', '-----', '-----', '-----', '-----', '-----', '-----', '-----', 'Dao de habilidad', 'Dao de media', '-----', '-----', '-----', '-----', '-----', 'Recistencia a guerrero', 'Recistencia a ninja', 'Recistencia a sura', 'Recistencia a Chaman')
BonusIDListe = {'': 0,'Maxima HP': 1,'Maxima SP': 2,'Vitalidad': 3,'Inteligencia': 4,'Fuerza': 5,'Destreza': 6,'Velocidad de ataque': 7,'Velocidad de movimiento': 8,'Velocidad de hechizo': 9,'Regeneracion de hp': 10,'Regeneracion de sp': 11,'Probabilidad de envenenamiento': 12,'Probabilidad de desmayo (Apagon)': 13,'Probabilidad de retardo': 14,'Probabilidad de golpes criticos': 15,'Probabilidad de penetracion': 16,'Fuerza contra mediohumanos': 17,'Fuerza contra animales': 18,'Fuerza contra orcos': 19,'Fuerza contra misticos': 20,'Fuerza contra nomuerto': 21,'Fuerza contra demonios': 22,'El dao sera absorbido por HP': 23,'El dao sera absorbido por SP': 24,'-----': 25,'-----': 26,'Probabilidad de bloquear golpes cuerpo a cuerpo': 27,'Probabilidad de evitar flecha': 28,'Defensa a espada': 29,'Defensa a espada de dos manos': 30,'Defensa a daga': 31,'Defensa a campana': 32,'Defensa a fan': 33,'Resistencia a flechas': 34,'Recistencia a fuego': 35,'Recistencia a relampago': 36,'Recistencia a magia': 37,'Recistencia a viento': 38,'Probabilidad de reflectar golpes cuerpo a cuerpo': 39,'-----': 40,'Recistencia Veneno': 41,'Probabilidad de regeneracion sp': 42,'Probablidad de bonus exp': 43,'Probabilidad de caer doble de yang': 44,'Probabilidad de caer doble de objetos': 45,'-----': 46,'Probabilidad de regeneracion hp': 47,'Defensa a apagon': 48,'Defensa a retardo': 49,'-----': 50,'-----': 51,'Valor de ataque': 52,'-----': 53,'-----': 54,'-----': 55,'-----': 56,'-----': 57,'-----': 58,'Fuerza contra guerrero': 59,'Fuerza contra Ninja': 60,'Fuerza contra Sura': 61,'Fuerza contra Chaman': 62,'Fuerza contra monstruos': 63,'-----': 64,'-----': 65,'-----': 66,'-----': 67,'-----': 68,'Max. TP (???)': 69,'Max. MP (???)': 70,'Dao de habilidad': 71,'Dao de media': 72,'-----': 73,'-----': 74,'-': 75,'-----': 76,'-----': 77,'Recistencia a guerrero': 78,'Recistencia a ninja': 79,'Recistencia a sura': 80,'Recistencia a Chaman': 81}

class FileListDialog(ui.ThinBoard):

    def __init__(self):
        ui.ThinBoard.__init__(self)
        self.isLoaded = 0
        self.selectEvent = None
        self.fileListBox = None
        self.SetPosition(438, -30)
        self.SetSize(300, 250)
        self.Show()
        self.AddFlag('movable')
        self.AddFlag('float')
        return

    def __del__(self):
        ui.ThinBoard.__del__(self)

    def Show(self):
        if self.isLoaded == 0:
            self.isLoaded = 1
            self.__Load()
        ui.ThinBoard.Show(self)

    def Open(self):
        self.Show()
        self.SetCenterPosition()
        self.SetTop()
        self.UpdateFileList()

    def Close(self):
        self.Hide()

    def OnPressEscapeKey(self):
        self.Close()
        return TRUE

    def __CreateFileListBox(self):
        fileListBox = ui.ListBoxEx()
        fileListBox.SetParent(self)
        fileListBox.SetPosition(15, 50)
        fileListBox.Show()
        return fileListBox

    def __Load(self):
        self.IkinciIrcRestKisim()
        self.UpdateFileList()

    def IkinciIrcRestKisim(self):
        self.fileListBox = self.__CreateFileListBox()
        self.EfsunScrollTarafiIrcRest()
        self.LoadTextLines()
        self.fileListBox.SetScrollBar(self.ScrollBar)
        self.UpdateButton = ui.Button()
        self.UpdateButton.SetParent(self)
        self.UpdateButton.SetUpVisual('d:/ymir work/ui/public/middle_button_01.sub')
        self.UpdateButton.SetOverVisual('d:/ymir work/ui/public/middle_button_02.sub')
        self.UpdateButton.SetDownVisual('d:/ymir work/ui/public/middle_button_03.sub')
        self.UpdateButton.SetText('Gncelletirme')
        self.UpdateButton.SetPosition(15, 265)
        self.UpdateButton.SetEvent(ui.__mem_func__(self.UpdateFileList))
        self.UpdateButton.Show()
        self.UpdateButton.Hide()
        self.SelectBonus = ui.Button()
        self.SelectBonus.SetParent(self)
        self.SelectBonus.SetPosition(210, 220)
        self.SelectBonus.SetUpVisual('d:/ymir work/ui/public/Middle_Button_01.sub')
        self.SelectBonus.SetOverVisual('d:/ymir work/ui/public/Middle_Button_02.sub')
        self.SelectBonus.SetDownVisual('d:/ymir work/ui/public/Middle_Button_03.sub')
        self.SelectBonus.SetText('Seleccionar')
        self.SelectBonus.SetEvent(ui.__mem_func__(self.SetBonis))
        self.SelectBonus.Show()
        self.CancelBonus = ui.Button()
        self.CancelBonus.SetParent(self)
        self.CancelBonus.SetPosition(285, 15)
        self.CancelBonus.SetUpVisual('d:/ymir work/ui/public/close_Button_01.sub')
        self.CancelBonus.SetOverVisual('d:/ymir work/ui/public/close_Button_02.sub')
        self.CancelBonus.SetDownVisual('d:/ymir work/ui/public/close_Button_03.sub')
        self.CancelBonus.SetEvent(ui.__mem_func__(self.Close))
        self.CancelBonus.Show()

    def LoadTextLines(self):
        self.copyright = ui.TextLine()
        self.copyright.SetParent(self)
        self.copyright.SetDefaultFontName()
        self.copyright.SetPosition(120, 29)
        self.copyright.SetFeather()
        self.copyright.SetText('|cFFFFCC00|H|h Elige el bonus')
        self.copyright.SetOutline()
        self.copyright.Show()

    def EfsunScrollTarafiIrcRest(self):
        self.ScrollBar = ui.ScrollBar()
        self.ScrollBar.SetParent(self)
        self.ScrollBar.SetPosition(280, 45)
        self.ScrollBar.SetScrollBarSize(180)
        self.ScrollBar.Show()

    def cRe35Copyright(self):
        self.guildNameBoard.Close()
        self.guildNameBoard = None
        return TRUE
        return

    def UpdateFileList(self):
        self.cRe35Yenile()
        for BonusType in BonusListe:
            if BonusType == '':
                self.fileListBox.AppendItem(Item('|cFFFFCC00|H|h _________________________________________________________________________________________________             '))
            else:
                if BonusType != '':
                    self.fileListBox.AppendItem(Item(BonusType))

    def cRe35Yenile(self):
        self.fileListBox.RemoveAllItems()

    def SetBonis(self):
        global cRe35Bot4
        global cRe35Bot3
        global cRe35Efsun1
        global cRe35Bot0
        global cRe35Efsun3
        global cRe35Efsun4
        global cRe35Efsun2
        global cRe35Bot2
        global cRe35Efsun0
        global cRe35Bot1
        SelectedIndex = self.fileListBox.GetSelectedItem()
        SelectedIndex = SelectedIndex.GetText()
        if str(SelectedIndex) != '' and str(SelectedIndex) != '':
            if cRe35Bot0 == 1:
                chat.AppendChat(chat.CHAT_TYPE_INFO, ' 1.Bonus ' + '|cFFFFCC00|H|h ' + str(SelectedIndex) + '  ')
                cRe35Efsun0 = BonusIDListe[str(SelectedIndex)]
                cRe35Bot0 = 0
            else:
                if cRe35Bot1 == 1:
                    chat.AppendChat(chat.CHAT_TYPE_INFO, ' 2.Bonus ' + '|cFFFFCC00|H|h ' + str(SelectedIndex) + '  ')
                    cRe35Efsun1 = int(BonusIDListe[SelectedIndex])
                    cRe35Bot1 = 0
                else:
                    if cRe35Bot2 == 1:
                        chat.AppendChat(chat.CHAT_TYPE_INFO, ' 3.Bonus ' + '|cFFFFCC00|H|h ' + str(SelectedIndex) + ' ')
                        cRe35Efsun2 = int(BonusIDListe[SelectedIndex])
                        cRe35Bot2 = 0
                    else:
                        if cRe35Bot3 == 1:
                            chat.AppendChat(chat.CHAT_TYPE_INFO, ' 4.Bonus ' + '|cFFFFCC00|H|h ' + str(SelectedIndex) + ' ')
                            cRe35Efsun3 = int(BonusIDListe[SelectedIndex])
                            cRe35Bot3 = 0
                        else:
                            if cRe35Bot4 == 1:
                                chat.AppendChat(chat.CHAT_TYPE_INFO, ' 5.Bonus ' + '|cFFFFCC00|H|h ' + str(SelectedIndex) + '  ')
                                cRe35Efsun4 = int(BonusIDListe[SelectedIndex])
                                cRe35Bot4 = 0
        else:
            chat.AppendChat(chat.CHAT_TYPE_INFO, ' ')
        self.Close()


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


FILE_NAME_LEN = 60

class Item(ui.ListBoxEx.Item):

    def __init__(self, fileName):
        ui.ListBoxEx.Item.__init__(self)
        self.canLoad = 0
        self.text = fileName
        self.textLine = self.cRe35SakinEditlemeyin(fileName[:FILE_NAME_LEN])

    def __del__(self):
        ui.ListBoxEx.Item.__del__(self)

    def GetText(self):
        return self.text

    def SetSize(self, width, height):
        ui.ListBoxEx.Item.SetSize(self, 6 * len(self.textLine.GetText()) + 4, height)

    def cRe35SakinEditlemeyin(self, fileName):
        textLine = ui.TextLine()
        textLine.SetParent(self)
        textLine.SetPosition(0, 0)
        textLine.SetText(fileName)
        textLine.Show()
        return textLine


StartDialog = EfsunBotuIrcRest()
StartDialog.Show()