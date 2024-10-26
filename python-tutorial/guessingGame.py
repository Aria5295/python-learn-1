
secret_word = "giraffe"
guess = ""
count = 0
limit = 3
out = False

while guess != secret_word and not(out):
    if count < limit:
        guess = input("Enter guess: ")
        count += 1
    else:
        out = True

if out:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")