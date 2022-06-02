### 함수 선언부
def add_data(friend):
    katok.append(None)
    kLen = len(katok)
    katok[kLen-1] = friend

def insert_data(position, friend):
    katok.append(None)
    kLen = len(katok)

    for i in range(kLen-1, position, -1):
        katok[i] =  katok[i-1]
        katok[i-1] = None

    katok[position] = friend

def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1, kLen):
        katok[i-1] = katok[i]
        katok[i] = None

    del(katok[kLen-1])

### 전역 변수부
katok = []
select = -1


### 메인 코드부
while (select !=4):

    select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)----->"))

    if select == 1:
        friend = input('추가할 친구의 이름 입력: ')
        add_data(friend)
        print(katok)

    elif select == 2:
        pos = int(input('삽입할 위치: '))
        friend = input('추가할 친구의 이름: ')
        insert_data(pos, friend)
        print(katok)

    elif select == 3:
        pos = int(input('삭제할 위치: '))
        delete_data(pos)
        print(katok)
    
    elif select == 4:
        print(katok)
        exit
    else:
        print("1~4 중 하나를 입력하세요")
        continue