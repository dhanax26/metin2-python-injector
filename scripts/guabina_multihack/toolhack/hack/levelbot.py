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
import event
import game
import os

class LevelbotDialog(ui.ScriptWindow):
    Levelbot = 0
    State = 0
    RestartPot = 0
    ActiveSkill = 0
    Buffskill1 = 0
    Buffskill2 = 0
    Damageskill = 0
    Horse = 0
    Tau = 1
    Rotate = 1
    RedPercent = 90
    BluePercent = 30
    TapfiSec = 20
    Line1 = 0
    SkillIndex = 0
    DeathSkill = 0
    
    def __init__(self):
        ui.ScriptWindow.__init__(self)
        self.Gui = []
        self.LoadGui()

    
    def __del__(self):
        ui.ScriptWindow.__del__(self)

    
    def Close(self):
        self.m2kBoard.Hide()

    
    def LoadGui(self):
        self.m2kBoard = ui.ThinBoard()
        self.m2kBoard.SetPosition(52, 40)
        self.m2kBoard.SetSize(300, 300)
        self.m2kBoard.Show()
        self.comp = Component()
        self.HeaderLabel = self.comp.TextLine(self.m2kBoard, 'Levelbot', 130, 8, self.comp.RGB(255, 255, 0))
        self.RedLabel = self.comp.TextLine(self.m2kBoard, '90 %', 240, 38, self.comp.RGB(255, 255, 255))
        self.BlueLabel = self.comp.TextLine(self.m2kBoard, '30 %', 240, 78, self.comp.RGB(255, 255, 255))
        self.TapfiLabel = self.comp.TextLine(self.m2kBoard, '20 Sec.', 240, 118, self.comp.RGB(255, 255, 255))
        self.SkillNumberLabel = self.comp.TextLine(self.m2kBoard, '1\t\t\t\t\t\t\t2\t\t\t\t\t\t\t3\t\t\t\t\t\t\t4\t\t\t\t\t\t\t5\t\t\t\t\t\t\t6\t\t', 45, 190, self.comp.RGB(255, 255, 255))
        self.SkillLabel = self.comp.TextLine(self.m2kBoard, 'No:', 10, 190, self.comp.RGB(255, 255, 0))
        self.BuffSkill1Label = self.comp.TextLine(self.m2kBoard, 'Active-Buffskill:', 10, 220, self.comp.RGB(255, 255, 255))
        self.BuffSkill2Label = self.comp.TextLine(self.m2kBoard, 'Buffskill_1:', 10, 240, self.comp.RGB(255, 255, 255))
        self.BuffSkill3Label = self.comp.TextLine(self.m2kBoard, 'Buffskill_2:', 10, 260, self.comp.RGB(255, 255, 255))
        self.DamageSkillLabel = self.comp.TextLine(self.m2kBoard, 'Damageskill:', 10, 280, self.comp.RGB(255, 255, 255))
        self.InstructinLabel = self.comp.TextLine(self.m2kBoard, 'Please read the Infos before using!', 130, 280, self.comp.RGB(255, 255, 0))
        self.HorseLabel = self.comp.TextLine(self.m2kBoard, 'Use Horse:', 140, 220, self.comp.RGB(255, 255, 255))
        self.TauLabel = self.comp.TextLine(self.m2kBoard, 'Use Taus:', 140, 240, self.comp.RGB(255, 255, 255))
        self.DragonLabel = self.comp.TextLine(self.m2kBoard, 'With Rotation:', 140, 260, self.comp.RGB(255, 255, 255))
        self.CloseButton = self.comp.Button(self.m2kBoard, '', 'Close', 270, 8, self.Close, 'd:/ymir work/ui/public/close_button_01.sub', 'd:/ymir work/ui/public/close_button_02.sub', 'd:/ymir work/ui/public/close_button_03.sub')
        self.ImageRed = self.comp.ExpandedImage(self.m2kBoard, 9, 30, str('icon/item/27003.tga'))
        self.ImageBlue = self.comp.ExpandedImage(self.m2kBoard, 9, 70, str('icon/item/27006.tga'))
        self.ImageTapfi = self.comp.ExpandedImage(self.m2kBoard, 9, 110, str('icon/item/70038.tga'))
        self.AutoSkillUse1 = self.comp.ExpandedImage(self.m2kBoard, 30, 150, 'm2kmod/Images/General/noskill.tga')
        self.AutoSkillUse2 = self.comp.ExpandedImage(self.m2kBoard, 70, 150, 'm2kmod/Images/General/noskill.tga')
        self.AutoSkillUse3 = self.comp.ExpandedImage(self.m2kBoard, 110, 150, 'm2kmod/Images/General/noskill.tga')
        self.AutoSkillUse4 = self.comp.ExpandedImage(self.m2kBoard, 150, 150, 'm2kmod/Images/General/noskill.tga')
        self.AutoSkillUse5 = self.comp.ExpandedImage(self.m2kBoard, 190, 150, 'm2kmod/Images/General/noskill.tga')
        self.AutoSkillUse6 = self.comp.ExpandedImage(self.m2kBoard, 230, 150, 'm2kmod/Images/General/noskill.tga')
        self.SlidbarRed = self.comp.SliderBar(self.m2kBoard, 0.90000000000000002, self.SlideRed, 50, 40)
        self.SlidebarBlue = self.comp.SliderBar(self.m2kBoard, 0.29999999999999999, self.SlideBlue, 50, 80)
        self.SlidebarTapfi = self.comp.SliderBar(self.m2kBoard, 0.20000000000000001, self.SlideTapfi, 50, 120)
        (self.Slotbar1, self.EditLine1) = self.comp.SlotBarEditLine(self.m2kBoard, '4', 90, 220, 18, 15, 1)
        (self.Slotbar2, self.EditLine2) = self.comp.SlotBarEditLine(self.m2kBoard, '2', 90, 240, 18, 15, 1)
        (self.Slotbar3, self.EditLine3) = self.comp.SlotBarEditLine(self.m2kBoard, '2', 90, 260, 18, 15, 1)
        (self.Slotbar4, self.EditLine4) = self.comp.SlotBarEditLine(self.m2kBoard, '2', 90, 280, 18, 15, 1)
        self.InfoButton = self.comp.Button(self.m2kBoard, 'Info', 'Run insructions for the levelbot', 240, 260, self.RunInfos, 'd:/ymir work/ui/public/small_button_01.sub', 'd:/ymir work/ui/public/small_button_02.sub', 'd:/ymir work/ui/public/small_button_03.sub')
        self.BuffBotStartButton = self.comp.Button(self.m2kBoard, '', '', 245, 220, self.CheckLevelbot, 'm2kmod/Images/start_0.tga', 'm2kmod/Images/start_1.tga', 'm2kmod/Images/start_2.tga')
        self.BuffBotStopButton = self.comp.Button(self.m2kBoard, '', '', 245, 220, self.CheckLevelbot, 'm2kmod/Images/stop_0.tga', 'm2kmod/Images/stop_1.tga', 'm2kmod/Images/stop_2.tga')
        self.BuffBotStopButton.Hide()
        self.Skill1On = self.comp.Button(self.m2kBoard, '', '', 110, 220, self.Skill1, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.Skill1Off = self.comp.Button(self.m2kBoard, '', '', 110, 220, self.Skill1, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.Skill1On.Hide()
        self.Skill2On = self.comp.Button(self.m2kBoard, '', '', 110, 240, self.Skill2, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.Skill2Off = self.comp.Button(self.m2kBoard, '', '', 110, 240, self.Skill2, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.Skill2On.Hide()
        self.Skill3On = self.comp.Button(self.m2kBoard, '', '', 110, 260, self.Skill3, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.Skill3Off = self.comp.Button(self.m2kBoard, '', '', 110, 260, self.Skill3, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.Skill3On.Hide()
        self.Skill4On = self.comp.Button(self.m2kBoard, '', '', 110, 280, self.Skill4, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.Skill4Off = self.comp.Button(self.m2kBoard, '', '', 110, 280, self.Skill4, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.Skill4On.Hide()
        self.HorseOn = self.comp.Button(self.m2kBoard, '', 'Use horse for leveling', 210, 220, self.UseHorse, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.HorseOff = self.comp.Button(self.m2kBoard, '', 'Use horse for leveling', 210, 220, self.UseHorse, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.HorseOn.Hide()
        self.TauOn = self.comp.Button(self.m2kBoard, '', 'Use Taus', 210, 240, self.UseTau, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.TauOff = self.comp.Button(self.m2kBoard, '', 'Use Taus', 210, 240, self.UseTau, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.TauOff.Hide()
        self.RotateOn = self.comp.Button(self.m2kBoard, '', 'Rotate while leveling', 210, 260, self.UseRotate, 'm2kmod/Images/on_0.tga', 'm2kmod/Images/on_1.tga', 'm2kmod/Images/on_2.tga')
        self.RotateOff = self.comp.Button(self.m2kBoard, '', 'Rotate while leveling', 210, 260, self.UseRotate, 'm2kmod/Images/off_0.tga', 'm2kmod/Images/off_1.tga', 'm2kmod/Images/off_2.tga')
        self.RotateOff.Hide()
        self.GetSkillIcon()

    
    def RunInfos(self):
        os.system('start http://i.epvpimg.com/5houf.png')

    
    def SlideRed(self):
        self.RedPercent = int(self.SlidbarRed.GetSliderPos() * 100)
        self.RedLabel.SetText(str(self.RedPercent) + ' %')

    
    def SlideBlue(self):
        self.BluePercent = int(self.SlidebarBlue.GetSliderPos() * 100)
        self.BlueLabel.SetText(str(self.BluePercent) + ' %')

    
    def SlideTapfi(self):
        self.TapfiSec = int(self.SlidebarTapfi.GetSliderPos() * 100)
        self.TapfiLabel.SetText(str(self.TapfiSec) + ' Sec.')

    
    def Skill1(self):
        if self.ActiveSkill == 0:
            self.ActiveSkill = 1
            self.Skill1On.Show()
            self.Skill1Off.Hide()
        else:
            self.ActiveSkill = 0
            self.Skill1Off.Show()
            self.Skill1On.Hide()

    
    def Skill2(self):
        if self.Buffskill1 == 0:
            self.Buffskill1 = 1
            self.Skill2On.Show()
            self.Skill2Off.Hide()
        else:
            self.Buffskill1 = 0
            self.Skill2Off.Show()
            self.Skill2On.Hide()

    
    def Skill3(self):
        if self.Buffskill2 == 0:
            self.Buffskill2 = 1
            self.Skill3On.Show()
            self.Skill3Off.Hide()
        else:
            self.Buffskill3 = 0
            self.Skill3Off.Show()
            self.Skill3On.Hide()

    
    def Skill4(self):
        if self.Damageskill == 0:
            self.Damageskill = 1
            self.Skill4On.Show()
            self.Skill4Off.Hide()
        else:
            self.Damageskill = 0
            self.Skill4Off.Show()
            self.Skill4On.Hide()

    
    def UseHorse(self):
        if self.Horse == 0:
            self.Horse = 1
            self.HorseOn.Show()
            self.HorseOff.Hide()
        else:
            self.Horse = 0
            self.HorseOff.Show()
            self.HorseOn.Hide()

    
    def UseTau(self):
        if self.Tau == 0:
            self.Tau = 1
            self.TauOn.Show()
            self.TauOff.Hide()
        else:
            self.Tau = 0
            self.TauOff.Show()
            self.TauOn.Hide()

    
    def UseRotate(self):
        if self.Rotate == 0:
            self.Rotate = 1
            self.RotateOn.Show()
            self.RotateOff.Hide()
        else:
            self.Rotate = 0
            self.RotateOff.Show()
            self.RotateOn.Hide()

    
    def CheckLevelbot(self):
        if self.Levelbot == 0:
            self.Levelbot = 1
            self.State = 1
            if self.Horse == 1:
                self.InstallQuestWindowHook()
            
            self.Line1 = self.EditLine1.GetText()
            self.Line2 = self.EditLine2.GetText()
            self.Line3 = self.EditLine3.GetText()
            self.Line4 = self.EditLine4.GetText()
            self.BuffBotStopButton.Show()
            self.BuffBotStartButton.Hide()
            self.Levelbot_1()
            self.Pull_1()
            self.Restart_1()
            self.Skillbot_1()
            self.Rotate_1()
            player.SetAttackKeyState(TRUE)
        else:
            self.Levelbot = 0
            self.State = 0
            self.BuffBotStopButton.Hide()
            self.BuffBotStartButton.Show()
            if self.Horse == 1:
                self.UnHookQuestWindow()
            
            self.Levelbot_0()
            self.Pull_0()
            self.Restart_0()
            self.Skillbot_0()
            self.Rotate_0()
            player.SetAttackKeyState(FALSE)

    
    def Levelbot_1(self):
        PlayerTP = player.GetStatus(player.HP)
        if self.State == 1:
            self.RedPot()
            self.BluePot()
            if PlayerTP < 1:
                self.State = 2
                player.SetAttackKeyState(FALSE)
                self.Restart_1()
            
        
        if self.RestartPot == 1:
            self.RedPot()
        
        self.UpdateBase = WaitingDialog()
        self.UpdateBase.Open(0.5)
        self.UpdateBase.SAFE_SetTimeOverEvent(self.Levelbot_1)

    
    def Levelbot_0(self):
        self.UpdateBase = WaitingDialog()
        self.UpdateBase.Close()

    
    def RedPot(self):
        MaxTP = player.GetStatus(player.MAX_HP)
        ActualTP = player.GetStatus(player.HP)
        if (float(ActualTP) / float(MaxTP)) * 100 < 80:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                RedPott = player.GetItemIndex(i)
                if RedPott == 27001 and RedPott == 27002 or RedPott == 27003:
                    net.SendItemUsePacket(i)
                    break
                
            
        

    
    def BluePot(self):
        MaxSP = player.GetStatus(player.MAX_SP)
        ActualSP = player.GetStatus(player.SP)
        if (float(ActualSP) / float(MaxSP)) * 100 < 40:
            for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                BluePott = player.GetItemIndex(i)
                if BluePott == 27004 and BluePott == 27005 or BluePott == 27006:
                    net.SendItemUsePacket(i)
                    break
                
            
        

    
    def Pull_1(self):
        if self.State == 1:
            UseItem(70038)
        
        self.UpdateTapfis = WaitingDialog()
        self.UpdateTapfis.Open(self.TapfiSec)
        self.UpdateTapfis.SAFE_SetTimeOverEvent(self.Pull_1)

    
    def Pull_0(self):
        self.UpdateTapfis = WaitingDialog()
        self.UpdateTapfis.Close()

    
    def Restart_1(self):
        if self.State == 2:
            PlayerTP = player.GetStatus(player.HP)
            MaxTP = player.GetStatus(player.MAX_HP)
            net.SendChatPacket('/restart_here')
            if PlayerTP > 1:
                self.RestartPot = 1
                if self.Horse == 1:
                    UseItem(int(50052))
                    UseItem(int(50053))
                    event.SelectAnswer(1, 0)
                    for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
                        index = player.GetItemIndex(i)
                        if index == 27112 and index == 50107 and index == 50108 and index == 71014 or index == 71034:
                            net.SendItemUsePacket(i)
                            break
                        
                    
                
            
            if PlayerTP == MaxTP:
                self.RestartPot = 0
                if self.ActiveSkill == 1:
                    player.ClickSkillSlot(int(self.Line1))
                    self.WaitMount = WaitingDialog()
                    self.WaitMount.Open(1.0)
                    self.WaitMount.SAFE_SetTimeOverEvent(self.MountOnly)
                
                if self.Buffskill1 == 1:
                    if CanUseSkill(int(self.Line2)):
                        player.ClickSkillSlot(int(self.Line1))
                        self.Restart_0()
                        self.State = 1
                        player.SetAttackKeyState(TRUE)
                    
                else:
                    self.Restart_0()
                    self.State = 1
                    player.SetAttackKeyState(TRUE)
            
        
        self.UpdateRestart = WaitingDialog()
        self.UpdateRestart.Open(2.0)
        self.UpdateRestart.SAFE_SetTimeOverEvent(self.Restart_1)

    
    def Restart_0(self):
        self.UpdateRestart = WaitingDialog()
        self.UpdateRestart.Close()

    
    def Skillbot_1(self):
        if self.State == 1:
            if self.ActiveSkill == 1:
                if not player.IsSkillActive(int(self.Line1)):
                    if self.Horse == 1:
                        if player.IsMountingHorse():
                            net.SendChatPacket('/unmount')
                            self.SkillIndex = self.Line1
                            self.WaitSA = WaitingDialog()
                            self.WaitSA.Open(0.5)
                            self.WaitSA.SAFE_SetTimeOverEvent(self.Mount)
                        else:
                            player.ClickSkillSlot(int(self.Line1))
                            net.SendChatPacket('/user_horse_ride')
                    else:
                        player.ClickSkillSlot(int(self.Line1))
                
            
            if self.Buffskill1 == 1:
                if CanUseSkill(int(self.Line2)):
                    if player.IsMountingHorse():
                        net.SendChatPacket('/unmount')
                        self.SkillIndex = self.Line2
                        self.WaitBS = WaitingDialog()
                        self.WaitBS.Open(0.5)
                        self.WaitBS.SAFE_SetTimeOverEvent(self.Mount)
                    else:
                        player.ClickSkillSlot(int(self.Line2))
                
            
            if self.Buffskill2 == 1:
                if CanUseSkill(int(self.Line3)):
                    if player.IsMountingHorse():
                        net.SendChatPacket('/unmount')
                        self.SkillIndex = self.Line3
                        self.WaitBS = WaitingDialog()
                        self.WaitBS.Open(0.5)
                        self.WaitBS.SAFE_SetTimeOverEvent(self.Mount)
                    else:
                        player.ClickSkillSlot(int(self.Line3))
                
            
            if self.Damageskill == 1:
                self.TryUseSkill(self.Line4)
            
        
        self.UpdateSkills = WaitingDialog()
        self.UpdateSkills.Open(2.0)
        self.UpdateSkills.SAFE_SetTimeOverEvent(self.Skillbot_1)

    
    def Skillbot_0(self):
        self.UpdateSkills = WaitingDialog()
        self.UpdateSkills.Close()

    
    def TryUseSkill(self, index):
        if CanUseSkill(int(index)):
            if self.Horse == 1:
                if player.IsMountingHorse():
                    net.SendChatPacket('/unmount')
                    self.SkillIndex = index
                    self.UpdateSk = WaitingDialog()
                    self.UpdateSk.Open(1.0)
                    self.UpdateSk.SAFE_SetTimeOverEvent(self.Mount)
                else:
                    player.ClickSkillSlot(int(index))
                    chat.AppendChat(1, index)
                    net.SendChatPacket('/user_horse_ride')
            else:
                player.ClickSkillSlot(int(index))
        

    
    def Mount(self):
        if not (self.SkillIndex == 0):
            player.ClickSkillSlot(int(self.SkillIndex))
            self.SkillIndex = 0
            net.SendChatPacket('/user_horse_ride')
        

    
    def MountOnly(self):
        net.SendChatPacket('/user_horse_ride')

    
    def Rotate_1(self):
        chat.AppendChat(1, 'StartRotate')
        Direction = app.GetRandom(0, 7)
        if self.Rotate == 1 and self.State == 1:
            chr.SetDirection(Direction)
            chat.AppendChat(1, 'Rotiert')
        
        self.UpdateAttack = WaitingDialog()
        self.UpdateAttack.Open(2.0)
        self.UpdateAttack.SAFE_SetTimeOverEvent(self.Rotate_1)

    
    def Rotate_0(self):
        self.UpdateAttack = WaitingDialog()
        self.UpdateAttack.Close()

    
    def InstallQuestWindowHook(self):
        self.OldRecv = game.GameWindow.OpenQuestWindow
        game.GameWindow.OpenQuestWindow = self.HookedQuestWindow

    
    def UnHookQuestWindow(self):
        game.GameWindow.OpenQuestWindow = self.OldRecv

    
    def HookedQuestWindow(self, skin, idx):
        pass

    
    def GetSkillIcon(self):
        race = net.GetMainActorRace()
        group = net.GetMainActorSkillGroup()
        if int(race) == 0 or int(race) == 4:
            if int(group) == 1:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/warrior/samyeon_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/warrior/gigongcham_01.sub')
            
        elif int(race) == 1 or int(race) == 5:
            if int(group) == 1:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/assassin/amseup_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/assassin/yeonsa_01.sub')
            
        elif int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/sura/swaeryeong_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/sura/maryeong_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/shaman/bipabu_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse1.LoadImage('d:/ymir work/ui/skill/shaman/noejeon_01.sub')
            
        
        if int(race) == 0 or int(race) == 4:
            if int(group) == 1:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/warrior/palbang_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/warrior/gyeoksan_01.sub')
            
        elif int(race) == 1 or int(race) == 5:
            if int(group) == 1:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/assassin/gungsin_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/assassin/gwangyeok_01.sub')
            
        elif int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/sura/yonggwon_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/sura/hwayeom_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/shaman/yongpa_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse2.LoadImage('d:/ymir work/ui/skill/shaman/byeorak_01.sub')
            
        
        if int(race) == 0 or int(race) == 4:
            if int(group) == 1:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/warrior/jeongwi_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/warrior/daejin_01.sub')
            
        elif int(race) == 1 or int(race) == 5:
            if int(group) == 1:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/assassin/charyun_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/assassin/hwajo_01.sub')
            
        elif int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/sura/gwigeom_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/sura/muyeong_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/shaman/paeryong_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse3.LoadImage('d:/ymir work/ui/skill/shaman/pokroe_01.sub')
            
        
        if int(race) == 0 or int(race) == 4:
            if int(group) == 1:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/warrior/geomgyeong_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/warrior/cheongeun_01.sub')
            
        elif int(race) == 1 or int(race) == 5:
            if int(group) == 1:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/assassin/eunhyeong_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/assassin/gyeonggong_01.sub')
            
        elif int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/sura/gongpo_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/sura/heuksin_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/shaman/hosin_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse4.LoadImage('d:/ymir work/ui/skill/shaman/jeongeop_01.sub')
            
        
        if int(race) == 0 or int(race) == 4:
            if int(group) == 1:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/warrior/tanhwan_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/warrior/geompung_01.sub')
            
        elif int(race) == 1 or int(race) == 5:
            if int(group) == 1:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/assassin/sangong_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/assassin/gigung_01.sub')
            
        elif int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/sura/jumagap_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/sura/tusok_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/shaman/boho_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/shaman/kwaesok_01.sub')
            
        
        if int(race) == 2 or int(race) == 6:
            if int(group) == 1:
                self.AutoSkillUse6.LoadImage('d:/ymir work/ui/skill/sura/pabeop_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse6.LoadImage('d:/ymir work/ui/skill/sura/geomhwan_01.sub')
            
        elif int(race) == 3 or int(race) == 7:
            if int(group) == 1:
                self.AutoSkillUse6.LoadImage('d:/ymir work/ui/skill/shaman/gicheon_01.sub')
            elif int(group) == 2:
                self.AutoSkillUse5.LoadImage('d:/ymir work/ui/skill/shaman/jeungryeok_01.sub')
            
        



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



def CanUseSkill(index):
    cd = player.IsSkillCoolTime(int(index))
    if cd < 1:
        return 1
    else:
        return None


def UseItem(id):
    for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
        index = player.GetItemIndex(i)
        if index == id:
            net.SendItemUsePacket(i)
            break
        
    


def CanUseItem(id):
    for i in xrange(player.INVENTORY_PAGE_SIZE * 3):
        item = player.GetItemIndex(i)
        if item == id:
            chat.AppendChat(7, 'can use')
            return 1
        else:
            return 0
            chat.AppendChat(7, 'cant use')
    


try:
    app.Shop.Close()
except:
    pass

app.Shop = LevelbotDialog()
