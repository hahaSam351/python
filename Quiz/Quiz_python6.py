# 퀴즈 1
# 삼각형을 클래스를 생성한 후 2개의 삼각형을 인스턴스화한 후
# 속성(이름, 밑변, 높이)과 메서드(면적, 삼각형 정보)를 정의하고 출력하여라
# 삼각형의 면적 구하는 공식 (밑변의길이 * 높이)/2

'''

 --------------------
삼각형 이름 :  triangle1
삼각형의 밑변 :  10
삼각형의 높이 :  5
삼각형의 면적 :  ?

 t2는 Triangle의 인스턴스인가요? True
 --------------------
삼각형 이름 :  triangle2
삼각형의 밑변 :  20
삼각형의 높이 :  10
삼각형의 면적 :  ?
'''


# ============================
# 퀴즈 2
# Cat 클래스를 만들고 인스턴스한 후 메서드를 호출하여라
# 속성 : kind, name, age, gender, animal_kind(고양이)
# 메서드 :  속성출력(print_info), 동작 : run, sleep(어디서), eat(무엇을)

# 인스턴스화 예)
# cat1 = Cat('코캣', '덩치', 1, '남')
# cat2 = Cat('러시안블루', '나비', 5, '여')
'''
# cat1.print_info()
 종류 = 러시안블루
 이름 = 나비
 나이 = 5
 성별 = 여

# cat1.run()
고양이 덩치 가 달린다.
# cat2.run()
고양이 나비 가 달린다.
# cat1.sleep('캣타워')
고양이 덩치가 캣타워에서 잔다.
# cat2.sleep('캣타워')
고양이 나비가 택배 박스에서 잔다.
# cat1.eat('사료')
고양이 덩치가 사료을(를) 먹는다.
# cat2.eat('춥스')
고양이 나비가 춥스을(를) 먹는다.

'''


# ============================
# 퀴즈 3
# 계산기를 클래스를 이용하여 구현하여라.
# 속성 : 2개의 숫자
# 4개의 메소드 (더하기 / 빼기 / 곱하기 / 나누기)
# 인스턴스화 시킨 후 다음과 같이 출력한다
#
# [ 출력형태 : ]
# 첫번째 숫자 : ?
# 두번째 숫자 : ?
# 더하기 : ?
# 빼기 : ?
# 곱하기 : ?
# 나누기 : ?



# ============================
# 퀴즈 4
# 숫자 n을 입력받아 n단의 구구단 결과를 특정 문서에 저장되도록 하여라.
# 출력파일경로 : output/gugu_n.txt
# 출력 예시
'''
3 단 
3  X  1 = 3
...
3  X  9 = 27
'''



# ============================
# 퀴즈 5
# data/color.txt 파일 읽어서 리스트로 저장하고
# 리스트에서 n개만 output/color2.txt 파일로 저장하여라.



# ============================
# 퀴즈 6

# data/black.txt 파일 읽어서 리스트로 저장하고
# 리스트 전체를
# 퀴즈 5의 output/color2.txt 파일에 내용을 추가하여라.



# ============================
# 퀴즈 7
# 'data/coding.txt' 문서를 읽고 코딩이라는 단어가 들어간 어구를 리스트화 한 후
# 총 갯수를 출력되도록 프로그래밍 하여라.
#

'''
파일명 :  data/coding.txt
코딩이라는 글자가 들어간 어구 출력
 : ['코딩을', '코딩을', '코딩에', '코딩을', '코딩을', '코딩을', '코딩도', '코딩에', 
       '코딩은', '코딩을', '코딩도', '코딩', '코딩도', '코딩을', '코딩을']
총 갯수는? 15
'''


# ============================
# 퀴즈 8
# 파일읽기, 쓰기, 추가 기능을 이용하여 다음과 같은 프로그램을 작성하여라.
# 파일에 추가되는 단어의 글자수는 2글자로 제한한다.

'''
# 프로그램 예시 
------------------------------
메뉴 번호를 입력하세요. 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...  1

[단어 추가]
두 글자로 구성된 단어를 입력하세요... 송아지
두글자가 아닙니다.
두 글자로 구성된 단어를 입력하세요... 사과
단어가 저장되었습니다.

------------------------------
메뉴 번호를 입력하세요. 1.단어추가 2.모두읽기 3.모두삭제 4.종료 ...  1

[단어 추가]
두 글자로 구성된 단어를 입력하세요... 자두
단어가 저장되었습니다.

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  2

[단어 모두 출력]
총 단어 수 ... 2 
사과
자두


------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  3

[파일 내용 모두 삭제]
단어 목록을 모두 삭제하였습니다.


메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  2

[단어 모두 출력]
총 단어 수 ... 0 

------------------------------
메뉴 번호를 입력하세요 1.단어추가 2.모두읽기 3.모두삭제 4.종료  ...  4

프로그램을 종료합니다.
'''

# ============================
# 퀴즈 9
# 구구단를 특정 파일에 함수로 정의하고 다른 파일에서 모듈로 임포트하여
# 함수를 호출하도록 하여라.
# Step1. gugu.py로 모듈파일 생성후
#        특정 n 단과 구구단 전체를 출력하는 함수 정의
# Step2. 별도의 파이썬 파일에서 import gugu로 모듈을 임포트 한 후
#        모듈의 함수가 실행되는지 확인

# import gugudan
# gugu.gugudanPrint1(5)
# gugu.gugudanPrint2()

# ============================
# 퀴즈 10
# Step1.lotto.py로 모듈파일 생성후 로또 번호와 관련된 함수 정의
#  로또 번호를 n개 생성하는 함수 정의
#  로또 번호를 생성하고 파일로 저장하는 함수 정의
#  로또 번호는 1~46 범위에서 6개 중복없이 생성되도록 한다. (random 이용)

# Step2. 별도의 파이썬 파일에서 import lotto로 모듈을 임포트 한 후
# 모듈의 함수가 실행되는지 확인

# import lotto
# lotto.lottoNum(5)
# lotto.lottoNumSave()