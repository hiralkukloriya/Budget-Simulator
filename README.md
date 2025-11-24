# Budget-Simulator
The Budget Buddy is a simple, command-line-based interactive program designed to help users track their personal monthly finances. It acts as a digital ledger, providing a straightforward way to set monthly income, record expenses by category.
# Budget Buddy 

Budget Buddy is a simple **Python console application** designed to help you track your monthly income and expenses. It provides a quick and easy way to monitor your budget and see your remaining balance.


##  Features

  * **Set Monthly Income:** Easily define your monthly earnings.
  * **Add Expenses:** Track spending across custom categories (e.g., Rent, Food, Fun).
  * **View Summary:** Get a detailed breakdown of your income, total expenses, category-wise spending, and remaining balance.
  * **Friendly Feedback:** Receive encouraging messages based on your current budget status (saving, balanced, or overspending).
  * **Persistent Menu:** The application runs in a loop, allowing you to perform multiple actions until you choose to exit.



## Getting Started

### Prerequisites

You need **Python 3.x** installed on your system to run this script.

### Installation

1.  **Save the code:** Copy the provided Python code and save it into a file named `budget_buddy.py`.

2.  **Run the script:** Open your terminal or command prompt, navigate to the directory where you saved the file, and execute the following command:

    ```bash
    python budget_buddy.py
    ```



## How to Use

When you run the script, the main menu will appear:


Hello there! I'm your Budget Buddy.
Let's keep track of your money together.

Welcome to Your Budget Buddy
What would you like to do today?
1. Set Monthly Income
2. Add an Expense
3. View My Budget Summary
4. Exit
Enter your choice (1-4):
```

1.  **Select `1. Set Monthly Income`** to enter your monthly earnings. **Always do this first** for an accurate budget summary.
2.  **Select `2. Add an Expense`** to log your spending. You'll be prompted for a category name and the amount.
3.  **Select `3. View My Budget Summary`** to see your current financial status, including category breakdowns and your remaining balance.
4.  **Select `4. Exit`** to close the application.



##  Code Structure

The script is organized into two main functions:

  * **`show_menu()`**: Prints the options available to the user.
  * **`main()`**: Contains the main application logic, including the infinite loop that drives the menu system, handles user input, and manages the `income` (a float) and `expenses` (a dictionary).

The budget data is stored in memory (`income` and `expenses`), meaning it will be **cleared every time you exit and restart** the application.

-----

## Potential Enhancements

  * **Data Persistence:** Implement saving/loading of the budget data to a file (e.g., JSON, CSV) so the data isn't lost when the application closes.
  * **Error Handling:** Add robust error checking for non-numeric or negative inputs.
  * **Expense Goals:** Allow users to set a maximum budget for specific categories.




