# Python Practice

This repository is a personal daily practice log for learning and improving Python skills. 
Each day includes a small coding challenge or project to reinforce core concepts.

---

## Goals
- Strengthen core Python fundamentals
- Build up to full-stack web apps
- Practice Git/Github workflows

---

## Completed Days

### Day01 - FizzBuzz
- **Task**: Print numbers 1 to 100.
- **Logic**:
    - "Fizz" if divisible by 3
    - "Buzz" if divisible by 5
    - "FizzBuzz" if divisible by both
    - number itself otherwise
- **File**: `fizzbuzz.py`

---

### Day02 - Basic Calculator
- **Task**: Create a command-line calculator.
- **Features**:
    - Add, Subtract, Multiply, Divide
    - Handles division by zero
    - Validates numeric input
- **File**: `calculator.py`

---

### Day03 - Word Counter
- **Task**: Count how many words are in a paragraph and how many times each word appears.
- **Features**:
    - Strips basic punctuation
    - Converts all words to lowercase
    - Displays total word count and word frequencies
- **File**: `word_counter.py`

---

### Day 4 - Number Guessing Game
- **Task**: User tries to guess a randomly generated number between 1 and 100.
- **Features**:
    - Tells the user if guess is too high, too low, or correct
    - Tracks number of attempts
    - Handles invalid inputs gracefully
- **File**: `guessing_game.py`

---

### Day 5 - To-Do List (Command Line App)
- **Task**: Create a basic command-line to-do list app.
- **Features**:
    - Add new tasks
    - View current tasks with completion status
    - Mark tasks as completed
    - Delete tasks
    - Simple text menu navigation
- **File**: `todo.py`

---

### Day 6 – Flashcard Quiz App
- **Task**: Create a terminal-based quiz that asks the user a set of questions and tracks correct answers.
- **Features**:
    - Dictionary of flashcard questions and answers
    - Accepts user input and checks for correctness
    - Shows score at the end
    - Case-insensitive matching
- **File**: `flashcards.py`

---

### Day 7 - Contact Book (File Storage)
- Created a contact book storing name, phone, and email.
- User can add, view, and search contacts.
- Data is saved in `contacts.txt`.
- Practiced file I/O and string formatting.
- **File**: `contact_book.py`

---

### Day 8 - Dice Roller App
- User chooses how many dice to roll and how many sides per die.
- Program generates random numbers using `random.randint`.
- Practiced input handling, lists, and loops.
- **File**: `dice_roller.py`

---

### Day 9 - Unit Converter App
- Converts between:
  - Kilometers ↔ Miles
  - Celsius ↔ Fahrenheit
  - Kilograms ↔ Pounds
- Used functions for each conversion.
- Included error handling for invalid input.
- **File**: `unit_convertor.py`

---

### Day 10 - 
**Project:** Password Generator
- Generates a random password based on user preferences.
- Options include length, uppercase letters, digits, and symbols.
- Practiced string manipulation and randomness with the `string` and `random` libraries.
- Input validation and error handling included.
- **File**: `password_generator.py`

---

### Day 11 
**Project:** Stopwatch & Countdown Timer
- Built a command-line stopwatch that tracks elapsed time in minutes, seconds, and milliseconds.
- Optional countdown feature where the user sets a timer in seconds.
- Used the `time` module and `divmod()` for formatting.
- Practiced user prompts, `input()`, loops, and real-time delays with `time.sleep()`.
- **File**: `stopwatch.py`

---

### Day 12
**Project:** 
- File Organizer Script
**Description:**
 - Created file_organizer.py, which organizes the contents of a specified folder into subfolders by file type (e.g., Images, Documents, Music, etc.).
 - How it works:
 - User sets the target folder path (e.g., "C:/Users/Username/Desktop/Folder").
 - Script scans the folder and categorizes each file by its extension.
 - Creates subfolders like Images/, Documents/, etc., and moves files into them.
 - Files with unknown or missing extensions are moved into Others/.
- **File**: `file_organizer.py`

---

## Day 13 – Calling APIs with Python
**Project:** Chuck Norris Joke Fetcher  
**Description:**  
- Connects to the [Chuck Norris Joke API](https://api.chucknorris.io/)
- Fetches and displays random Chuck Norris jokes in the terminal
- Includes error handling for bad requests or failed connections
- Uses a simple command-line menu to let the user get new jokes or exit
**File:** `chuck_jokes.py`  

---

## Day 14 – Calling APIs with Python
**Project:** Python News Scraper 
**Description:** 
- A Python script that fetches the latest blog posts from the Python.org RSS Feed using feedparser.
- Fetches RSS feed from Python.org
- Parses and displays the latest blog headlines
- Includes error handling for missing or malformed feeds
**File:** `python_news_scraper.py`  

---

## Day 15 – Password Strength Checker
**Project:**  Password Strength Checker
**Description:**
- A Python script that evaluates the strength of a user-provided password.
- Checks for minimum length, digits, uppercase/lowercase letters, and special characters.
- Rates the password as Weak, Moderate, or Strong.
- Uses getpass to securely take password input.
- Provides feedback on which criteria were or weren’t met.
**File:** `password_strength_checker.py`

---

## Day 16 – Weather App CLI
**Project:** Weather App CLI
**File:** `weather_cli.py`
**Description:**
- A Python script that fetches current weather data for any city using the OpenWeatherMap API.
- Uses the requests and python-dotenv libraries.
- Reads the API key securely from a .env file (not committed to GitHub).
- Displays temperature (in Fahrenheit), "feels like" value, and weather description.
- Includes error handling for missing API keys or invalid city names.

---

## Day 17 – Command-Line Expense Tracker
**Project:** Expense Tracker CLI
**File:** `expense_tracker.py`
**Description:**
-A command-line app that lets users record and review daily expenses.
-Features:
-Add a new expense with date, category, description, and amount
-View all saved expenses in a formatted table
-Calculates and displays the total amount spent
-Data is stored in a CSV file (expenses.csv) for persistence across sessions
-Includes basic input validation and menu-driven interface

---

## Day 18 – Binary Search Visualizer
**Project:** Binary Search Visualizer (CLI)
**File:** `binary_search_visualizer.py`
**Description:**
- A command-line tool that demonstrates the binary search algorithm step-by-step on a sorted list.
- Visualizes how the algorithm narrows down the search range using low, mid, and high pointers.
- Accepts a sorted list and a target number from the user.
- Shows each comparison and the current slice of the list being evaluated.
- Notifies the user whether the number was found and how many steps it took.

---

## Day 19 – Mad Libs Generator
**Project:** Mad Libs Generator
**File:** `mad_libs.py`, `mad_libs_template.txt`
**Description:**
- A command-line Mad Libs game that reads a story template from a file.
- Prompts the user to input various parts of speech (nouns, verbs, adjectives, etc.).
- Replaces placeholders in the template with user inputs to generate a funny story.
- Demonstrates string manipulation, file reading, and regular expressions for placeholder detection.

---

## Day 20 – Markdown to HTML Converter
**Project:** Markdown to HTML Converter
**File:** `markdown_to_html.py`
**Description:**

- A Python script that converts a basic Markdown file to HTML.
- Supports headers (# to ######), bold, italics, bold-italics, unordered lists, and links.
- Uses regular expressions to parse and replace Markdown syntax.
- Reads from an input .md file and writes to an output .html file.
- Demonstrates regex usage, file handling, and simple text transformation.