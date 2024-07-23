def display(starter):
    print('this are the menu list items \n',starter)
    
        
def add(starter):
    item=input('enter the item to add in menu')
    starter.append(item)
    for i in starter:
        print(i) 
        
def update(starter):
    update_item=input('enter the item to update').lower()
    pos=int(input('in which position is update:'))
    starter[pos]=update_item
    for i in starter:
        print(i) 
    
def remove(starter):
    item=input('enter the element to remove:').lower()
    if item in starter:
        starter.remove(item)
        print('item removed successfully..')
    else:
        print('item doesnot exists in menu card')





if __name__=="__main__":
    starter=['chicken 65','burger','cheese burger','egg sandwitch']
   
    print('''
          display - 1
          add-2
          update-3
          remove-4
          exit-5
        
          ''')
    while(True):
        option=int(input('enter your option:'))
        if option==1:
            display(starter)
        elif option==2:
            add(starter)
        elif option==3:
            update(starter)
        elif option==4:
            remove(starter)
        elif option==5:
            exit()
        else:
            print('your are selecting wrong input.....')