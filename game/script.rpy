# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define n = Character("")
define j = Character("Johanna")
define y = Character(_("You"), color="#c8c8ff")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene office

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    n "You have been interviewing people all day and honstly you feel exhausted. None of the canditates feel good fit for the role."

    n "\"Only one more person and then I can go home and sleep.\" You think"

    n "You call the last person in"

    show default

    menu:

        j "Hi! I'm Johanna! Thank you for having me."

        "Nice to meet you. Would you tell me about yourself?":
            jump nice1

        "Oh god, that is so cliche and I don't like your face. Please leave":
            jump instadeath

label nice1:

    j "I'm third year software engineering student who likes to tinker with things and who likes to be useful rather than sit around doing nothing."

    hide default
    show happy
    # joe smiles widley

    j "I'm also a really good baker."

    menu:
        "Damn, that's a boring answer":
            jump offended

        "Well, good to know. Though bakers are not really what we are looking for":
            jump baker

label instadeath:

    hide default
    #joe turns angry
    show angry

    j "Well that's just rude! I don't want to come work here anyway if the environment is this toxic!"

    #joe leaves

    hide angry
    n "Johanna leaves the interview"

    n "You lost."

    # This ends the game.

    return

label offended:

    #joe becomes offended
    hide happy
    show angry

    j "Well, I'm sorry if I don't happen to do base jumping on weekly bases."
    hide angry
    show default
    jump education

label baker:

    hide happy
    show nervous
    #joe becomes nervous

    j "Haha, I just thought it might break the ice a little bit"
    hide nervous
    show default
    jump education

label education:


    menu:
        "Tell me more about your education and what you can do":
            jump ed2

label ed2:

    #joe returns default

    j "Well, I am now doing my third year, which means that all the basic programming courses are behind me."

    j "I know how to code with c++, java, python and javascript"

    #joe smiles widely
    hide default
    show happy

    j "I'm also quite handy with SQL. Especially now that I've needed to use that in working life."

    menu:
        "We don't want those kinds of skills. Sorry, but you can go.":
            jump death2

        "Care to elaborate?":
            jump work

label work:

    hide happy
    show default
    j "I started as an application specialist trainee in CGI in may 2023. As a part of my job I needed to do database searches using SQL."

    menu:
        "Ok. How confident are you with your coding skills?":
            jump coding

        "Yeah, no. Not a set of skill we want":
            jump death2

label death2:

    hide default
    hide happy
    show nervous
    #joe turns sad
    j "Oh, well I'm sorry to hear that."
    hide nervous
    show default
    j "If you change your mind, you can contact me with email: jonsku022@gmail.com."
    #joe leaves
    hide default

    n "Johanna leaves"

    n "You pack your stuff and go home."

    n "You sleep very poorly that night. Your gut is telling that you missed a possibility to hire a great employee."

    n "Game over"

    return

label coding:
    #turns nervous
    hide default
    show nervous

    j "Heh, well I'm more confident that what I was when I started"

    hide nervous
    show default
    #turns normal

    j "But yeah, I'm quite confident with the basics but I do not know those languages by heart."

    j "So far though I have always manged to complete all projects I have had to do for school. I've found out that asking advice from a another person or googling really helps a lot."

    menu:
        "We are not looking for rookies. All our hires need to be god-level coders.":
            jump death2

        "That's good. We hold teamwork in high regards here":
            jump good

label good:

    menu:
        "Few questions more and then I think were are done":
            jump questions

label questions:
    menu:
        "Why should we hire you?":
            jump hire1

        "What are your salary expatation?":
            jump salary1

label hire1:
    j "Well, I'm very diligent worker so you know I'll show up and do what is required from me. I speak both English and Finnish fluently. I know basics of coding and I'm keen to always learn more."

    hide default
    show happy
    #joe smiles widely
    j"I'm also very cheery co-worker"

    menu:
        "Hmm, I would have hoped for something more original. You do know we have hundreds of applications for this position.":
            jump hundreds

        "Okey, then what are your salary expatations?":
            jump salary2

label hundreds:
    #Looks nervous
    hide happy
    show nervous
    j "Oh, sorry. It's hard to stand out nowadays"
    hide nervous
    show default
    menu:
        "What are your salary expetation?":
            jump salary2


label salary2:
    #returns defaul
    hide happy
    show default
    j "Well, I don't have too much knowledge, but engineering union says that a person who has at least 150 credits should have a salary between  2 500 – 2 800€ and a person who has a little bit of experience should have a salary of  3 300€."
    j "Since my studies are not yet complete but I do have some experience, I would expect somewhere around the 2900€"
    j "But I'm willing to hear what you can offer"

    hide default
    show happy
    #smiles widely

    j"Especially if you offer more. Haha"

    menu:
        "Yeah, no. Not happening. Learn to be more humble lady.":
            jump over
        "Okey, we'll see what we usually offer for people in this position with similar background as you.":
            jump hireme

label over:
    #turns angry
    hide happy
    show angry
    j"You could have just politelty say what you usually offer. I'm just trying to make my way in this world and women often underestimate their worth."
    #turns normal
    hide angry
    show default
    j"If you happen to change your mind, you can contact me with email: jonsku022@gmail.com."
    hide default
    n"Johanna leaves"
    n"You pack your packs and go home. You are unable to sleep well, knowing you let a great employee slip through your fingers"
    n"Game over"

    return

label hireme:
    #turns normal
    hide happy
    show default
    menu:
        "Thank you for the interview. We would love to hire you! Could you please give me your contact information so we can be in touch!":
            jump contacts

label contacts:

    hide default
    show happy
    j"Oh that's amazing! My email is: jonsku022@gmail.com. That is the most sure way to reach me."

    hide happy
    show default
    j"Thank you for the interwiev. I can't wait to start working here!"

    hide default
    n"Johanna leaves"

    n"You stand up and start to pack your stuff being happy that you have found your new employee. Now you can finally go home and sleep well."

    n"Game over"

    return

label salary1:
    #returns defaul
    show default
    j "Well, I don't have too much knowledge, but engineering union says that a person who has at least 150 credits should have a salary between  2 500 – 2 800€ and a person who has a little bit of experience should have a salary of  3 300€."
    j "Since my studies are not yet complete but I do have some experience, I would expect somewhere around the 2900€"
    j "But I'm willing to hear what you can offer"

    #smiles widely
    hide default
    show happy

    j"Especially if you offer more. Haha"

    menu:
            "Yeah, no. Not happening. Learn to be more humble lady.":
                jump over

            "Okey, we'll see what we usually offer for people in this position with similar background as you.":
                jump hire2



label hire2:
    hide happy
    show default
    menu:
        "For the last question, why should we hire you?":
            jump hi

label hi:
    j "Well, I'm very diligent worker so you know I'll show up and do what is required from me. I speak both English and Finnish fluently. I know basics of coding and I'm keen to always learn more."
    hide default
    show happy
    #joe smiles widely
    j"I'm also very cheery co-worker"

    menu:
        "Hmm, I would have hoped for something more original. You do know we have hundreds of applications for this position.":
            jump hundreds2
        "That sounds great!":
            jump hireme


label hundreds2:
    #Looks nervous
    hide happy
    show nervous
    j "Oh, sorry. It's hard to stand out nowadays"
    hide nervous
    jump hireme