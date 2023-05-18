# 퀴즈 1
# 입력받은 수식에 관련된 결과계산값을 출력한다.
# eval() 이용
'''
계산식 입력 >> 3+4*20-100

결과 >>
3+4*20-100 = ?

'''

# result = input('계산식을 입력하세요?.... ')
# print('결과 >>')
# print(result, ' = ', eval(result))


# =========================
# 퀴즈 2
# enumerate() 함수를 이용하여 아래 리스트를
# 딕셔너리 형태로 변환한 후
# 아래 형태로 출력하여라
'''
foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']
foodDict = {1: '감자탕', 2: '떡국', 3: '모밀냉면', 4: '연어덮밥', 5: '케이준 샐러드'}

1 번째 메뉴: 감자탕
2 번째 메뉴: 떡국
3 번째 메뉴: 모밀냉면
4 번째 메뉴: 연어덮밥
5 번째 메뉴: 케이준 샐러드


'''

foodList = ['감자탕', '떡국', '모밀냉면', '연어덮밥', '케이준 샐러드']
foodDict = dict(enumerate(foodList, 1))
print('foodDict = ', foodDict)
for key in foodDict:
    print('{} 번째 메뉴: {}'.format(key, foodDict[key]))


# =========================
# 퀴즈 3
# zip() 함수등을 이용하여 myDict 를 myTupleList 로 변경하여라
'''
myDict = {'p': 'python', 'm': 'mySql', 'n': 'numpy', 'h': 'html'}, <class 'dict'>
myTupleList = [('p', 'python'), ('m', 'mySql'), ('n', 'numpy'), ('h', 'html')], <class 'list'>
'''

myDict = {'p': 'python', 'm': 'mySql', 'n': 'numpy', 'h':'html'}
print(f'myDict = {myDict}, {type(myDict)}')
# 키 조합으로 리스트 생성
key_list = list(myDict)
value_list = list(myDict.values())
myTupleList = list(zip(key_list, value_list))
# zip 객체로 변경한 후 하나씩 출력
print(f'myTupleList = {myTupleList}, {type(myTupleList)}')


# =========================
# 퀴즈 4
# 대문자 A ~ Z, 소문자 a ~ z 의 조합으로 구성된 리스트를 생성하고 출력하여라.
# chr() , ord() 를 이용
'''
['Aa', 'Bb', 'Cc', 'Dd', 'Ee', 'Ff', 'Gg', 'Hh', 'Ii', 
        'Jj', 'Kk', 'Ll', 'Mm', 'Nn', 'Oo', 'Pp', 'Qq', 'Rr',
         'Ss', 'Tt', 'Uu', 'Vv', 'Ww', 'Xx', 'Yy', 'Zz']
'''


print(ord('A')) # 65
print(ord('Z')) # 90
# upper_alpha_list = [chr(i)+chr(i).lower() for i in range(65, 91)]
upper_alpha_list = [chr(i)+chr(i).lower() for i in range(ord('A'), ord('Z'))]
print(upper_alpha_list)

# =========================
# 퀴즈 5
# time 모듈에서 제공하는 함수를 이용하여 아래와 같이 오늘 날짜를 기준으로
# 출력되도록 하여라.
'''
오늘은 ? 월  ? 입니다.
1년을 기준으로 ? 번째 날이며 올해는 ? 일 남았습니다. 
'''

import time

now = time.localtime(time.time())
print(now)
print(f'오늘은 {now.tm_year} 년 {now.tm_mon} 월  {now.tm_mday}일 입니다.')
print(f'1년을 기준으로 {now.tm_yday} 번째 날이며 올해는 {365-now.tm_yday} 일 남았습니다. ')

# =========================
# 퀴즈 6
# time 모듈에서 제공하는 함수를 이용하여
# 특정 날짜에 대한 요일을 출력하여라.

# 나는 무슨 요일에 태어났을까? ..... ? 요일

d_day = '2009-12-03'
tm = time.strptime(d_day, '%Y-%m-%d')
print(tm, type(tm))
print(time.strftime('%A', tm)) # Thursday
day_list = ['월', '화', '수', '목', '금', '토', '일']
print(tm.tm_mday, day_list[tm.tm_mday])

# =========================
# 퀴즈 7
# datetime 모듈에서 제공하는 함수를 이용하여
# 특정 날짜를 기준으로 몇일이 남았는지 출력하여라

# 오늘 : ????-??-??
# 수료일 2022-01-25 ...
# ? 일 남았습니다.


import datetime

# 날짜 데이타로 생성
date1 = datetime.datetime(2022,1,25).date()
# date2 = datetime.datetime(2021,9,2).date()
date2 = datetime.datetime.now().date()

print(date1, type(date1))
print(date2, type(date2))
print(date1-date2, type(date1-date2))
print(str(date1-date2)[:3])


# =========================
# 퀴즈 8
# 문자열 변수를 정의하고 숫자와 글자를 제외한
# 나머지 글자를 리스트 형태로 출력하도록 프로그래밍하여라.
# 단 filter() 함수를 활용한다.

'''
 myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 =  ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''
# print('-'*20)
# myString = 'a4+5b6&word*bn%~564^3'
# print(f'\n filter() 함수 활용 >> \n myString = {myString}')
# def filtering_f(c):
#     if not (c.isdigit() or c.isalpha()):
#        return True
# # print(' '.join(myString).split())
# print(' 숫자와 글자 제외 결과 리스트 = ', list(filter(filtering_f, ' '.join(myString).split())))
# print(f' 총 갯수 = {len(list(filter(filtering_f, " ".join(myString).split())))}')
#
#
# print(f'\n filter()와 lambda 함수 활용 >> \n myString = {myString}')
# # f = lambda x : not(x.isdigit()) and not(x.isalpha())
# # print(f('100'))
# # print(f('a'))
# # print(f('@'))
# '''
# False
# False
# True
# '''
# # ' '. join(myString).split()
#
# # lambda로 변경
# print(' 숫자와 글자 제외 결과 리스트 = ', list(filter(lambda x : not(x.isdigit()) and not(x.isalpha()), ' '. join(myString).split() )))
# print(f' 총 갯수 = {len(list(filter(lambda x : not(x.isdigit()) and not(x.isalpha()), " ". join(myString).split() )))}')

# =========================
# 퀴즈 9
# 5~10 까지의 모든 수의 곱이 출력되도록 프로그래밍하여라.
# lambda 함수, reduce()를 이용해야한다.

# reduce() 함수 임포트 명령어는?
# import functools as f

'''
5 ~ 10 까지의 곱 >> 
numList = [5, 6, 7, 8, 9, 10]
5 X 6 X 7 X 8 X 9 X 10  =  151200
'''



# print(f'\n\n lambda 함수, reduce() 이용 >> 5~10까지의 곱 >> ')
# numList = list(range(5,11))
# print(f' numList = {numList}')
# import functools as f
# print(" X ".join([str(i) for i in numList ]) , ' = ', f.reduce(lambda x,y:x*y , numList))

# =========================
# 퀴즈 10
# 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경되도록 프로그래밍하여라.
# 이때 딕셔너리 키는 'class숫자' 형태이며
# map 함수를 이용해야한다.
'''
 map함수와 lambda 이용 결과 >> 
 class_list = ['python', 'mySQL', 'HTML', 'CSS', 'scrapping', 'kaggle']
[{'class_1': 'python'}, {'class_2': 'mySQL'}, {'class_3': 'HTML'}, {'class_4': 'CSS'}, {'class_5': 'scrapping'}, {'class_6': 'kaggle'}]
'''


class_list = ['python', 'mySQL', 'HTML', 'CSS', 'scrapping', 'kaggle']
print(f'\n map함수와 lambda 이용 결과 >> \n class_list = {class_list}')
print(list(map(lambda k,v:{'class_' + str(k): v}, list(range(1,len(class_list)+1)), class_list)))


# =========================
# 퀴즈 11
# 다음 리스트를 이용하여 7개의 이름으로 구성된 리스트를 생성하여라.
# 이때 최종 리스트는 중복 이름이 없어야하며 가나다순으로 정렬되어야한다.
'''
first_name = ['박', '김', '이', '최', '신', '장', '윤']
last_name1 = ['은', '강', '종', '영', '준', '민']
last_name2 = ['철','수', '미', '원', '주', '혁', '희', '수']

>>> 생성된 이름 예시 
['박영수', '박준혁', '신영수', '신종주', '이민수', '이종혁', '최강철']

'''

import random

first_name = ['박', '김', '이', '최', '신', '장', '윤']
last_name1 = ['은', '강', '종', '영', '준', '민']
last_name2 = ['철','수', '미', '원', '주', '혁', '희', '수']

def make_name():
    name_list = []
    while True:
        x = random.choice(first_name)
        y = random.choice(last_name1)
        z = random.choice(last_name2)
        if len(name_list) >= 7:
            break
        if (x + y + z) not in name_list:
            name_list.append(x + y + z)
    name_list.sort()
    print(name_list)

make_name()

# =========================
# 퀴즈 12
# 알파벳, 숫자, 특수문자(!$%#@*^&)로 구성된
# 비밀번호 리스트를 생성하여라
# 중복번호 없음. 비밀번호는 8글자.
# 비밀번호 리스트의 전체 길이는 5
'''
>>> 비밀번호 예시 
['CER9jvT3', 'QRUc!f^J', 'FQPtBKGZ', '8adlQIFb', 'j8Prk&l9']
'''

upper_alpha_list = [chr(i) for i in range(65, 91)]
lower_alpha_list = [chr(i).lower() for i in range(65, 91)]
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special_character_list = list('!$%#@*^&')
print(upper_alpha_list)
print(lower_alpha_list)
print(num_list)
print(special_character_list)
p_list = upper_alpha_list + lower_alpha_list + num_list + special_character_list
pwd_list = []
while True:
    if len(pwd_list) >= 5 :
        break
    random.shuffle(p_list)
    temp = ''.join(p_list[:8])
    if temp not in pwd_list:
        pwd_list.append(temp)

print(pwd_list)
