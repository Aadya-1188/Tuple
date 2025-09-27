#create a tuple with different data types
tuplex = ("tuple" , False , 3.2 , 1)
print(tuplex)

#create a tuple
tuplex = (4 , 6 , 2 , 8 , 3 , 1)
print(tuplex)
#tuples are immutable , so u can not add new elements 
#using merge of tuples with the + operator so u can add element and it will create a new tuple 
tuplex = tuplex + (9,)
print(tuplex)

tuple1 = (50 , 10 , 60 , 70 , 50)
print(tuple1.count(50))

#create a tuple
tuplex = (2 , 4 , 3 , 5 , 4 , 6 , 7 , 8 , 6 , 1)
#used tuple[start:stop] the start index is inclusive and the stop index 
_slice = tuplex[3:5]
#is exlusive
print(_slice)
# if the index isn't defined  , it;s taken from the begging of the tuple
_slice = tuplex[:6]
print(_slice)

