from random import randint

print (" Hello, Welcome to Choice game")
print(" Instruction : \n Python will genrate random number between [1,20] \n You will get 3 chances to guess that random number \n Best of LUCK!!! ")

while(True):
    a=int(input(' Are you ready, press 1: \n To exit, press 2 : '))
    if(a==1):
        print(" Game start!!!!")
        random_num=randint(1,20)
        for i in range(1,4):
            user_num=int(input(f' This is your {i} chance, Please enter your number : '))
            if(user_num==random_num):
                print(' Well DONE,Correct number!!')
                break
            elif(user_num>random_num):
                print(' ***this number is greater, try again :( ***')
                if(i==3):
                    print(f' YOu used all of your chances, The correct number is {random_num}.\n You lost bruh!!')
            elif(user_num<random_num):
                print(' ***this number is smaller,try again :( ***')
                if(i==3):
                    print(f' YOu used all of your chances, The correct number is {random_num}.\n You lost bruh!!')
    if(a==2):
        print(' Bye :)')
        break
    else:
        break
