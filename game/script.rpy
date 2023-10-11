# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")
define t = Character("Technician", color="FF9900")
define a = Character("Admiral", color="#244EB0")
define b = Character("Biologist", color="#E6FF00")

# The game starts here.

label start:


    scene bg controlroom

    "The room jolts you off of your feet. The sound of a great crash and crushing metal fill your ears and everything goes dark."

    "You awake to the sound of an alarm, a red light spins and strobes a dim room from above the door to your right."

    "As you regain some sense of your whereabouts, the strain on your chest causes you to wheeze coughing as the air had been knocked from your lungs since the disorder began."

    "You were in the Communications Room to divvy out tasks, now you’re met with blank monitors and an ear piercing alert."

    "\"WARNING! WARNING! LOW-POWER INSTANTIATED! WARNING!\""

    "Low-power, not a good sign. Low-power puts the energy remaining at about 25\%, it’s best to use what remains wisely."

    "You are a technician aboard this ship, the only technician aboard this ship. Getting the power back to a mid-state is not going to be an easy task and what of the crash that knocked you out cold?"

    "What dangers must lurk amid the crushing depth?"    

label choice1:

    menu:
        "Try the door":
            jump choice1_door
            
        "Try to turn on the Communication Monitor System":
            jump choice1_communication_monitor_system
    
    label choice1_door:
        show bg submarine1
        "The door is sealed shut, a symptom of the Low-Power."
        jump choice1_done

    label choice1_communication_monitor_system:
        show bg submarine2
        "A low hum reverberates from the whirring fans within as the system struggles to produce even a flicker among any of the screens. "
        jump choice1_done

    label choice1_done:

    "With what seems like a dead end, 3 monitors manage to come to light. The left monitor portrays the Captain pacing around trying to work a device in the Communications Bridge. The top middle shows the Botanist attempting to fix a steaming pipe in the Biosphere. On the right, the Quartermaster, trying but with no avail to open the door keeping him locked within."

    "You can’t help but to let out a cough, which in turn echoes out on the loud intercom within the corner of your room."
    t "'Hey Techy, is that you?'"
    t "'You gotta help me out here, every door is sealed shut and not even the Lifeboat wants to turn on, I know you’d be able to fix it.'"

    b "'Hey Teach, there’s a bit of a problem here!'"
    b "'If I can’t get this pipe to stop from bursting, there won’t be any air left to spare on the sub for any of us.'"

    a "'Not an option rookies, we all know that the power will need to be cut from one of ours just to help any of our given situations. Luckily, the power will be staying right here in the Bridge as I order it to be. I trust the Technician will make…. The right call.'"

    "They all appear to be in a dire need of assistance, luckily you had last left the repair drone in the room you now occupy, which will make it easy to calibrate to the controls of the Monitor System. However, as the Captain deemed correct, the energy required to operate it remotely outside the room would require an ample amount of energy consumption, not that that would be an issue were you not left in such a frugal position."

    jump decision_menu

label decision_menu:
    menu:
        "Cut power to the Living Quarters":
            "“I’m cutting power to the Living Quarters,” you say on the intercom."
            t "'What!? You damn traitor! I trusted your ass and now you’re going to just leave me here? You better rethink your choices Techy!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You pull the switch, cutting power to the Living Quarters."
                    # Additional code or dialogue for the resulting scenario can be added here.

        "Cut power to the Biosphere":
            "“I’m cutting power to the Biosphere,” you say on the intercom."
            b "'Teach, you got to think logically about this one, if the Biosphere falls, everyone is going to die. This isn’t a choice that you can just make lightly. Please, I’m begging you to see reason!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You hesitantly pull the switch, cutting power to the Biosphere."
                    # Additional code or dialogue for the resulting scenario can be added here.

        "Cut power to the Comm. Bridge":
            "“I’m cutting power to the Command Bridge,” you say on the intercom."
            a "'I’d take this to be treason then Technician! I’m allowing you to take back your words and do as I say. Besides, my daughter is in the room, would you be so callous to leave a child in the darkness?'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "With great hesitation, you pull the switch, cutting power to the Command Bridge."
                    # Additional code or dialogue for the resulting scenario can be added here.

    return

