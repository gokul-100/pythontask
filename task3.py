def userorder(*menu):
    print()
    for i in menu:
        print(i)
def main():
    sandwitch=[]
    noofitems=int(input('enter the no of itesms order'))
    for i in range(noofitems):
        print(f'enter your {i+1} order')
        sandwitch.append(input())
    userorder(*sandwitch)
 
    
if __name__=="__main__":
    main()