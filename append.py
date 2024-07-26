import os


def append(filename):
    if (os.path.exists(filename)):
        text=input('enter the text to append: ')
        file=open(filename,'a')
        file.write(text)
        print('file append successfully...')
    else:
        print('file doesnot exists...')

def main():
    filename1=input('enter the filname to append')
    append(filename1)


if __name__=="__main__":
    main()