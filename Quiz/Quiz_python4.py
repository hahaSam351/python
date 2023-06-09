# 퀴즈 1
# 함수를 호출하면 각각의
# 구성 아이템이 다음과 같이 출력되도록 함수를 정의하여라
# 입력되는 메뉴데이타의 값은 가변으로 한다.
# 메뉴데이타가 없는 경우 품절 메세지를 출력한다.

'''
# printList('라면', '빙수')

   오늘의 메뉴
1  :  라면
2  :  빙수

# printList('모밀', '탕수육', '육계장')
   오늘의 메뉴
1  :  모밀
2  :  탕수육
3  :  육계장


# printList()
모두 품절되었습니다.
'''




# 퀴즈 2
# 아래의 예제를 참조하여 함수를 호출하면 메세지가 출력되도록
# 함수를 정의하여라
# 이때 함수 인자는 3개로 구성하며 마지막 man 만 True 형태로
# 초기값을 지정한다.
'''
# 함수 정의 
def say_myself(name, old, man=True):
    ?

# 함수 호출 
say_myself('김철수', 20)
say_myself('백설공주', 15, False)

# 결과값 1
나의 이름은 김철수 입니다.
나이는 20살입니다.
남자입니다.
--------------------------------------------------
# 결과값 2
나의 이름은 백설공주 입니다.
나이는 15살입니다.
여자입니다.

'''




# 퀴즈 3
# 여러가지 값이 리스트에 저장될 수 있게
# 인자가 가변인 함수를 정의하고 호출하여라
'''
# 함수 호출 
addList(1,2,3,4)
addList('가','나','다','라','마')

결과1 >>>
총 갯수 : 4
데이타형 : <class 'list'>
0 번째 => 1
1 번째 => 2
2 번째 => 3
3 번째 => 4

결과2 >>>
총 갯수 : 5
데이타형 : <class 'list'>
0 번째 => 가
1 번째 => 나
2 번째 => 다
3 번째 => 라
4 번째 => 마


'''





# 퀴즈 4
# 첫번째 인자의 값이 'min'이면 다음 인자의 숫자 중
# 최대값을 출력하고
# 첫번째 인자의 값이 'max'이면 다음 인자의 숫자중
# 최소값을 출력하여라
# 이 때 전달하는 숫자의 갯수는 가변으로 한다.

'''
min_max_number('min', 100, 20, 40)
min_max_number('min', 100, 20, 40, 500, 1)
min_max_number('max', 100, 20, 40)
min_max_number('max', 100, 20, 40, 500, 1)

# 결과 
최소값은?  20
최소값은?  1
최대값은?  100
최대값은?  500

'''




# 퀴즈 5
# 7개의 입력받은 숫자 값을 리스트로 저장한 후
# 최대값과 최소값을 출력하도록 함수를 정의하고 호출하여라.
'''
숫자 1? .... 56
숫자 2? .... 34
숫자 3? .... 100
숫자 4? .... 23
숫자 5? .... 78
숫자 6? .... 90
숫자 7? .... 3
입력 리스트 :  ['56', '34', '100', '23', '78', '90', '3']
최소값 :  100
최대값 :  90
'''




# 퀴즈6
# aList = [78,90,80,50]
# bList = [8,100,34,60]
# 두개의 리스트 요소중에서 최대값과 최소값을 출력하여라
# 함수 이용

'''
aList = [78,90,80,50]
bList = [8,100,34,60]

최소값 : 8
최대값 : 100
'''




# 퀴즈 7
# 별의 갯수를 인자값으로 지정하면
# 아래와 같은 형태로 출력되도록 함수를 정의하고 호출하여라.
'''
# 함수 호출 
# start(5) 
====================
*
* *
* * *
* * * *
* * * * *


# 함수 호출 
# start(7) 
====================
*
* *
* * *
* * * *
* * * * *
* * * * * *
* * * * * * *

'''



# 퀴즈 8
# 리스트를 딕셔너리 리스트(리스트안의 딕셔너리 구조)로 변경되도록 함수를 이용하여
# 프로그래밍 하여라
# 이때 딕셔너리 키는 'user숫자' 형태이다.
'''
valueList = ['양준일', '노사연', '구창모', '조용원', '김정화']

# 결과 =>
[{'user1': '양준일'}, {'user2': '노사연'}, {'user3': '구창모'}, {'user4': '조용원'}, {'user5': '김정화'}]
'''




# 퀴즈 9
# numList의 값을 모두 양수로 변경해서 리스트로 반환하는 함수를 정의하고 호출하여라.

# numList = [100, -45, 20, 40, -500]
# 결과
# [100, 45, 20, 40, 500]




# 퀴즈 10
# 문자열에서 숫자와 글자를 제외하고 나머지 글자만 리스트로로
# 출력되도록 함수를 정의하고 호출하여라
'''
  myString = a4+5b6&word*bn%~564^3
 숫자와 글자 제외 결과 리스트 = ['+', '&', '*', '%', '~', '^']
 총 갯수 = 6
'''




# 퀴즈 11
# n개의 단어를 입력받은 후 리스트로 저장되도록 프로그래밍하여라.
# 이때 저장되는 리스트에는 중복값이 없어야 하며 함수를 이용하여야 한다.

'''
# 함수 호출시 
단어를 입력하세요 ... 장발장
단어를 입력하세요 ... 신데렐라
단어를 입력하세요 ... 콩쥐팥쥐
단어를 입력하세요 ... 라푼젤
단어를 입력하세요 ... 라푼젤
단어를 입력하세요 ... 선녀와 나뭇꾼
입력된 단어 리스트 : ['장발장', '신데렐라', '콩쥐팥쥐', '라푼젤', '선녀와 나뭇꾼'] 
'''

