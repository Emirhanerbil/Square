a=int(input("Which number do you want to square? : "))
küme=[]
for n in range(a*100):
    if(n**2<=a*100):
            küme.append(n)
    else:
             a+1
print("Result is : " , max(küme)/10)


