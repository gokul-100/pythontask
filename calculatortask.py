def Addition(val1,val2):
    ans=val1+val2
    return ans

def Subtraction(val1,val2):
    ans=val1-val2
    return ans

def Multiplication(val1,val2):
    ans=val1*val2
    return ans

def division(val1,val2):
    ans=val1/val2
    return ans

def main():
    num1=int(input('enter the number1: '))
    num2=int(input('enter the number2: '))
    print('''
          addition - 1
          subtraction-2
          multiplication-3
          divison-4
          exit-5
        
          ''')
    while(True):
        option=int(input('enter your option:'))
        if option==1:
            print( Addition(num1,num2))
        elif option==2:
            print(Subtraction(num1,num2))
        elif option==3:
            print(Multiplication(num1,num2))
        elif option==4:
            print(division(num1,num2))
        elif option==5:
            print("shutdown.....")
            exit()
        else:
            print('your are selecting wrong input.....')

if __name__=="__main__":
    
    main()