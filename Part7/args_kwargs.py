# *args **kwargs
def check_basket(**item):
    print(f'장바구니 상황 : {item}')
    # 반복문
    
check_basket(breakfast='사과', lunch='고기', dinner='삶은 계란')
#  {'breakfast': '사과', 'lunch': '고기', 'dinner': '삶은 계란'} -> dictionary