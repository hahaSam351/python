
# 1. 다음과 같은 형태로 반복문을 이용하여 출력하여라.
'''
====================
*
* *
* * *
* * * *
* * * * *
====================
        *
      * *
    * * *
  * * * *
* * * * *
====================
         *
        * *
       * * *
      * * * *
     * * * * *
====================

     * * * * *
      * * * *
       * * *
        * *
         *

'''
# 첫번째
print('='*50)
cnt = 1
while cnt<=5:
    print("* "*cnt)
    cnt += 1

print('='*50)
for i in range(1, 6):
    print("* " * i)

# 2번째
print('='*50)
cnt = 1
while cnt<=5:
    print(f'{"* "*cnt:>10}')
    cnt += 1


# 3번째
print('='*50)
cnt = 1
while cnt<=5:
    print(f'{"* "*cnt:^20}')
    cnt += 1

print('='*50)
for i in range (6):
    print((" ")*(5 - i), end='')
    print((" *")*i)
    i +=1

# 4번째
print('='*50)
cnt = 5
while cnt>0:
    print(f'{"* "*cnt:^20}')
    cnt -= 1

print('='*50)
for i in range(1, 6):
    idx = []
    star = ''
    for j in range(i, 11-i, 2):
        idx.append(j)
    for x in range(1, 10):
        if x in idx:
            star += '*'
        else:
            star += ' '
    print(star)



# 2. bmi 값에 따라 다음과 같은 메세지를 출력하여라.
'''
# 키를 입력해주세요... 단위 cm...175
# 체중을 입력해주세요... 단위 kg...67
# bmi = 21.8776
# ?
'''


# bmi 공식
# k = 키(입력값) 단위 cm
# w = 체중(입력값)
# bmi = 체중(kg)/키(m)의제곱, 키의 단위는 미터(m)

# bmi 값에 따라 출력되는 메세지
# 고도 비만 : 35 보다 클 경우
# 중등도 비만  : 30 - 35 미만
# 경도 비만 : 25 - 30 미만
# 과체중 : 23 - 25 미만
# 정상 : 18.5 - 23 미만
# 저체중 : 18.5 미만


# t = int(input('키를 입력해주세요... 단위 cm...'))
# w = int(input('체중을 입력해주세요... 단위 kg...'))
# # 미터로 변경
# t2 = t/100
# # bmi = w/(t2*t2)
# bmi = w/(t2**2)
#
# print( f'bmi = {bmi:.2f}' )
#
# if bmi>=35 :
#     print('고도 비만')
# if 30 <= bmi < 35 :
#     print('중등도 비만')
# if 25 <= bmi < 30 :
#     print('경도 비만')
# if 23 <= bmi < 25 :
#     print('중등도 비만')
# if 18.5 <= bmi < 23 :
#     print('정상')
# if bmi < 18.5 :
#     print('저체중')




# 3. 1~30까지 숫자중에서 3의 배수만 제외하고 출력하여라.
cnt = 0
while cnt < 30:
    cnt += 1
    if cnt%3 == 0:
        continue
    print(cnt, end=' ')



# 4. 학점을 입력받아서 다음과 같은 메세지를 출력하여라.
# score = float(input("학점 입력> "))
# if ~ elif ~ else 문 이용하여 메세지 출력
#
# 4.2 <= score <= 4.5 : 교수님의 사랑
# 3.5 <= score < 4.2 : 현 체제의 수호자
#  2.8 <= score < 3.5 : 일반인
# 2.3 <= score < 2.8  : 일탈을 꿈꾸는 소시민
# 2.3 미만 : 시대를 앞서가는 혁명의 씨앗
#
# '''
# 학점 입력> 4.5
#
# score = 4.5   : 교수님의 사랑
#
# '''
# print()
# print('='*50)
# score = float(input("학점 입력> "))
# if 4.2 <= score <= 4.5 :
#     print(f'score = {score} : 교수님의 사랑')
# elif 3.5 <= score < 4.2 :
#     print(f'score = {score} : 현 체제의 수호자')
# elif 2.8 <= score < 3.5 :
#     print(f'score = {score} : 일반인')
# elif 2.3 <= score < 2.8 :
#     print(f'score = {score} : 일탈을 꿈꾸는 소시민')
# elif 2.3 > score :
#     print(f'score = {score} : 시대를 앞서가는 혁명의 씨앗')
# else:
#     print('입력 값이 올바르지 않습니다.')





# 5. 세 개의 숫자를 입력받아 리스트로 구성하고 가장 큰 수를 출력하여라.
# 리스트, input, for, while 반복문
# '''
# 첫번째 숫자 입력 => 100
# 두번째 숫자 입력 => 59
# 세번째 숫자 입력 => 70
# numList = [100, 59, 70]
# 가장 큰 수는 100 입니다.


# # 조건문만 이용
# # 숫자를 입력받아서 리스트 생성
# numList = []
# numList.append(int(input('첫번째 숫자 입력 => ')))
# numList.append(int(input('두번째 숫자 입력 => ')))
# numList.append(int(input('세번째 숫자 입력 => ')))
#
# # 리스트에서 최댓값 구하기
# result = numList[0]
#
# if result < numList[1]:
#     result = numList[1]
#     if result < numList[2]:
#         result = numList[2]
# else:
#     if result < numList[2]:
#         result = numList[2]
#
# print(f'numList = {numList}')
# print(f'가장 큰 수는 {result} 입니다.')
#
# # for 문 이용
# num1 = int(input('첫번째 숫자 입력 => '))
# num2 = int(input('두번째 숫자 입력 => '))
# num3 = int(input('세번째 숫자 입력 => '))
# # 리스트 생성
# numList = [num1,num2,num3]
# maxi = numList[0]
# for i in numList :
#     if i > maxi :
#         maxi = i
#     else : pass
# print (f'가장 큰 수는 {maxi} 입니다.')
#
# # while 문
# f = int(input('첫번째 숫자 입력 => '))
# s = int(input('두번째 숫자 입력 => '))
# t = int(input('세번째 숫자 입력 => '))
# numList = [f, s, t]
# temp = numList[0]
# cnt = 0
# while (cnt<len(numList)):
#      if numList[cnt] > temp:
#          temp = numList[cnt]
#      cnt += 1
# print(f'가장 큰 수는 {temp}입니다.')

# 참고 리스트 관련 함수
# min(리스트) => 최솟값
# sum(리스트) => 합계
# max(리스트) => 최댓값



# 6. 숫자값을 입력받아 총 길이 5의 리스트를 생성하고 최대값과 최소값을 출력하여라
'''
숫자 1 입력 .... ?
숫자 2 입력 .... ?
숫자 3 입력 .... ?
숫자 4 입력 .... ?
숫자 5 입력 .... ?

생성된 리스트 ...  ?
최대값은 ... 999
최솟값은 ... -30
'''

# myNumList2 = [100, 200, 50, -30, 999, 10, -30]
# print('Before = ',myNumList2)
# myNumList2 = list(set(myNumList2))
# cnt = 0
# target1 = myNumList2[0]
# target2 = myNumList2[0]
# while cnt<len(myNumList2) :
#     if target1<myNumList2[cnt]:
#         target1 = myNumList2[cnt]
#     if target2>myNumList2[cnt]:
#         target2 = myNumList2[cnt]
#     cnt += 1
#
# print('최대값은?', target1)
# print('최솟값은?', target2)
# myNumList2.remove(target1)
# myNumList2.remove(target2)
# print('Result = ', myNumList2)
# print('-'*30,'\n\n')





# 7. 딕셔너리 값에 'a' 글자가 있는 아이템만 표시하고 총 갯수를 출력하여라
# dict2 = {'a': 'africa', 's': 'say',
#         'c': 'coffee', 'd': 'drama', 'y':'yes'}

# dict2 = {'a': 'africa', 's': 'say',
#         'c': 'coffee', 'd': 'drama', 'y':'yes'}
# tot = 0
# for key in dict2:
#     if 'a' in dict2[key]:
#         print(f'{key} => {dict2[key]}')
#         tot += 1
# print('총 갯수는? ', tot)



# 8. 다음 리스트 중에서 '을' 글자를 제외하고 출력하여라.
# for, if 이용
# '''
# qList = ['갑', '을', '병', '정']
# 갑 / 병 / 정 /
# '''

qList = ["갑", "을", "병", "정"]
# 전체 리스트 출력
print('qList = {}'.format(qList))
for i in qList:
    if i == '을':
        pass
    else:
        print(i, end=' / ')



# 9. 1부터 30까지 자연수 중 '홀수'만 한 라인으로 출력 하여라.
#  반복문 for와 조건문 사용
'''
 Result -------------------- 

1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 
'''
# 방법1
# print('\n\n Result', '-'*20, '\n')
# for i in range(1, 31):
#     if i%2 == 0:
#         pass
#     else:
#         print(i, end=' ')
# print()

# 방법 2
# print('-'*50)
# for i in range(1, 31, 2):
#     print(i, end=' ')

# 방법3
print()
print(list(range(1, 31, 2)))


# 10. 1부터 50까지 자연수 중 6의 배수만 리스트로 생성하고 다음과 같이 출력 하여라.
'''
Result --------------------
결과 리스트 = [6, 12, 18, 24, 30, 36, 42, 48]
총합 = 216
'''
# 방법1
# print('\n\n Result', '-'*20)
# result = []
# count = 1
# sum = 0
# while count<51:
#     if count%6 == 0:
#         result.append(count)
#         sum += count
#     count += 1
#
# print('결과 리스트 = %s' % result)
# print('총합 = %d' % sum)

# 방법 2
result = list(range(0,50,6))[1:]
print('결과 리스트 = %s' % result)
print('총합 = %d' % sum(result))



# 11. 다음 리스트에서 평균, 합, 최소값을 출력하여라.
# 리스트 : [95, 77, 56, 100, 85]
# 합 : 413
# 평균 : 82.60
# 최소값 : 56

# 방법 1
# numList = [95, 77, 56, 100, 85]
# sum = 0
# minNumber = numList[0]
# for i in numList:
#     sum+=i
#     if minNumber>i:
#         minNumber = i
#
# print(f'리스트 : {numList}')
# print(f'합 : {sum}')
# avg = sum/len(numList)
# print(f'평균 : {avg:.2f}')
# print(f'최소값 : {minNumber}')

# 방법 2
# statistics 연결
import statistics
numList = [95, 77, 56, 100, 85]
print(f'리스트 : {numList}')
print(f'합 : {sum(numList)}')
# 모듈명.함수(옵션)
print(f'평균 : {statistics.mean(numList):.2f}')
print(f'최소값 : {min(numList)}')



# 12. 아래 리스트 항목 중에서 5글자 이상의 단어만 출력하여라.
# 제어문과 len() 이용
# qList2 = ["nice", "study", "python", "anaconda", "!"]

qList2 = ["nice", "study", "python", "anaconda", "!"]
print(f'qList2 = {qList2}')
print('Result','-'*30)
for i in qList2:
    if len(i)>=5:
        print(i, end=' ')
print()
print('-'*30,'\n\n')




# 13. 다음과 같은 wordList 에서 첫 글자만 추출하여 keyList 리스트를 만들고
#  두개의 리스트 조합으로 딕셔너리를 만들어 출력하여라.
# 첫글자를 추출한다. => 리스트 keyList
# 빈 딕셔너리 정의
# 딕셔너리로 구성 :  keyList => 키 , wordList => 데이타
# '''
# wordList = ['nice', 'study', 'python', 'anaconda', 'mySQL']
# keyList = ['n', 's', 'p', 'a', 'm']
# Result ------------------------------
#  dictList = {'n': 'nice', 's': 'study', 'p': 'python', 'a': 'anaconda', 'm': 'mySQL'}
# '''

# wordList = ['nice', 'study', 'python', 'anaconda', 'mySQL']
# keyList = []
# dictlist = {}
#
# for word in wordList:
#     keyList.append(word[0])
# print(keyList)
#
# for i, val in enumerate(keyList):
#     dictlist[val] = wordList[i]
# print(dictlist)


wordList = ['nice', 'study', 'python', 'anaconda', 'mySQL']
# 첫글자만 인덱싱해서 리스트 생성
keyList = []
for i in wordList:
    keyList.append(i[0])

print(f'wordList = {wordList}')
print(f'keyList = {keyList}')
print('Result','-'*30)

# 딕셔너리 생성 과정
# 딕셔너리명[키] = 값
dictList = {}
for i in range(0, len(wordList)):
    dictList[keyList[i]] = wordList[i]
print(f' dictList = {dictList}')
print('-'*30,'\n\n')



# 14. 1~100 사이의 숫자 중 11의 배수이거나 7의 배수로 구성된 리스트를
# 리스트 내포 방식을 이용하여 출력하고 총 갯수도 함께 출력하여라.
'''
[7, 11, 14, 21, 22, 28, 33, 35, 42, 44, 49, 55, 56, 63, 66, 70, 77, 84, 88, 91, 98, 99]
 총 22 개
'''

# 일반 리스트 생성 후 for 문 이용
numList = []
for i in range(1, 101):
    if (i%11 == 0) or (i%7==0):
        numList.append(i)
print(numList)
print(f' 총 {len(numList)} 개')
print('-')

# 리스트 내포방식1
numList = [ i for i in range(1,101) if (i%11==0) or (i%7==0)]
print(numList)
print(f' 총 {len(numList)} 개')

# 리스트 내포방식2
numList = [i for i in list(range(1,101)) if (i % 7 == 0) or (i % 11 == 0)]
print(numList)
print(f' 총 {len(numList)} 개')



# 15. 이중 리스트 내포 방식을 이용하여 다음과 같은 리스트를 생성하고 출력하여라.
# ['1 - 1', '1 - 2', '1 - 3', '2 - 1', '2 - 2', '2 - 3',
#    '3 - 1', '3 - 2', '3 - 3', '4 - 1', '4 - 2', '4 - 3',
#    '5 - 1', '5 - 2', '5 - 3']

print('\n'*2)
result = []
for i in range(1,6):
    for j in range(1,4):
        # result.append(f'{i} - {j}')
        result.append(str(i) + ' - ' + str(j))
print(result)

# 리스트 내포 방식
result2 = [f'{i} - {j}' for i in range(1,6) for j in range(1,4)]
print(result2)


# 16. 다음 2차원 리스트를 생성하고 결과와 같이 for...in 문을 이용하여 출력하여라.
# employees = [
#                 ['김수철', '서울', 25, '남', '총무부'],
#                 ['고길동', '부산', 33, '남', '회계부'],
#                 ['최미나', '대전', 22, '여', '기획부'],
#                 ['은지원', '서울', 44, '남', '영업부'],
#                 ['김영탁', '울산', 36, '남', '영업부'],
#                 ['마동탁', '대구', 50, '남', '기획부'],
#                 ['이은미', '창원', 42, '여', '총무부']
#               ]
#
# 	----------------------------------------
#  	 사원명 	 출신지 	 나이 	 성별 	 부서
# 	----------------------------------------
#  	 김수철 	 서울 	 25 	 남 	 총무부
#  	 고길동 	 부산 	 33 	 남 	 회계부
#  	 최미나 	 대전 	 22 	 여 	 기획부
#  	 은지원 	 서울 	 44 	 남 	 영업부
#  	 김영탁 	 울산 	 36 	 남 	 영업부
#  	 마동탁 	 대구 	 50 	 남 	 기획부
#  	 이은미 	 창원 	 42 	 여 	 총무부


print('\t'+'-'*40)
employees = [
                ['김수철', '서울', 25, '남', '총무부'],
                ['고길동', '부산', 33, '남', '회계부'],
                ['최미나', '대전', 22, '여', '기획부'],
                ['은지원', '서울', 44, '남', '영업부'],
                ['김영탁', '울산', 36, '남', '영업부'],
                ['마동탁', '대구', 50, '남', '기획부'],
                ['이은미', '창원', 42, '여', '총무부']
              ]
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t 부서 ')
print('\t'+'-'*40)
for (name, homtown, age, gender, part) in employees:
    print(f' \t {name} \t {homtown} \t {age} \t {gender} \t {part} ')



# 17. 16번의 리스트에서 남자 사원 목록만 출력하여라.
# if ~  연산자

print('\t'+'-'*40)
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t 부서 ')
print('\t'+'-'*40)
for (name, homtown, age, gender, part) in employees:
    if gender == '남':
        print(f' \t {name} \t {homtown} \t {age} \t {gender} \t {part} ')


# 18. 16번의 리스트에서 성이 '김'인 사원 목록만 출력하여라.
print('\t'+'-'*40)
print(f' \t 사원명 \t 출신지 \t 나이 \t 성별 \t 부서 ')
print('\t'+'-'*40)
for (name, homtown, age, gender, part) in employees:
    if name[0] == '김':
        print(f' \t {name} \t {homtown} \t {age} \t {gender} \t {part} ')

