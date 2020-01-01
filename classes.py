import math
class MNode :
    def __init__(self,data=None,pointer=None):
        self.data= data
        self.pointer = pointer
class MTNode :
    def __init__(self,stride ):
        self.stride = stride
        self.list = []
        while len(self.list) != int(math.pow(2,self.stride)):
            self.list.append(MNode())
class Node :
    def __init__(self , data=None , left = None, right =None , skipvalue=None, segment = None ):
        self.data = data
        self.skipvalue = skipvalue
        self.segment = segment
        self.right = right
        self.left = left

class Binary_Trie :

    def __init__(self,dict):
        self.pt = dict
        self.root=Node('root')

    def retu(self):
        return self.root
    def CreatRoot(self):
        for info , data in self.pt.items() :
            self.dict = {info : data}
            self.Addition(self.dict)
        print(self.Print())

    def Print(self):
        self.visited = []
        self.q = []
        self.q.append(self.root)
        while len(self.q) > 0:
            self.first = self.q[0]
            if self.first.data == None:
                self.visited.append('no')
                if self.first.left:
                    self.q.append(self.first.left)
                if self.first.right:
                    self.q.append(self.first.right)
                self.q.pop(0)
                # print(' no ')

            else:
                self.visited.append(self.first.data)
                if self.first.left:
                    self.q.append(self.first.left)
                if self.first.right:
                    self.q.append(self.first.right)
                self.q.pop(0)
                # print(self.first.data)
        return self.visited

    def Search (self,address):
        self.pointer = self.root
        self.lm = ''
        self.add=address
        # self.parrent = self.root

        for i in self.add :
            if i == '0' :
                if self.pointer.left:
                    # self.parrent = self.pointer
                    self.pointer = self.pointer.left

            elif i == '1' :
                if self.pointer.right:
                    # self.parrent = self.pointer
                    self.pointer = self.pointer.right

            if  self.pointer.data :
                self.lm = self.pointer.data
                # print(self.pointer.data)

        if self.lm :
            return self.lm
        else:
            return 'no longst match finded'

    def Addition(self,dic):
        self.data = ''
        self.addr = ''
        self.newdict = dic
        self.ar = self.root

        for x , y  in self.newdict.items():
            self.data = x
            self.addr = y
            if self.addr == '*':
                self.root.data=self.data

            for i in self.addr:
                if i == '1':
                    if self.ar.right:
                        self.ar = self.ar.right
                    else:
                        self.ar.right = Node()
                        self.ar = self.ar.right

                if i == '0':
                    if self.ar.left:
                        self.ar = self.ar.left
                    else:
                        self.ar.left = Node()
                        self.ar = self.ar.left

            if self.ar.data == None:
                self.ar.data = self.data
            else:
                print("there is a Node contaning a Data pls change your path")
        self.pt[self.data] = self.addr

    def Stackmaker(self , addr):
        self.newadd = self.pt[addr]
        self.art = self.root
        self.stack = []
        self.stack.append([self.root, 'root'])
        for i in self.newadd:
            if i != '*':
                if i == '0':
                    if not self.art.left:
                        print("no path")
                        break
                    self.art = self.art.left
                    self.stack.append([self.art, i])

                elif i == '1':
                    if not self.art.right:
                        print("no path")
                        break
                    self.art = self.art.right
                    self.stack.append([self.art, i])
        return self.stack

    def isdeletable(self,child, parent):
        self.child = child
        self.parent = parent
        if self.child[1] == '0':
            if self.parent[0].data == None and self.parent[0].right == None:
                return True
            else:
                return False

        elif self.child[1] == '1':
            if self.parent[0].data == None and self.parent[0].left == None:
                return True
            else:
                return False

    def Deletion(self,add):
       if add in self.pt:
          print("Done !")
       else:
          return print("prefix does not exist")

       self.stack = self.Stackmaker(add)
       self.index = self.stack.pop(len(self.stack) - 1)
       self.parent = self.stack.pop(len(self.stack) - 1)

       if self.index[0].right == None and self.index[0].left == None:

           while self.isdeletable(self.index, self.parent):
               self.index = self.parent
               if self.stack[len(self.stack)-1][1] == 'root':
                   self.parent = self.stack.pop(len(self.stack) - 1)
                   break
               else:
                   self.parent = self.stack.pop(len(self.stack) - 1)

           if self.index[1] == '1':
               self.parent[0].right = None
           else:
               self.parent[0].left = None

       else:
           self.index[0].data = None

       print(self.Print())

    def Prt(self):

        self.li = []
        self.li.append(self.root)

        while self.li:

            self.count = len(self.li)

            while self.count > 0:
                self.temp = self.li.pop(0)
                if self.temp.data == None:
                    print('no', end='  ')
                else:
                    if self.temp.skipvalue:
                        print(self.temp.data, self.temp.skipvalue, end='  ')
                    else:
                        print(self.temp.data, end='  ')
                if self.temp.left:
                    self.li.append(self.temp.left)
                if self.temp.right:
                    self.li.append(self.temp.right)

                self.count -= 1
            print(' ')

class PathCompTrie :
    def __init__(self,dict):
        self.pathtable = dict
        self.test = Binary_Trie(self.pathtable)
        self.test.CreatRoot()
        self.root = self.test.retu()

    def Prt(self):
        self.li = []
        self.li.append(self.root)

        while self.li:

            self.count = len(self.li)

            while self.count > 0:
                self.temp = self.li.pop(0)
                if self.temp.data == None:
                    print('no', end='  ')
                else:
                    if self.temp.skipvalue:
                        print(self.temp.data, self.temp.skipvalue, end='  ')
                    else:
                        print(self.temp.data, end='  ')
                if self.temp.left:
                    self.li.append(self.temp.left)
                if self.temp.right:
                    self.li.append(self.temp.right)

                self.count -= 1
            print(' ')

    def Isrightorleft(self ,ar, i):
        self.ar=ar
        self.i = i

        if self.i == '1':
            if self.ar.right:
                self.ar = self.ar.right

        elif self.i == '0':
            if self.ar.left:
                self.ar = self.ar.left
        return self.ar

    def Pathlistgen(self,dict):
        self.dict = dict
        #     {'p4':'101*'}
        self.int = 0
        self.pathlist = []
        self.pathlist.append([self.root, '404'])
        self.ar = self.root
        for x, y in self.dict.items():
            for i in y:
                if self.int:
                    self.int -= 1
                    continue

                if i != '*':
                    self.ar = self.Isrightorleft(self.ar, i)
                    self.pathlist.append([self.ar, i])
                else:
                    # befor we put value in final node we must check if the path we've got
                    # is a oneway path or not and if it is we must compress the path
                    self.ar.data = x
                    return self.pathlist
                if self.ar.skipvalue:
                    self.int += self.ar.skipvalue

    def Isitgood(self,last, anlast):
        self.last = last
        self.anlast = anlast
        if self.last[1] == '1':
            if self.anlast[0].left:
                return False
            else:
                if self.anlast[0].data == None:
                    return True
                else:
                    return False
        else:
            if self.anlast[0].right:
                return False
            else:
                if self.anlast[0].data == None:
                    return True
                else:
                    return False

    def Isonewaypath(self,pathlist):
        self.pathlis = pathlist
        self.sv = 0
        if len(self.pathlis) > 1:
            self.las = self.pathlis.pop(len(self.pathlis) - 1)
        else:
            return print('empty list')
        if len(self.pathlis) > 1:
            self.anlas = self.pathlis.pop(len(self.pathlis) - 1)
        else:
            return print('empty list')

        self.data = self.las[0]
        while self.Isitgood(self.las, self.anlas):
            self.las = self.anlas
            self.anlas = self.pathlis.pop(len(self.pathlis) - 1)
            self.sv += 1

        if self.las[1] == '1':
            self.data.skipvalue = self.sv
            self.anlas[0].right = self.data
        else:
            self.data.skipvalue = self.sv
            self.anlas[0].left = self.data

    def Compressroot(self):
        for x , y in self.pathtable.items():
            if len(y)>=3:
                self.jeez = self.Pathlistgen({x:y})
                self.Isonewaypath(self.jeez)

        print(self.Prt())

class MultiBitTrie:
    def __init__(self,dict,stride):
        self.stride=stride
        self.table=dict
        self.root = MTNode(stride)

    def Splitaddress(self,txt):
        self.txt=txt
        self.st = []
        self.a = self.stride
        self.str = ''
        # print(len(txt))
        for i in range(len(self.txt)):
            if self.a != 0:
                if i == len(self.txt) - 1:
                    self.str += self.txt[i]
                    self.st.append(self.str)
                    break
                else:
                    self.str += self.txt[i]
                    self.a -= 1
            elif self.a == 0:
                if i == len(self.txt) - 1:
                    self.str += self.txt[i]
                    self.st.append(self.str)
                    break
                else:
                    self.st.append(self.str)
                    self.a = self.stride
                    self.str = ''
                    self.str += self.txt[i]
                    self.a -= 1
        return self.st

    def Pathmaker(self,st):
        self.st=st
        self.path = []
        for i in self.st:
            self.tool = 0
            for j in i:
                if j != '*':
                    self.tool += 1
            if self.tool == self.stride:
                #     address kamel hast  peyda kon
                self.a = self.stride - 1
                self.s = 0
                for c in i:
                    if c != '*':
                        self.s += int(c) * (math.pow(2, self.a))
                        self.a -= 1
                self.path.append([self.s])
            else:
                #         address kamel nist bayad be andazehye tafavot  tool ba stride halghe sakht va adress khone haro peyda kard
                self.distance = self.stride - self.tool
                self.a = self.stride - 1
                self.s = 0
                for c in i:
                    if c != '*':
                        self.s += int(c) * (math.pow(2, self.a))
                        self.a -= 1
                self.empty = []
                self.empty.append(self.s)
                while len(self.empty) != math.pow(2, self.distance):
                    self.s0 = self.empty[0] + 0 * (math.pow(2, self.a))
                    self.s1 = self.empty[0] + 1 * (math.pow(2, self.a))
                    self.empty.append(self.s0)
                    self.empty.append(self.s1)
                    self.empty.pop(0)
                    if self.a != 0:
                        self.a -= 1
                if len(self.empty) > math.pow(2, self.stride) / 2:
                    self.path.append(['all'])
                else:
                    self.path.append(self.empty)
        return self.path

    def Nodemaker(self,path,txtdata):
        self.path =path
        self.txtdata = txtdata
        self.d = self.root
        while len(self.path) != 0:
            self.first = self.path.pop(0)
            if len(self.first) == 1:
                if self.first[0] == 'all':
                    for k in self.d.list:
                        k.data = self.txtdata
                else:
                    if len(self.path) >= 1:
                        if self.d.list[int(self.first[0])].pointer:
                            self.d = self.d.list[int(self.first[0])].pointer
                        else:
                            self.d.list[int(self.first[0])].pointer = MTNode(3)
                            self.d = self.d.list[int(self.first[0])].pointer
                    else:
                        self.d.list[int(self.first[0])].data = self.txtdata
            else:
                for ir in self.first:
                    self.d.list[int(ir)].data = self.txtdata

    def printit(self,pointerslist):
        self.pointerslist = pointerslist
        for nm in self.pointerslist.list:
            print(nm.data, nm.pointer)
        print('\n\n')

    def Nodefinder(self):
        self.damn = []
        self.damn.append(self.root)
        self.poped = []
        while len(self.damn) != 0:
            self.item = self.damn.pop(0)
            self.poped.append(self.item)
            for new in self.item.list:
                if new.pointer:
                    self.damn.append(new.pointer)
        return self.poped

    def printer(self):
        for i in self.Nodefinder():
            self.printit(i)

    def Creator(self):
        for x, y in self.table.items():
            self.stb = self.Splitaddress(y)
            self.patha = self.Pathmaker(self.stb)
            # print(self.patha)
            self.Nodemaker(self.patha, x)
        self.printer()

