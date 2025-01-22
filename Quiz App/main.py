from time import sleep
from quiz import Quiz
from leaderboard import Leaderboard

def main():
    print("Quiz App Tətbiqinə Xoş Gəldiniz!")

    while(True):
        print("""\nSeçimlər:
1. Quiz-ə Başla
2. Lider Lövhəsini Gör
3. Çıxış\n""")

        choice = input("Seçiminiz: ")

        if(choice == '1'):
            quiz = Quiz('questions.txt')
            quiz.start()
        elif(choice == '2'):
            Leaderboard.show()
        else:
            print("Sağ olun!")
            break

        sleep(1)



if(__name__ == '__main__'):
    main()