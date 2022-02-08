def calc_price(**data):
    total = sum(data.values())
    print("You have purchases")
    for k,v in data.items():
        print(f'{k} -> {v}')
    
    print("total amount:",total)


calc_price(mouse=500, laptop=60000)
calc_price(brush=200,paint=3000,canvas=500)