n1=int(input("Enter Number1 :"))
n2=int(input("Enter Number2 :"))
n3=int(input("Enter Number3 :"))
try:
    print("Max is :",max(int(n1),int(n2),int(n3)))
except Exception as e:
    print(e,'\n',"Given Only Integer")
