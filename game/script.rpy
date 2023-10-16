# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


init python:
    class Inventory():
        def __init__(self, items, number_of_items):
            self.items = items
            self.number_of_items = number_of_items

        def add_item(self, item):
            self.items.append(item)
            self.number_of_items += 1

        def remove_item(self, item):
            self.items.remove(item)
            self.number_of_items -= 1


    class InventoryItem():
        def __init__(self, name):
            self.name = name
            

init:
    # Initialize the enter_bridge variable.
    $ enter_bridge = False
    $ enter_biosphere = False
    $ enter_living_quarters = False
    $ a_angry = False
    $ qm_angry = False
    $ rations = 30 # Count of rations
    $ power = 25 # % of power left out of 100
    $ oxygen = 100 # % of oxygen left out of 100
    $ fix_toy = False
    $ fix_bridge = False
    $ fix_pipe = False
    $ fix_lifeboat = False
    $ full_oxygen = True
    $ sonar_device = False
    $ deep_sea_suit = False
    $ captains_log = False
    $ note = False
    $ radio = False
    $ low_power = True
    $ depleted_rations = False
    $ finish_game = False
    define ending_1 = False
    define ending_2 = False
    define ending_3 = False
    define good_points = 0
    define bad_points = 0
    define neutral_points = 0
    define evil_points = 0
    default inventory = Inventory([], 0)
    define repair_drone = InventoryItem("Repair Drone")
    define sonar_device = InventoryItem("Sonar Device")
    define deep_sea_suit = InventoryItem("Deep Sea Suit")
    define captains_log = InventoryItem("Captain\'s Log")
    define note = InventoryItem("Note")
    define radio = InventoryItem("Radio")
    define toy = InventoryItem("Toy")
       

define p = Character("Player")
define q = Character("Quartermaster", color="FF9900")
define a = Character("Captain", color="#244EB0")
define b = Character("Botanist", color="#E6FF00")
define c = Character("Child", color="")

image repair_drone_img = "UI/repair_drone.png"
image sonar_device_img = "UI/sonar_device.png"
image deep_sea_suit_img = "UI/sea_suit.png"
image captains_log_img = "UI/captains_log.png"
image note_img = "UI/note.png"
image radio_img = "UI/radio.png"
image toy_img = "UI/toy.png"
image gun = "UI/gun.png"


label stuff:
    $ cut_power_to_living_quarters = False
    $ cut_power_to_biosphere = False
    $ cut_power_to_command_bridge = False
    
return:



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
        "The door is sealed shut, a symptom of the Low-Power."
        jump door_choice

    label choice1_communication_monitor_system:
        "A low hum reverberates from the whirring fans within as the system struggles to produce even a flicker among any of the screens. "
        jump choice1_done

    label choice1_done:

    "With what seems like a dead end, 3 monitors manage to come to light."

    "The left monitor portrays the Captain pacing around trying to work a device in the Communications Bridge."
    "The top middle shows the Botanist attempting to fix a steaming pipe in the Biosphere." 
    "On the right, the Quartermaster, trying but with no avail to open the door keeping him locked within."

    "You can\’t help but to let out a cough, which in turn echoes out on the loud intercom within the corner of your room."
    show quartermaster normal at right
    q "'Hey Techy, is that you?'"

    q "'You gotta help me out here, every door is sealed shut and not even the Lifeboat wants to turn on, I know you\’d be able to fix it.'"

    show botanist normal
    b "'Hey Teach, there’s a bit of a problem here!'"

    b "'If I can’t get this pipe to stop from bursting, there won\’t be any air left to spare on the sub for any of us.'"

    show captain worried at left
    a "'Not an option rookies, we all know that the power will need to be cut from one of ours just to help any of our given situations."

    a "Luckily, the power will be staying right here in the Bridge as I order it to be. I trust the Technician will make…. The right call.'"

    "They all appear to be in a dire need of assistance, luckily you had last left the repair drone in the room you now occupy, which will make it easy to calibrate to the controls of the Monitor System."
    
    $ inventory.add_item(repair_drone)
    # HIDE INVENTORY
    # ============================================================
    hide sonar_device_img
    hide deep_sea_suit_img
    hide captains_log_img
    hide note_img
    hide radio_img
    hide toy_img
    # ============================================================

    # SHOW INVENTORY
    # ============================================================
    $ itemCount = inventory.number_of_items - 1
    $ xPos = 0.1

    while itemCount >= 0:
        if inventory.items[itemCount].name == "Repair Drone":
            show repair_drone_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Sonar Device":
            show sonar_device_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Deep Sea Suit":
            show deep_sea_suit_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Captain\'s Log":
            show captains_log_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Note":
            show note_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Radio":
            show radio_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        if inventory.items[itemCount].name == "Toy":
            show toy_img:
                xalign xPos yalign 0.01
                xysize(100,100)

        $ xPos += 0.125
        $ itemCount -= 1
    # ============================================================
    "However, as the Captain deemed correct, the energy required to operate it remotely outside the room would require an ample amount of energy consumption, not that that would be an issue were you not left in such a frugal position."



    jump decision_menu


show quartermaster at right
show botanist normal
show captain worried at left
label decision_menu:
    menu:
        
        "Cut power to the Living Quarters":
            "“I\’m cutting power to the Living Quarters,” you say on the intercom."
            show quartermaster angry at right
            q "'What!? You damn traitor! I trusted your ass and now you\’re going to just leave me here? You better rethink your choices Techy!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You pull the switch, cutting power to the Living Quarters."
                    hide quartermaster
                    hide botanist
                    hide captain
                    $ cut_power_to_living_quarters = True
                    $ qm_angry = True
                    jump branch1

        "Cut power to the Biosphere":
            "“I\’m cutting power to the Biosphere,” you say on the intercom."
            show botanist angry
            b "'Teach, you got to think logically about this one, if the Biosphere falls, everyone is going to die. This isn\’t a choice that you can just make lightly. Please, I\’m begging you to see reason!'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "You hesitantly pull the switch, cutting power to the Biosphere."
                    # Additional code or dialogue for the resulting scenario can be added here.
                    hide quartermaster
                    hide botanist
                    hide captain
                    $ cut_power_to_biosphere = True
                    jump branch2

        "Cut power to the Comm. Bridge":
            "“I\’m cutting power to the Command Bridge,” you say on the intercom."
            show captain angry at left
            a "'I\’d take this to be treason then Technician! I\’m allowing you to take back your words and do as I say. Besides, my daughter is in the room, would you be so callous to leave a child in the darkness?'"
            menu:
                "Return to deciding":
                    jump decision_menu
                "Cut the power":
                    "With great hesitation, you pull the switch, cutting power to the Command Bridge."
                    # Additional code or dialogue for the resulting scenario can be added here.
                    hide quartermaster
                    hide botanist
                    hide captain
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
            
            show captain happy
            a "Good work Technician, I knew you’d be able to get things working once more."
            hide captain
            "The Captain takes a long hit from his cigar before coughing."
        
            $ power += 25
            $ low_power = False
            $ med_power = True
            "You notice the Captain goes to respond to something coming from the Command Bridge, however there is interference through the monitors for you to be able to tell what’s being heard."
            if fix_bridge:
                menu:
                    "Enter Room with Drone":
                        "Upon entering you hear words that catch your attention, deep-sea monster, suicide mission, bomb. These words catch your attention the most."
                        "The Captain goes berserk and shoots rounds into the Command Bridge."
                        show captain angry
                        a "I have my daughter on board you sick bastards!"
                        "He then starts to sulk over, catching himself upon the edge of the console before crying and catching himself in a seat."
                        "His daughter remained startled in the far edge of the room."
                        hide captain
            "The Botanist speaks out loud to the monitor"
            show botanist normal
            b "I knew you had it in you Teach!"
            "He said that with so much pride"
            hide botanist
            if fix_pipe:
                "Now let’s go see what is really going on out there."
            if not full_oxygen:
                "I can’t stand idly while this is still broken, it’s not steaming as much now which is a really bad sign that the oxygen may have depleted too much already. He continues to find a solution to the pipe."
            jump status_branch1
        "Deny":
            $ a_angry = True
            "You decide that things should stay depowered until you have had a chance to make sure the rest of the submersible is in working condition before turning everything back on just in case."
            show captain angry
            a "You traitor! I ordered you to turn things on to mid-power!"
            "The Captain angrily storms out of the room shooting the console before storming off the monitor. His daughter also leaves the edge of the monitor to follow after him."
            hide captain
            "The Botanist looks around and sighs."
            show botanist normal
            b "Well there could in fact be things aboard the ship that could be in danger if turned back up to mid-power, good call I suppose."
            "He nods in agreement."
            hide botanist
            
            if fix_pipe:
                "Now let’s go see what is really going on out there."
            if not full_oxygen:
                "I can’t stand idly while this is still broken, it’s not steaming as much now which is a really bad sign that the oxygen may have depleted too much already. He continues to find a solution to the pipe."
            jump status_branch1
label entered_bridge1:

show bg helm
show captain worried
show toy at left


"You enter the Command Bridge, the Captain paces back and forth, he bats an eye at the drone, but doesn’t leave much regard for it, he soon shifts to the Command Console."
"His daughter seems to be in the corner sad about her toy which seems to be of mechanical design."

"You could fix the child’s toy or the Bridge, but you won’t have the luxury to choose both, which do you decide?"
jump fix_choice1a

label fix_choice1a:
    menu:
        "Fix Toy. -5 Rations (Current rations: [rations])":
            show captain happy
            "As you go inspect the toy the girl is holding, it seems to be malfunctioning, twitching even, as though it were meant to do more. Your drone reaches for the object, at first she seems startled but allows you to take it."
            "After some time and a few tools, the toy is working again as if it were brand new. She is overjoyed and thanks you graciously."
            hide captain
            hide toy
            $ fix_toy = True
            $ inventory.add_item(toy)
            # HIDE INVENTORY
            # ============================================================
            hide sonar_device_img
            hide deep_sea_suit_img
            hide captains_log_img
            hide note_img
            hide radio_img
            hide toy_img
            # ============================================================

            # SHOW INVENTORY
            # ============================================================
            $ itemCount = inventory.number_of_items - 1
            $ xPos = 0.1

            while itemCount >= 0:
                if inventory.items[itemCount].name == "Repair Drone":
                    show repair_drone_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Sonar Device":
                    show sonar_device_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Deep Sea Suit":
                    show deep_sea_suit_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Captain\'s Log":
                    show captains_log_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Note":
                    show note_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Radio":
                    show radio_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Toy":
                    show toy_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                $ xPos += 0.125
                $ itemCount -= 1
            # ============================================================
            $ rations -= 5
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:
                jump branch1_menu
          
        "Fix Bridge. -5 Rations (Current rations: [rations])":
            "You go to inspect the Command Bridge, it is pulsing as if it’s struggling to turn on. The Captain sits idly by watching on as you investigate the damage." 
            "Once inside the machinery, a couple loose slots and plugs seemed to have been the case after the initial knock around and you go to plug and fit them in place once again."
            "However, it seems without at least mid-power, the bridge won’t be able to carry out its intended functionality."
            hide captain
            hide toy
            $ fix_bridge = True
            $ rations -= 5
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:
                jump branch1_menu

label entered_biosphere1:
    
    show bg biodome
    show botanist angry

    "You enter the Biosphere, the Botanist is still struggling with his pipe problem as it spews steam from its surface."
    "Fixing the pipe might solve the oxygen problem, but the plants in the Biosphere might make up for a lot of time spent while you try to figure out how to get out of this situation."
    "Which feels like more of a fruitful decision to you?"
    jump fix_choice1b

label fix_choice1b:
    menu:
        "Fix Pipe. -5 Rations (Current rations: [rations])":
            $ rations -= 5
            "The Botanist backs away from his struggle to seal the leak while your drone inches near. With some bolts, tools, and applied heat, the steam draws its last from the choking pipe and the Oxygen level begins to steady on the meter."
            show botanist normal
            b " Eureka! This brings me much joy."
            hide botanist
            if enter_bridge and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power1
            else:   
                jump branch1_menu

        "Scavenge Plants. +10 Rations (Current rations: [rations])":
            $ rations += 10
            "Perhaps it’s a dead end to fix the broken pipe, it’s broken after all, the Botanist, to his dismay sees the drone go to snip at some of the plants, parsley, tomatoes, carrots, a variety of foods get stuffed into the open cartridge of the drone."
            "Hopefully this was worth the cost."
            hide botanist
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
    menu:
        "Restore":
            "You decide that the power needs to be restored, maybe things can begin to become operable once more aboard this damaged vessel."

            show captain happy
            a "Good work Technician, I knew you’d be able to get things working once more."
            hide captain
            "The Captain takes a long hit from his cigar before coughing."
            $ power += 25
            $ low_power = False
            $ med_power = True
            "You notice the Captain goes to respond to something coming from the Command Bridge, however there is interference through the monitors for you to be able to tell what’s being heard."
            if fix_bridge:
                menu:
                    "Enter Room with Drone":
                        "Upon entering you hear words that catch your attention, deep-sea monster, suicide mission, bomb. These words catch your attention the most."
                        show captain angry
                        a "I have my daughter on board you sick bastards!"
                        "He then starts to sulk over, catching himself upon the edge of the console before crying and catching himself in a seat."
                        "His daughter remained startled in the far edge of the room."
                        hide captain
            show quartermaster normal
            q "Nice work Techy! Now then let’s do good on our part and work on getting the hell off this coffin! I'll grab my tools."
            hide quartermaster
                
            jump status_branch1
        "Deny":
            $ a_angry = True
            $ qm_angry = True
            "You decide that things should stay depowered until you have had a chance to make sure the rest of the submersible is in working condition before turning everything back on just in case."
            show captain angry
            a "You traitor! I ordered you to turn things on to mid-power!"
            "The Captain angrily storms out of the room shooting the console before storming off the monitor. His daughter also leaves the edge of the monitor to follow after him."
            hide captain
            show quartermaster angry
            q "Techy, what the actual hell?! You were supposed to turn everything back on you son of a-"
            "He stops himself before finishing."
            q "“I knew better than to trust a bastard like you and I did anyway, hope you ain’t thinking about returning over here you dumb fool.”"
            "The Quartermaster punches the door before nearly breaking his hand, he squirms off holding it, too far to be seen from the monitor."
            hide quartermaster
        
            jump status_branch1

label entered_bridge2:

    show bg helm
    show captain worried
    show toy at left

    "You enter the Command Bridge, the Captain paces back and forth, he bats an eye at the drone, but doesn’t leave much regard for it, he soon shifts to the Command Console."
    "His daughter seems to be in the corner sad about her toy which seems to be of mechanical design."

    "You could fix the child’s toy or the Bridge, but you won’t have the luxury to choose both, which do you decide?"
    jump fix_choice2a

label fix_choice2a:
    menu:
        "Fix Toy. -5 Rations (Current rations: [rations])":
            show captain happy
            "As you go inspect the toy the girl is holding, it seems to be malfunctioning, twitching even, as though it were meant to do more. Your drone reaches for the object, at first she seems startled but allows you to take it."
            "After some time and a few tools, the toy is working again as if it were brand new. She is overjoyed and thanks you graciously."
            hide captain
            hide toy
            $ fix_toy = True
            $ inventory.add_item(toy)
            # HIDE INVENTORY
            # ============================================================
            hide sonar_device_img
            hide deep_sea_suit_img
            hide captains_log_img
            hide note_img
            hide radio_img
            hide toy_img
            # ============================================================

            # SHOW INVENTORY
            # ============================================================
            $ itemCount = inventory.number_of_items - 1
            $ xPos = 0.1

            while itemCount >= 0:
                if inventory.items[itemCount].name == "Repair Drone":
                    show repair_drone_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Sonar Device":
                    show sonar_device_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Deep Sea Suit":
                    show deep_sea_suit_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Captain\'s Log":
                    show captains_log_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Note":
                    show note_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Radio":
                    show radio_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Toy":
                    show toy_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                $ xPos += 0.125
                $ itemCount -= 1
            # ============================================================
            $ rations -= 5
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:
                jump branch2_menu
          
        "Fix Bridge. -5 Rations (Current rations: [rations])":
            "You go to inspect the Command Bridge, it is pulsing as if it’s struggling to turn on. The Captain sits idly by watching on as you investigate the damage."
            "Once inside the machinery, a couple loose slots and plugs seemed to have been the case after the initial knock around and you go to plug and fit them in place once again."
            "However, it seems without at least mid-power, the bridge won’t be able to carry out its intended functionality."
            hide captain
            hide toy
            $ fix_bridge = True
            $ rations -= 5
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:
                jump branch2_menu

label entered_living_quarters2:

    show bg quarters
    show quartermaster angry
    show radio at left

    "You enter the Living Quarters, the Quartermaster is still struggling to unseal the door with the wheel at its center. The Lifeboat pod is flickering with its lights, a sign of its malfunction."
    "On the floor a radio is at a low frequency, it repeats a message over and over, but is immediately cut off before it can finish its message. Perhaps the radio will give a clue that could come handy in the future?."
    "With the state of things, you won’t be able to repair both, which do you choose?"
    jump fix_choice2b

label fix_choice2b:
    menu:
        "Fix Lifeboat. -5 Rations (Current rations: [rations])":
            show quartermaster normal
            "The Lifeboat pod is sleek and simple, one that would be easy for any inexperienced novice to understand and operate should the need ever arise to use. Though for the state it is in, this may require some careful analysis."
            hide quartermaster
            hide radio
            "Some time passes and you identify through the drone that the AI Mainframe is damaged in the ship and that you’ll have to reroute it to a manual override. This will allow the pod to be operated without the authorization of the AI. Good as new… sort of."
            $ fix_lifeboat = True
            $ rations -= 5
            if enter_bridge and enter_living_quarters:
                    menu:
                        "Continue to power":
                            jump restore_deny_power2
            else:   
                jump branch2_menu

        "Fix Radio. -5 Rations (Current rations: [rations])":
            "After some fiddling with the inside of the electronic box and rearranging some wires, the radio begins to emit a message on repeat. Numerical in nature, but otherwise useless unless you decode it. You write it down in a handy note for later."
            hide quartermaster
            hide radio
            $ fix_radio = True
            $ evil_points += 1
            $ inventory.add_item(note)
            # HIDE INVENTORY
            # ============================================================
            hide sonar_device_img
            hide deep_sea_suit_img
            hide captains_log_img
            hide note_img
            hide radio_img
            hide toy_img
            # ============================================================

            # SHOW INVENTORY
            # ============================================================
            $ itemCount = inventory.number_of_items - 1
            $ xPos = 0.1

            while itemCount >= 0:
                if inventory.items[itemCount].name == "Repair Drone":
                    show repair_drone_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Sonar Device":
                    show sonar_device_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Deep Sea Suit":
                    show deep_sea_suit_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Captain\'s Log":
                    show captains_log_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Note":
                    show note_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Radio":
                    show radio_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Toy":
                    show toy_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                $ xPos += 0.125
                $ itemCount -= 1
            # ============================================================
            $ rations -= 5
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
    menu:
        "Restore":
            "You decide that the power needs to be restored, maybe things can begin to become operable once more aboard this damaged vessel."
            "The Botanist speaks out loud to the monitor, I knew you had it in you Teach! he says pridefully."
            if fix_pipe:
                "Now let’s go see what is really going on out there."
            if not full_oxygen:
                "I can’t stand idly while this is still broken, it’s not steaming as much now which is a really bad sign that the oxygen may have depleted too much already. He continues to find a solution to the pipe."
                jump status_branch1
            $ power += 25
            $ low_power = False
            $ med_power = True
            show quartermaster normal
            q "Nice work Techy! Now then let’s do good on our part and work on getting the hell off this coffin! I'll grab my tools."
            hide quartermaster
            jump status_branch1
        "Deny":
            $ qm_angry = True
            "You decide that things should stay depowered until you have had a chance to make sure the rest of the submersible is in working condition before turning everything back on just in case."
            show botanist normal
            "The Botanist looks around and sighs."
            b "Well there could in fact be things aboard the ship that could be in danger if turned back up to mid-power, good call I suppose.” He nods in agreement."
            hide botanist normal
            if fix_pipe:
                "Now let’s go see what is really going on out there."
            if not full_oxygen:
                "I can’t stand idly while this is still broken, it’s not steaming as much now which is a really bad sign that the oxygen may have depleted too much already. He continues to find a solution to the pipe."
            show quartermaster angry
            q "Techy, what the actual hell?! You were supposed to turn everything back on you son of a-"
            "He stops himself before finishing." 
            q "I knew better than to trust a bastard like you and I did anyway, hope you ain’t thinking about returning over here you dumb fool."
            "The Quartermaster punches the door before nearly breaking his hand, he squirms off holding it, too far to be seen from the monitor."
            hide quartermaster
        
            jump status_branch1

label entered_living_quarters3:

    show bg quarters
    show quartermaster angry
    show radio at left

    "You enter the Living Quarters, the Quartermaster is still struggling to unseal the door with the wheel at its center. The Lifeboat pod is flickering with its lights, a sign of its malfunction."
    "On the floor a radio is at a low frequency, it repeats a message over and over, but is immediately cut off before it can finish its message. Perhaps the radio will give a clue that could come handy in the future?."
    "With the state of things, you won’t be able to repair both, which do you choose?"
    jump fix_choice3a

label fix_choice3a:
    menu:
        "Fix Lifeboat. -5 Rations (Current rations: [rations])":
            "The Lifeboat pod is sleek and simple, one that would be easy for any inexperienced novice to understand and operate should the need ever arise to use. Though for the state it is in, this may require some careful analysis."
            show quartermaster normal
            "Some time passes and you identify through the drone that the AI Mainframe is damaged in the ship and that you’ll have to reroute it to a manual override. This will allow the pod to be operated without the authorization of the AI. Good as new… sort of."
            hide quartermaster
            hide radio
            $ fix_lifeboat = True
            $ rations -= 5
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:   
                jump branch3_menu

        "Fix Radio. -5 Rations (Current rations: [rations])":
            "After some fiddling with the inside of the electronic box and rearranging some wires, the radio begins to emit a message on repeat. Numerical in nature, but otherwise useless unless you decode it. You write it down in a handy note for later."
            hide quartermaster
            hide radio
            $ inventory.add_item(note)
            $ fix_radio = True
            $ evil_points += 1
            # HIDE INVENTORY
            # ============================================================
            hide sonar_device_img
            hide deep_sea_suit_img
            hide captains_log_img
            hide note_img
            hide radio_img
            hide toy_img
            # ============================================================

            # SHOW INVENTORY
            # ============================================================
            $ itemCount = inventory.number_of_items - 1
            $ xPos = 0.1

            while itemCount >= 0:
                if inventory.items[itemCount].name == "Repair Drone":
                    show repair_drone_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Sonar Device":
                    show sonar_device_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Deep Sea Suit":
                    show deep_sea_suit_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Captain\'s Log":
                    show captains_log_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Note":
                    show note_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Radio":
                    show radio_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                if inventory.items[itemCount].name == "Toy":
                    show toy_img:
                        xalign xPos yalign 0.01
                        xysize(100,100)

                $ xPos += 0.125
                $ itemCount -= 1
            # ============================================================
            $ rations -= 5
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:
                jump branch3_menu

label entered_biosphere3:

    show bg biodome
    show botanist angry

    "You enter the Biosphere, the Botanist is still struggling with his pipe problem as it spews steam from its surface."
    "Fixing the pipe might solve the oxygen problem, but the plants in the Biosphere might make up for a lot of time spent while you try to figure out how to get out of this situation."
    "Which feels like more of a fruitful decision to you?"
    jump fix_choice3b

label fix_choice3b:
    menu:
        "Fix Pipe. -5 Rations (Current rations: [rations])":
            $ rations -= 5
            "The Botanist backs away from his struggle to seal the leak while your drone inches near. With some bolts, tools, and applied heat, the steam draws its last from the choking pipe and the Oxygen level begins to steady on the meter."
            show botanist normal
            b " Eureka! This brings me much joy."
            hide botanist
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:   
                jump branch3_menu

        "Scavenge Plants. +10 Rations (Current rations: [rations])":
            "Perhaps it’s a dead end to fix the broken pipe, it’s broken after all, the Botanist, to his dismay sees the drone go to snip at some of the plants, parsley, tomatoes, carrots, a variety of foods get stuffed into the open cartridge of the drone. Hopefully this was worth the cost."
            hide botanist
            $ full_oxygen = False
            $ rations += 10
            if enter_living_quarters and enter_biosphere:
                    menu:
                        "Continue to power":
                            jump restore_deny_power3
            else:
                jump branch3_menu
label status_branch1:
    "Now that you have made a firm decision on the state of the power, you decide it\’\s time to give more exploration to the other rooms and what they may offer to you in helping you get off this doomed submersible."
    "On the left side of the submarine towards the Command Bridge is the Captain\’\s Quarters and the Scuba Room."
    "On the right side towards the Living Quarters is the Drone Room and Cafeteria."
    if fix_toy:
        $ a_angry = False
    else:
        "With the Captain on the move he could be anywhere, it’s best to find out where he’s not."
    if qm_angry:
        "With the Quartermaster swearing revenge on me, I better keep a close eye out for him"
        jump menu_monitor_check1
label menu_monitor_check1:
    menu:
        "Check Monitors":
            show bg controlroomgameover
            if low_power:
                jump monitor_branch_low1
            if not low_power:
                jump monitor_branch_med1
        "Search Rooms":
            jump search_rooms1
label monitor_branch_low1:

    menu:
        "Check Left Monitors": 
            menu:
                "Check Captain’s Quarters. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    "You check CQ for the Captain’s presence, he doesn’t seem to be there."
                    jump monitor_branch_low1
                "Check Scuba Room. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    if a_angry:
                        show captain angry
                        show gun at left
                        "You check the Scuba Room, you see the Captain pacing around it swinging his gun in anger."
                        hide captain
                        hide gun
                        jump monitor_branch_low1
                    else:
                        "You check the Scuba Room for the Captain’s presence, he doesn’t seem to be there."
                        jump monitor_branch_low1
        "Check Right Monitors":
            menu: 
                "Check Drone Room. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    if qm_angry:
                        "The Quartermaster seems to be thrashing some things around in the Drone Room, it seems inaccessible for the time being."
                        jump monitor_branch_low1
                    else: 
                        "The Quartermaster doesn’t seem to be in there."
                "Check Cafeteria. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    "The Quartermaster doesn’t seem to be in there."
                    jump monitor_branch_low1
        "Search Rooms":
            jump search_rooms1
label monitor_branch_med1:
    menu:
        "Check Left Monitors": 
            menu:
                "Check Scuba Room. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    "You check the Scuba Room for the Captain’s presence, he doesn’t seem to be there."
                    jump monitor_branch_med1
                "Check Captain’s Quarters. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    if a_angry:
                        show captain angry
                        show gun at left
                        "You check the Captain’s Quarters, you see the Captain pacing around it swinging his gun in anger."
                        hide captain
                        hide gun
                        jump monitor_branch_med1
                    else:
                        "You check the Scuba Room for the Captain’s presence, he doesn’t seem to be there."
                        jump monitor_branch_med1
        "Check Right Monitors":
            menu: 
                "Check Cafeteria. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    if qm_angry:
                        "The Quartermaster seems to be thrashing some things around in the Cafeteria, it seems inaccessible for the time being."
                        jump monitor_branch_med1
                    else: 
                        "The Quartermaster doesn’t seem to be in there."
                "Check Drone Room. -5\% power (Current power: [power])":
                    $ power -= 5
                    if power == 0:
                        jump power_ending
                    "The Quartermaster doesn’t seem to be in there."
                    jump monitor_branch_med1
        "Search Rooms":
            jump search_rooms1
label search_rooms1:
    menu:
        "Search Captain’s Quarters":
            "You decide to search the Captain’s Quarters, it's littered with maps and graphs attached to the walls, various notes strewn about the table." 
            "One thing seems to catch your eye, a peculiar brown notebook with a title that reads Mission: Crushing Depth"
            "Do you take and read it?"
            menu:
                "Take and read it. -5 rations (Current rations: [rations])":
                    $ rations -= 5
                    if rations == 0:
                        jump rations_ending
                    $ inventory.add_item(captains_log)
                    # HIDE INVENTORY
                    # ============================================================
                    hide sonar_device_img
                    hide deep_sea_suit_img
                    hide captains_log_img
                    hide note_img
                    hide radio_img
                    hide toy_img
                    # ============================================================

                    # SHOW INVENTORY
                    # ============================================================
                    $ itemCount = inventory.number_of_items - 1
                    $ xPos = 0.1

                    while itemCount >= 0:
                        if inventory.items[itemCount].name == "Repair Drone":
                            show repair_drone_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Sonar Device":
                            show sonar_device_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Deep Sea Suit":
                            show deep_sea_suit_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Captain\'s Log":
                            show captains_log_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Note":
                            show note_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Radio":
                            show radio_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Toy":
                            show toy_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        $ xPos += 0.125
                        $ itemCount -= 1
                    # ============================================================
                    $ captains_log = True
                    $ good_points += 1
                    "Upon closer inspection of the contents, you learn that the true nature of this mission was to be a suicide mission, one where the crew is left in the dark of the details."
                    "The Captain is to assure control of the crew and order them to arm the bomb in the armory."
                    "The Captain's safety wasn't guaranteed either. As you read on, you snack a bit on your rations."
                    jump search_rooms1
                "Exit the room":
                    "You decide it's not in your authority to read the contents of the mission and decide to look elsewhere."
                    jump search_rooms1

        "Search Scuba Room":
            if a_angry:
                "You go into the Scuba Room but find your drone unexpectedly kicked over, by the time you’re able to restabilize you have lost both power and time. -5 Rations and -5\% power."
                $ rations -= 5
                $ power -= 5
                if rations == 0:
                    jump rations_ending
                if power == 0:
                    jump power_ending
            
            "Upon entering the Scuba Suit Room, you are greeted by flickering lights. A sealed door leading to a loading dock lies on the floor. Multiple compartments are set around the room to host Deep-sea Diving Gear." 
            "However, as you look around, you see only one suit hanging in its compartment as if there was only enough to bring one on board."
            "Do you take the suit?"
            menu:
                "Take the suit":
                    $ inventory.add_item(deep_sea_suit)
                    # HIDE INVENTORY
                    # ============================================================
                    hide sonar_device_img
                    hide deep_sea_suit_img
                    hide captains_log_img
                    hide note_img
                    hide radio_img
                    hide toy_img
                    # ============================================================

                    # SHOW INVENTORY
                    # ============================================================
                    $ itemCount = inventory.number_of_items - 1
                    $ xPos = 0.1

                    while itemCount >= 0:
                        if inventory.items[itemCount].name == "Repair Drone":
                            show repair_drone_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Sonar Device":
                            show sonar_device_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Deep Sea Suit":
                            show deep_sea_suit_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Captain\'s Log":
                            show captains_log_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Note":
                            show note_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Radio":
                            show radio_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Toy":
                            show toy_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        $ xPos += 0.125
                        $ itemCount -= 1
                    # ============================================================
                    $ deep_sea_suit = True
                    $ bad_points +=1
                    "Surely this will be more useful in your hands should you find yourself on the other side of the submersible's hull. Better safe than sorry. It takes some time to pack it away into your drone."
                    jump search_rooms1
                "Leave the Room.":
                    "You believe it's not worth taking the suit. If there is the off chance you'd find yourself on the other side of the submersible, you find it to be quite small for the time being."
                    jump search_rooms1
        "Search Cafeteria":
            "The Cafeteria is dormant and empty. What once was a place to eat and enjoy with friends is now a grim empty mess hall." 
            "As your drone rummages through the cupboards, you find plenty of canned goods and MRE’s, this should last you for quite some time should you take the supplies."
            menu:
                "Take 10 Rations (Current rations: [rations])":
                    if depleted_rations:
                        jump search_rooms1
                    if not depleted_rations:
                        $ depleted_rations = True
                        $ rations += 10
                        "Not like anyone will be needing this anytime soon, these rations should allow for more time and flexibility with your options." 
                        jump search_rooms1
                "Take a cake for 10 rations":
                    if not full_oxygen:
                        $ oxygen -= 10
                        if oxygen == 0:
                           jump oxygen_ending
                    elif full_oxygen:
                        pass
                        "You begin to cut into a big cake with your drone’s tools. It’s been a while since you had something sweet to enjoy, plus it’ll be filling. To your surprise, the cake doesn’t budge... "
                        "Until it does and you realize a burst of smoke is sprung and before you is a dark pipe spewing oxygen into the air." 
                        jump search_rooms1
                "Leave the Food":
                    "You decide to leave the food where it is, you anticipate that you won't be needing it in the near future."
                    jump search_rooms1

        "Search Drone Room":
            
            show bg dronerepair

            if qm_angry:
                "You go into the Drone Room but find your drone unexpectedly kicked over, by the time you’re able to restabilize you have lost both power and time. (-5 rations and -5\% power)"
                $ rations -= 5
                $ power -= 5
                if rations == 0:
                    jump rations_ending
                if power == 0:
                    jump power_ending
            "Heading into the Drone Room, rows of equipment lie behind metal grates and locks. Resting on the floor near the backside of the room lay a medium sized metal structure." 
            "Various prongs jutted out from the object, this thing looked quite dangerous. You look upon the object, “ZETA-38”. Resting upon the table you notice another object, it’s round and seems to emit a yellow light." 
            "This is a sonar device, used to attach to more navigable drones, but can very well be activated manually. Perhaps this could come in handy?"
            menu:
                "Take the device":
                    $ inventory.add_item(sonar_device)
                    # HIDE INVENTORY
                    # ============================================================
                    hide sonar_device_img
                    hide deep_sea_suit_img
                    hide captains_log_img
                    hide note_img
                    hide radio_img
                    hide toy_img
                    # ============================================================

                    # SHOW INVENTORY
                    # ============================================================
                    $ itemCount = inventory.number_of_items - 1
                    $ xPos = 0.1

                    while itemCount >= 0:
                        if inventory.items[itemCount].name == "Repair Drone":
                            show repair_drone_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Sonar Device":
                            show sonar_device_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Deep Sea Suit":
                            show deep_sea_suit_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Captain\'s Log":
                            show captains_log_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Note":
                            show note_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Radio":
                            show radio_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        if inventory.items[itemCount].name == "Toy":
                            show toy_img:
                                xalign xPos yalign 0.01
                                xysize(100,100)

                        $ xPos += 0.125
                        $ itemCount -= 1
                    # ============================================================
                    $ sonar_device = True
                    $ neutral_points += 1
                    "It glows dimly yellow, yet dormant, what use may this find you wonder? Your drone tweaks at it a bit to stay powered beyond its stationary charger and drops it into its compartment."
                    jump search_rooms1
                    if not full_oxygen:
                        menu:
                            "Take the supercharged battery. -5 rations (Current power: [power])":
                                "Reaching for what seems to be an ultra-charged battery your drone is immediately zapped as you awake to your senses, realizing you just touched what was actually another drone dissected of its electrical components." 
                                "This feeling of low oxygen is not attributing well to your sense of decision." 
                                $ power -= 5
                                if power == 0:
                                    jump power_ending
                                jump search_rooms1
                    elif full_oxygen:
                        pass
                    if not full_oxygen:
                        menu:
                            "Try to unlock the gun cabinet. -5 rations (Current oxygen: [oxygen])":
                                "You use your drone to try to lockpick your way to a stack of guns. Perhaps it’d be useful to have some sort of weapon or at least put their components to greater use." 
                                "To your surprise a geyser of steaming oxygen sprays wildly as the cabinet you were trying to lockpick was just shy of your tool and you actually ended up puncturing another pipe." 
                                "That definitely was not worth the cost you were expecting."
                                $ oxygen -= 10
                                if oxygen == 0:
                                    jump oxygen_ending
                                jump search_rooms1
                    elif full_oxygen:
                        pass
                "Leave the Room.":
                    "As cool as it would be to fiddle with gadgets, you have more dire things to worry about. You decide not to take the device."
                    
                    jump search_rooms1
        "Change to full power mode and get off the sub":
                jump end_determine

label end_determine:
    if bad_points >= 0 and good_points < 0 and neutral_points < 0 and evil_points < 0:
        jump ending1
    if good_points > 0 and neutral_points > 0 and bad_points > 0:
        jump ending2
    if good_points > 0 and evil_points > 0 and bad_points < 0:
        jump ending3
    
label ending1:

    scene bg controlroomgameover

    menu:
        "Ending 1: Not Much to Go On":
            "You don’t feel so much at ease, trial and tribulation has led you with not much to go off of or to go on for that matter. There doesn’t seem to be an easy way off this ship."
            if fix_lifeboat:
                menu:
                    "Take Lifeboat":                        
                        show bg ending1lifeboat                        
                        "The Lifeboat pod seems like your best bet, everyone lines up to join you and are prepared for whatever may come next." 
                        "As all safety procedures are met, you all journey through the deep dark." 
                        "Sighs of relief can be heard amongst you and some eager to finally go home. In a distant view a tidal wave of darkness comes quickly in front of the pod, there is no way of dodging this enigmatic wave of darkness at the rate it seems to be coming into view." 
                        "To your shock and awe, this object abrupts your new found hope destroying the pod and all those onboard. You have succumbed to the Crushing Depth."
                        return
            else:
                menu:
                    "Find Another Way":
                        "You attempt to make your way to the Scuba Room, even with a suit on hand there doesn’t seem to be much chance of survival with your limited knowledge of the situation." 
                        "However, you won’t have to choose as you get knocked off of your feet once more but this time you don’t feel the clamoring of a floor or wall on your back. You have succumbed to the Crushing Depth."
return
label ending2:
    
    scene bg ending2

    menu:
        "Ending 2: Ascend the Deep":
            "You decide you will distract the monster that is keeping you and your crew hostage in these treacherous depths. At the loading dock you ready yourself according to procedure with the Deep-Sea Suit and the mechanisms around you."
            "In a moment's notice you are swept into the dark depths with the door sealing behind you."
            "As your buoyancy drifts you across the chasm deep, you activate your sonar device and it pulses in synchronous chirps." 
            "You witness a dark mass rush from your peripheral and the sensation of light allows you just enough to see your hands in front of you as if an umbral veil had been lifted from the world around you."
            if fix_lifeboat:
                "As you ascend from the depths, you feel a moment of relief as you see in the distance a pod floating away from the submarine." 
                "You see 3 figures at its helm and you can’t help but at least feel an ounce of thankfulness that you and your crew were able to survive this hellscape of a situation."
            "Coming to the surface a large frigate sails just by you, a spotlight meets your rippling body amidst the waves and you hear calls for rescue. You have been saved. But perhaps more will perish from the monster beneath the Crushing Depth."
return
label ending3:

    scene bg ending3

    menu:
        "Ending 3: Crushing Departure":
            "You have the option to blow up the bomb in the Drone Room. No one left on the Submersible will survive the blast, but doing so will complete the intended mission." 
            "You make your way out the monitor room, with your notes in hand and your expression of acceptance, no one feels any ill will towards you." 
            "Any hostility is met with a cautious nod, even if they seem unknown to you true intentions. There is no reason to hate one another at this point, this is the end." 
            "You reach the bomb and recite the code into its 9-digit pad. A red light and a beep follow soon after and before you know it, darkness clouds your mind."
            "There will be no monster today, not now, not ever again."
            "Mission: Crushing Depth Complete."
return
label power_ending:
"With your carelessness everything goes dark, you stumble around waiting for a sign that the power will return, but all you hear now are the creaks of strut and metal." 
"You soon find yourself gasping in the darkness and feel the encroaching of frost upon your skin. You have succumbed to the Crushing Depth."
return
label oxygen_ending:
"You begin to feel your vision blur and you slump upon the ground gasping for more air, but it does not come to you anymore. The oxygen has begun to reach to the point of no return." 
"You choke one last time for the respite of an air that was once there, instead you feel your mind fade into and out of darkness until you have succumbed to the Crushing Depth."
return
label rations_ending:
"Your stomach aches in every manner, you begin to lose sight of your main objective, it’s replaced by the under satiating sensation of starvation." 
"Whatever you may do to survive past this point doesn’t earn you the time or resources you need to stay alive long enough to find your way off of the ship." 
"With grim dismay and a yearning for sustenance of any kind, your world fades before you and you soon after succumb to the Crushing Depth."
return