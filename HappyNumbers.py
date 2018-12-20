x=n=int(input())
for i in[1]*9:
 n=sum(map(lambda x:x*x,map(int,str(n))))
print(x,"IS",["UN",""][n==1]+"HAPPY")
