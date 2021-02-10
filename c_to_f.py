celcius = input('請輸入攝氏溫度:')
# celcius = int(celcius) 用浮點更好
celcius = float(celcius)
# print('華氏溫度=', celcius * 9 / 5 + 32, 'F') 先定義變數再 print
f = celcius * 9 / 5 + 32
print('華氏溫度=', f, 'F')