#### Function
def isStackFull():
    global SIZE, stack, top
    if (top >= SIZE-1) :
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if isStackFull() == True:
        print('Stack is full')
        return
    else:
        top += 1
        stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if (top <= -1):
        return True
    else:
        return False

def pop():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('Stack is Empty')
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

def peek():
    global SIZE, stack, top
    if (isStackEmpty()):
        print('Stack is Empty')
        return
    return stack[top]    

#### Global Variable
SIZE = 5 # 스택의 크기
stack = [None for _ in range(SIZE)]

top = -1

#### Main
push('커피')
push('녹차')
push('꿀물')
push('콜라')
push('환타')

print(stack)

push('사이다')

return_data = pop()
print('추출: ', return_data)

print('다음 음료: ', peek())

if __name__ == '__main__':
    select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택하세요: ')

    while (select != X and select!= 'x'):
        if select == 'I' or select == 'i':
            data = input('입력할 데이터: ')
            push(data)
            print('Stack: ', stack)
        elif select == 'E' or select == 'e':
            data = pop()
            print('추출된 데이터: ', data)
            print('Stack: ', stack)
        elif select == 'V' or select == 'v':
            data = peek()
            print('확인된 데이터: ', data)
            print('Stack: ', stack)
        else:
            print('입력 오류')

        select = input('삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택하세요: ')
        
    print('프로그램 종료!')