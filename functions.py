import csv
import random


def load_questions(file_name):
    with open(file_name, mode='r', encoding='utf-8') as file:
        csv_reader = csv.reader(file)
        headers = next(csv_reader)
        questions_list = list(csv_reader)
    return headers, questions_list

def save_results(output_file_name, updated_rows):
    with open(output_file_name, mode='w', encoding='utf-8', newline='') as output_file:
        csv_writer = csv.writer(output_file)
        csv_writer.writerows(updated_rows)
    print(f"Results saved to '{output_file_name}'.")

def ask_question(row):
    print(f"Question: {row[0]}")
    print(f"A) {row[1]}")
    print(f"B) {row[2]}")
    print(f"C) {row[3]}")
    print(f"D) {row[4]}")

    answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    while answer not in ['A', 'B', 'C', 'D']:
        print("Invalid answer. Please enter A, B, C, or D.")
        answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

    correct_answer = row[5].strip().upper()
    if answer == correct_answer:
        print("Correct!")
        return 1
    else:
        print(f"Incorrect! The correct answer was: {correct_answer}")
        return 0

def run_quiz_for_player(player_name, questions_list, number_of_players):
    total_points = 0
    random.shuffle(questions_list)
    for row in questions_list:
        if number_of_players > 1:
            print(f"\nPlayer: {player_name}")
        points = ask_question(row)
        total_points += points
    print(f"\n{player_name}, you scored {total_points} points.")
    return total_points