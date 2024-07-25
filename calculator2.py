def Addition(val1,val2):
    ans=val1+val2
    return (ans)

def Subtraction(val1,val2):
    ans=val1-val2
    return ans

def Multiplication(val1,val2):
    ans=val1*val2
    return ans

def division(val1,val2):
    ans=val1/val2
    return ans

if __name__=="__main__":
    num1=int(input('enter the value: '))
    num2=int(input('enter the value2: '))
    
    options={
        1:Addition(num1,num2),
        2:Subtraction(num1,num2),
        3:Multiplication(num1,num2),
        4:division(num1,num2)
    }
    print('''
          addition - 1
          subtraction-2
          multiplication-3
          divison-4
          exit-5
        
          ''')
    while True:
        option=int(input('enter your option: '))
        if option ==1:
           print(options[option])
        elif option ==2:
           print(options[option])
        elif option ==3:
           print(options[option])
        elif option ==4:
           print(options[option])
            
            
        elif option==5:
            exit()
        else:
            print('you enter the wrong choice')
        