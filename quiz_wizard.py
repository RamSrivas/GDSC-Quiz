import random
import question_bank

class quiz_flow:
    l=[]
    
    def __init__(self):
        self.totalQuesNumber=0
        self.totalQuesAttempted=0
        self.q_remaining=self.totalQuesNumber
        self.currentQuesNumber=1
        self.q_id=0
        self.score=0
        self.totalCorrectQues=0
        self.totalIncorrectQues=0
        self.quesMFR=[]

    

    def MFR(self):
        self.l[self.currentQuesNumber-1][3]=1
        self.quesMFR.append(self.quesMFR)
        print("This question has been marked for review.")

    def show_MFR(self):
        print(self.quesMFR)
        
    def set_responce(self,response):
        self.l[self.currentQuesNumber-1][1]=response
        self.totalQuesAttempted+=1
    
    def next_question(self):
        if(self.currentQuesNumber==self.totalQuesNumber):
            self.submit()
        else:
            self.currentQuesNumber+=1

    def previous_question(self):
        if(self.currentQuesNumber==1):
            print("There are no questions before this.")
            return
        self.currentQuesNumber-=1

    def move_to_question_num(self,num):
        self.currentQuesNumber=num

    def is_attempted(self,que):
        if(self.l[que][1]!=0):
            return True
        else:
            return False

    def get_num_attempted(self):
        print(self.totalQuesAttempted)

    def get_num_remaining(self):
        self.q_remaining= self.totalQuesNumber - self.totalQuesAttempted

    def clear_response(self):
        self.l[self.currentQuesNumber-1][0]=0
        self.totalQuesAttempted-=1

    def clear_all_response(self):
        for i in range(self.totalQuesNumber):
            self.l[i][1]=0
        self.totalQuesAttempted=0
    
    def unMFR(self):
        self.l[self.currentQuesNumber-1][3]=0
        print("The question has been marked for review.")

    def submit(self):
        for i in range(self.totalQuesNumber):
            if(self.l[i][1]==0):
                pass
            elif(self.l[i][1]==self.l[i][2]):
                self.score+=2
                self.totalCorrectQues+=1
            else:
                self.score-=1
                self.totalIncorrectQues+=1
        print("The quiz has been submitted.\nNumber of questions attempted: " ,self.totalQuesAttempted, "\nNumber of questions answered correctly: ", self.totalCorrectQues, "\nNumber of questions answered incorrectly:", self.totalIncorrectQues)
        print("Total Score: ", self.score)
        exit()
    


choice=input("1. Press any key to start quiz \n2. press e to exit\n")
if(choice=='e'):
    print("You should have tried, i worked really hard on this quiz :(")
    exit()
else:
    pass

wiz=quiz_flow()

print("Welcome to the quiz!")
wiz.totalQuesNumber=int(input("Enter the number of questions in the quiz: "))

randomlist = []
i=1
while (i<=wiz.totalQuesNumber):
    n = random.randint(0,11)
    if n in randomlist:
        i-=1
    else:
        randomlist.append(n)
    i+=1

j=0
for i in randomlist:
    wiz.l.append([i,0,0,0])
    wiz.l[j][2]=question_bank.question_list[i]["answer"]
    j+=1

while(True):
    print("\npress:\n1. Give Response \n2. Mark For Review\n3. Unmark for review \n4. Next Question \n5. Previous question \n6. Move to Question Number \n7. Clear Response \n8. Clear all Response\n9. Show questions marked for review\n10. Submit")
    print("\n", wiz.currentQuesNumber)
    print(question_bank.question_list[wiz.l[(wiz.currentQuesNumber)-1][0]]["text"],"\n")
    ch_1=int(input())
    
    match ch_1:
        case 1:
            while(wiz.currentQuesNumber<=wiz.totalQuesNumber):
                print("Press 't' for True \nPress 'f' for False")
                res=input().lower()
                if(res=='t'):
                    wiz.set_responce("True")
                    break
                elif(res=='f'):
                    wiz.set_responce("False")
                    break
                else:
                    print("Enter a valid choice.")
            wiz.next_question()

        case 2:
            wiz.MFR()

        case 3:
            wiz.unMFR()
        
        case 4:
            wiz.next_question()

        case 5:
            wiz.previous_question()
        case 6:
            print("Enter the Number You want to move")
            x=int(input())
            wiz.move_to_question_num()
        case 7:
            wiz.clear_response()
        case 8:
            while(True):
                print("\n Are you sure you want to Clear all Response\nPress 'y' for Yes\nPress 'n' for No")
                confirm=input().lower()
                if(confirm=='y'):
                    wiz.clear_all_response()
                    break
                elif(confirm=='n'):
                    break
                else:
                    print("Enter a valid input")
        case 9:
            wiz.show_MFR()

        case 10:
            wiz.submit()