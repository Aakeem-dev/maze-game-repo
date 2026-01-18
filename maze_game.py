
#allocate gameboard

rooms = {
    'default' : { 'health': 0, 'message': 'This room is empty, proceed'},
    (0,3): { 'health': 0, 'message': "You've found a hint scroll! it say's... Go 'west' for 1 room and 'south' for 3 rooms to safely advance.", 'item': 'hint scroll'},
    (1,1): { 'health': -100, 'message': 'OH NOOO!!! this room was rigged with a bomb, you got blown up :('},
    (1,4): { 'health': -30, 'message': "You got stung by a scorpion! :(, -30 health"},
    (2,1): { 'health': 0, 'message': "You've found a hint scroll! it say's... The next 2 safe moves are 'south' and then 'east'", 'item': 'hint scroll'},
    (2,3): { 'health': -50, 'message': "This room is booby trapped! OUCH!! You stepped on a bear trap. :(, -50 health"},
    (2,4): { 'health': 20, 'message': "You've found a potion! +20 health\n" +"You've also found a cheat token! it says... 'west' is unsafe", 'item': 'potion'},
    (3,4): { 'health': 0, 'message': "You've found a hint scroll! it says... Trap in the next room! 'east'", 'item': 'hint scroll'},
    (3,5): { 'health': -20, 'message': 'trap!'},
    (4,1): { 'health': -20, 'message': "This room is booby trapped! you were hit in the head by a swinging hammer. -20 health"},
    (4,2): { 'health': 40, 'message': "You've found a potion! +40 health\n" + "You've also found a cheat token! it says... Next safe move is 'south'", 'item': ('potion','hint scroll')},
    (4,3): { 'health': -35, 'message': "This room is booby trapped! you got shot in the leg by an arrow. -35 health"},
    (5,0): { 'health': 20, 'message': "You've found a potion! +20 health", 'item': 'potion'},
    (5,5): { 'health': 0, 'message': "Congrat's you've found the exit!"}
}

player = {'x' : 0, 'y' : 0, 'status': {'health' : 100, 'inventory' : []}}

    
def valid_direction(direction):
    valid_moves = ['d', 'a','w','s','quit', 'status']
    if direction not in valid_moves:
        print ("That is not a valid input. Try again.")
        return False
    return True
    
def make_move(direction, player):
    
    moves = { #y,x
        'd' : (0, 1),
        'a' : (0,-1),
        'w' : (-1,0),
        's' : (1, 0)
    }
    
    dy, dx = moves[direction]
    new_x = player['x'] + dx
    new_y = player['y'] + dy
    
    if 0 <= new_x <= 5 and 0 <= new_y <= 5:
        player['x'], player['y'] = new_x, new_y
        return True
    print('sorry that is not a valid move.')
    return False

def apply_room_logic(rooms, player):
    
    current_room = (player['y'],player['x'])
    room = rooms.get(current_room, rooms['default'])
    
    room_health = room['health']
    item = room.get('item')
    if item is not None:
        player['status']['inventory'].append(item)
        
    print(f"> Current Location, room {current_room}")
    print(room['message'])
    print('\n')
    
    player['status']['health'] = max(0, min(100, player['status']['health'] + room_health))
    
        
def play_game(rooms, player):
    
    print("You are in a maze of rooms. The first room is in the north west corner of the maze [room (0,0)]. You must make it to the last room in the south east corner of the maze alive to escape [room (5,5)]. Valid moves are ['A'/'a' = west, 'D'/'d' = east, W'/'w' north, and S'/'s' = south]. Input 'status' to see your status, you can also input 'quit' at any time to end the game. Good luck!\n")
    
    while (player['x'] != 5 or player['y'] != 5) and player['status']['health'] > 0:
        
        direction = input('> ').lower()
        if direction == 'quit':
            break
        
        while not valid_direction(direction):
            direction = input('> ')
            if direction == 'quit':
                break
        if direction != 'status':  
            if not make_move(direction, player):
                continue
        
            apply_room_logic(rooms, player)
        else:
            print(f"> status\nHEALTH: {player['status']['health']}\nInventory: {player['status']['inventory']}\n")
        
        if player['status']['health'] == 0:
            print('---YOU DIED! GAME OVER---')
            break
        
            
    print('press run to play again.')
    return

play_game(rooms, player)
    
#print(game_room)

