#### Function

class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    print(current.data, end=' ')

    while (current.link != None):
        current = current.link
        print(current.data, end =' ')
    print()

def insertNode(findData, insertData):
    global memory, head, pre, current # 전역변수화

    # 첫 노드 앞에 삽입하는 Case
    if findData == head.data:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    # 중간에 노드를 삽입하는 Case
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    # 마지막 노드 삽입하는 Case
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, pre, current
    # 첫 노드를 삭제
    if deleteData == head.data:
        current = head
        head = head.link
        del(current)
        return
    # 두 번째 이후 노드 삭제
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

#### Global Variable

memory = []
head, pre, current = None, None, None

dataArray = ['다현', '정연', '쯔위', '사나', '지효']

#### Main

node = Node() # 1st Node
node.data = dataArray[0]

head = node

memory.append(node)

for data in dataArray[1:]:
    pre = node
    node = Node()
    node.data = data
    pre.link = node
    memory.append(node)

printNodes(head)

# insertNode('다현', '화사')
# printNodes(head)

# insertNode('사나', '솔라')
# printNodes(head)

# insertNode('재남', '문별')
# printNodes(head)

# deleteNode('다현')
# printNodes(head)

# deleteNode('쯔위')
# printNodes(head)