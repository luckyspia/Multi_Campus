#### Function
class Node():
    def __init__(self):
        self.data = None
        self.link = None

#### Main
node_1 = Node()
node_1.data = '다현'

node_2 = Node()
node_2.data = '정연'
node_1.link = node_2

node_3 = Node()
node_3.data = '쯔위'
node_2.link = node_3

node_4 = Node()
node_4.data = '사나'
node_3.link = node_4

node_5 = Node()
node_5.data = '지효'
node_4.link = node_5

# Data Insert
newNode = Node()
newNode.data = '재남'
newNode.link = node_2.link

node_2.link = newNode

# Data Delete (Insert 와 둘 중 하나만 실행)
node_2.link = node_3.link
del(node_3)

current = node_1
print(current.data, end=' ')

while (current.link != None):
    current = current.link
    print(current.data, end =' ')

print('END')