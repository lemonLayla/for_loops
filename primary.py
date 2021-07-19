# author:layla
# date:7/17/2021

# -------------------- Section 1 -------------------- #

# ---------- Part 1 | Basic for Loops ---------- #
print(
    '>> Section 1\n'
    '>> Part 1\n'
)

# For the following for Loops, use in range(n), where n is the number of times ran.
#
# 1 - for Loop | Printing your Name
#   a. Create a for loop that runs 5 times.
#   b. Within the for loop, print your name.
#
# Example Output
#
#   elia
#   elia
#   elia
#   elia
#   elia
#
# Write Code Below #

for k in range(1,6):
    print('layla')

# 2 - for Loop | Printing i
#   a. Create a for loop that runs 5 times.
#   b. Within the for loop, print the value of iterator variable (i).
#
# Example Output #
#
#   0
#   1
#   2
#   3
#   4
#
# Write Code Below #
for p in range(0,5):
    print(p)
    print('i')

# 3 - for Loop | Running According to the User
#   a. Prompt the user for input in the form of an integer. Save it to a variable. This will be used as the argument
#       for range().
#   b. Create a for loop that runs n times, where n is the value entered by the user.
#   c. Within that for loop, print a symbol of your choice duplicated by the value of the iterator *variable.
#   d. CHALLENGE: Instead of choosing the symbol yourself, allow the user to specify by prompting their input.
#
# Example Output
#   >> 7
#
#   $
#   $$
#   $$$
#   $$$$
#   $$$$$
#   $$$$$$
#
# Write Code Below #
for n in range (1,7):
    print('#' * n)

# ---------- Part 2 | Direct Access ---------- #
print(
    '\n\n>> Section 1\n'
    '>> Part 2\n'
)

# For the following for Loops, use direct access.
#
# 1 - for Loop | Printing your Name
#   a. Create a variable named name, that stores your name as a string.
#   b. Create a for loop that uses your name as the sequence.
#   c. Print each letter of your name using the iterator variable.
#
# Example Output
#
#   e
#   l
#   i
#   a
#
# Write Code Below #
u = 'layla'
for char in u:
  print(char)
print (' ')
# 2 - for Loop | Printing the User's Name
#   a. Prompt input from the user in the form of their name. Save to a variable named name.
#   b. Create a for loop that uses the name of the user as the sequence.
#   c. Print each letter of the user's name using the iterator variable.
#
# Example Output
#
#   >> name... elia deppe
#
#   e
#   l
#   i
#   a
#
#   d
#   e
#   p
#   p
#   e
#
# Write Code Below #
l = 'layla'
for char in l:
  print(char)
print(' ')
o = 'Jones'
for char in o:
  print(char)
# ---------- Part 3 | range() variations ---------- #
print(
    '\n\n>> Section 1\n'
    '>> Part 3\n'
)

# range(stop)
# range(start, stop)
# range(start, stop, step)

# For the following for Loops, use direct access.
#
# 1 - for Loop | Custom Start
#   a. Create a for loop that runs from 10 to 25.
#   b. Print the value of the current iterator variable in the loop.
#
# Example Output
#
#   10
#   11
#   12
#   13
#   14
#   15
#   16
#   17
#   18
#   19
#   20
#   21
#   22
#   23
#   24
#
# Write Code Below #
for Q in range(10,25):
    print(Q)

print(' ')
# 2 - for Loop | Custom Step
#   a. Create a for loop that runs from 5 to -5.
#   b. Print the value of the current iterator variable in the loop.
#
# Example Output
#
#   5
#   4
#   3
#   2
#   1
#   0
#   -1
#   -2
#   -3
#   -4
#
# Write Code Below #

for z in range(5,-5,-1):
    print(z)