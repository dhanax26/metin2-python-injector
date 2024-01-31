#############################################################
# Metin2 | Bot | Farm | Level | Buff | (c) since 2017 iPUSH #
#############################################################

import sys, os, math, time, random

### Classes instead of packages & modules to fit all in one file ###
class Util:
    class File:
        @staticmethod
        def read(path):
            try:
                f = open(path, 'r')
                lines = f.readlines()
                f.close()
                return lines
            except:
                pass

        @staticmethod
        def write(path, name, id, time):
            f = open(path, 'a+')
            f.write("Name=%s\n" % (name))
            f.write("ID=%i\n" % (id))
            f.write("Time=%i\n\n" % (time))
            f.close()

        @classmethod
        def removeLastLines(cls, path, num):
            allLines = cls.read(path)
            f = open(path, "w+")
            f.writelines(allLines[:-num])
            f.close()

    class Module:
        @classmethod
        def find(cls, name, atr):
            for module_name in sys.modules:
                if name == '*' or name in module_name:
                    try:
                        module = __import__(module_name)
                        getattr(module, atr)
                        return module
                    except:
                        pass

            return cls.find('*', atr)

        @staticmethod
        def dump(path):
            for m in sys.modules:
                f = open(path, 'a+')
                
                try:
                    module = __import__(m)

                    f.write("\n# %s\nimport %s\n" % (m, m))

                    for atr in dir(module):
                        atr_name = atr
                        atr = getattr(module, atr)

                        if callable(atr):
                            f.write("%s.%s() # %s\n" % (m, atr_name, type(atr)))
                            for sub_atr in ['__code__', '__defaults__', '__kwdefaults__']:
                                if sub_atr == '__code__':
                                    for co_atr in ['co_argcount', 'co_varnames', 'co_nlocals', 'co_names', 'co_cellvars', 'co_consts', 'co_freevars', 'co_posonlyargcount', 'co_kwonlyargcount']:
                                        try:
                                            f.write("%s.%s.%s.%s = %s\n" % (m, atr_name, sub_atr, co_atr, getattr(getattr(atr, sub_atr), co_atr)))
                                        except:
                                            pass
                                else:
                                    try:
                                        f.write("%s.%s.%s = %s\n" % (m, atr_name, sub_atr, getattr(atr, sub_atr)))
                                    except:
                                        pass
                        else:
                            f.write("%s.%s # %s\n" % (m, atr_name, type(atr)))
                except:
                    f.write("\n# ImportError: No module named %s\n" % (m))

                f.close()

### Import Metin2 modules ###
app = Util.Module.find('app', 'GetRandom')
item = Util.Module.find('item', 'GetItemName')
chr = Util.Module.find('chr', 'SetRotation')
net = Util.Module.find('net', 'SendChatPacket')
player = Util.Module.find('player', 'SetAttackKeyState')
ui = Util.Module.find('ui', 'ThinBoard')
textTail = Util.Module.find('textTail', 'Pick')
chat = Util.Module.find('chat', 'AppendChat')
systemSetting = Util.Module.find('systemSetting', 'GetCurrentResolution')

class Mt2:
    class Event:
        def __init__(self, delay, task, name=None, repeat=False):
            self.delay = delay
            self.task = task
            self.name = name
            self.repeat = repeat
            self.over = False
            self.timeOfExec = time.clock() + delay

        def run(self, curTime):
            if not self.over and curTime >= self.timeOfExec:
                self.timeOfExec = curTime + self.delay
                self.task()
                self.over = True if not self.repeat else False

    class EventHandler(ui.Window):
        def __init__(self, layer = "UI"):
            ui.Window.__init__(self, layer)
            self.events = []
            self.add(10, self.clean, "Clean Events", True)
            self.Show()

        def __del__(self):
            ui.Window.__del__(self)

        def get(self, name):
            return next((e for e in self.events if e.name == name), None)

        def has(self, name):
            return eventHandler.get(name) is not None

        def add(self, delay, task, name=None, repeat=False):
            self.events.append(Mt2.Event(delay, task, name, repeat))

        def remove(self, name, task=None):
            self.events = [e for e in self.events if e.name != name]
            if task is not None: task()

        def pause(self, name, delay):
            event = self.get(name)
            if event is None: return
            self.remove(name)
            self.add(delay, lambda: self.add(event.delay, event.task, event.name, event.repeat))

        def clean(self):
            self.events = [e for e in self.events if not e.over]

        def OnUpdate(self):
            curTime = time.clock()
            for event in self.events: event.run(curTime)

    class Gui:
        @staticmethod
        def addThinBoard(parent, x, y, width, heigh):
            board = ui.ThinBoard()
            if parent is not None: board.SetParent(parent)
            board.AddFlag('movable')
            board.AddFlag('float')
            board.SetPosition(x, y)
            board.SetSize(width, heigh)
            board.Hide()
            return board

        @staticmethod
        def addTextLine(parent, text, x, y, color):
            textline = ui.TextLine()
            if parent is not None: textline.SetParent(parent)
            if color is not None: textline.SetFontColor(color[0]*255, color[1]*255, color[2]*255)
            textline.SetPosition(x, y)
            textline.SetText(text)
            textline.SetOutline()
            textline.Show()
            return textline

        @staticmethod
        def addEditLine(parent, x, y, width, heigh, text, charLimit):
            slotBar = ui.SlotBar()
            if parent is not None: slotBar.SetParent(parent)
            slotBar.SetSize(width, heigh)
            slotBar.SetPosition(x, y)
            slotBar.Show()
            editLine = ui.EditLine()
            editLine.SetParent(slotBar)
            editLine.SetSize(width, heigh)
            editLine.SetPosition(6, 2)
            editLine.SetMax(charLimit)
            editLine.SetNumberMode()
            editLine.SetText(text)
            editLine.Show()
            return slotBar, editLine

        @staticmethod
        def addButton(parent, label, x, y, size, event, *args):
            button = ui.Button()
            if parent is not None: button.SetParent(parent)
            button.SetPosition(x, y)
            button.SetUpVisual('d:/ymir work/ui/public/' + size + '_button_01.sub')
            button.SetOverVisual('d:/ymir work/ui/public/' + size + '_button_02.sub')
            button.SetDownVisual('d:/ymir work/ui/public/' + size + '_button_03.sub')
            button.SetText(label)
            button.SetEvent(event, *args)
            button.Show()
            return button

        @staticmethod
        def addToggleButton(parent, label, x, y, size, eventDown, eventUp=None, delay=None, closure=False):
            button = ui.ToggleButton()
            if parent is not None: button.SetParent(parent)
            button.SetPosition(x, y)
            button.SetUpVisual('d:/ymir work/ui/public/' + size + '_button_01.sub')
            button.SetOverVisual('d:/ymir work/ui/public/' + size + '_button_02.sub')
            button.SetDownVisual('d:/ymir work/ui/public/' + size + '_button_03.sub')
            button.SetText(label)
            button.SetToggleDownEvent(eventDown if delay is None else lambda: eventHandler.add(delay, eventDown() if closure else eventDown, label, True))
            button.SetToggleUpEvent(eventUp if delay is None else lambda: eventHandler.remove(label, eventUp))
            button.Show()
            return button

    class Api:
        ### Use item from inventory ###
        @staticmethod
        def useItem(itemID):
            for i in xrange(player.INVENTORY_PAGE_SIZE*5):
                if player.GetItemIndex(i) == itemID:
                    net.SendItemUsePacket(i)
                    return True

        ### Get VIDs of near items ###
        @staticmethod
        def getItems():
            itemList = []
            x, y, _ = systemSetting.GetCurrentResolution()

            for x in xrange(x/2-200, x/2+200, 10):
                for y in xrange(y/2-400, y/2+400, 10):
                    iVID = textTail.Pick(x, y)
                    if iVID != -1 and iVID not in itemList:
                        itemList.append(iVID)
            
            return itemList

        ### Get degree in between char and target ###
        @staticmethod
        def getDegree(vid):
            mobX, mobY, _ = chr.GetPixelPosition(vid)
            playerX, playerY, _ = player.GetMainCharacterPosition()
            try:
                rada = 180 * (math.acos((mobY-playerY)/math.sqrt((mobX - playerX)**2 + (mobY - playerY)**2))) / math.pi + 180
                if playerX >= mobX:
                    rada = 360 - rada
            except:
                rada = 0
            return rada

        ### Char move to position and dodge if get stucked ###
        @classmethod
        def moveToTarget(cls, vid):
            x, y, _ = chr.GetPixelPosition(vid)
            mX, mY, _ = player.GetMainCharacterPosition()
			
            x = x + 135 if x < mX else x - 135
            y = y + 135 if y < mY else y - 135

            def moveToDestPosition(x, y):
                chr.MoveToDestPosition(player.GetMainCharacterIndex(), x, y)
                eventHandler.add(2, lambda: eventHandler.remove("moveToTarget"))
                
            if not eventHandler.has("moveToTarget"): eventHandler.add(0, lambda x=x, y=y: moveToDestPosition(x, y), "moveToTarget")

            if not eventHandler.has("dodge"): eventHandler.add(5, lambda: cls.dodge(vid), "dodge")

        ### Char dodge into random direction ###
        @staticmethod
        def dodge(vid):
            if player.GetCharacterDistance(vid) < 500: return

            directions = [ app.DIK_UP, app.DIK_DOWN, app.DIK_LEFT, app.DIK_RIGHT ]
            direction = directions[random.randint(0, 3)]

            if player.IsMountingHorse(): player.ClickSkillSlot(9)

            player.SetSingleDIKKeyState(direction, True)

            def stopDodge():
                player.SetSingleDIKKeyState(direction, False)
                eventHandler.remove("dodge")

            eventHandler.add(2, stopDodge)

        ### Get VIDs of near targets ###
        @classmethod
        def getTargets(cls, Type):
            targets = []
            r = [0]

            def getTargetVIDs():
                if not targets or (Type == 0 and not any(player.GetCharacterDistance(t) < 5000 for t in targets[:5])) or all(player.GetCharacterDistance(t) == -1 for t in targets[:5]):
                    del targets[:]
                    targets.extend([ vid for vid in xrange(r[0], r[0]+1000000, 3 if Type == 0 else 1) if chr.GetInstanceType(vid) == Type and (Type != 0 or player.GetCharacterDistance(vid) < 10000) ])
                    targets.sort(key=lambda t: player.GetCharacterDistance(t))
                    r[0] += 1000000
                    return targets
                if targets or r[0] > 100000000:
                    r[0] = 0
                return targets
            
            return getTargetVIDs

class Bot:
    class Api:
        ### AutoTP ###
        @staticmethod
        def autoTP(threshold):
            if (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100) < int(threshold):
                if not Mt2.Api.useItem(27001):
                    if not Mt2.Api.useItem(27002):
                        Mt2.Api.useItem(27003)

        ### AutoMP ###
        @staticmethod
        def autoMP(threshold):
            if (float(player.GetStatus(player.SP)) / (float(player.GetStatus(player.MAX_SP))) * 100) < int(threshold):
                if not Mt2.Api.useItem(27004):
                    if not Mt2.Api.useItem(27005):
                        Mt2.Api.useItem(27006)

        ### AutoAttack ###
        @staticmethod
        def autoAttack(Type):
            getTargets = Mt2.Api.getTargets(Type)

            def attack():
                if 0 < (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100) < 90:
                    chr.SetDirection(random.randint(0, 8))
                    player.SetAttackKeyState(True)
                    return

                targets = getTargets()
                target = next((t for t in targets if player.GetCharacterDistance(t) != -1), False)

                if not target: return

                Mt2.Api.moveToTarget(target)
                
                if 0 < player.GetCharacterDistance(target) < 300:
                    chr.SetRotation(Mt2.Api.getDegree(target))
                    player.SetAttackKeyState(True)
                else:
                    player.SetAttackKeyState(False)

            return attack

        ### Follow target ###
        @staticmethod
        def followTarget():
            targetVID = player.GetTargetVID()

            def follow():
                player.SetTarget(targetVID)
                if player.GetCharacterDistance(targetVID) > 1000:
                    Mt2.Api.moveToTarget(targetVID)

            return follow

        ### Horse ###
        @staticmethod
        def useHorse():
            tp = (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100)

            if player.IsMountingHorse():
                if 0 < tp < 30:
                    chr.SetDirection(random.randint(0, 8))
                    player.ClickSkillSlot(9)
            else:
                def callHorse():
                   if not player.IsMountingHorse():
                       net.SendItemUsePacket(0)
                
                net.SendChatPacket("/ride")
                eventHandler.add(1, callHorse)

        ### Skills ###
        @staticmethod
        def loadSkills(board):
            btns = []
            editLines = []
            for i in xrange(1, 7):
                editLines.append(Mt2.Gui.addEditLine(board, 50, (i * 20) + 1, 25, 16, "5", 3))
                btns.append(Mt2.Gui.addToggleButton(board, str(i), 5, i * 20, "small", lambda i=i: Bot.Api.useSkill(i), delay=int(editLines[i-1][1].GetText())))
            return btns, editLines

        @staticmethod
        def useSkill(skill):
            tp = (float(player.GetStatus(player.HP)) / (float(player.GetStatus(player.MAX_HP))) * 100)
            
            if player.IsSkillActive(skill) == 0 and player.IsSkillCoolTime(skill) == 0 and tp > 30:
                if player.IsMountingHorse():
                    eventHandler.pause("Horse", 2)
                    net.SendChatPacket("/ride")
                eventHandler.add(1, lambda: player.ClickSkillSlot(skill))

        ### UseItem ###
        @staticmethod
        def showUseItem(board, btns):
            board.SetSize(130, (len(btns) + 2) * 25)
            board.Show()

        @staticmethod
        def addUseItem(board, btns, time):
            item.SelectItem(player.GetItemIndex(0))
            itemName = str(item.GetItemName())
            itemID = int(player.GetItemIndex(0))
            itemTime = time
            Util.File.write("Bot-Settings.txt", itemName, itemID, itemTime)
            btns.append(Mt2.Gui.addToggleButton(board, itemName, 20, (len(btns) + 2) * 25, "large", lambda: Mt2.Api.useItem(itemID), delay=itemTime))
            Bot.Api.showUseItem(board, btns)

        @staticmethod
        def removeUseItem(board, btns):
            Util.File.removeLastLines("Bot-Settings.txt", 4)
            btns[-1].Hide()
            del btns[-1]
            Bot.Api.showUseItem(board, btns)

        @staticmethod
        def loadUseItem(board):
            btns = []
            settings = Util.File.read("Bot-Settings.txt")
            if settings is not None:
                for i in range(0, len(settings), 4):
                    itemName = str(settings[i].split('=')[1])
                    itemID = int(settings[i+1].split('=')[1])
                    itemTime = int(settings[i+2].split('=')[1])
                    btns.append(Mt2.Gui.addToggleButton(board, itemName, 20, (len(btns) + 2) * 25, "large", lambda: Mt2.Api.useItem(itemID), delay=itemTime))
            return btns

        ### Pick up item ###
        @staticmethod
        def pickUp():
            try:
                player.PickCloseItem()
            except:
                for item in Mt2.Api.getItems():
                    net.SendItemPickUpPacket(item)

        ### Restart here ###
        @staticmethod
        def restartHere():
            if player.GetStatus(player.HP) <= 0:
                player.SetAttackKeyState(False)
                
                eventHandler.pause("AutoAttack", 10)
                eventHandler.pause("Pull", 10)

                net.SendChatPacket("/restart_here")

                for i in xrange(5): eventHandler.add(1+i*0.1, lambda i=i: net.SendItemUsePacket(i))

    class Gui:
        def __init__(self):
            self.pos = 10

            ### Main ###
            self.mainBoard = Mt2.Gui.addThinBoard(None, 15, 100, 100, 240)
            self.mainBtn = Mt2.Gui.addToggleButton(None, "iPUSH", 20, 75, "large", self.mainBoard.Show, self.mainBoard.Hide)
            ### AutoTP ###
            self.autoTPEditLine = Mt2.Gui.addEditLine(self.mainBoard, 70, self.pos+1, 20, 16, "90", 2)
            self.autoTPBtn = Mt2.Gui.addToggleButton(self.mainBoard, "AutoTP", 5, self.pos, "middle", lambda: Bot.Api.autoTP(self.autoTPEditLine[1].GetText()), delay=1)
            self.pos += 20
            ### AutoMP ###
            self.autoMPEditLine = Mt2.Gui.addEditLine(self.mainBoard, 70, self.pos+1, 20, 16, "90", 2)
            self.autoMPBtn = Mt2.Gui.addToggleButton(self.mainBoard, "AutoMP", 5, self.pos, "middle", lambda: Bot.Api.autoMP(self.autoMPEditLine[1].GetText()), delay=1)
            self.pos += 20
            # AutoAttack | 0 = Mobs | 2 = Metins | 6 = Players ###
            self.autoAttackEditLine = Mt2.Gui.addEditLine(self.mainBoard, 70, self.pos+1, 20, 16, "0", 2)
            self.autoAttackBtn = Mt2.Gui.addToggleButton(self.mainBoard, "AutoAttack", 5, self.pos, "middle",
                lambda: Bot.Api.autoAttack(int(self.autoAttackEditLine[1].GetText())),
                lambda: player.SetAttackKeyState(False),
                1, True
            )
            self.pos += 20
            ### Pull ###
            self.pullBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Pull", 5, self.pos, "large", lambda: net.SendItemUsePacket(5), delay=1)
            self.pos += 20
            ### Follow target ###
            self.followTarBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Follow", 5, self.pos, "large", Bot.Api.followTarget, delay=1, closure=True)
            self.pos += 20
            ### Horse ###
            self.useHorseBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Horse", 5, self.pos, "large", Bot.Api.useHorse, delay=1)
            self.pos += 20
            ### Skills ###
            self.skillsBoard = Mt2.Gui.addThinBoard(None, 115, 100, 85, 160)
            self.skillsMainBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Skills", 5, self.pos, "large", self.skillsBoard.Show, self.skillsBoard.Hide)
            self.skillsBtnList, self.skillsEditLineList = Bot.Api.loadSkills(self.skillsBoard)
            self.pos += 20
            ### Items ###
            self.useItemBoard = Mt2.Gui.addThinBoard(None, 115, 100, 100, 200)
            self.useItemBtnList = Bot.Api.loadUseItem(self.useItemBoard)
            self.useItemBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Items", 5, self.pos, "large", lambda: Bot.Api.showUseItem(self.useItemBoard, self.useItemBtnList), self.useItemBoard.Hide)
            self.pos += 20
            self.useItemEditLine = Mt2.Gui.addEditLine(self.useItemBoard, 95, 11, 25, 16, "5", 3)
            self.addUseItemBtn = Mt2.Gui.addButton(self.useItemBoard, "+", 5, 10, "small", lambda: Bot.Api.addUseItem(self.useItemBoard, self.useItemBtnList, int(self.useItemEditLine[1].GetText())))
            self.delUseItemBtn = Mt2.Gui.addButton(self.useItemBoard, "-", 50, 10, "small", lambda: Bot.Api.removeUseItem(self.useItemBoard, self.useItemBtnList))
            ### PickUp ###
            self.pickUpBtn = Mt2.Gui.addToggleButton(self.mainBoard, "PickUp", 5, self.pos, "large", Bot.Api.pickUp, delay=1)
            self.pos += 20
            ### Restart here###
            self.restartBtn = Mt2.Gui.addToggleButton(self.mainBoard, "Restart", 5, self.pos, "large", Bot.Api.restartHere, delay=5)
            self.pos += 20
            ### Ghost ###chr.Revive
            self.ghostBtn = Mt2.Gui.addButton(self.mainBoard, "Ghost", 5, self.pos, "large", chr.Revive)
            self.pos += 20

# Init the Hack
eventHandler = Mt2.EventHandler()
gui = Bot.Gui()