string = input("enter the string : ")
l = 1
dic={}

for i in range(97,123):
    alpha = chr(i)
    dic.update({alpha:l})
    l+=1
    
flag = True

for i in string:
    if i==" ":
        continue
    elif (string.count(i)!=dic[i]):
        flag = False
        break
    else:
        continue

print("Yes") if (flag) else  print("No")
