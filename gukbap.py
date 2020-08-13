import os
os.system('clear')
print('\n2020년 순대/돼지/내장 국밥 시세 : 7000원\n2020년 콩나물 국밥 시세 : 5500원')

money = int(input('국밥의 가격을 입력하세요 :'))
gukbap = int(input('현재 가지고 있는 돈을 입력하세요  : '))
guk = gukbap/money

print('그돈이면 뜨끈한 국밥', round(guk, 2), '그릇 든든하게 먹고말지!')
