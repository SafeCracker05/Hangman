# Hangman Game in Python

Welcome to the Hangman game implemented in Python! This classic word-guessing game challenges you to guess a hidden word letter by letter. You have a limited number of attempts before the hanging man is fully drawn.

## Instructions

1. **Clone the Repository:**
   - Clone this repository to your local machine using the following command:
     ```bash
     git clone https://github.com/your-username/hangman-python.git
     ```
   - Replace `your-username` with your GitHub username.

2. **Navigate to the Project:**
   - Change your working directory to the cloned repository:
     ```bash
     cd hangman-python
     ```

3. **Run the Game:**
   - Execute the following command to start the Hangman game:
     ```bash
     python hangman.py
     ```
   - Make sure you have Python installed on your machine.

4. **Follow the On-screen Instructions:**
   - The game will prompt you to enter an index to choose a word from the predefined list.

5. **Guess the Word:**
   - Try to guess the word by entering letters one at a time.
   - The game will display your progress and the status of the hanging man.

6. **Win or Lose:**
   - You win if you successfully guess the entire word within the given number of attempts.
   - You lose if the hanging man is fully drawn before you guess the word.

## Hangman Art

The hanging man drawings are displayed for each incorrect guess. Here are the different stages:

1. 
    ```
    x-------x
    |
    |
    |
    |
    |
    ```

2.
    ```
    x-------x
    |       |
    |
    |
    |
    |
    ```

3.
    ```
    x-------x
    |       |
    |       0
    |
    |
    |
    ```

4.
    ```
    x-------x
    |       |
    |       0
    |       |
    |
    |
    ```

5.
    ```
    x-------x
    |       |
    |       0
    |      /|\
    |
    |
    ```

6.
    ```
    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |
    ```

7.
    ```
    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |
    ```

## Have Fun Playing!

Enjoy the classic Hangman game in Python. Feel free to customize and improve the game as you see fit. If you have any suggestions or find issues, please open an [issue](https://github.com/your-username/hangman-python/issues) on GitHub. Happy guessing!
