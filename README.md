# P4_openclassroom_python

The 4th project of the python app dev course

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requierments.

```bash
pip install requirements.txt
```

## Usage
To launch the project, simply use:
```bash
python3 controllers.py
```
To create a Tournament you must first have created the Players.
You can navigate within the menu by typing the number of the 
wanted option and pressing enter.

In the main menu, for each options:<br>
0: Start the creation of a new Tournament<br>
1: Start the creation of a new Player<br>
2: Start the modification of a Player's elo/ranking.<br>
After selecting this option, you must type in the ID of the Player 
that you wish to edit, press enter, then enter the new elo.<br>
3: Select a Tournament, then either finish or/and start a new round,
depending if it's the first, last or neither.<br>
A scoreboard will be shown after completing the input of the match's scores
when finishing a round.<br>
The matchups for the new round will also be shwon the same way.<br>
4: The reports. First choose if you want to see something specific of a tournament
(Tournament Player's ordered by name/ranking, matches separated by round or not)
or globally (Players ordered by name/ranking, Tournaments), then select the report 
you want to see.


