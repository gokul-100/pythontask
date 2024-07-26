import os
import shutil
import filecmp as fc
def createfile(filename):
    if (os.path.exists(filename)):
        print('filename already exists..')
    else:
        file_create=open(filename,'w')
        
def copy(file1,file2):
    res=shutil.copy(file1,file2)
    print('file copy successfully')
    
def Comparefiles(filname1,filname2):
    if( not os.path.exists(filname1)):
        print('Not exists',filname1)
    elif( not os.path.exists(filname2)):
        print('Not exists',filname2)
        
    else:
        compare=fc.cmp(filname1,filname2)
        if compare==True:
            print('both the fies are same')
        else:
            print('files are not same')
        
def main():
    filename1=input('enter the filname to copy')
    
    print('enter the filename you want to create ')
    filename2=input()
     
    createfile(filename2)
    copy(filename1,filename2)
    Comparefiles(filename1,filename2)
    
if __name__=="__main__":
    main() 