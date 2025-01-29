for i in range(0,100): 
    for j in range(0,100):
        if i%j == 0:
            break
    if i == j:
        print(i,end=",")
