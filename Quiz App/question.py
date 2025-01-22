class Question:
    def __init__(self,question,options,correct_option):
        self.question = question
        self.options = options # ["..","..",".."]
        self.correct_option = correct_option # [2]
        self.variants = ['A','B','C']

    def is_correct(self, answer):
        return answer == self.correct_option

    def __str__(self):
        options = []

        for i, option in enumerate(self.options):
            options.append(f"{self.variants[i]}) {option}")

        options_display = "\n".join(options)

        return f"{self.question}\n{options_display}"

