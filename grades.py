score = input('Enter your a number to see your grade (between 0 and 100 ONLY) (DO NOT TYPE LETTERS...OR ELSE BEWARE!!) : ')
try:
    score = int(score)
    if score<=100 and score>=90:
        
        print('You Passed! You got an A!')
    elif score<=89 and score>=80:
        
        print('You Passed! You got a B')
    elif score<=79 and score>=70:
        
        print('You did OK, you got a C')
    elif score<=59 and score>=60:
       
        print('Better luck next time - D')
    else:
        
        print('You failed the test - :( F')
except:
    print(' ERROR '*1000000)
    print(' Do not do it again! ')


    
    
