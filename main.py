import random
import turtle

def draw_line(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.pencolor(color)
    turtle.setposition(x1, y1)
    turtle.pendown()
    turtle.setposition(x2, y2)
    turtle.penup()

def write_text(xc, yc, text):
    turtle.pencolor("black")
    turtle.setposition(xc, yc)
    turtle.pendown()
    turtle.write(text, align = "center", font = ("Courier", 20, "bold"))
    turtle.penup()

def draw_box(x1, y1, x2, y2, color):
    turtle.penup()
    turtle.pencolor(color)
    turtle.fillcolor(color)
    turtle.setposition(x1, y1)
    turtle.begin_fill()
    turtle.pendown()
    turtle.setposition(x2, y1)
    turtle.setposition(x2, y2)
    turtle.setposition(x1, y2)
    turtle.setposition(x1, y1)
    turtle.penup()
    turtle.end_fill()

def draw_higher():
    draw_line(100, 170, 100, 210, "black")
    draw_line(85, 190, 100, 210, "black")
    draw_line(115, 190, 100, 210, "black")

def draw_lower():
    draw_line(100, 170, 100, 210, "black")
    draw_line(85, 190, 100, 170, "black")
    draw_line(115, 190, 100, 170, "black")

class R:
    user_total = 0
    magic_number = random.randint(1, 1000)

def user_round(num):
    draw_line(-200, 220, 200, 220, "black")
    draw_line(0, 220, 0, 100, "black")

    guess_list = [num]
    print("I'm thinking of a number between 1 and 1000. Try to guess it!")
    print("If you can guess it in 12 tries or less, you win!")
    user_guess = int(input("Enter your first guess: "))
    R.user_total = R.user_total + 1
    guess_list = [user_guess]
    write_text(-100, 160, user_guess)

    while user_guess != num:
        if user_guess < num and user_guess > 0:
            draw_higher()
            user_guess = int(input("My number is higher than that. Try again: "))
            for i in range(len(guess_list)):
                if(guess_list[i]) == user_guess:
                    user_guess = int(input("You've already guessed that number. Try a different one: "))
            draw_box(-200, 199, -1, 100, "white")
            draw_box(1, 219, 150, 100, "white")
            write_text(-100, 160, user_guess)
            R.user_total = R.user_total + 1
            guess_list.append(user_guess)

        elif user_guess > num and user_guess < 1000:
            draw_lower()
            user_guess = int(input("My number is lower than that. Try again: "))
            for i in range(len(guess_list)):
                if(guess_list[i]) == user_guess:
                    user_guess = int(input("You've already guessed that number. Try a different one: "))
            draw_box(-200, 199, -1, 100, "white")
            draw_box(1, 219, 150, 100, "white")
            write_text(-100, 160, user_guess)
            R.user_total = R.user_total + 1
            guess_list.append(user_guess)

        else:
            user_guess = int(input("Your guess has to be between 1 and 1000. Try again: "))

    if user_guess == num:
        draw_line(90, 170, 110, 150, "green")
        draw_line(110, 150, 145, 200, "green")
        print("")
        print("You guessed it! It took you " + str(R.user_total) + " tries.")

def final_score(num1):
    draw_box(-200, -100, 200, -400, "white")
    print("")
    write_text(0, -100, "Your tries: " + str(num1))

    if num1 <= 12:
        print("You guessed it in 12 tries or less, so you win! Nice job!")

    else:
        print("You had more tries than 12, so I win! Better luck next time!")

user_round(R.magic_number)
final_score(R.user_total)