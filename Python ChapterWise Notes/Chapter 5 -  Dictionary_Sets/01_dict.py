# cretaing a dictionary
dict1={'arun':'saini', 1:2, 'naveen':'sharma'}
print(dict1)
key1=('arjun','karnana',1,8) # create a list which contains keys
values1=('deol','ram',23,4.6) # create a list which contains values
dict2=dict(zip(key1,values1)) # combine both values using dict() and zip() funciton
print(dict2)
dict1 ['hello']='hi' # to add a item to dictionary
dicupdate ={'hello':'bro'} # declare a variable
dict2.update(dicupdate) # using update functiont to add the declared variable to dictionary items
udpatedic= {
    'harry':'porter' ,
    'aladin':'abu' ,
    'simba':'mufasa' ,
    'arun':'parul' # arun key is already available in dict1 but we are updating the value of arun key.Update function also updates the value of a key
}
dict1.update(udpatedic)
print(dict2)
print(dict1)
print(dict1.get('arun1')) # by default get (function) returns none 
print(dict1.get('arun1','Not Avaialble')) # we can provide a custom message in event of key not available in dictionary

