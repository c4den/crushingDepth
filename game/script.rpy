# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    # Initialize the enter_bridge variable.
    $ enter_bridge = False
    $ enter_biosphere = False
    $ enter_living_quarters = False
    $ a_angry = False
    $ qm_angry = False

define e = Character("Eileen")
define t = Character("Technician", color="FF9900")
define a = Character("Admiral", color="#244EB0")
define b = Character("Biologist", color="#E6FF00")

label inventory:
    $ rations = 30 # Count of rations
    $ power = 25 # % of power left out of 100
    $ oxygen = 100 # % of oxygen left out of 100
    $ fix_toy = False
    return

label stuff:
    $ cut_power_to_living_quarters = False
    $ cut_power_to_biosphere = False
    $ cut_power_to_command_bridge = False
    
return:



# How to access vars in inventory
# First, write call inventory in the label if its not already there
# Then you can access variables like below
# "This will show the ration amount: [rations]"
# Above will print "This will show the ration amount: 30"

# call inventory
# "This will show the ration amount: 30"
# $ rations -= 10
# "This will show the ration amount: 20"



# The game starts here.

label start:


    scene bg controlroom
    

    "The room jolts you off of your feet. The sound of a great crash and crushing metal fill your ears and everything goes dark."

    "You awake to the sound of an alarm, a red light spins and strobes a dim room from above the door to your right."

    "As you regain some sense of your whereabouts, the strain on your chest causes you to wheeze coughing as the air had been knocked from your lungs since the disorder began."

    "You were in the Communications Room to divvy out tasks, now you\’re met with blank monitors and an ear piercing alert."

    "\"WARNING! WARNING! LOW-POWER INSTANTIATED! WARNING!\""

    "Low-power, not a good sign. Low-power puts the energy remaining at about 25\%, it\’s best to use what remains wisely."

    "You are a technician aboard this ship, the only technician aboard this ship. Getting the power back to a mid-state is not going to be an easy task and what of the crash that knocked you out cold?"

    "What dangers must lurk amid the crushing depth?"    

label choice1:

    menu door_choice:
        "Try the door":
            jump choice1_door
            
        "Try to turn on the Communication Monitor System":
            jump choice1_communication_monitor_system
    
    label choice1_door:
        show bg submarine1
        "The door is sealed shut, a symptom of the Low-Power."
        jump door_choice

    label choice1_communication_monitor_system:
        show bg submarine2
        "A low hum reverberates from the whirring fans within as the system struggles to produce even a flicker among any of the screens. "
        jump choice1_done

    label choice1_done:

    "With what seems like a dead end, 3 monitors manage to come to light."

    "The left monitor portrays the Captain pacing around trying to work a device in the Communications Bridge."
    "The top middle shows the Botanist attempting to fix a steaming pipe in the Biosphere." 
    "On the right, the Quartermaster, trying but with no avail to open the door keeping him locked within."

    "You can\’t help but to let out a cough, which in turn echoes out on the loud intercom within the corner of your room."
    show tech normal at right
    t "'Hey Techy, is that you?'"

    show tech scared at right
    t "'You gotta help me out here, every door is sealed shut and not even the Lifeboat wants to turn on, I know you\’d be able to fix it.'"

    show bio normal at left
    b "'Hey Teach, there’s a bit of a problem here!'"

    show bio scared at left
    b "'If I can’t get this pipe to stop from bursting, there won\’t be any air left to spare on the sub for any of us.'"

    show admiral angry
    a "'Not an option rookies, we all know that the power will need to be cut from one of ours just to help any of our given situations."
    a "Luckily, the power will be staying right here in the Bridge as I order it to be. I trust the Technician will make…. The right call.'"

    "They all appear to be in a dire need of assistance, luckily you had last left the repair drone in the room you now occupy, which will make it easy to calibrate to the controls of the Monitor System."
    "However, as the Captain deemed correct, the energy required to operate it remotely outside the room would require an ample amount of energy consumption, not that that would be an issue were you not left in such a frugal position."

    jump decision_menu
label decision_menu:
    menu:
        "Cut power to the Living Quarters":
            "“I\’m cutting power to the Living Quarters,” you say on the intercom."
            show tech angry at right
            t "'What!? You damn traitor! I trusted your ass and now you\’re going to just leave me here? You better rethink your choices Techy!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You pull the switch, cutting power to the Living Quarters."
                    $ cut_power_to_living_quarters = True
                    $ qm_angry = True
                    jump branch1
        "Cut power to the Biosphere":
            "“I\’m cutting power to the Biosphere,” you say on the intercom."
            b "'Teach, you got to think logically about this one, if the Biosphere falls, everyone is going to die. This isn\’t a choice that you can just make lightly. Please, I\’m begging you to see reason!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You hesitantly pull the switch, cutting power to the Biosphere."
                    # Additional code or dialogue for the resulting scenario can be added here.
                    $ cut_power_to_biosphere = True
                    jump branch2

        "Cut power to the Comm. Bridge":
            "“I\’m cutting power to the Command Bridge,” you say on the intercom."
            a "'I\’d take this to be treason then Technician! I\’m allowing you to take back your words and do as I say. Besides, my daughter is in the room, would you be so callous to leave a child in the darkness?'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "With great hesitation, you pull the switch, cutting power to the Command Bridge."
                    # Additional code or dialogue for the resulting scenario can be added here.
                    $ cut_power_to_command_bridge = True
                    $ a_angry = True
                    jump branch3

label branch1:
    if cut_power_to_living_quarters:
        menu branch1_menu: 
            "Enter the Command Bridge":
                if not enter_bridge:
                    $ enter_bridge = True
                    jump entered_bridge1
                else:
                    "You\'\ve already entered the Command Bridge."
                    jump branch1

            "Enter the Biosphere":
                if not enter_biosphere:     
                    $ enter_biosphere = True
                    jump entered_biosphere1
                else:
                    "You\'\ve already entered the Biosphere"
                    jump branch1
    
    if enter_bridge and enter_biosphere:
        menu:
            "Continue to power":
                jump restore_deny_power1

label restore_deny_power1:
    # ... (rest of the code under this label)
    menu:
        "Restore":
            "You decide that the power needs to be restored, maybe things can begin to become operable once more aboard this damaged vessel."
            "“Good work Technician, I knew you’d be able to get things working once more.” The Captain takes a long hit from his cigar before coughing."
    return

label entered_bridge1:
"You enter the Command Bridge, the Captain paces back and forth, he bats an eye at the drone, but doesn’t leave much regard for it, he soon shifts to the Command Console."
"His daughter seems to be in the corner sad about her toy which seems to be of mechanical design."

"You could fix the child’s toy or the Bridge, but you won’t have the luxury to choose both, which do you decide?"
jump fix_choice1a

label fix_choice1a:
    menu:
        "Fix Toy. -5 Rations":
            "As you go inspect the toy the girl is holding, it seems to be malfunctioning, twitching even, as though it were meant to do more. Your drone reaches for the object, at first she seems startled but allows you to take it."
            "After some time and a few tools, the toy is working again as if it were brand new. She is overjoyed and thanks you graciously."
            $ fix_toy = True
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:
                jump branch1_menu
          
        "Fix Bridge. -5 Rations":
            "You go to inspect the Command Bridge, it is pulsing as if it’s struggling to turn on. The Captain sits idly by watching on as you investigate the damage. Once inside the machinery, a couple loose slots and plugs seemed to have been the case after the initial knock around and you go to plug and fit them in place once again. However, it seems without at least mid-power, the bridge won’t be able to carry out its intended functionality."
            $ fix_bridge = True
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:
                jump branch1_menu

label entered_biosphere1:
    "You enter the Biosphere, the Botanist is still struggling with his pipe problem as it spews steam from its surface."
    "Fixing the pipe might solve the oxygen problem, but the plants in the Biosphere might make up for a lot of time spent while you try to figure out how to get out of this situation."
    "Which feels like more of a fruitful decision to you?"
    jump fix_choice1b

label fix_choice1b:
    menu:
        "Fix Pipe. -5 Rations":
            "The Botanist backs away from his struggle to seal the leak while your drone inches near. With some bolts, tools, and applied heat, the steam draws its last from the choking pipe and the Oxygen level begins to steady on the meter. \"Eureka!\" the Botanist shouts in joy."
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:   
                jump branch1_menu

        "Scavenge Plants. +10 Rations":
            "Perhaps it’s a dead end to fix the broken pipe, it’s broken after all, the Botanist, to his dismay sees the drone go to snip at some of the plants, parsley, tomatoes, carrots, a variety of foods get stuffed into the open cartridge of the drone. Hopefully this was worth the cost."
            $ full_oxygen = False
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:
                jump branch1_menu

label branch2:
    if cut_power_to_biosphere:
        menu branch2_menu: 
            "Enter the Command Bridge":
                if not enter_bridge:
                    $ enter_bridge = True
                    jump entered_bridge2
                else:
                    "You\'\ve already entered the Command Bridge."
                    jump branch2

            "Enter the Living Quarters":
                if not enter_living_quarters:     
                    $ enter_living_quarters = True
                    jump entered_living_quarters2
                else:
                    "You\'\ve already entered the Living Quarters"
                    jump branch2
    
    if enter_bridge and enter_living_quarters:
        menu:
            "Continue to power":
                jump restore_deny_power2

label restore_deny_power2:
    # ... (rest of the code under this label)
    "Whoopie"
    return

label entered_bridge2:
"You enter the Command Bridge, the Captain paces back and forth, he bats an eye at the drone, but doesn’t leave much regard for it, he soon shifts to the Command Console."
"His daughter seems to be in the corner sad about her toy which seems to be of mechanical design."

"You could fix the child’s toy or the Bridge, but you won’t have the luxury to choose both, which do you decide?"
jump fix_choice2a

label fix_choice2a:
    menu:
        "Fix Toy. -5 Rations":
            "As you go inspect the toy the girl is holding, it seems to be malfunctioning, twitching even, as though it were meant to do more. Your drone reaches for the object, at first she seems startled but allows you to take it."
            "After some time and a few tools, the toy is working again as if it were brand new. She is overjoyed and thanks you graciously."
            $ fix_toy = True
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:
                jump branch2_menu
          
        "Fix Bridge. -5 Rations":
            "You go to inspect the Command Bridge, it is pulsing as if it’s struggling to turn on. The Captain sits idly by watching on as you investigate the damage."
            "Once inside the machinery, a couple loose slots and plugs seemed to have been the case after the initial knock around and you go to plug and fit them in place once again."
            "However, it seems without at least mid-power, the bridge won’t be able to carry out its intended functionality."
            $ fix_bridge = True
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:
                jump branch2_menu

label entered_living_quarters2:
    "You enter the Living Quarters, the Quartermaster is still struggling to unseal the door with the wheel at its center. The Lifeboat pod is flickering with its lights, a sign of its malfunction."
    "On the floor a radio is at a low frequency, it repeats a message over and over, but is immediately cut off before it can finish its message. Perhaps the radio will give a clue that could come handy in the future?."
    "With the state of things, you won’t be able to repair both, which do you choose?"
    jump fix_choice2b

label fix_choice2b:
    menu:
        "Fix Lifeboat. -5 Rations":
            "The Lifeboat pod is sleek and simple, one that would be easy for any inexperienced novice to understand and operate should the need ever arise to use. Though for the state it is in, this may require some careful analysis."
            "Some time passes and you identify through the drone that the AI Mainframe is damaged in the ship and that you’ll have to reroute it to a manual override. This will allow the pod to be operated without the authorization of the AI. Good as new… sort of."
            $ fix_lifeboat = True
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:   
                jump branch2_menu

        "Fix Radio. -5 Rations":
            "After some fiddling with the inside of the electronic box and rearranging some wires, the radio begins to emit a message on repeat. Numerical in nature, but otherwise useless unless you decode it. You write it down in a handy note for later."
            $ fix_radio = True
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:
                jump branch2_menu

label branch3:
    if cut_power_to_command_bridge:
        menu branch3_menu: 
            "Enter the Living Quarters":
                if not enter_living_quarters:
                    $ enter_living_quarters = True
                    jump entered_living_quarters3
                else:
                    "You\'\ve already entered the living quarters."
                    jump branch3

            "Enter the Biosphere":
                if not enter_biosphere:     
                    $ enter_biosphere = True
                    jump entered_biosphere3
                else:
                    "You\'\ve already entered the Biosphere"
                    jump branch3
    
    if enter_living_quarters and enter_biosphere:
        menu:
            "Continue to power":
                jump restore_deny_power3

label restore_deny_power3:
    # ... (rest of the code under this label)
    "Whoopie"
    return

label entered_living_quarters3:
    "You enter the Living Quarters, the Quartermaster is still struggling to unseal the door with the wheel at its center. The Lifeboat pod is flickering with its lights, a sign of its malfunction."
    "On the floor a radio is at a low frequency, it repeats a message over and over, but is immediately cut off before it can finish its message. Perhaps the radio will give a clue that could come handy in the future?."
    "With the state of things, you won’t be able to repair both, which do you choose?"
    jump fix_choice3a

label fix_choice3a:
    menu:
        "Fix Lifeboat. -5 Rations":
            "The Lifeboat pod is sleek and simple, one that would be easy for any inexperienced novice to understand and operate should the need ever arise to use. Though for the state it is in, this may require some careful analysis."
            "Some time passes and you identify through the drone that the AI Mainframe is damaged in the ship and that you’ll have to reroute it to a manual override. This will allow the pod to be operated without the authorization of the AI. Good as new… sort of."
            $ fix_lifeboat = True
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:   
                jump branch3_menu

        "Fix Radio. -5 Rations":
            "After some fiddling with the inside of the electronic box and rearranging some wires, the radio begins to emit a message on repeat. Numerical in nature, but otherwise useless unless you decode it. You write it down in a handy note for later."
            $ fix_radio = True
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:
                jump branch3_menu

label entered_biosphere3:
    "You enter the Biosphere, the Botanist is still struggling with his pipe problem as it spews steam from its surface."
    "Fixing the pipe might solve the oxygen problem, but the plants in the Biosphere might make up for a lot of time spent while you try to figure out how to get out of this situation."
    "Which feels like more of a fruitful decision to you?"
    jump fix_choice3b

label fix_choice3b:
    menu:
        "Fix Pipe. -5 Rations":
            "The Botanist backs away from his struggle to seal the leak while your drone inches near. With some bolts, tools, and applied heat, the steam draws its last from the choking pipe and the Oxygen level begins to steady on the meter. \"Eureka!\" the Botanist shouts in joy."
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:   
                jump branch3_menu

        "Scavenge Plants. +10 Rations":
            "Perhaps it’s a dead end to fix the broken pipe, it’s broken after all, the Botanist, to his dismay sees the drone go to snip at some of the plants, parsley, tomatoes, carrots, a variety of foods get stuffed into the open cartridge of the drone. Hopefully this was worth the cost."
            $ full_oxygen = False
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:
                jump branch3_menu

label task_menu:
    menu:
        "Fix Toy or Fix Radio":
            "As you fix you go inspect the toy the girl is holding, it seems to be malfunctioning, twitching even, as though it were meant to do more."
            "Your drone reaches for the object, at first she seems startled but allows you to take it."
            "After some time and few tools, the toy is working again as if it were brand new."
            "She is overjoyed and thanks you graciously."
            "You go to inspect the Comms Bridge, it is pulsing as if it\’s struggling to turn on."
            "The Captain sits idly by watching on as you investigate the damage."
            "Once inside the machinery, a couple loose slots and plugs seemed to have been the case after the initial knock around and you go to plug and fit them in place once again."
            "However, it seems without at least mid-power, the bridge won\’t be able to carry out its intended functionality."
            return
        "Fix Pipe or Scavenge Plants for Food":
            "The Botanist backs away from his struggle to seal the leak while your drone inches near."
            "With some bolts, tools, and applied heat, the steam draws its last from the choking pipe and the Oxygen level begins to steady on the meter."
            "“Eureka!” the Botanist shouts in joy."
            "Perhaps it\’s a dead end to fix the broken pipe, it\’s broken after all, the Botanist, to his dismay sees the drone go to snip at some of the plants, parsley, tomatoes, carrots, a variety of foods get stuffed into the open cartridge of the drone."
            "Hopefully this was worth the cost."
            return
        "Fix Radio or Lifeboat":
            "You offer to the Quartermaster to fix the radio, he stops pacing and hands it to you curiously."
            "After some fiddling with the inside of the electronic box and rearranging some wires, the radio begins to emit a message on repeat."
            "Numerical in nature, but otherwise useless unless you decode it."
            "You write it down in a handy note for later."
            "“Eck! It was useless after all…” the Quartermaster scowls in disappointment."
            "The Lifeboat pod is sleek and simple, one that would be easy for any inexperienced novice to understand and operate should the need ever arise to use."
            "Though for the state it is in, this may require some careful analysis."
            "Some time passes and you identify through the drone that the AI Mainframe is damaged in the ship and that you’ll have to reroute it to a manual override."
            "This will allow the pod to be operated without the authorization of the AI."
            "Good as new… sort of."
            return
        "Restore or Deny Power":
            menu:
                "Branch 1: Restore":
                    "You decide that the power needs to be restored, maybe things can begin to become operable once more aboard this damaged vessel."
                    "Good work Technician, I knew you\’d be able to get things working once more.” The Captain takes a long hit from his cigar before coughing"
                    "(If the Command Bridge works): You notice the Captain goes to respond to something coming from the Command Bridge, however there is interference through the monitors for you to be able to tell what\’s being heard." 
                    "Leave him to his privacy"
                    "Enter room with drone Upon entering you hear words that catch your attention, “deep-sea monster”, “suicide mission”, “bomb”. These words catch your attention the most. The Captain goes berserk and shoots rounds into the Command Bridge." 
                    "“I have my daughter on board you sick bastards!” he screams in anger before sulking over, catching himself upon the edge of the console before crying and catching himself in a seat. His daughter remained startled in the far edge of the room."
                    "The Botanist speaks out loud to the monitor, “I knew you had it in you Teach!” he says pridefully."
#(if the pipe is fixed: “Now let’s go see what is really going on out there.”) (if the pipe is broken: “I’d celebrate but I can’t stand idly while this is still broken, it’s not steaming as much now which is a really bad sign that the oxygen may have depleted too much already.” He continues to find a solution to the pipe.)
                    return
                "Branch 2: Deny":
                    "You decide that things should stay depowered until you have had a chance to make sure the rest of the submersible is in working condition before turning everything back on just in case."
                    "You decide that the power needs to be restored. The ship's systems begin to whir to life, illuminating the corridors and bringing hope to the crew."
                    return
                "Branch 2: Deny":
                    "You decide against restoring power. It's too risky and might jeopardize the other systems further. The crew remains in the dimly lit conditions, relying on emergency lights."
                    return
                "Branch 3: Delay Decision":
                    "You're not certain what the best course of action is. Perhaps you should consult with the crew or assess the damage further before making a decision."
                    return

