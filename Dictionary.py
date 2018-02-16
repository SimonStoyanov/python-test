# Dictionary
myDict = {
    'LeChuck': 'lechuck@mail.com',
    'Casual': 'casual@mail.com'
}

# Deleting a key-value pair
del myDict['Casual']

# Adding a key-value pair
myDict['Simon'] = 'simon@mail.com'

print("Simon's mail: "+str(myDict['Simon']))
print(myDict)
