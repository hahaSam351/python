# 퀴즈1
# a, b, c, d, e를 저장하는 튜플을 만들고 첫 번째 튜플값과
# 마지막번째 튜플값을 출력하여라.

myTuple = ('a', 'b', 'c', 'd', 'e')
print('myTuple = {0}'.format(myTuple))
print('myTuple[0] = {0}, myTuple[-1] = {1}'.format(myTuple[0], myTuple[-1]))



# 퀴즈 2.
# 다음 리스트에서 "Apple" 항목만 삭제하여라 :
# ["Banana", "Apple", "Orange"]

fruits = ["Banana", "Apple", "Orange"]
print(f'fruits = {fruits}')
fruits.remove("Apple") # 값으로 삭제
print(f'fruits = {fruits}')


# 퀴즈 3.
# 다음 튜플 데이터에서 'fun-coding0' 데이터를 첫번째에 추가하여라.
# tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')

tupledata = ('fun-coding1', 'fun-coding2', 'fun-coding3')
print(f'tupledata = {tupledata}')
temp = list(tupledata)
temp.insert(0, 'fun-coding0' )
print(f'temp = {temp}')
tupledata = tuple(temp)
print(f'tupledata = {tupledata}')



# 퀴즈4.
# 다음 항목을 딕셔너리(dict)으로 선언하여라
# : <성인 - 100000 , 청소년 - 70000 , 아동 - 30000>
fare = {'성인':100000 , '청소년':70000 , '아동':30000}
print(f'fare = {fare}')




# 퀴즈5.
# 4번 에서 선언한 dict 항목에 <소아 - 0> 항목을 추가하여라
fare['소아'] = 0
print(f'fare = {fare}')


# 퀴즈6.
# 5번의 딕셔너리(dict)에서 Key 항목만 리스트로 변경하고 정렬한 후
# 튜플로 변경하여라.
#  결과 => ('성인', '소아', '아동', '청소년')
# keys(), list(), tuple(), sort()
print(fare)
temp = list(fare.keys())
print(temp)
temp.sort()
print(temp)
print('결과 => ' , tuple(temp))


# 퀴즈 7.
# number_list에서 중복 숫자를 제거한 후 리스트를 만들어서 출력하여라.
#  number_list = [ 5, 1, 2, 2, 3,4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
# 리스트 => 집합 => 리스트
number_list = [ 5, 1, 2, 2, 3, 4, 5, 6, 7, 6, 7, 8, 9, 9, 10, 10 ]
print('-'*20)
print(number_list)
temp = set(number_list)
print(temp)
print(list(temp))


# 퀴즈 8.
# 두 집합의 중복 값으로 리스트를 생성하여라.
# set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
# set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
# & 연산자
set1 = { '쥬만치', '정글북', '타이타닉', '월E', 'ET' }
set2 = { '타이타닉', '아바타', '에일리언', '스타워즈', '쥬만치'}
result = list(set1 & set2)
print('-'*20)
print(result)


#퀴즈 9.
# 8의 리스트를 다음과 같이 구분자 '/'를 이용한 문자열로 출력하여라.
#  아이템1 / 아이템2 / ....
print('-'*20)
print( ' / '.join(result))


# 퀴즈 10.
# 빈 집합을 생성하고 값을 입력받아 집합의 원소를 삽입하여라.
# 집합 원소의 갯수는 5개로 한다.(입력문+set)
'''
 mySet = set() <class 'set'>
첫번째 아이템 값 => 갈비탕 
두번째 아이템 값 => 소머리국밥
세번째 아이템 값 => 삼계탕
네번째 아이템 값 => 순두부
다섯번째 아이템 값 => 김치찌게
 mySet = {'김치찌게', '소머리국밥', '갈비탕 ', '순두부', '삼계탕'} <class 'set'>
'''
# 빈 집합 정의
# mySet = set()
# print('-'*20)
# print( ' mySet ', mySet, type(mySet))
# mySet.add(input('첫번째 아이템 값 => '))
# mySet.add(input('두번째 아이템 값 => '))
# mySet.add(input('세번째 아이템 값 => '))
# mySet.add(input('네번째 아이템 값 => '))
# mySet.add(input('다섯번째 아이템 값 => '))
# print( ' mySet = ', mySet, type(mySet))


# 퀴즈 11.
# 아래와 같이 리스트를 정의하고 다음과 같이 출력하여라
# foods = ['사과','망고','치즈케이크','쥬스']

# 우리집 냉장고에는?  ['사과', '망고', '치즈케이크', '쥬스']
# 동생이 사과를 먹었다
# 우리집 냉장고에는?  ['망고', '치즈케이크', '쥬스']
# 이모가 수박을 사오셨다.
# 우리집 냉장고에는?  ['망고', '치즈케이크', '쥬스', '수박']
# 동생 친구가 치즈케이크, 수박을 먹었다.
# 우리집 냉장고에는?  ['망고', '쥬스']

foods = ['사과','망고','치즈케이크','쥬스']
print(f'우리집 냉장고에는? {foods}')
# foods.remove('사과')
print(f'동생이 {foods.pop(0)}를 먹었다')
print(f'우리집 냉장고에는? {foods}')
foods.append('수박')
print(f'이모가 {foods[-1]}을 사오셨다.')
print(f'우리집 냉장고에는? {foods}')
print(f'동생 친구가 {foods[2]}, {foods[-1]}을 먹었다.')
foods.remove('치즈케이크')
foods.remove('수박')
print(f'우리집 냉장고에는? {foods}')


