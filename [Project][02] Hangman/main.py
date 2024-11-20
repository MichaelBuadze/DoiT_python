from hangman_art import stages
from hangman_words import valid_simbols
from fmain import (
    start_game,
    choose_word,
    initialize_display,
    get_valid_guess,
    update_display,
)

def play_game():
    start_game()

    chosen_word, quest = choose_word()
    word_length = len(chosen_word)
    print("\n" + quest + "\n")
    display = initialize_display(word_length)

    lives = len(stages) - 1
    game_is_finished = False

    while not game_is_finished:
        guess = get_valid_guess(valid_simbols)

        if guess in display:
            print(f"\nშენ უკვე გამოიცანი ეს სიმბოლო - {guess}")
        else:
            update_display(chosen_word, display, guess)

        print(f"{' '.join(display)}")

        if guess not in chosen_word:
            print(f"\n {guess}, სხვაგან ხარ, ერთი შანსით ნაკლები გაქვს ;).")
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("\nწააგე!")
                print("\nთამაში დასრულდა!")
        
        if "_" not in display:
            game_is_finished = True
            print("\nგილოცავ, შენ შეძელი ეს!")

        print(stages[lives])

# თამაშის გაშვება
# if __name__ == "__main__":  შესაძლებელია მომავალი განვითარებისთვის გახდეს საჭირო. 
play_game()
