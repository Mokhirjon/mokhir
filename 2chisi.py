try:
     b=input('a=')
     m=[]
     s=0
     for i in b:
         if 47<ord(i)<58:
             m.append(int(i))
             s=i+i
         print(s)
 except IndexError:
     print("indexerror")