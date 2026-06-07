import time,os,random

def word_ps(start_time,end_time,written_string):
    time_taken = end_time - start_time
    word=time_taken/len(written_string)
    return( round(word,2))

def error(given_string,written_string):
    error=0
    for i in range(len(given_string)):
        try:
            if given_string[i] != written_string[i]:
                error+=1
        except:
            error+=1
    return error


test=['Classification is the process of categorizing objects, individuals.',
      'Or entities into predefined groups or classes based on their.',
      'Characteristics, features, or attributes.']

while True:
    os.system('cls')
    print('****************** Welcome To Speed Testor ******************')
    given_string= random.choice(test)
    print(given_string)

    start_time=time.time()
    written_string= input("Enter Above string:  ")
    end_time=time.time()

    print("\n\n\nYou write ",word_ps(start_time,end_time,written_string),'w/s.')
    print('\nEoors In your writting paragraph is ',error(given_string,written_string))

    chec=input('Do you want to continue Program(yes/no):')
    if chec.upper()=='YES':
        continue
    else:
        os.system('cls')
        print('Thanks for using our program................')
        break
