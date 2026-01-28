from time import *
import random as r

def check_errors(test_para,test_input):
    errors = 0
    min_len = min(len(test_input), len(test_para))

    for i in range(min_len):
        if test_para[i] != test_input[i]:
            errors += 1

    # extra characters count as errors
    errors += abs(len(test_para) - len(test_input))
    return errors

def speed_time(start_time, end_time, user_input):
    time_taken = round(end_time - start_time, 2)

    words = len(user_input.split())
    wpm = (words / time_taken) * 60
    return round(wpm)


if __name__ == '__main__':
    while True:
        print("-"*8,"Check Your Typing Speed","-"*8)
        print()
        choice = input("Ready (Y/N): ")
        if choice.lower() == "y":
            paragraphs = [
                "The morning was calm and quiet. Sunlight slowly entered the room through the window, making everything look warm and peaceful. Birds were chirping outside, and the air felt fresh. It was the kind of morning that made you want to start the day with a smile.",

                "She decided to take a long walk after a busy day. The streets were less crowded, and the sound of traffic felt distant. With every step, her thoughts became lighter. Walking helped her clear her mind and feel relaxed again.",

                "The small café on the corner was always welcoming. The smell of coffee filled the air, and soft music played in the background. People sat quietly, lost in their own thoughts or conversations. It was a perfect place to spend a peaceful evening.",

                "He opened his notebook and began to write without thinking too much. Words flowed naturally, capturing his feelings on the page. Writing helped him understand himself better. Sometimes, all it takes is a pen and paper to find clarity.",

                "The library was silent except for the sound of pages turning. Rows of books stood neatly on the shelves, holding stories from different worlds. Sitting there made time feel slower and more meaningful.",

                "Rain started falling suddenly, tapping gently on the windows. The streets became shiny and clean within minutes. Children laughed as they jumped into puddles, enjoying the unexpected weather.",

                "She learned that patience often brings the best results. Not everything needs to happen immediately. Some things grow beautifully when given enough time.",

                "The train journey was long but comforting. Watching the scenery change through the window made the hours pass quickly. It reminded him that every journey has its own charm.",

                "At night, the city lights looked like stars on the ground. The roads were quieter, and the cool air felt soothing. It was a peaceful end to a busy day."
            ]

            test_para = r.choice(paragraphs)

            print()
            print(test_para)
            print()
            print("Let's Go...Start typing the given paragraph..")
            print()
            start_time = time()
            test_input = input()
            end_time = time()
            print()

            print("Speed: ", speed_time(start_time, end_time, test_input),"wpm")
            print("Error: ", check_errors(test_para, test_input))
            print()

            print("Do you wanna continue with the game??(Y/N): ")
            ch = input()
            if ch.lower() != "y":
                print("Thank you!!, Have a nice day..")
                break
        
        else:
            print("Thank you!!, Have a nice day..")
            break


