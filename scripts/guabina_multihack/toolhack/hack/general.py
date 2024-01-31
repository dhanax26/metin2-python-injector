import ui
import app
import chat
import chr
import net
import player
import item
import skill
import time
import game
import shop
import chrmgr
import background
import constInfo
import miniMap
import uiminimap
import wndMgr
import math
import uiCommon
import grp

class GeneralDialog(ui.ScriptWindow):
    MoveSpeed1 = 0
    AttackSpeed1 = 0
    MovePercent = 300
    AttackPercent = 200
    
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.LoadGui()

    
    def __del__(self):
        ui.ScriptWindow.__del__(self)

    
    def Close(self):
        self.m2kBoard.Hide()

    
    def LoadGui(self):
        self.m2kBoard = ui.ThinBoard()
        self.m2kBoard.SetPosition(52, 40)
        self.m2kBoard.SetSize(300, 230)
        self.m2kBoard.Show()
        self.comp = Component()
        self.HeaderLabel = self.comp.TextLine(self.m2kBoard, 'General', 130, 8, self.comp.RGB(255, 255, 0))
        self.MovespeedLabel = self.comp.TextLine(self.m2kBoard, '300', 240, 38, self.comp.RGB(255, 255, 255))
        self.AttackspeedLabel = self.comp.TextLine(self.m2kBoard, '250', 240, 78, self.comp.RGB(255, 255, 255))
        self.ImageMovespeed = self.comp.ExpandedImage(self.m2kBoard, 9, 30, str('icon/item/27104.tga'))
        self.ImageAttackspeed = self.comp.ExpandedImage(self.m2kBoard, 9, 70, str('icon/item/27101.tga'))
        self.SlideMovespeed = self.comp.SliderBar(self.m2kBoard, 0.59999999999999998, self.SlideMove, 50, 40)
        self.SlideAttackspeed = self.comp.SliderBar(self.m2kBoard, 0.40000000000000002, self.SlideAttack, 50, 80)
        self.CloseButton = self.comp.Button(self.m2kBoard, '', 'Close', 270, 8, self.Close, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.OneHandedButton = self.comp.Button(self.m2kBoard, '', 'OneHanded', 15, 120, self.OneHand, 'm2kmod/Images/General/onehand_0.tga', 'm2kmod/Images/General/onehand_1.tga', 'm2kmod/Images/General/onehand_0.tga')
        self.TwoHandedButton = self.comp.Button(self.m2kBoard, '', 'TwoHanded', 55, 120, self.TwoHand, 'm2kmod/Images/General/twohand_0.tga', 'm2kmod/Images/General/twohand_1.tga', 'm2kmod/Images/General/twohand_0.tga')
        self.ComboButton = self.comp.Button(self.m2kBoard, '', 'Combo', 95, 120, self.Combo, 'm2kmod/Images/General/combo_0.tga', 'm2kmod/Images/General/combo_1.tga', 'm2kmod/Images/General/combo_0.tga')
        self.ZoomImageButton = self.comp.Button(self.m2kBoard, '', 'Zoom', 135, 120, self.Zoom, 'm2kmod/Images/General/zoom_0.tga', 'm2kmod/Images/General/zoom_1.tga', 'm2kmod/Images/General/zoom_0.tga')
        self.NoFogImageButton = self.comp.Button(self.m2kBoard, '', 'NoFog', 175, 120, self.NoFog, 'm2kmod/Images/General/nofog_0.tga', 'm2kmod/Images/General/nofog_1.tga', 'm2kmod/Images/General/nofog_0.tga')
        self.DayImageButton = self.comp.Button(self.m2kBoard, '', 'Day', 215, 120, self.Day, 'm2kmod/Images/General/sun_0.tga', 'm2kmod/Images/General/sun_1.tga', 'm2kmod/Images/General/sun_0.tga')
        self.NightImageButton = self.comp.Button(self.m2kBoard, '', 'Night', 255, 120, self.Night, 'm2kmod/Images/General/moon_0.tga', 'm2kmod/Images/General/moon_1.tga', 'm2kmod/Images/General/moon_0.tga')
        self.GhostButton = self.comp.Button(self.m2kBoard, '', 'GhostMod', 15, 170, self.GhostMod, 'm2kmod/Images/General/ghost_0.tga', 'm2kmod/Images/General/ghost_1.tga', 'm2kmod/Images/General/ghost_0.tga')
        self.CrashButton = self.comp.Button(self.m2kBoard, '', 'InstantCrash', 255, 170, self.Crash, 'm2kmod/Images/General/crash_0.tga', 'm2kmod/Images/General/crash_1.tga', 'm2kmod/Images/General/crash_0.tga')
        self.GoForward = self.comp.Button(self.m2kBoard, '', 'Forward', 150, 160, self.Forward, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.GoBack = self.comp.Button(self.m2kBoard, '', 'Back', 150, 210, self.Back, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.GoRight = self.comp.Button(self.m2kBoard, '', 'Right', 180, 185, self.Right, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.GoLeft = self.comp.Button(self.m2kBoard, '', 'Left', 120, 185, self.Left, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.MoveOn = self.comp.Button(self.m2kBoard, '', '', 268, 38, self.MoveSpeed, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.MoveOff = self.comp.Button(self.m2kBoard, '', '', 268, 38, self.MoveSpeed, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.MoveOn.Hide()
        self.AttackOn = self.comp.Button(self.m2kBoard, '', '', 268, 78, self.AttackSpeed, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.AttackOff = self.comp.Button(self.m2kBoard, '', '', 268, 78, self.AttackSpeed, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.AttackOn.Hide()
        self.Day()
        Speed = player.GetStatus(player.ATT_SPEED)
        chr.SetAttackSpeed(int(Speed))
        WalkSpeed = player.GetStatus(player.MOVING_SPEED)
        chr.SetMoveSpeed(int(WalkSpeed))

    
    def SlideMove(self):
        self.MovePercent = int(self.SlideMovespeed.GetSliderPos() * 500)
        self.MovespeedLabel.SetText(str(self.MovePercent) + '%')

    
    def SlideAttack(self):
        self.AttackPercent = int(self.SlideAttackspeed.GetSliderPos() * 400)
        self.AttackspeedLabel.SetText(str(self.AttackPercent) + '%')

    
    def AttackSpeed(self):
        if self.AttackSpeed1 == 0:
            self.AttackSpeed1 = 1
            self.AttackOn.Show()
            self.AttackOff.Hide()
            self.AttackSP('On')
        else:
            self.AttackSpeed1 = 0
            self.AttackOff.Show()
            self.AttackOn.Hide()
            self.AttackSP('Off')

    
    def AttackSP(self, state):
        if state == 'On':
            chr.SetAttackSpeed(int(self.AttackPercent))
        else:
            Speed = player.GetStatus(player.ATT_SPEED)
            chr.SetAttackSpeed(int(Speed))

    
    def MoveSpeed(self):
        if self.MoveSpeed1 == 0:
            self.MoveSpeed1 = 1
            self.MoveOn.Show()
            self.MoveOff.Hide()
            self.Movespeed_1()
        else:
            self.MoveSpeed1 = 0
            self.MoveOff.Show()
            self.MoveOn.Hide()
            self.Movespeed_0()

    
    def Movespeed_1(self):
        WalkSpeed = player.GetStatus(player.MOVING_SPEED)
        chr.SetMoveSpeed(int(WalkSpeed))
        chr.SetMoveSpeed(int(self.MovePercent))
        self.Update = WaitingDialog()
        self.Update.Open(int(1.0))
        self.Update.SAFE_SetTimeOverEvent(self.Movespeed_1)

    
    def Movespeed_0(self):
        self.Update = WaitingDialog()
        self.Update.Close()
        WalkSpeed = player.GetStatus(player.MOVING_SPEED)
        chr.SetMoveSpeed(int(WalkSpeed))

    
    def OneHand(self):
        chr.SetMotionMode(chr.MOTION_MODE_ONEHAND_SWORD)

    
    def TwoHand(self):
        chr.SetMotionMode(chr.MOTION_MODE_TWOHAND_SWORD)

    
    def Combo(self):
        chr.testSetComboType(2)

    
    def Zoom(self):
        app.SetCameraMaxDistance(60500)

    
    def NoFog(self):
        app.SetMinFog(12000)

    
    def Day(self):
        background.SetEnvironmentData(0)

    
    def Night(self):
        background.RegisterEnvironmentData(1, constInfo.ENVIRONMENT_NIGHT)
        background.SetEnvironmentData(1)

    
    def GhostMod(self):
        PlayerTP = player.GetStatus(player.HP)
        if PlayerTP < 1:
            chr.Revive()
        else:
            chat.AppendChat(7, 'You have to die and than you can restart in the Ghost-Mod!')

    
    def Crash(self):
        app.Abort()

    
    def Forward(self):
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) - 2000, int(z))
        self.stepbystep()

    
    def Right(self):
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) + 2000, int(y), int(z))
        self.stepbystep()

    
    def Back(self):
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x), int(y) + 2000, int(z))
        self.stepbystep()

    
    def Left(self):
        (x, y, z) = player.GetMainCharacterPosition()
        chr.SetPixelPosition(int(x) - 2000, int(y), int(z))
        self.stepbystep()

    
    def stepbystep(self):
        player.SetSingleDIKKeyState(app.DIK_UP, TRUE)
        player.SetSingleDIKKeyState(app.DIK_UP, FALSE)



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

    
    def TextLine(self, parent, textlineText, x, y, color):
        textline = ui.TextLine()
        if parent != None:
            textline.SetParent(parent)
        
        textline.SetPosition(x, y)
        if color != None:
            textline.SetFontColor(color[0], color[1], color[2])
        
        textline.SetText(textlineText)
        textline.SetOutline()
        textline.Show()
        return textline

    
    def RGB(self, r, g, b):
        return (r * 255, g * 255, b * 255)

    
    def ExpandedImage(self, parent, x, y, img):
        image = ui.ExpandedImageBox()
        if parent != None:
            image.SetParent(parent)
        
        image.SetPosition(x, y)
        image.LoadImage(img)
        image.Show()
        return image

    
    def SliderBar(self, parent, sliderPos, func, x, y):
        Slider = ui.SliderBar()
        if parent != None:
            Slider.SetParent(parent)
        
        Slider.SetPosition(x, y)
        Slider.SetSliderPos(sliderPos)
        Slider.Show()
        Slider.SetEvent(func)
        return Slider

    
    def EditLine(self, parent, width, heigh, x, y, editlineText, max):
        Value = ui.EditLine()
        if parent != None:
            Value.SetParent(parent)
        
        Value.SetSize(width, heigh)
        Value.SetPosition(x, y)
        Value.SetMax(max)
        Value.SetText(editlineText)
        Value.SetNumberMode()
        Value.Show()
        return Value

    
    def SlotBarEditLine(self, parent, editlineText, x, y, width, heigh, max):
        SlotBar = ui.SlotBar()
        if parent != None:
            SlotBar.SetParent(parent)
        
        SlotBar.SetSize(width, heigh)
        SlotBar.SetPosition(x, y)
        SlotBar.Show()
        Value = ui.EditLine()
        Value.SetParent(SlotBar)
        Value.SetSize(width, heigh)
        Value.SetPosition(6, 0)
        Value.SetMax(max)
        Value.SetLimitWidth(width)
        Value.SetMultiLine()
        Value.SetText(editlineText)
        Value.SetNumberMode()
        Value.Show()
        return (SlotBar, Value)



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
            return None

    
    def OnPressExitKey(self):
        self.Close()
        return TRUE



try:
    app.Shop.Close()
except:
    pass

app.Shop = GeneralDialog()
