import time
sec=0
min=0
hour=0
while True :
	time.sleep(1)
	sec+=1
	if sec > 59 :
		sec = 0
		min+=1
		if min > 59 :
			min = 0
			hour+=1
	print("ca fait " + str(hour) + " : " + str(min) + " : " + str(sec))
