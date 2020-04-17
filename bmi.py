h = input('Enter your height(cm): ')
w = input('Enter your weight(kg): ')
h = int(h)
w = int(w)
h = h / 100 #換成公尺
bmi = w / h / h  
if bmi < 18.5:
	print('你的bmi值為',bmi, '體重過輕')
elif 18.5 <= bmi < 24:
	print('你的bmi值為',bmi,'正常範圍')
elif 24 <= bmi < 27:
	print('你的bmi值為',bmi,'過重')
elif 27 <= bmi < 30:
	print('你的bmi值為',bmi,'輕度肥胖')
elif 30 <= bmi < 35:
	print('你的bmi值為',bmi,'中度肥胖',)
elif bmi > 35:
	print('你的bmi值為',bmi,'重度肥胖') 
