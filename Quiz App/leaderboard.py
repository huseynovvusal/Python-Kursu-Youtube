class Leaderboard:
    @staticmethod
    def show():
        try:
            with open('leaderboard.txt','r',encoding='UTF-8') as file:
                print("\nLider Lövhəsi:")

                for line in file:
                    score, duration = line.strip().split("|")

                    print(f"{score}/10 {duration} saniyə ərzində")
        except:
            print("Fayl açarkən xəta baş verdi.")