from hangman_art import stages
from hangman_words import valid_simbols
from fmain import (
    start_game,
    choose_word,
    initialize_display,
    get_valid_guess,
    update_display,
)

def play_game(): # თამაშის სრული განსაზღვრა საბოლოო ფუნქციაში
    start_game()

    chosen_word, quest = choose_word()
    word_length = len(chosen_word)
    print("\n" + quest + "\n")
    display = initialize_display(word_length)

    lives = len(stages) - 1
    game_is_finished = False

    while not game_is_finished:

        print(f"{' '.join(display)}")
        guess = get_valid_guess(valid_simbols)

        if guess in display:
            print(f"\nშენ უკვე გამოიცანი ეს სიმბოლო - {guess}")
        else:
            update_display(chosen_word, display, guess)

        if guess not in chosen_word:
            
            lives -= 1
            if lives == 0:
                game_is_finished = True
                print("\nწააგე!")
                print("\nთამაში დასრულდა!")
            elif lives == 1:
                print(f"\n {guess}, არ არის სიტყვაში. ბ ო ლ ო   ც დ ა!")
            else:
                print(f"\n {guess}, სხვაგან ხარ, {lives} ცდა გაქვს ;).")

        print(stages[lives])

        if "_" not in display:
            game_is_finished = True
            print(f"\n{' '.join(display)}")
            print("\nგილოცავ, შენ შეძელი ეს!\n")
           

       

# თამაშის გაშვება
# if __name__ == "__main__":  შესაძლებელია მომავალი განვითარებისთვის გახდეს საჭირო. 
play_game() # შესაძლებელია თამაში ჩაჯდეს while ციკლში და მომხმარებელს შესთავაზოთ თამაში თავიდან, ან პროგრამის დახურვა. 
