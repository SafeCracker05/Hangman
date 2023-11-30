def main():
    Max_tries = 6
    Hangman_Entry = """
Welcome to the game hangman 
    _    _
   | |  | |
   | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
   |  __  |/ _' | '_ \ / _' | '_ ' _ \ / _' | '_ \\
   | |  | | (_| | | | | (_| | | | | | | (_| | | | |
   |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |
                        |___/

"""
    HANGMAN_PHOTOS = {
1: """

""",
2: """
x-------x
|
|
|
|
|
""",
3: """
x-------x
|       |
|       0
|
|
|
""",
4: """
x-------x
|       |
|       0
|       |
|
|
""",
5: """
x-------x
|       |
|       0
|      /|\\
|
|
""",
6: """
x-------x
|       |
|       0
|      /|\\
|      /
|
""",
7: """
x-------x
|       |
|       0
|      /|\\
|      / \\
|
"""
    }
     
     
    def print_hangman(num_of_tries):
       print(HANGMAN_PHOTOS[num_of_tries])
     
     
    print(Hangman_Entry)
    print(Max_tries)
    index_of_the_word = int(input("Enter a index: "))
    def choose_word(index):
        """Choosing word from a text file.
        :param file_path: file's path location
        :param index: selected word's index
        :type file_path: string
        :type index: int
        :return: The selected word
        :rtype: string
        """
        with open(r"C:\Users\User\Desktop\python\Words_for_the_hangman.txt", 'r') as f:
           words_list = f.read().split()
        count_of_words = 0
        a = []
        for words in words_list:
            if not words in a :
                count_of_words += 1
                a.append(words)
        index %= len(words_list)
                
                  
        tuple1 = (count_of_words, words_list[index - 1])
        return tuple1 
    secret_word_tuple = choose_word(index_of_the_word)
    secret_word1 = secret_word_tuple[1]
    def check_win(secret_word1, a):
         """check if the user win the game or not
         :param secret_word: user's chosen word
         :param old_letters_guessed: List of guessed letters
         :type secret_word: String
         :type old_letters_guessed:list
         :return:true if the user guessed all the leter in the word of false if not
         :rtype:bool"""
         count = 0
         for i in secret_word1:
             if i in a:
                 count += 1
          
         if count == len(secret_word1):
             return True
         return False
    sc_list = list('[@_!#$%^&*()<>?/\|}{~:]')
    def check_valid_input(letter_guessed, a):
       """this function get a string param and list of letter that the user alredy guessed
       and check's if the the letter is from alphabet
       and also check's if the letter is not a sign and return treu if the letter is good
       and also check's if the user already guessed this letter.
       and false if its not.
       :param letter_guessed: guessed letter from the user
       :type letter_guessed: string
       :return: true if the letter is correct false if it's not
       :rtype:bool"""
       if len(letter_guessed) > 1:
           return False
       elif letter_guessed in sc_list:
           return False
       elif letter_guessed.lower() in a:
           return False
       else:
           return True
    def show_hidden_word(secret_word1, a):
        '''show the status of the hiiden word.
        :param secret_word: user's chosen word
        :param old_letters_guessed: List of guessed letters
        :type secret_word: String
        :type old_letters_guessed:list
        :return: variable 'result' which contain the status of the letter allready gussed
         :rtype: str'''
        displayed_word = ""
        for i in secret_word1:
            if i in a:
                 displayed_word += i + " "
            else:
                displayed_word += "_ "
        
        print(displayed_word)

    def try_update_letter_guessed(letter_guessed, a):
        """this function get a letter from the user and a list of letter that the user already guessed,
        and check's if the letter is new it will append the letter to the list of the letter allredy guessed and print 'X' and under the list of letter that guessed with -> between them
        :param letter_guessed: letter from the user
        :param old_letter_guessed: list of letter allredy guessed
        :type letter_guessed: string
        :type old_letter_guessed: list
        :return: true or false
        :rtype: bool"""
        if not check_valid_input(letter_guessed, a):
            print("X")      
            print(" -> ".join(sorted(a)))
        else:
            a.extend(letter_guessed)

    print("let's start")
    print_hangman(1)
    print("_ " * len(secret_word_tuple[1]))
    num_of_tries = 6 # it's start from 6 to 0 
    Hangman_photo = 1 # it's start from 1 to 7
    a = []  # old letters guessed
    while num_of_tries > 0 and not check_win(secret_word1, a):
        letters = (input("Guess a letter : ")).lower()  

        if check_valid_input(letters, a) and letters in secret_word1 :
            a.append(letters.lower())
            show_hidden_word(secret_word1, a)
        elif not check_valid_input(letters, a) or not letters.isalpha():
            print("X") 
        elif not check_valid_input(letters, a) and letters in a :
            try_update_letter_guessed(letters, a)
        else:
            print(f":(")
            a.append(letters.lower())
            num_of_tries -= 1
            Hangman_photo += 1
            print_hangman(Hangman_photo)
            show_hidden_word(secret_word1, a)
            print("Tries --> ", num_of_tries, ", Win? --> ", check_win(secret_word1, a))
    if check_win(secret_word1, a):
        print("You won!!!")
    else:
        print("You're loser!!!")

if __name__ == '__main__':
    main()

