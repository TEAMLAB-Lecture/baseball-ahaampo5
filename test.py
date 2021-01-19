# -*- coding: utf-8 -*-

import random


def get_random_number():
    # Helper Function - 지우지 말 것
    # 100부터 999까지 수를 램덤하게 반환함
    return random.randrange(100, 1000)


def is_digit(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number가 정수로 변환 가능할 경우는 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_digit("551")
    #   True
    #   >>> bg.is_digit("103943")
    #   True
    #   >>> bg.is_digit("472")
    #   True
    #   >>> bg.is_digit("1032.203")
    #   False
    #   >>> bg.is_digit("abc")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    user_input_number = user_input_number[:]
    result = user_input_number.isdigit()
    # ==================================
    return result


def is_between_100_and_999(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    #                         입력된 값은 숫자형태의 문자열 값임이 보장된다.
    # Output:
    #   - user_input_number가 정수로 변환하여 100이상 1000미만일 경우 True,
    #     그렇지 않을 경우는 False
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_between_100_and_999("551")
    #   True
    #   >>> bg.is_between_100_and_999("103943")
    #   False
    #   >>> bg.is_between_100_and_999("472")
    #   True
    #   >>> bg.is_between_100_and_999("0")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result = (int(user_input_number) >= 100 and int(user_input_number) < 1000)
    # ==================================
    return result


def is_duplicated_number(three_digit):
    # '''
    # Input:
    #   - three_digit : 문자열로 된 세자리 양의 정수 값
    #                   문자열로 된 세자리 양의 정수값의 입력이 보장된다.
    # Output:
    #   - three_digit 정수로 변환하였을 경우 중복되는 수가 있으면 True,
    #     그렇지 않을 경우는 False
    #   ex) 117 - True, 123 - False, 103 - False, 113 - True
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_duplicated_number("551")
    #   True
    #   >>> bg.is_duplicated_number("402")
    #   False
    #   >>> bg.is_duplicated_number("472")
    #   False
    #   >>> bg.is_duplicated_number("100")
    #   True
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    result = True
    str_three_digit = str(three_digit)
    for i in str_three_digit:
        if str_three_digit.count(i) != 1:
            result = False
        else:
            continue
    # ==================================
    return result


def is_validated_number(user_input_number):
    # '''
    # Input:
    #   - user_input_number : 문자열 값
    # Output:
    #   - user_input_number 값이 아래 조건이면 True, 그렇지 않으면 False를 반환
    #        1) 숫자형 문자열이며, 2) 100이상 1000미만이며, 3) 중복되는 숫자가 없을 경우
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.is_validated_number("amvd")
    #   False
    #   >>> bg.is_validated_number("402")
    #   True
    #   >>> bg.is_validated_number("472")
    #   True
    #   >>> bg.is_validated_number("100")
    #   False
    #   >>> bg.is_validated_number("1000")
    #   False
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당

    result = None
    result = is_digit(user_input_number) and is_between_100_and_999(user_input_number) and is_duplicated_number(user_input_number)
    # ==================================
    return result


def get_not_duplicated_three_digit_number():
    # '''
    # Input:
    #   - None : 입력값이 없음
    # Output:
    #   - 중복되는 숫자가 없는 3자리 정수값을 램덤하게 생성하여 반환함
    #     정수값으로 문자열이 아님
    # Examples:
    #   >>> import baseball_game as bg
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   125
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   634
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   583
    #   >>> bg.get_not_duplicated_three_digit_number()
    #   381
    # '''
    # ===Modify codes below=============
    # 조건에 따라 변환되어야 할 결과를 result 변수에 할당
    # get_random_number() 함수를 사용하여 random number 생성

    result = None
    while True:
        random_number = get_random_number()
        if is_validated_number(random_number):
            result = random_number
            break
        else:
            continue
    # ==================================
    return result

print(is_between_100_and_999('134'))

print(is_duplicated_number('333'))
print(is_validated_number('123'))
print(get_not_duplicated_three_digit_number())