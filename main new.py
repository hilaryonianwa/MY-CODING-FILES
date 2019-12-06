def ask_replay1():
    from time import sleep
    
    Replay=['replay',' replay','re-play',' re-play','re_play',' re_play']
    Exit=['exit',' exit','  exit']
    
    ask_replay1=input('Would you like to replay or exit?: ').lower()
    if ask_replay1 in Replay:
        print('Pls wait,Processing...')
        sleep(4)
        print('\nNew guess,Good luck')
        Guess()
    elif ask_replay in Exit:
        exit()
    else:
        print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
        sleep(1)
        ask_replay1()

def ask_replaycon():             #con in ask_replay represent a continuos asking of questions until num which is num_attempt+1, It was laid there for proper understanding.
    ask_replaycon=input('Would you like to replay or exit?: ').lower()
    from time import sleep
    Replay=['replay',' replay','re-play',' re-play','re_play',' re_play']
    Exit=['exit',' exit','  exit']
    if ask_replaycon in Replay:
        print('Pls wait,Processing...')
        sleep(4)
        print('\nNew guess,Good luck')
        Guess()
    elif ask_replay in Exit:
        exit()
    else:
        print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
        sleep(1)
        ask_replaycon()

def ask_replay_last():
    from time import sleep
    Replay=['replay',' replay','re-play',' re-play','re_play',' re_play']
    Exit=['exit',' exit','  exit']
    if ask_replay_last in Replay:
        print('Pls wait,Processing...')
        sleep(4)
        print('\nNew guess,Good luck')
        Guess()

    elif ask_replay_last in Exit:
        
        exit()

    else:
        print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
        sleep(1)
        ask_replay_last()
        
print('''Welcome to "HILARY'S" Guess Game''')
from time import sleep
sleep(1)
def Guess():
    
    
    from random import choice
    attempt_list=[4,5,4,4,4,7,8,8,5,9,8,3]
    num_attempt=choice(attempt_list)
    num=num_attempt+1

    guess_list=['physics','control','cchub','windows','indomie','document','microsoft','computer','picture','cabinet','kangaroo','formula','picnic','laptop','hilary','delete','insert','print','latitude']
    guess_answer=choice(guess_list)
    answer=len(guess_answer)

    first_word=guess_answer[0]                                                                                        #- int to get the first and last word
    last_word=guess_answer[-1]                                                                                        #   in a sentence.

    s_last_word=guess_answer[-2]
    second_word=guess_answer[1]

    third_word=guess_answer[2]
    fourth_word=guess_answer[3]
    fifth_word=guess_answer[4]

    
    
    
    WORD={
        4:'four',
        5:'five',
        6:'six',
        7:'seven',
        8:'eight',
        9:'nine',
        10:'ten',
        11:'eleven',
        12:'twelve',
        13:'thirteen',
        14:'fourteen',
        15:'fifteen',
        16:'sixteen',
        17:'seventeen',
        18:'eighteen',
        }

    a_word=WORD[answer]
    
    

    
    INT_list=[f''' 
Guess Int: The first letter is "{first_word}" and the last letter of the word is "{last_word}"
               ''',
              f'''
Guess Int: The fourth,fifth and last letter of the word is {fourth_word},{fifth_word} and {last_word}
               ''',
              f'''
Guess Int: The first two letter's of the word are {first_word} and {second_word}
               ''',
              f'''
Guess Int: The last two letter's of the word are {s_last_word} and {last_word}
               ''',
              f'''
Guess Int: {third_word} is the Third letter in the word.
               ''',
              f'''
Guess Int: The word is a {a_word} lettered word
              ''',
              f'''
Guess Int: The first and last two letter's of the words are ({first_word}{second_word}) and ({s_last_word}{last_word})
               ''',
              f'''
Guess Int: The third and fourth letter of the word are '{third_word}' and '{fourth_word}
               ''',
              f'''\nGuess Int: {first_word} and {s_last_word} are individual letter's in the word
               ''']
    from time import sleep

    INT=choice(INT_list)

    print(f'\nYou have {(WORD[num_attempt])} attempts to guess the secret word')
    sleep(1)

    #After that
    print(INT)

    
    

    question1=['Your first guess,you can do it?: ','1st try,get it once: ']
    question1=choice(question1)
    answer1_good_comments=['That was a terrific guess','That was nice','Good one','God bless you,nice guess']
    good_comments=choice(answer1_good_comments)

    for_print=['Wrong','That was incorrect','That was very wrong','Nope,That was incorrect']
    wrong=choice(for_print)

    
    
    Replay=['replay',' replay','re-play',' re-play','re_play',' re_play']
    Exit=['exit',' exit','  exit']
    
    for i in range(1,num):
        if i == 1:
            enc=input(question1).lower()
            if enc == guess_answer:
                print(good_comments)
                ask_replay1=input('Would you like to replay or exit?: ').lower()
                if ask_replay1 in Replay:
                    print('Pls wait,Processing...')
                    sleep(4)
                    print('\nNew guess,Good luck')
                    Guess()
                elif ask_replay in Exit:
                    exit()
                else:
                    print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
                    ask_replay1()
            else:
                print(wrong)

                
                
        elif i>1 and  i != num_attempt:
            other_question=['Re-guess the word?: ','Re-think, and re-guess: ',"Arrange your thoughts and Re-guess: ",'Guess well,You can do it,re-input Guess: ','Come on,Input guess: ']
            re_asking=choice(other_question)
            for_print=['Wrong','That was incorrect','That was very wrong','Nope,That was incorrect']
            wrong1=choice(for_print)

            
            enc1=input(re_asking).lower()
            if enc1 == guess_answer:
                print(good_comments)
                
                
                ask_replaycon=input('Would you like to replay or exit?: ').lower()
                if ask_replaycon in Replay:
                    print('Pls wait,Processing...')
                    sleep(4)
                    print('\nNew guess,Good luck')
                    Guess()
    
                elif ask_replay in Exit:
                    exit()
                else:
                    print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
                    
                    ask_replaycon()
            else:
                print(wrong1)

        
            
        elif i == num_attempt:
            sleep(1)
            print('\nLast attempt')
            last_guess=input('Input Last-Guess: ')
            if last_guess == guess_answer:
                print('Correct')
                ask_replay_last=input('Would you like to replay or exit?: ').lower()
                if ask_replay_last in Replay:
                    print('Pls wait,Processing...')
                    sleep(4)
                    print('\nNew guess,Good luck')
                    Guess()

                elif ask_replay_last in Exit:
                    exit()

                else:
                    print('Wrong input,Pls kindly follow this instruction "replay" or "exit".')
                    ask_replay_last()                
        
            else:
                print('You failed')
                sleep(1)
                print(f'The word is {guess_answer}')
                sleep(1)
                ask_replay_last=input('Would you like to replay or exit?: ').lower()
                if ask_replay_last in Replay:
                    print('Pls wait,Processing...')
                    sleep(4)
                    print('\nNew guess,Good luck')
                    Guess()

                elif ask_replay_last in Exit:
                    exit()

                


Guess()
