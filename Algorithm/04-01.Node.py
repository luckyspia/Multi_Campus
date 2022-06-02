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

# node_1 을 통해 접근해야 함
print(node_1.data, end=' ')
print(node_1.link.data, end=' ')
print(node_1.link.link.data, end=' ')
print(node_1.link.link.link.data, end=' ')
print(node_1.link.link.link.link.data, end=' ')
