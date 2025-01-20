'''온도 표기법
섭씨(Celsius) ℃ = (℉ - 32) / 1.8 , = K - 273.15
화씨(Fahrenheit) ℉ = (℃ * 1.8) + 32 = (K - 273.15) * 1.8 + 32
절대온도(Kevin) K = ℃ + 273.15, = (℉ = 32) / 1.8 + 273.15
'''

def convert_temperature(c, unit):
    if unit == 'C':
        c = t
        f = c * 1.8 + 32
        k = c + 273.15
        return c, f, k  
    elif unit == 'F':
        f = t
        c = (f - 32) / 1.8
        k = c + 273.15
        return c, f, k
    elif unit == 'K':
        k = t
        c = k - 273.15
        f = c * 1.8 + 32
        return c, f, k

    c, f, k = False, False, False
    return c, f, k

# 함수 실행
t = 25.5
t_expr = convert_temperature(t, 'C')
print(t_expr)

t = 25.5
t_expr = convert_temperature(t, 'F')
print(t_expr)

t = 25.5
t_expr = convert_temperature(t, 'K')
print(t_expr)

t = 25.5
t_expr = convert_temperature(t, 'A')
print(t_expr)




