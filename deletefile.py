import os
def delete(filename):
    if os.path.exists(filename):
        os.remove(filename)
        print('file removed successfully')
    else:
        print('the file doesnot exists')
        
def main():
    print('enter the filename to delete: ')
    filename=input()
    delete(filename)
    
if __name__=="__main__":
    main()