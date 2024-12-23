import random
import time
diff = 0
while diff < 3:
    diff = int(input('Insert the difficulty level. Normal is 50, recommended is between 20 and 200.\n'))

def random_num_getter(difficulty):
    def random_num_inner():
        return random.randint(2, difficulty)
    return random_num_inner

random_num = random_num_getter(diff)

def random_signal():
    signal = random.randint(1, 4)
    ran_num = random_num()
    ran_num2 = random_num()
    if signal == 1:
        ran_num, ran_num2 = random_num(), random_num()
        return ran_num*3, '+', ran_num2*3
    elif signal == 2:
        while ran_num <= ran_num2:
            ran_num = random_num()
            ran_num2 = random_num()
        return ran_num*2,'-', ran_num2*2
    elif signal == 3:
        while ran_num*ran_num2 >= 100:
            ran_num = random_num()
            ran_num2 = random_num()
        return ran_num,'*', ran_num2
    else:
        while ((ran_num*2) % ran_num2 != 0 or (ran_num*2) == ran_num2):
            ran_num = random_num()
            ran_num2 = random_num()
        return ran_num*2,'/', ran_num2

def score_counter(was_true, current_score, current_score_mult):
    if was_true == 1:
        score = current_score + current_score_mult
    else:
        score = (current_score - current_score_mult) - 2
    current_score_mult += 1
    print(f'Score is {score} right now, and the score multiplier is currently {current_score_mult}')
    return score, current_score_mult

def equation_solver():
    equation = random_signal()
    num1 = equation[0]
    operator = equation[1]
    num2 = equation[2]
    if operator == '/':
        ran_question_solved = num1/num2
    elif operator == '*':
        ran_question_solved = num1*num2
    elif operator == '-':
        ran_question_solved = num1-num2
    else:
        ran_question_solved = num1+num2
    return f'{num1}{operator}{num2}', ran_question_solved

def was_correct(answer, ran_question_solved, elapsed_time, max_time,):
    over_time_time = elapsed_time - max_time
    if over_time_time == 1:
        pluralization = ''
    else:
        pluralization = 's'

    if elapsed_time >= max_time:
        print(f'You took {over_time_time:.1f} second{pluralization} over {max_time} seconds to answer the question. The correct answer was {ran_question_solved}.')
        return 0, 1, 1

    if answer == ran_question_solved:
        print('Correct answer!')
        return 1, 0, 1

    if answer == 123:
        print('You have chosen to quit.')
        return 0, 0, 0

    print(f'Wrong answer, correct answer was {int(ran_question_solved)}.')
    return 0, 0, 1


def question_asker():
    print('As you answer questions, the score multiplier will go higher. This will proportionally increase your score.\nInsert \"123\" to exit.')
    will = 1
    score = 5
    max_time = abs(float(input('Select maximum time for the questions, in seconds.\n')))
    score_mult = 1
    while True:
        current_time = time.time()
        ran_question_formed, ran_question_solved = equation_solver()
        answer = int(input(f'What is the answer to the following question? \n\n{ran_question_formed}\n'))
        elapsed_time = time.time() - current_time
        was_true, over_time, will = was_correct(answer, ran_question_solved, elapsed_time, max_time)
        if will != 1:
            break
        score, score_mult = score_counter(was_true, score, score_mult)
        if score < 0:
            print('As the score was negative, you lose! Please try again.')
            break
        if int(elapsed_time) == 1:
            pluralization = ''
        else:
            pluralization = 's'
        if over_time is False:
            print(f'You took {float(elapsed_time):.1f} second{pluralization} to answer the question out of the maximum {max_time}.')

question_asker()
