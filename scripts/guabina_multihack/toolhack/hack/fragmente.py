## -- ©BlackBulls GANG
## ---------------------

# --<
import os
import ui
import app
import ime
import grp
import net
import snd
import item
import chat
import player
import locale
import grpText
import uiRefine
import constInfo
import uiToolTip
import mouseModule
import uiAttachMetin
import uiScriptLocale

class changeequip(ui.ScriptWindow):
	def __init__(self):
		import exception
		ui.ScriptWindow.__init__(self)
		self.wndEquip = None
		self.tokens = None
		self.tooltipItem = uiToolTip.ItemToolTip()
		self.tooltipItem.Hide()
		if constInfo.FAST_PAGE == 1:
			self.saveName = "lib/FastEquipPage1.pyc"
		elif constInfo.FAST_PAGE == 2:
			self.saveName = "lib/FastEquipPage2.pyc"
		elif constInfo.FAST_PAGE == 3:
			self.saveName = "lib/FastEquipPage3.pyc"
		elif constInfo.FAST_PAGE == 4:
			self.saveName = "lib/FastEquipPage4.pyc"
		elif constInfo.FAST_PAGE == 5:
			self.saveName = "lib/FastEquipPage5.pyc"
		elif constInfo.FAST_PAGE == 6:
			self.saveName = "lib/FastEquipPage6.pyc"

	def __del__(self):
		ui.ScriptWindow.__del__(self)

	def Show(self):
		self.__LoadWindow()
		ui.ScriptWindow.Show(self)

	def Close(self):
		constInfo.FAST_EQUIP = 0
		snd.PlaySound("sound/ui/click.wav")
		self.Hide()

	def __LoadWindow(self):
		try:			
			pyScrLoader = ui.PythonScriptLoader()
			pyScrLoader.LoadScriptFile(self, "uiscript/uiscript/fastequip_window.py")
		except:
			import exception
			exception.Abort("CostumeWindow.LoadWindow.LoadObject")
		
		self.wndEquip = self.GetChild("equipslot")
		self.bottone_change = self.GetChild("change_button")
		self.clear_button = self.GetChild("clear_button")
		self.TitleBar = self.GetChild("TitleBar")
		self.pag1_button = self.GetChild("page1_button")
		self.pag2_button = self.GetChild("page2_button")
		self.pag3_button = self.GetChild("page3_button")
		self.pag4_button = self.GetChild("page4_button")
		self.pag5_button = self.GetChild("page5_button")
		self.pag6_button = self.GetChild("page6_button")
		
		
		self.TitleBar.SetCloseEvent(ui.__mem_func__(self.Close))
		self.wndEquip.SetSelectEmptySlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetSelectItemSlotEvent(ui.__mem_func__(self.SelectItemSlot))
		self.wndEquip.SetOverInItemEvent(ui.__mem_func__(self.OverInItem))
		self.wndEquip.SetOverOutItemEvent(ui.__mem_func__(self.OnOverOutItem))
		self.bottone_change.SetEvent(ui.__mem_func__(self.__change_button))
		self.clear_button.SetEvent(ui.__mem_func__(self.__clear_button))
		self.pag1_button.SAFE_SetEvent(self.__pag1_button)
		self.pag2_button.SetEvent(ui.__mem_func__(self.__pag2_button))
		self.pag3_button.SetEvent(ui.__mem_func__(self.__pag3_button))
		self.pag4_button.SetEvent(ui.__mem_func__(self.__pag4_button))
		self.pag5_button.SetEvent(ui.__mem_func__(self.__pag5_button))
		self.pag6_button.SetEvent(ui.__mem_func__(self.__pag6_button))
		
		if os.path.exists(self.saveName):
			self.tokens = open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		
		button = self.GetChild("page1_button")
		button.Down()

	def __clear_button(self):
		if constInfo.FAST_PAGE == 1:
			self.saveName = "lib/FastEquipPage1.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		elif constInfo.FAST_PAGE == 2:
			self.saveName = "lib/FastEquipPage2.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		elif constInfo.FAST_PAGE == 3:
			self.saveName = "lib/FastEquipPage3.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		elif constInfo.FAST_PAGE == 4:
			self.saveName = "lib/FastEquipPage4.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		elif constInfo.FAST_PAGE == 5:
			self.saveName = "lib/FastEquipPage5.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")
		elif constInfo.FAST_PAGE == 6:
			self.saveName = "lib/FastEquipPage6.pyc"
			if os.path.exists(self.saveName):
				os.remove(self.saveName)
				open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag1_button(self):
		constInfo.FAST_PAGE = 1
		button2 = self.GetChild("page2_button")
		button3 = self.GetChild("page3_button")
		button4 = self.GetChild("page4_button")
		button5 = self.GetChild("page5_button")
		button6 = self.GetChild("page6_button")
		button2.SetUp()
		button3.SetUp()
		button4.SetUp()
		button5.SetUp()
		button6.SetUp()
		
		self.saveName = "lib/FastEquipPage1.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag2_button(self):
		constInfo.FAST_PAGE = 2
		button1 = self.GetChild("page1_button")
		button3 = self.GetChild("page3_button")
		button4 = self.GetChild("page4_button")
		button5 = self.GetChild("page5_button")
		button6 = self.GetChild("page6_button")
		button1.SetUp()
		button3.SetUp()
		button4.SetUp()
		button5.SetUp()
		button6.SetUp()
		
		self.saveName = "lib/FastEquipPage2.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag3_button(self):
		constInfo.FAST_PAGE = 3
		button1 = self.GetChild("page1_button")
		button2 = self.GetChild("page2_button")
		button4 = self.GetChild("page4_button")
		button5 = self.GetChild("page5_button")
		button6 = self.GetChild("page6_button")
		button1.SetUp()
		button2.SetUp()
		button4.SetUp()
		button5.SetUp()
		button6.SetUp()
		
		self.saveName = "lib/FastEquipPage3.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag4_button(self):
		constInfo.FAST_PAGE = 4
		button1 = self.GetChild("page1_button")
		button2 = self.GetChild("page2_button")
		button3 = self.GetChild("page3_button")
		button5 = self.GetChild("page5_button")
		button6 = self.GetChild("page6_button")
		button1.SetUp()
		button2.SetUp()
		button3.SetUp()
		button5.SetUp()
		button6.SetUp()
		
		self.saveName = "lib/FastEquipPage4.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag5_button(self):
		constInfo.FAST_PAGE = 5
		button1 = self.GetChild("page1_button")
		button2 = self.GetChild("page2_button")
		button3 = self.GetChild("page3_button")
		button4 = self.GetChild("page4_button")
		button6 = self.GetChild("page6_button")
		button1.SetUp()
		button2.SetUp()
		button3.SetUp()
		button4.SetUp()
		button6.SetUp()
		
		self.saveName = "lib/FastEquipPage5.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __pag6_button(self):
		constInfo.FAST_PAGE = 6
		button1 = self.GetChild("page1_button")
		button2 = self.GetChild("page2_button")
		button3 = self.GetChild("page3_button")
		button4 = self.GetChild("page4_button")
		button5 = self.GetChild("page5_button")
		button1.SetUp()
		button2.SetUp()
		button3.SetUp()
		button4.SetUp()
		button5.SetUp()
		
		self.saveName = "lib/FastEquipPage6.pyc"
		if os.path.exists(self.saveName):
			open(self.saveName, "r").read().split()
		else:
			open(self.saveName, "w").write("@\t@\t@\t@\t@\t@\t@\t@\t@\t@")

	def __change_button(self):
		for i in range(1,11):
			if self.tokens[i-1] != "@":
				net.SendItemUsePacket(int(self.tokens[i-1]))	

	def OverInItem(self, slotNumber):
		if self.tooltipItem:
			self.tooltipItem.SetInventoryItem(int(self.tokens[slotNumber-1]))

	def OnOverOutItem(self):
		if self.tooltipItem:
			self.tooltipItem.HideToolTip()

	def SelectItemSlot(self, itemSlotIndex):
		isAttached = mouseModule.mouseController.isAttached()
		if isAttached:
			attachedSlotType = mouseModule.mouseController.GetAttachedType()
			attachedSlotPos = mouseModule.mouseController.GetAttachedSlotNumber()
			itemIndex = player.GetItemIndex(attachedSlotPos)
			itemCount = player.GetItemCount(attachedSlotPos)
			item.SelectItem(itemIndex)
			itemType = item.GetItemType()
			itemSubType = item.GetItemSubType()
			
			if item.IsWearableFlag(item.WEARABLE_BODY):
				self.tokens[1-1] = attachedSlotPos
				snd.PlaySound("sound/ui/equip_metal_armor.wav")
			elif item.IsWearableFlag(item.WEARABLE_HEAD):
				self.tokens[2-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			elif item.IsWearableFlag(item.WEARABLE_FOOTS):
				self.tokens[3-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			elif item.IsWearableFlag(item.WEARABLE_WRIST):
				self.tokens[4-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			elif item.IsWearableFlag(item.WEARABLE_WEAPON):
				self.tokens[5-1] = attachedSlotPos
				if itemSubType == 2:
					snd.PlaySound("sound/ui/equip_bow.wav")
				else:
					snd.PlaySound("sound/ui/equip_metal_weapon.wav")
			elif item.IsWearableFlag(item.WEARABLE_NECK):
				self.tokens[6-1] = attachedSlotPos
				snd.PlaySound("sound/ui/equip_ring_amulet.wav")
			elif item.IsWearableFlag(item.WEARABLE_EAR):
				self.tokens[7-1] = attachedSlotPos
				snd.PlaySound("sound/ui/equip_ring_amulet.wav")
			elif item.IsWearableFlag(item.WEARABLE_SHIELD):
				self.tokens[8-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			elif item.IsWearableFlag(item.WEARABLE_ARROW):
				self.tokens[9-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			elif item.GetItemType()==item.ITEM_TYPE_BELT:
				self.tokens[10-1] = attachedSlotPos
				snd.PlaySound("sound/ui/drop.wav")
			else:
				return
			
			open(self.saveName, "w").write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % tuple(self.tokens))	
			mouseModule.mouseController.DeattachObject()

	def OnUpdate(self):	
		tokens = open(self.saveName, "r").read().split()		
		self.tokens = tokens
		for i in range(1,11):	
			if tokens[i-1] == "@":
				self.wndEquip.SetItemSlot(i, 0, 0)
			else:
				itemIndex = player.GetItemIndex(int(tokens[i-1]))
				if itemIndex != 0:
					item.SelectItem(itemIndex)
					if i == 1 and item.IsWearableFlag(item.WEARABLE_BODY):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 2 and item.IsWearableFlag(item.WEARABLE_HEAD):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 3 and item.IsWearableFlag(item.WEARABLE_FOOTS):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 4 and item.IsWearableFlag(item.WEARABLE_WRIST):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 5 and item.IsWearableFlag(item.WEARABLE_WEAPON):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 6 and item.IsWearableFlag(item.WEARABLE_NECK):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 7 and item.IsWearableFlag(item.WEARABLE_EAR):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 8 and item.IsWearableFlag(item.WEARABLE_SHIELD):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 9 and item.IsWearableFlag(item.WEARABLE_ARROW):
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					elif i == 10 and item.GetItemType()==item.ITEM_TYPE_BELT:
						self.wndEquip.SetItemSlot(i, itemIndex, 0)
					else:
						self.wndEquip.SetItemSlot(i, 0, 0)
						self.tokens[i-1] = "@"
						open(self.saveName, "w").write("%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s\t%s" % tuple(self.tokens))
						continue
				else:
					self.wndEquip.SetItemSlot(i, 0, 0)				

	def OnPressEscapeKey(self):
		self.Close()
		snd.PlaySound("sound/ui/click.wav")
		return TRUE
# -->
a=changeequip()
a.Show()
