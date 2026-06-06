# ====================================
# GENERAL KNOWLEDGE QUIZ
# ====================================

print("====================================")
print("       GENERAL KNOWLEDGE QUIZ")
print("====================================")

score = 0

# Question 1
print("\nQuestion 1:")
print("What is the capital of France?")
answer = "Paris"   # given answer

if answer.lower() == "paris":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

# Question 2
print("\nQuestion 2:")
print("Which planet is known as the Red Planet?")
answer = "Mars"

if answer.lower() == "mars":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

# Question 3
print("\nQuestion 3:")
print("Who developed Python programming language?")
answer = "Guido van Rossum"

if answer.lower() == "guido van rossum":
    print("Correct answer!")
    score += 1
else:
    print("Wrong answer!")

# Result
print("\n====================================")
print("            QUIZ RESULT")
print("====================================")

print("Your final score is:", score, "/3")

if score == 3:
    print("Excellent! All answers are correct.")
elif score == 2:
    print("Good job!")
elif score == 1:
    print("Need more practice.")
else:
    print("Try again.")

print("====================================")