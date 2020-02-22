"""
for in list
- 코드를 필요한 만큼 반복해서 실행
- 리스트 patterns의 값을 하나씩 꺼내 pattern 으로 전달
- 리스트의 길이만큼 print(pattern) 실행
"""

lists = ['1','2','3','4','5']

for v in lists :
    print(v)

"""
for in range
range 함수
- 필요한 만큼의 숫자를 만들어 내는 유용한 기능
- rnage([start,]stop[,step]) 는 for 문과 함께 자주 사용되는 함수이다.
 이 함수는 입력받은 숫자에 해다되는 범위의 범위의 값을 반복 가능한 객체로 만들어 리턴한다
"""

# 인수 1개 - 시작 숫자를 지정해 주지 않으면 range 함수는 0 qnxj tlwkrgksek
list(range(5))
# [0, 1, 2, 3, 4]

# 인수 2개 - 입ㄹ력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다
# 단, 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자
list(range(5, 10))
# [5, 6, 7, 8, 9]

"""
# 인수 3개 - 세 번째 인수는 숫자 사이의 거리를 말한다.
>>> range(1, 10, 3)
[1, 4, 7]
>>> range(20, 10, -2)
[20, 18, 16, 14, 12]
"""

for i in range(5):
  print(i)

# for in list : 순회할 리스트가 정해져 있을 때 사용
# for in range : 순회할 횟수가 정해져 있을 떄 사용

"""
enumerate 함수
- 리스트가 잇는 경우 순서와 리스트의 값을 전달하는 기능
- enumerate 는 열거하다 라는 뜻이다. 
  이 함수는 순서가 있는 자료형 (리스트,튜플,문자열) 을 입력으로 받아 인덱스 값을 포함하는 enuberate 객체를 리턴한다.
- 보통 eumerate 함수는 아래 예제처럼 for문과 함께 자주 사용된다.
"""

for i, name in enumerate(['body','foo','bar']) :
    print(i,name)

"""
for 문처럼 반복되는 구간에서 객체가 현재 어느 위치에 있는지 알려주는 인덱스 값이 필요할때 enmerate 함수를 사용하면 매우 유용하다
"""

names = ['철수', '영희', '영수']
for i, name in enumerate(names):
  print('{}번: {}'.format(i + 1, name))
