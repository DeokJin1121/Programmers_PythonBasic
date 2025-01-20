# 쇼핑몰 할인율 -> 구매가격
def purchase_price(price, sale_per):
    new_price = price * (100 - sale_per) / 100
    new_price = int(new_price)
    
    return new_price
    
# 함수 실행
p1 = purchase_price(20000, 50)
p2 = purchase_price(40000, 20)
print(p1, p2)    # None None -> 10000 32000
print(p1 + p2) 
    