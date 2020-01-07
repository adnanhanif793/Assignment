import pyperclip
import sys
print("enter lines and Control+D to quit")
userInput = sys.stdin.read()

# Separate lines and add stars.
lines = userInput.split('\n')
for i in range(len(lines)):    # loop through all indexes for "lines" list
    lines[i] = '* ' + lines[i] # add star to each string in "lines" list
text = '\n'.join(lines)
pyperclip.copy(text)
print(pyperclip.paste())