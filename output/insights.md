# BASIC CHATBOT USING PYTHON

## 1. Introduction

This project is a simple rule-based chatbot developed using Python. The chatbot takes input from the user and provides predefined responses based on the entered message.

The chatbot can respond to greetings such as "hello", "hi", "hii", and "hey". It can also answer questions such as "how are you" and "what is your name". The user can type "bye" or "goodbye" to end the conversation.

This project demonstrates the basic concepts of Python programming, including functions, loops, user input, conditional statements, lists, strings, and the `break` statement.

## 2. Objective

The main objectives of this project are:

* To understand basic Python programming.
* To learn how to create and call a function.
* To understand the use of a `while` loop.
* To use `if`, `elif`, and `else` conditions.
* To take input from the user.
* To process user input using string methods.
* To create a simple interactive chatbot.

## 3. Requirements

### Software Requirements

* Python 3.x
* Visual Studio Code, IDLE, PyCharm, or any Python-supported editor
* Windows, Linux, or macOS

### Hardware Requirements

* Computer or laptop
* Keyboard

## 4. Concepts Used

The following Python concepts are used in this project:

* Function
* `while` loop
* `if-elif-else`
* User input
* Lists
* String `.lower()` method
* `break` statement
* `print()` function

## 5. Program Explanation

### 5.1 Creating the Function

The program starts by defining a function called `chatbot()`.

```python
def chatbot():
```

A function is a block of code designed to perform a specific task. In this project, the complete chatbot is written inside the `chatbot()` function.

### 5.2 Displaying the Welcome Message

The chatbot displays two messages when it starts:

```python
print("Simple Chatbot")
print("Type 'bye' to exit.\n")
```

The first message introduces the chatbot, while the second tells the user how to exit the program.

### 5.3 Using a While Loop

The chatbot uses:

```python
while True:
```

This creates an infinite loop, allowing the chatbot to continuously accept messages from the user until the user enters an exit command.

### 5.4 Taking User Input

The program asks the user to enter a message:

```python
user = input("You: ").lower()
```

The `input()` function receives the user's message.

The `.lower()` method converts the message into lowercase. This allows inputs such as `HI`, `Hi`, and `hi` to be treated in the same way.

### 5.5 Responding to Greetings

The chatbot checks whether the user's input is a greeting:

```python
if user in ["hello", "hi", "hii", "hey"]:
    print("Bot: Hi! How are you?")
```

The `in` operator checks whether the user's message matches any item in the list.

If the user enters `hello`, `hi`, `hii`, or `hey`, the chatbot responds with:

```text
Bot: Hi! How are you?
```

### 5.6 Checking "How Are You"

The next condition is:

```python
elif user in ["how are you"]:
    print("Bot: I'm fine, thanks!")
```

If the user enters `how are you`, the chatbot responds:

```text
Bot: I'm fine, thanks!
```

### 5.7 Answering the Name Question

The chatbot can answer a question about its name:

```python
elif user in ["what is your name", "your name"]:
    print("Bot: My name is basic Chatbot.")
```

Therefore, both `what is your name` and `your name` produce the same response.

### 5.8 Exiting the Chatbot

The chatbot checks whether the user wants to exit:

```python
elif user in ["bye", "goodbye"]:
    print("Bot: Goodbye!")
    break
```

If the user enters `bye` or `goodbye`, the chatbot displays a goodbye message.

The `break` statement terminates the `while` loop, which ends the chatbot.

### 5.9 Handling Unknown Messages

If none of the conditions match the user's input, the `else` block executes:

```python
else:
    print("Bot: Sorry, I don't understand.")
```

This provides a default response when the chatbot does not recognize the user's message.

### 5.10 Calling the Function

At the end of the program:

```python
chatbot()
```

This calls the `chatbot()` function and starts the program.

## 6. Working of the Chatbot

The working process is:

```text
Start
  ↓
Call chatbot() function
  ↓
Display welcome message
  ↓
Ask user for input
  ↓
Convert input to lowercase
  ↓
Check greeting
  ↓
Check "how are you"
  ↓
Check name question
  ↓
Check exit command
  ↓
If unknown → Display "I don't understand"
  ↓
Continue taking input
  ↓
User enters "bye"
  ↓
Display "Goodbye!"
  ↓
Break the loop
  ↓
End
```

## 7. Sample Output

```text
Simple Chatbot
Type 'bye' to exit.

You: hi
Bot: Hi! How are you?

You: how are you
Bot: I'm fine, thanks!

You: what is your name
Bot: My name is basic Chatbot.

You: xyz
Bot: Sorry, I don't understand.

You: bye
Bot: Goodbye!
```

## 8. Advantages

* Simple and easy to understand.
* Uses basic Python concepts.
* Interactive with the user.
* Easy to modify and add new responses.
* Good beginner project for understanding conditional statements and loops.

## 9. Limitations

* It can only understand predefined phrases.
* It does not use artificial intelligence or machine learning.
* Similar questions with different wording may not be recognized.
* The responses are fixed and predefined.

## 10. Future Improvements

The chatbot can be improved by:

* Adding more questions and responses.
* Supporting more variations of the same question.
* Adding a larger conversation database.
* Using Natural Language Processing (NLP).
* Adding a graphical user interface.
* Connecting the chatbot to an AI or language model.
* Adding voice input and voice output.

## 11. Conclusion

The Basic Chatbot project demonstrates how Python can be used to create a simple interactive application. The program receives input from the user and uses conditional statements to select an appropriate predefined response.

Through this project, basic concepts such as functions, loops, user input, lists, conditional statements, string methods, and the `break` statement are demonstrated. It provides a strong foundation for developing more advanced chatbot applications in the future.
