# str_func.py

# upper
text = 'AbCdE'
text = text.upper()  # non-destructive
print(text)   

# lower
text = 'AbCdE'
text = text.lower()  # non-destructive
print(text)   


# count
cnt_C = 'aCvCdCeC'.count('C')
print(cnt_C)

# isalpha - 알파벳 체크
text = '10 years old'
check = text.isalpha()
print(check)

# isnumeric - 숫자만 체크
text = '10 years old'
check = text.isnumeric()
print(check)

# isalnum = 문자 숫자로만 체크
text = '10살입니다'
check = text.isalnum()
print(check)

# ljust, center, rjust
text1 = 'hello'.ljust(10)
text2 = 'hello'.center(10)
text3 = 'hello'.rjust(10)
print(text1, text2, text3, sep = '-')

# len(v) - 길이 length
text = 'abcdefg'
print(len(text))