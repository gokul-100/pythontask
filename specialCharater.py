def checkSpecialCharcter(str):
    special="!@#$%^&*"
    bool=False
    for i in str:
        if i in special:
            bool=True
    if bool:
        print(f'{str}  contains the special charcter')
    else:
        print(f'{str} doenot contains the special charcter')


if __name__=="__main__":
    str=input("enter the string: ")
    checkSpecialCharcter(str)