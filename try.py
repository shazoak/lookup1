from classes import Binary_Trie ,Node , PathCompTrie
from classes import MultiBitTrie

root = Node('root',Node(None,Node(None,Node('c',Node(None,None,Node('h',None,None)),None),None),None),Node('a',Node('b',Node(None,Node('e',None,None),None),None),Node(None,Node('d',None,Node('f',None,None)),Node(None,None,Node('g',None,None)))))

table = {
    'a':'1*',
    'b':'10*',
    'c':'000*',
    'd':'110*',
    'e':'1000*',
    'f':'1101*',
    'g':'1111*',
    'h':'00001*',
}
table1 = {
    'p1':'*',
    'p2':'1*',
    'p3':'00*',
    'p4':'101*',
    'p5':'111*','p6':'1000*','p7':'11101*','p8':'111001*','p9':'1000011*'
}
# making Multi-bit Trie
stride= 3
test = MultiBitTrie(table1,stride)
test.Creator()




# making PathCompTrie
# test = PathCompTrie(table1)
# test.Compressroot()




# makking Binary Trie
# test=Binary_Trie(table1)
# test.CreatRoot()

















