"""Runs the Expense Tracker with scripted input and records PASS/FAIL.
Test helper only - not part of the tracker itself."""
import subprocess
import sys

TESTS = [
    # (name, typed input lines, text that must appear, text that must NOT appear)
    ("Add a valid expense", ["1", "Lunch", "150.50", "4"], ["Added: Lunch - 150.50"], []),
    ("Blank description is re-prompted", ["1", "", "   ", "Tea", "20", "2", "4"],
     ["Description cannot be blank", "1. Tea - 20.00"], []),
    ("Letters as amount", ["1", "Tea", "abc", "20", "4"], ["Invalid amount", "Added: Tea - 20.00"], ["Traceback"]),
    ("Blank amount", ["1", "Tea", "", "20", "4"], ["Invalid amount", "Added: Tea - 20.00"], ["Traceback"]),
    ("Negative amount", ["1", "Tea", "-5", "20", "4"], ["cannot be negative", "Added: Tea - 20.00"], ["Added: Tea - -5"]),
    ("Amount 'nan' rejected", ["1", "Tea", "nan", "20", "3", "4"], ["Invalid amount", "Total expenses: 20.00"], ["nan -", "Total expenses: nan"]),
    ("Amount 'inf' rejected", ["1", "Tea", "inf", "20", "3", "4"], ["Invalid amount", "Total expenses: 20.00"], ["Total expenses: inf"]),
    ("Amount '-inf' rejected", ["1", "Tea", "-inf", "20", "4"], ["Invalid amount"], ["Added: Tea - -inf"]),
    ("Amount with comma '1,200'", ["1", "Rent", "1,200", "1200", "4"], ["Invalid amount", "Added: Rent - 1200.00"], ["Traceback"]),
    ("Amount with spaces ' 75 '", ["1", "Tea", " 75 ", "4"], ["Added: Tea - 75.00"], []),
    ("Zero amount accepted", ["1", "Free sample", "0", "3", "4"], ["Added: Free sample - 0.00", "Total expenses: 0.00"], []),
    ("Decimal amount 0.1 + 0.2", ["1", "A", "0.1", "1", "B", "0.2", "3", "4"], ["Total expenses: 0.30"], []),
    ("View with no expenses", ["2", "4"], ["No expenses recorded yet."], []),
    ("View several expenses", ["1", "Tea", "20", "1", "Bus", "35.5", "1", "Food", "100", "2", "4"],
     ["1. Tea - 20.00", "2. Bus - 35.50", "3. Food - 100.00"], []),
    ("Total with no expenses", ["3", "4"], ["Total expenses: 0.00"], []),
    ("Total matches entries", ["1", "Tea", "20", "1", "Bus", "35.5", "1", "Food", "100", "3", "4"], ["Total expenses: 155.50"], []),
    ("Very large amount", ["1", "Gold", "99999999999", "3", "4"], ["Total expenses: 99999999999.00"], []),
    ("Invalid menu: letter", ["x", "4"], ["Invalid choice", "Goodbye!"], ["Traceback"]),
    ("Invalid menu: 5", ["5", "4"], ["Invalid choice", "Goodbye!"], []),
    ("Invalid menu: blank", ["", "4"], ["Invalid choice", "Goodbye!"], []),
    ("Invalid menu: '1.0'", ["1.0", "4"], ["Invalid choice"], []),
    ("Menu keeps running until Exit", ["9", "2", "3", "8", "4"], ["Goodbye!"], []),
    ("Exit cleanly", ["4"], ["Goodbye!"], ["Traceback"]),
    ("Input ends mid-entry (EOF)", ["1", "Tea"], ["Exiting the Expense Tracker"], ["Traceback"]),
]

passed = 0
lines = []
for number, (name, typed, must, must_not) in enumerate(TESTS, 1):
    result = subprocess.run([sys.executable, "expense_tracker.py"],
                            input="\n".join(typed) + "\n", capture_output=True, text=True)
    out = result.stdout + result.stderr
    ok = all(m in out for m in must) and not any(m in out for m in must_not) and result.returncode == 0
    passed += ok
    lines.append(f"{number:2}. [{'PASS' if ok else 'FAIL'}] {name}")
    lines.append(f"      input: {typed}")
    if not ok:
        lines.append(f"      output was:\n{out}")

lines.append("")
lines.append(f"{passed}/{len(TESTS)} tests passed")
report = "\n".join(lines)
print(report)
open("test_results.txt", "w").write(report + "\n")
