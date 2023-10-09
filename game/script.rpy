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
    # These display lines of dialogue.

    # INTRO

    "The room jolts you off of your feet. The sound of a great crash and crushing metal fill your ears and everything goes dark."

    "You awake to the sound of an alarm, a red light spins and strobes a dim room from above the door to your right."

    "As you regain some sense of your whereabouts, the strain on your chest causes you to wheeze coughing as the air had been knocked from your lungs since the disorder began."

    "You were in the Communications Room to divvy out tasks, now you’re met with blank monitors and an ear piercing alert."

    "\"WARNING! WARNING! LOW-POWER INSTANTIATED! WARNING!\""

    "Low-power, not a good sign. Low-power puts the energy remaining at about 25\%, it’s best to use what remains wisely."

    "You are a technician aboard this ship, the only technician aboard this ship. Getting the power back to a mid-state is not going to be an easy task and what of the crash that knocked you out cold?"

    "What dangers must lurk amid the crushing depth?"    

    menu:
        "Try the door":
            jump door
            
        "Try to turn on the Communication Monitor System":
            jump communication_monitor_system
    
label door:

    "The door is sealed shut, a symptom of the Low-Power."


label communication_monitor_system:

    "A low hum reverberates from the whirring fans within as the system struggles to produce even a flicker among any of the screens. "










    # scene bg submarine2
    # show biologist happy

    # b "Once they add in a story, pictures, and music, they can release it to the world!"


    # scene bg submarine3
    # show admiral normal

    # a "The crew is hard at work to bring quality here."

    # show admiral angry
    # a "YOU HEAR THAT!? I DONT PAY YOU TO SIT AND LOOK CUTE! GET TO WORK!!"

    # b "You dont pay us, period."


    # scene bg submarine1
    # show technician happy

    # t "Ingore him, he's a stick in the mud. You can come back when we get more dialoge in here. Take care now."

    # This ends the game.

    return
