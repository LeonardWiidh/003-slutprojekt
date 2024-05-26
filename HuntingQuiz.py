import os
import json
from msvcrt import getwch
from SPfunk import ask_question, welcometext, easteregg

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def load_questions(file_path):
    with open(file_path, 'r', encoding="utf-8") as file:
        return json.load(file)

def main():
    points = 0
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_name = os.path.join(current_dir, "Questions.json")
    questions = load_questions(file_name)

    welcometext()
    print("Klicka på valfri knapp för att starta ")
    getwch()

    for question in questions:
        clear_screen()
        player_answer = ask_question(question)
        if player_answer == question.get('correctAnswer'):
            points += 1

    # After answering all questions, show the result
    clear_screen()
    print(f"Du fick {points} av {len(questions)} rätt!")

    # Show easter egg if the user got all answers correct
    if points == len(questions):
        easteregg()

if __name__ == "__main__":
    main()