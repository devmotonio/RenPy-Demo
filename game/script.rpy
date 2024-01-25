define i = Character('Interviewer', color="#ff8888")
define c = Character('Candidate', color="#0000ff")

label start:

    show interviewer default

    i "Hello! Welcome to the interview. Before we start, I want to ask you: if you were an animal, what would you be?"

    hide interviewer
    with pixellate
    show candidate default

    c "Hi! What an unusual question! I think I would be a wolf. I've always liked the idea of working as a team, howling at the moon, and of course I love good meat."

    hide candidate
    show interviewer default

    i "Interesting choice! Teamwork is key. Seriously now, what do you think is your greatest strength?"

    hide interviewer
    show candidate default

    c "I'd say it's my ability to turn coffee into code. Or would it be the other way around? Either way, I keep things going with just the right dose of caffeine."

    hide candidate
    show interviewer default

    i "Coffee is the powerhouse of many offices, to be sure. What about its weaknesses?"

    hide interviewer
    show candidate default

    c "Oh, I'm completely vulnerable to cakes. If anyone brings a chocolate cake to the company, forget about any deadlines. I'm officially out of commission."

    hide candidate
    show interviewer default

    i "Noted. Chocolate cake is your Kryptonite. Changing the subject a little, how do you deal with tight deadlines?"

    hide interviewer
    show candidate default

    c "Tight deadlines are like the monsters under the bed. You just need to laugh at them and keep working. Or, of course, cry a little in the bathroom if necessary."

    hide candidate
    show interviewer default

    i "Laughing at deadlines, good strategy! And what motivated you to apply for this job?"
    
    hide interviewer
    show candidate default

    c "Well, I heard you guys have a state-of-the-art coffee machine here. And of course, the opportunity to work with a brilliant mind like mine."

    hide candidate
    show interviewer default

    i "The coffee machine is really amazing. As for the brilliant mind, we'll see. Last question: where do you see yourself in five years?"

    hide interviewer
    show candidate default

    c "Ah, in five years I see myself taking a nap in the break room, because, like I said, chocolate cake is my weakness and will probably have won the office by now."

    hide candidate
    show interviewer default

    i "Sounds like a solid plan! Thanks for stopping by, we'll review your interview and get back to you. Good luck with the chocolate cake!"

    hide interviewer
    show candidate default

    c "Thank you! I can't wait to sink into work (and cake) here. See you later!"