# Tic-Tac-Toe
In this classic game of Tic Tac Toe, we have used simple programming techniques such as the 
use of dictionaries, functions, methods, conditional statements etc. Switching between 2 users 
so that they can input their moves in the spaces in turns. Checking all the possible conditions to 
be met to decide the winner. Error analysis in case of a wrong input and continuity of the 
process. Ending the game as a draw if there is no winner after a total of nine moves when all 
the positions are filled.
Tic Tac Toe is one of the most played games in the world. We have implemented this game in 
Python. It is a very simple game between 2 players who put X or O in the Tic Tac Toe board. The 
board is a 3x3 grid where players take turns to connect their moves. The first player to connect 
his moves horizontally/ diagonally/ vertically across the board wins.
This game is simple and easy to play. Users only need to choose the space where they will put 
their move in the 3x3 square grid. There are 3 rows and 3 columns. The dictionary keys will be 
used as the inputs to select those spaces. This also makes it possible to check if a space is empty 
or occupied. We have also added an upper() method for the ease of the users. So that even if 
the users put a lower-case letter it will convert it to an upper-case letter and avoid errors. By 
using a loop, the program runs as long as no one won or the game ends with a draw. Switching 
between the users to take inputs in turns. Error analysis makes it possible to avoid errors and 
continue the program by taking the input again. It will also show a message in the case of an 
invalid input by the users. The Tic Tac Toe board is displayed every time showing the previous 
moves as well as the empty spaces. The program is compact. We used a function to store all the 
conditional statements that can be called in the main function to check if a player has won. If a 
player wins, a message will show up determining the winner and ending the game. 
The Tic Tac Toe board is shown with the name of all the grids. The Alphabets A represents row 
1, B represents row 2 and C represents row 3 of the board. The numbers corresponding to it 
represent their respective columns. Dictionary is used to store data values in keys. The keys are 
the grids. It is shown as:
A1 | A2 | A3
---+----+---
B1 | B2 | B3
---+----+---
C1 | C2 | C3
Players inputs from the dictionary keys from above. If the user puts an invalid input, “Wrong 
Input! Please Try Again” message will show up and the user can input again. The player will 
change after one player puts their input. The inputs are stored in the dictionary and displayed 
on the screen every time incrementing the variable moves. After all the grids are filled or moves
are executed 9 times the program will end. Therefore, resulting in a draw. There are eight 
different scenarios for each player to win. The player needs to succeed in connecting three 
consecutive moves either in the horizontal, diagonal or vertical way.
If Player 1 manages to win by connecting the X’s, “Player 1 is the Winner! Congrats” message wi
ll be shown and the game will end. Consequently “Player 2 is the Winner! Congrats” will be sho
wn if Player 2 wins by connecting the O’s in those orders. The game is fun to play and competiti
ve. The Player has to think about winning as well as not letting his opponent win. 
We have only implemented the classic Tic Tac Toe game in Python. We can add user interface 
and other features such as Graphical User Interface (GUI) with pygame library. Moreover, we 
can also develop the project even further by using various Artificial Intelligence techniques. 
Implementing the minimax algorithm for the best gameplay experience adding difficulty levels 
for the game. Tic Tac Toe is the basis of game theory with various combinations that require
players to strategize for the best outcome.