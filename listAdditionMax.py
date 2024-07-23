def additionofList(lst):
    sum=0
    for val in lst:
        sum=sum+val
    
    return sum

def maxNumber(lst):
    max_num=0
    for i in lst:
        if(i>max_num):
            max_num=i
            
    return max_num




def main():
    list=[]
    size=int(input('enter the size of list:'))
    for i in range(size):
        value=int(input())
        list.append(value)
    print(additionofList(list))
    print(maxNumber(list))

if __name__=="__main__":
    main()