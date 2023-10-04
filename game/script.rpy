# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define t = Character("Technician", color="FF9900")
define a = Character("Admiral", color="#244EB0")
define b = Character("Biologist", color="#E6FF00")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    scene bg submarine1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show technician happy
    # These display lines of dialogue.


    t "This is the start of Howard's Hooligan's new Ren'Py game."

    
    scene bg submarine2
    show biologist happy

    b "Once they add in a story, pictures, and music, they can release it to the world!"


    scene bg submarine3
    show admiral normal

    a "The crew is hard at work to bring quality here."

    show admiral angry
    a "YOU HEAR THAT!? I DONT PAY YOU TO SIT AND LOOK CUTE! GET TO WORK!!"

    b "You dont pay us, period."


    scene bg submarine1
    show technician happy

    t "Ingore him, he's a stick in the mud. You can come back when we get more dialoge in here. Take care now."

    # This ends the game.

    return
