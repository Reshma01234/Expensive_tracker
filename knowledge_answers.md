# Day 7 – Knowledge Assessment Answers (Days 1–6)

**1. Integer, float, string, Boolean?**
They are different kinds of values. An integer is a whole number (`5`), a float has a decimal part (`5.75`), a string is text inside quotes (`"hello"`), and a Boolean is only `True` or `False`. The type decides what you can do with the value, for example you can add two numbers but `"5" + "5"` joins text and gives `"55"`.

**2. Why convert input before arithmetic?**
`input()` always gives back a string, even if the user types digits. `"10" + "5"` gives `"105"`, not 15, and `"10" * 2` repeats the text. So I convert with `int()` or `float()` first, e.g. `price = float(input("Price: "))`.

**3. `=` vs `==`?**
`=` assigns a value to a variable (`age = 18`). `==` compares two values and gives `True` or `False` (`age == 18`). Writing `=` inside an `if` is a mistake.

**4. When use if/elif/else instead of separate ifs?**
When the choices are mutually exclusive and only one branch should run, like grade bands or a menu choice. With `elif`, Python stops at the first true condition. With separate `if`s, every condition is checked, so more than one block can run by accident.

**5. for loop vs while loop?**
A `for` loop is used when I know what I'm looping over or how many times (a list, or `range(5)`). A `while` loop is used when I repeat until a condition changes and don't know the count in advance, such as asking until the user types valid input.

**6. What do break and continue do?**
`break` leaves the loop completely. `continue` skips the rest of the current round and goes to the next one. Example: in a "sum until 0" loop, `break` on 0, and `continue` when the input is invalid.

**7. List vs tuple?**
Both hold ordered items, but a list is mutable (I can add, remove, or change items) and a tuple is immutable (fixed once created). I use a list for things that grow, like expenses, and a tuple for fixed data like `(latitude, longitude)`.

**8. Why a dictionary instead of a list?**
A dictionary stores key–value pairs, so I look things up by a meaningful name instead of a position. `expense["amount"]` is clearer than `expense[1]`, and counting words with `counts[word]` is much faster than searching a list.

**9. Parameter vs argument?**
A parameter is the variable name in the function definition (`def greet(name)`). An argument is the actual value I pass when calling it (`greet("Reshma")`).

**10. print() vs return?**
`print()` only shows text on the screen; the function gives nothing usable back (`None`). `return` sends a value back to the caller so it can be stored or used in more calculations, and it ends the function. `calculate_total()` returns the total so other code can use it.

**11. What is variable scope?**
Scope is where a variable can be used. A variable created inside a function is local and disappears when the function ends, so other functions can't see it. That's why I pass data like `expenses` in as a parameter instead of depending on outside variables.

**12. Purpose of try and except?**
They let the program handle an error without crashing. The risky code goes in `try`, and if it raises an error, the matching `except` block runs and I can show a helpful message instead of a traceback.

**13. When does ValueError happen with input?**
When the text can't be converted to the type I asked for, e.g. `int("abc")`, `float("")`, or `int("3.5")`. Typing letters, leaving it blank, or typing `1,200` for a number all cause it.

**14. Syntax error vs exception vs logic error?**
- *Syntax error:* the code breaks Python's rules (a missing colon), so it won't even start running.
- *Exception:* the code is valid but fails while running (`ZeroDivisionError`, `ValueError`). It can be handled with `try/except`.
- *Logic error:* the program runs without any error but gives the wrong result, like using `<` instead of `<=`. Python doesn't warn me, so I only find it by testing.

**15. Steps to investigate a traceback?**
1. Read the last line first: it names the error type and message.
2. Look at the file and line number just above it to see where it happened.
3. Read the lines of the call chain upward to see how the code got there.
4. Reproduce it with the same input.
5. Find the cause (for example, print the variable's value and type).
6. Make one focused fix and run the same test again.
