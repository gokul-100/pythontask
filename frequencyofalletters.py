def frequvenceOfall(str):
    str_set=set(str)
    for i in str_set:
        count=0
        for j in str:
            if i==j:
                count+=1
        print(f'frequncy of charcater {i} is {count}')

    




if __name__=="__main__":
    str=input('enter the string: ')
    str=str.lower()
    frequvenceOfall(str)