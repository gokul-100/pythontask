foods={
    "biriyani":200,
    "fried rice":120,
    "chicken sandwitch":80
}
def displayFoods():
    print(f'name    price')
    for key,val in foods.items():
        
        print(f'{key}   {val}')
    
def addFood():
    foodName=input("enter the food name")
    price=int(input('enter the price : '))
    foods[foodName]=price
    

def update1food():
    print(foods)
    foodId=int(input('enter the food id to modify: '))
    print(f'you are modifying the {list(foods)[foodId-1]}')
    foods.pop(list(foods)[foodId-1])
    list_items=list(foods.items())
    print(list_items)
    food_name=input("enter the new name: ")
    food_price=int(input(f'new price of : '))
    list_items.insert(foodId-1,(food_name,food_price))
    new_foods=dict(list_items)
    return new_foods
    
def deleteFood():
    item_name=input('enter the food name to delete: ')
    foods.pop(item_name)
    
        
    

if __name__=="__main__":
    
   
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
            displayFoods()
        elif option==2:
            addFood()
        elif option==3:
            foods=update1food()
        elif option==4:
            deleteFood()
        elif option==5:
            exit()
        else:
            print('your are selecting wrong input.....')
    
