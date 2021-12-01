Juan Pablo Urista (jurista)
Project Description:
        This game is called 'Furious Fowl'! It is similar to the famous 'Angry Birds'. 
                - In the game, you launch birds at the green pigs in an attempt to defeat them all
                - As the pigs are hit, they are removed from the game
                - Once you hit all the pigs in a level, new pigs will fall from the sky onto platforms, taking you to the next level
                - When you complete the four levels, you will be asked to input a username
                        - this username and your score is recorded into a .csv file and then displayed on the scoreboard

        Apart from playing the four pre-built levels, you can build your own levels by following the menu
                - the games are stored in a directory with all levels built by all users
                - to access a level you built in a previous session, you follow the menu to the 'open' screen where you will enter the filename

Run the Project:
        - When developing this game, I used Python v3.10.0
        - To actually run the game, the user should run the main.py file
                - this can be done through the 'start' or 'cmb+b' buttons  in the user's python interpreter
        - Although not necessary, installing the PressStart2P.ttf font to one's system adds an additional layer to the aesthetic of the game
        - Nothing else needs to be done to play the game or use certain features

Libraries and Files:
        - I did not use any libraries that were not used in the 15-112 course at some point
                - I used math, random, and cmu_112_graphics in various places
        - In terms of files read, written, created, and interpreted
                - All of the Python files are linked to each other in one way or another through importing them
                        -ex: import game, other, nav
                - Custom user-built levels are stored in .csv files are created and read in the 'userLevels' folder in game.py
                - The scores are also stored in a .csv file that is updated and read in the main directory
                - I also created the clouds that are in background through photoshop

Command and Shortcuts:
        - There are not really any secret shortcuts or commands
                - The only is hitting the 't' key on your keyboard
                        - this needs to be done when on the game menu, but before you start the game
                        - this command will create a larger bird, making it a bit easier to complete the built-in levels
        - The user can navigatee through the game with a combination of keystrokes and mouse
                - Keystrokes are not needed to navigate through the menus, but can be a convenient way to get from page to page
                        - any keystrokes that are needed will be clearly labeled on the button they correspond to