

def leap():
    a=[]
    b=[]
    for i in range (y1,y2+1):
        if (i%4==0 and i%100!=0 )or i%400==0:
            a=a+[i]
        else:
            b=b+[i]
    print("the leap years are>>>>\n",a,"\n")
    print("the non leap years are>>\n",b,"\n")

while True:
    n=input("TO FIND LEAP AND NON LEAP YEARS PRESS (yes) |||| (no) FOR EXIT: ")
    if n=="yes":
        d1, m1, y1 = list(map(int, input("(starting date)DD/MM/YYYY: ").split("/")))
        d2, m2, y2 = list(map(int, input("(ending date)DD/MM/YYYY: ").split("/")))
        print("THE LEAP YEAR and NON LEAP YEARS BETWEEN THE DATES ARE")
        leap()
    elif n=="no":
        exit()
    else:
        print("Restart")



