print('Hello! My name is Aid.')
print('I was created in 2020.')
print('Please, remind me your name.')

name = input()

print('What a great name you have, ' + name + '!')
print('Let me guess your age.')
print('Enter remainders of dividing your age by 3, 5 and 7.')

# reading all remainders
r1 = int(input())
r2 = int(input())
r3 = int(input())

your_age = (r1 * 70 + r2 * 21 + r3 * 15) % 105
print("Your age is " +str(your_age)+"; that's a good time to start programming!")
