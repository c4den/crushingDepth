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

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    t "This is the start of Howard's Hooligan's new Ren'Py game."

    b "Once you add a story, pictures, and music, you can release it to the world!"

    a "So quit your lallygagging and GET TO WORK CREW!!"

    # This ends the game.

    return
