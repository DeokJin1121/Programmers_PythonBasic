# for문 도중 member의 remove > 넘어가는 데이터가 생김
member = ['Spencer', 'Adela', 'Allen', 'Chen', 'John', 'Albert', 'Andy', 'Darby']
for user in member.copy():
    if user[0] in ['A', 'a']:
        member.remove(user)
print(member)
# 기대 : ['Spencer', 'Chen', 'John', 'Darby']
# 실제 : ['Spencer', 'Allen', 'Chen', 'John', 'Andy', 'Darby']