print('\n')
print('Welcome to the FloK Fashion Quiz ')

playing = input('Would you want to play? ')

if playing.lower() != 'yes':
    quit()

print('\n')
print('Great! Lets play :)')
score = 0
print('\n')

answer = input('Roca wear was founded by which rap star? ')
if answer.lower() == 'jay z':
    print('\n')
    print('Correct answer!')
    score += 1
    print('\n')
else:
    print('\n')
    print('Incorrect answer!')
    print('\n')

answer = input('The Hermes brand is most famous what item? ')
if answer.lower() == 'scarves':
    print('\n')
    print('Correct answer!')
    score += 1
    print('\n')
else:
    print('\n')
    print('Incorrect answer!')
    print('\n')

answer = input('Which animal appears on the logo for Coach? ')
if answer.lower() == 'horse':
    print('\n')
    print('Correct answer!')
    score += 1
    print('\n')
else:
    print('\n')
    print('Incorrect answer!')
    print('\n')

answer = input('Shoe designer Manolo Blahnik was born in which country? ')
if answer.lower() == 'spain':
    print('\n')
    print('Correct answer!')
    score += 1
    print('\n')
else:
    print('\n')
    print('Incorrect answer!')
    print('\n')

print("You got " +str(score) +  " questions correct!")
print('\n')
print("You got " +str((score/4) * 100) +  "%.")
print('\n')