from time import sleep
num1=int(input("Please enter first number: "))
num2=int(input("Please enter second number: "))
num3=int(input("Please enter third number: "))
num4=int(input("Please enter fourth number: "))
num5=int(input("Please enter fifth number: ")) 
degerler = (num1,num2,num3,num4,num5)
kucukten_buyuge=sorted(degerler)
min=kucukten_buyuge[0]
max=kucukten_buyuge[-1]
print(sorted(degerler))
print(f"minimum : {min} , maximum :{max}")
sleep(3)
