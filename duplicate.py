import filecmp as fc 
import os
def Comparefiles(filname1,filname2):
    if( not os.path.exists(filname1)):
        print('Not exists',filname1)
    elif( not os.path.exists(filname2)):
        print('Not exists',filname2)
        
    else:
        compare=fc.cmp(filname1,filname2)
        if compare==True:
            os.remove(filname2)
            print(f'{filname2} is removed successfully')
        else:
            print('files are not same')



def main():
    print('enter the first filename')
    filename1=input()
    print('enter the second filename')
    filename2=input()
    Comparefiles(filename1,filename2)


if __name__=="__main__":
    main()