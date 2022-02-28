'''
lab5
'''

#3.1

alien_color = 'green'

if alien_color == 'green':
    print('you have earned 5 points')
    
#3.2

alien_color = 'green'

if alien_color == 'green':
    print('you have earned 5 points')

else:
    print('you have earned 10 points')

#3.3

favorite_fruits = ['strawberry', 'pineapple', 'orange']

if 'banana' in favorite_fruits:
    print('you really like bananas')
    
if 'strawberry' in favorite_fruits:
    print('i love strawberries')

if 'orange' in favorite_fruits:
    print('I really like oranges')

#3.4

age = 34

if age <10:
    print('kid')

elif age >=10 and age<20:
    print('teenager')

else:
    print('adult')
    
    if age>= 65:
        print('elder')
