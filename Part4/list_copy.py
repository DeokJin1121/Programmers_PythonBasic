# list 참조와 복사
score_A = [80, 70, 60, 50, 40]
score_B = score_A.copy() # [80, 70, 60, 50, 40] # 주소값 별개
# score_B = score_A[:] # [80, 70, 60, 50, 40] # 주소값 별개
# score_B = score_A # score_A 리스트를 참조
score_B[0] = 100  # [100, 70, 60, 50, 40]

print(score_A)
print(score_B)

# id()
print(id(score_A))
print(id(score_B))

# is -> 같은 메모리에 있는지 확인하는 연산자
print(score_A is score_B)