#Tic-Tac-Toe
box = {
    'A1': ' ', 'A2': ' ', 'A3': ' ',
    'B1': ' ', 'B2': ' ', 'B3': ' ',
    'C1': ' ', 'C2': ' ', 'C3': ' '
}   # Dictionary

player = 1    # Initialize 1st player
moves = 0     # Counting the moves
Check = 0

def check():
    # Checking the moves for Player 1
    # Horizontal Check
    if box['A1'] == 'X' and box['A2'] == 'X' and box['A3'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1    # Ends the game and prompts the message of the winner
    if box['B1'] == 'X' and box['B2'] == 'X' and box['B3'] == 'X':
        print('Player 1 is the Winner! Congrats!')
        return 1
    if box['C1'] == 'X' and box['C2'] == 'X' and box['C3'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1
    # Diagonal Check
    if box['A1'] == 'X' and box['B2'] == 'X' and box['C3'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1
    if box['A3'] == 'X' and box['B2'] == 'X' and box['C1'] == 'X':
        print('"Player 1 is the Winner! Congrats')
        return 1
    # Vertical Check
    if box['A1'] == 'X' and box['B1'] == 'X' and box['C1'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1
    if box['A2'] == 'X' and box['B2'] == 'X' and box['C2'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1
    if box['A3'] == 'X' and box['B3'] == 'X' and box['C3'] == 'X':
        print('Player 1 is the Winner! Congrats')
        return 1

    #Checking the moves for Player 2
    #Horizontal Check
    if box['A1'] == 'O' and box['A2'] == 'O' and box['A3'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    if box['B1'] == 'O' and box['B2'] == 'O' and box['B3'] == 'O':
        print('Player 2 is the Winner! Congrats!')
        return 1
    if box['C1'] == 'O' and box['C2'] == 'O' and box['C3'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    #Diagonal Check
    if box['A1'] == 'O' and box['B2'] == 'O' and box['C3'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    if box['A3'] == 'O' and box['B2'] == 'O' and box['C1'] == 'O':
        print('"Player 2 is the Winner! Congrats')
        return 1
    #Vertical Check
    if box['A1'] == 'O' and box['B1'] == 'O' and box['C1'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    if box['A2'] == 'O' and box['B2'] == 'O' and box['C2'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    if box['A3'] == 'O' and box['B3'] == 'O' and box['C3'] == 'O':
        print('Player 2 is the Winner! Congrats')
        return 1
    return 0

print('A1 | A2 | A3')
print('---+----+---')
print('B1 | B2 | B3')
print('---+----+---')
print('C1 | C2 | C3')
print('***************************')

while True:
    print(box['A1'] + '|' + box['A2'] + '|' + box['A3'])
    print('-+-+-')
    print(box['B1'] + '|' + box['B2'] + '|' + box['B3'])
    print('-+-+-')
    print(box['C1'] + '|' + box['C2'] + '|' + box['C3'])
    print()
    Check = check()
    if moves == 9 or Check == 1:
        break
    while True:     # Player Input
        if player == 1:  # Choose Player
            p1_input = input('Player 1: ') # For Player 1
            if p1_input.upper() in box and box[p1_input.upper()] == ' ':
                box[p1_input.upper()] = 'X'
                player = 2
                break
            # On wrong input
            else:
                print('Wrong Input! Please Try Again')
                continue
        else:
            p2_input = input('Player 2: ') # For Player 2
            if p2_input.upper() in box and box[p2_input.upper()] == ' ':
                box[p2_input.upper()] = 'O'
                player = 1
                break
            # On wrong input
            else:
                print('Wrong Input! Please Try Again')
                continue
    moves += 1
    print('***************************')
    print()