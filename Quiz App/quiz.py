import random
import time

from requests import options

from question import Question

class Quiz:
    def __init__(self, question_file):
        self.question_file = question_file
        self.questions = []
        self.load_questions()

    def load_questions(self):
        try:
            with open(self.question_file,'r',encoding='UTF-8') as file:
                for line in file:
                    parts = line.strip().split("|")
                    question_text = parts[0]
                    options = parts[1:4]
                    correct_option = options.index(parts[4])

                    question = Question(question_text, options, correct_option)

                    self.questions.append(question)
        except Exception as e:
            print(e)
            print("Sualları yükləyərkən xəta baş verdi.")

    def start(self):
        random.shuffle(self.questions)
        score = 0
        start_time = time.time()

        for i, question in enumerate(self.questions):
            print(f"{i + 1}. {question}")

            try:
                answer = input("Cavabınız: ")

                if(answer not in question.variants):
                    raise Exception("Yalnış Daxiletmə")

                answer = question.variants.index(answer)

                if(question.is_correct(answer)):
                    score += 1

            except:
                print('Xahiş olunur doğru məlumat daxil edin.')

        end_time = time.time()
        duration = round(end_time - start_time)
        print(f"Quiz tamamlandı! Nəticəniz: {score}/10 ({duration} saniyədə)")

        self.save_score(score,duration)

    def save_score(self,score,duration):
        with open('leaderboard.txt','a') as file:
            file.write(f"{score}|{duration}\n")

        print('Skorunuz lider lövhəsinə yazıldı.')













