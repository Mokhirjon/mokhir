try:
    b= list(input())
    for i in range(len(b)):
        if b[i] == '6':
             b[i] ='9'
        elif b[i]=='9':
            b[i] =='6'
    print("".join(b))   
except:
    print('Error')