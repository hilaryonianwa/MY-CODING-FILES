
def retry_times():
    trials=int(input('How many questions do you want to practice with?:'))
    
    
    LIST=['''
-The act of selling in a foreign market at a price lower than cost is called

A. Dumping   
B. hedging
C. fair trading
d. under sale''',
'''
-Current account holders withdraw money through

A. Credit card
B. cheque     
C. Transfer
D. Withdrawal form''',
'''
-One of thee major problems of a sole proprietor is sourcing for

A. funds      
B. Labour
C. Raw materials
D. machineries''',
'''
Which of the following is a verbal means of communication

A. Telephone      
B. Express mail
C. Business reply services
D. Telex''',
'''
-Trade fair in nigeria are organized by

A. Ministry of commerce and industry
B. Chambers of commerce     
C. The fedral government
D. Manufacturer's association of nigeria''',
'''
-Privatization is

A. Transfer of ownership to individual or government
B. Transfer of ownership from government to stakeholders
C. Transfer of ownership from government to individuals    
D. Government taking charge of all buisness''',
'''
-In the law of contact, acounter officer opperates as

A. A contact
B. an acceptance
C. a rejection       
D. a receptionist''',
'''
-What is a quota

A. Tax paid on goods produced within a country
B. A  physical restriction placed on quantity of goods that can be imported  
C. Tax paid on goods produced outside a country
D. Ban on all imported goods''',
'''
-Which of the following funtion is not perform by the warehousing

A. Stabilization of price
B. production of head demand
C. creating scarcity of goods    
D. storage of goods''',
f'''
-One of these is a current asset

A. fittings
B. machineries
C. motor vehincles
D. stock        ''']

    count=len(LIST)
    


    LIST_ANSWERS=['A','B','A','A','B','C','C','B','C','D']

    
    Type_list=['waec','post utme','jamb','nabteb','neco','mock']
    Type_answer=['"WAEC EXAMINATION"','"POST UTME"','"CBT JAMB"','"NABTEB EXAMINATION"','"NECO EXAMINATION"','"MOCK EXAMINATION"']
    
    Type=input('Examination Type: ').lower()

    
    if Type in Type_list:
        x=Type_list.index(Type)                                        # display was derived from this loop
    disp=Type_list[x]                                      
    if trials < count:
        pass
    if trials >= count:
        print(f'There are only {count} questions on our {disp} question store!')
        ask_retry=input('Do you want to continue: ').lower()
        yes=['yes',' yes','  yes']
        
        main_menu=['main','main_menu','main menu',' main menu','main  menu']
        if ask_retry in yes:
            print('Pls wait...')
            sleep(2)
            retry_times()

        else:
            exit()


    
    
        





    







    display=Type_answer[x]                                                #  display in a connection with brother 1
    if trials>5:
       print(f'''
You are Practicing with {trials} {display} questions''')
       if trials>7:
           print('Good_luck')
       else:
           pass
    else:
        pass
       

    num_score=0

    from random import sample
    num=trials
    times=sample(LIST,num)
    for i in range(len(times)) :
        print(times[i])
        ask=input('''
Your response: ''').upper()
        question_index =LIST.index(times[i])
        if ask == LIST_ANSWERS[question_index]:
            num_score+=1

        ca=(num_score/trials)*100
        cal=round(ca,1)
     
    print(f'You scored {num_score}/{trials} which is {cal}%')
    replay=['replay',' replay','  replay','re-play',' re play']
    ask_replay=input('''
Do you want to replay or Go to main menu?:
''')
    if ask_replay in replay:
        retry_times()

    '''if ask_replay in main_menu:
        main()
        '''

    


def commercial():
    from time import sleep
    print('''
 Commercial Practice
       ''')
    trials=int(input('How many questions do you want to practice with?:'))
    
    
    LIST=['''
-The act of selling in a foreign market at a price lower than cost is called

A. Dumping   
B. hedging
C. fair trading
d. under sale''',
'''
-Current account holders withdraw money through

A. Credit card
B. cheque     
C. Transfer
D. Withdrawal form''',
'''
-One of thee major problems of a sole proprietor is sourcing for

A. funds      
B. Labour
C. Raw materials
D. machineries''',
'''
Which of the following is a verbal means of communication

A. Telephone      
B. Express mail
C. Business reply services
D. Telex''',
'''
-Trade fair in nigeria are organized by

A. Ministry of commerce and industry
B. Chambers of commerce     
C. The fedral government
D. Manufacturer's association of nigeria''',
'''
-Privatization is

A. Transfer of ownership yo individual or government
B. Transfer of ownership from government to stakeholders
C. Transfer of ownership from government to individuals    
D. Government taking charge of all buisness''',
'''
-In the law of contact, acounter officer opperates as

A. A contact
B. an acceptance
C. a rejection       
D. a receptionist''',
'''
-What is a quota

A. Tax paid on goods produced within a country
B. A  physical restriction placed on quantity of goods that can be imported  
C. Tax paid on goods produced outside a country
D. Ban on all imported goods''',
'''
-Which of the following funtion is not perform by the warehousing

A. Stabilization of price
B. production of head demand
C. creating scarcity of goods
D. storage of goods''',
f'''
-One of these is a current asset

A. fittings
B. machineries
C. motor vehincles
D. stock        ''']

    count=len(LIST)
    


    LIST_ANSWERS=['A','B','A','A','B','C','C','B','C','D']

    
    Type_list=['waec','post utme','jamb','nabteb','neco','mock']
    Type_answer=['"WAEC EXAMINATION"','"POST UTME"','"CBT JAMB"','"NABTEB EXAMINATION"','"NECO EXAMINATION"','"MOCK EXAMINATION"']
    
    Type=input('Examination Type: ').lower()
    

    
    if Type in Type_list:
        x=Type_list.index(Type)                                        # display was derived from this loop
    disp=Type_list[x]                                      
    if trials < count:
        pass
    if trials >= count:
        print(f'There are only {count} questions on our {disp} question store!')
        ask_retry=input('Do you want to continue: ').lower()
        yes=['yes',' yes','  yes']
        replay=['replay',' replay','  replay','re-play',' re play']
        main_menu=['main','main_menu','main menu',' main menu','main  menu']
        if ask_retry in yes:
            print('Pls wait...')
            sleep(2)
            retry_times()

        else:
            exit()


    
    
        





    







    display=Type_answer[x]                                                #  display in a connection with brother 1
    if trials>5:
       print(f'''
You are Practicing with {trials} {display} questions''')
       if trials>7:
           print('Good_luck')
       else:
           pass
    else:
        pass
       

    num_score=0

    from random import sample
    num=trials
    times=sample(LIST,num)
    for i in range(len(times)) :
        print(times[i])
        ask=input('''
Your response: ''').upper()
        question_index =LIST.index(times[i])
        if ask == LIST_ANSWERS[question_index]:
            num_score+=1

        ca=(num_score/trials)*100
        cal=round(ca,1)
     
    print(f'You scored {num_score}/{trials} which is {cal}%')
    ask_replay=input('''
Do you want to replay or Go to main menu?:
''')
    replay=['replay',' replay','  replay','re-play',' re play']
    if ask_replay in replay:
        retry_times()

    '''if ask_replay in main_menu:
        main()
        '''


commercial()
        


    
