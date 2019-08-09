#產生一個隨機整數1~100
#讓使用者重複輸入數字去猜
#猜對的話 印出"終於猜對了!"
#猜錯的話 印出"比答案大或小"

import random
r = random.randint(1,100)

while True:
	ans = input('請輸入一數字介於1~100 : ')
	ans = int(ans)
	if ans == r :
		print('終於猜對了!')
		break
	else:
		if ans < r :
			print('您的數字較答案來的小')
		else:
			print('您的數字較答案來的大')
