def create_car(*carMod,**spec):

    car = {
        'manufacturer': carMod[0],
        'model': carMod[1]
    }
    car.update(spec)

    for car in carMod:
         print(car.title())

    for key,val in spec.items():
         print(f'\t{key} = {val.title()}')
   

def main():
   

    
        manufacturer=input("Enter Manufacturer : ")
        model=input("Enter Model : ")
        choice=int(input("To add Spec Enter \'0\' : "))
        spec ={}

        while(not choice):
            key=input("Enter Spec Name : ")
            value=input("Enter Spect Type : ")
            spec[key]=value
            choice=int(input("To add More Spec Enter \'0\' :"))
            
        create_car(manufacturer, model, **spec)

   

if _name_ == "__main__":
    main()