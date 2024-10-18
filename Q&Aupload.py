from functions import load_questions, save_results, run_quiz_for_player

if __name__ == "__main__":
    file_name = 'Q&A.csv'
    output_file_name = 'Q&A_points.csv'

    headers, questions_list = load_questions(file_name)

    results = [['Player Name', 'Points']]
    num_players = int(input("Enter the number of players: "))

    for i in range(num_players):
        player_name = input(f"\nEnter the name of player {i + 1}: ")
        player_points = run_quiz_for_player(player_name, questions_list, num_players)
        results.append([player_name, player_points])

    save_results(output_file_name, results)


    print("\nQuiz completed! Here are the final results:")
    for result in results[1:]:
        print(f"{result[0]}: {result[1]} points")