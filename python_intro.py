print('Hello, Django girls!')
if 3>2:
    print('Ça marche !')
if 5>2:
    print('5 est effectivement plus grand que 2')
else:
    print("5 n'est pas plus grand que 2")
name = 'Elise'
if name == 'Charles':
    print('Hey Charles!')
elif name == 'Elise':
    print('Hey Elise!')
else:
    print('Hey anonymous!')    
def hi():
    print('Hi there!')
    print('How are you?')    
hi()    
def hi(name):
    if name == 'Ola':
        print('Hi Ola!')
    elif name == 'Sonja':
        print('Hi Sonja!')
    else:
        print('Hi anonymous!')
hi("Ola")        
hi("Elise")
def hi(name):
    print('Hi '+ name + '!')
hi ("Elise")   
girls = ['Rachel', 'Monica', 'Phoebe', 'Ola', 'You']
for name in girls:
    hi(name)
    print('Next girl')