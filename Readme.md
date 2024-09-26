# Find Pairs Project

## About
This is a simple Python project that allows users to find pairs of numbers in an array whose sum matches a given target. The program prompts the user to input an array of integers and a target sum, then finds and prints the pairs of numbers that add up to the target.

## Features
- Accepts user input from the terminal.
- Finds all pairs of elements in the array that sum up to a given target.
- Prints the indices and values of these pairs.

## Installation

### Prerequisites
Before running this project, ensure you have the following installed:
- Python (version 3.6 or higher)

### Steps
1. Clone the repository or download the source files.
2. Open your terminal and navigate to the project folder.
3. (Optional) Create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   ```
   Activate the virtual environment:
   - For Windows:
     ```bash
     venv\Scripts\activate
     ```
   - For macOS and Linux:
     ```bash
     source venv/bin/activate
     ```
4. Run the program using the following command:
   ```bash
   python main.py
   ```
5. The program will prompt you to enter an array of integers (comma-separated) and then a target sum.
    Example:
    ```bash
    Enter the array of integers (comma separated): 1,3,5,7,2,4
    Enter the target sum: 8
    ```
    Expected output:
    ```bash
    Pair found at 0 and 3 (1 + 7)
    Pair found at 1 and 2 (3 + 5)
    ```
    If no pairs are found that sum up to the target, the program will output:
    ```bash
    No pairs found
    ```
    Example:
    ```bash
    $ python main.py
    Enter the array of integers (comma separated): 1,3,5,7,2,4
    Enter the target sum: 8
    Pair found at 0 and 3 (1 + 7)
    Pair found at 1 and 2 (3 + 5)
    ```

## License
This project is licensed under the MIT License