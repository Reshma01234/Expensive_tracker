# Expense Tracker CLI

A simple command-line program to record expenses and see their total.
Built as the Day 7 mini-project of the Python roadmap (Days 1-6 concepts).

## Features
- Add an expense (description and amount)
- View all expenses in a numbered list
- Show the total of all expenses
- Input validation: blank descriptions, non-numeric, negative, `nan` and `inf` amounts are rejected and the user is asked again
- Exits cleanly on the Exit option, Ctrl+C, or end of input

## Requirements
- Python 3.6 or newer (no external libraries)

## How to run
```
python expense_tracker.py
```
If `python` does not work, use `python3 expense_tracker.py` (Mac/Linux) or `py expense_tracker.py` (Windows).

## Menu
| Option | Action |
|--------|--------|
| 1 | Add Expense |
| 2 | View Expenses |
| 3 | Show Total |
| 4 | Exit |

## Example session
```
=== Expense Tracker ===
1. Add Expense
2. View Expenses
3. Show Total
4. Exit
Choose an option (1-4): 1
Description: Lunch
Amount: 150.50
Added: Lunch - 150.50
```

## Running the tests
```
python run_tests.py
```
Runs 24 scripted tests (valid input, invalid input, edge cases) and saves the results to `test_results.txt`.

## Project files
| File | Purpose |
|------|---------|
| `expense_tracker.py` | The program |
| `run_tests.py` | Test script |
| `test_results.txt` | Recorded test results (24/24 passed) |
| `day7_review_notes.txt` | Bugs found, causes, fixes, and retest results |
| `knowledge_answers.md` | Knowledge assessment answers |

## Notes
- Expenses are stored in memory only, so they are cleared when the program exits.
- Amounts are shown with 2 decimal places. An amount of 0 is accepted.
