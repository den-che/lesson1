answer = {
    "привет":"Привет!",
    "как дела":"Отлично, а у тебя?",
    "отлично":"Хорошего тебе дня",
    "пока":"Еще увидимся!"

}
def get_answer(question,answer):
    return answer.get(question)

def ask_user(answer):
    while True:
        user_input = input('Скажи что-нибудь: ')
        answer = get_answer(user_input,answer)
        print(answer)
        if user_input == 'Пока':
            print('Ну пока')
            break
        
if __name__ == "__main__":
	ask_user(answer)