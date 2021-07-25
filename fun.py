#function 練習

#function 是用來收納程式碼的
#他是個功能，不執行

def wash(dry):
	print('add_water')
	print('add_detergent')
	print('whirling')
	if dry : #參數 parameter，投硬幣 >>是非題
	    print('烘衣')

wash(True) #使用function

def add(a, b):
	print(a + b)
add(1, 3) #一定要投幣

def add(c = 0, d = 1):
	print(c + d)
add() #不一定要投幣
add(5) # c = 5
add(d = 3)

#return
def r(x, y):
	return x + y # 回傳 >> 投幣然後噴出飲料
result = r(3, 4)
print(result)

def average(numbers):
	avg = sum(numbers) / len(numbers)
	return avg 

a1 = average([1, 2, 3])
print(a1)
print(average([1, 2, 3]))

def hello(x, y=1): #"沒預設值的"　一定要在　"有預設值的"　的前面
    print(x, y)
 
hello(3, 4) #雖然有預設值，但有投東西給它，所以不管預設值