def count_up(n):
    for i in range(0,n+1):#告诉生成器要循环数数量
        yield(i)
for num in count_up(5):
            print(num) 
