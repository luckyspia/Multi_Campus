#### Function

#### Global Variable

# stack = [None, None, None, None, None]
SIZE = 5 # 스택의 크기
stack = [None for _ in range(SIZE)]

top = -1

#### Main

# Push()
top += 1
stack[top] = '커피'

top += 1
stack[top] = '녹차'

top += 1
stack[top] = '꿀물'

print('바닥: ', stack)

print('-----------스택 상태-----------')
for i in range(len(stack)-1, -1, -1):
    print(stack[i])

# Pop()
data = stack[top]
stack[top] = None
top -= 1

print("POP: ", data)