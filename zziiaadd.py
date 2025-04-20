# this code is made by ziad /:
budget = int(input("enter_your_budget :"))
item_1 = int(input("enter_item_1 :"))
item_2 = int(input("enter_item_2 :"))
item_3 = int(input("enter_item_3 :"))

total_price= item_1 + item_2 +  item_3
difference= budget-total_price

print("/////////////////////////////////" )
print("item_1_price =" , " "  , item_1)
print("item_2_price =" , " "  , item_2)
print("item_3_price =" , " "  , item_3)
print("total_price  :" , " " , total_price)

if difference<0 :
    print("i_want :" , difference*-1)
    print("you_want : 0")
else:
       print("i_want : 0" )
       print("you_want : " , difference)

    