from Question import Question

print ("Welcome to Two Truths & Lie Game in order to get to know Akbar!")

intro_q = input("Would you like to play this game? Y/N ")
if intro_q == "Y":
    print ("All right let's play!, choose the answer that is a LIE")
else:
    print ("Looks like you don't want to play right now, see you next time! ")
    quit()

question_prompts = [
    "(a) Akbar knows 3 languages fluently\n"
    "(b) Akbar has travelled all over the world \n"
    "(c) Akbar was born and raised in Tashkent, Uzbekistan \n\n",


    "(a) Akbar doesnt have a favorite sport and does not enjoy playing\n"
    "(b) Akbar has two lovely daughters and a beautiful wife Emily\n"
    "(c) Akbar enjoys playing video games & reading historical books\n\n ",


    "(a) Akbars dream is to take his entire family to an amazing tour of Europe\n"
    "(b) Akbar has a 4-1 W/L in amateur Kickboxing \n"
    "(c) Akbar has a fully tatted body except for his face \n\n ",

    
]

questions = [
    Question(question_prompts[0], "b"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[1], "c"),


 ]


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")
    print(" Here are the LIES:\n Akbar has only been to two countries, Uzbekistan and the US, he would love to travel more!\n "
    "Akbar actually loves playing soccer and his favorite team is Real Madrid, #Hala Madrid!\n"
    " He has absolutely no Tattoos! But it definitely is on his interest list for the future \n")
    print("Thanks for playing!")
run_test(questions)
