print('Welcome to Treasure Island! Your mission is to find the treasure!')
direction = input('You have woken up in the forest, not sure where you are or how you got here. Would you like to go left or right?').lower()

if direction == 'left':
    swim = input('You have ended up at a lake. It reaches far and wide, what will you do next? Would you like to swim across or wait.').lower()
    if swim == 'wait': 
        door = input('Waiting for someone was a good idea. You reach of to the local fisherman and they help you get across to the abandoned castle in the middle of the lake. After searching through the first layer. You end up in front of 3 doors. Which will you choose? Yellowm, Blue or Red?').lower()
        if door == 'yellow':
            print('Well done! You have found the treasure!')
        elif door == 'red':
            print('You have fell into a pit of the eternal flames, you have burnt to death. ')
        elif door == 'blue':
            print('You open the door to find the beast of Beastuolio waiting for you. You fight as much as you can but find no way to defeat the beast. Game Over.')
        else:
            print('GAME OVER!')
    else: 
        print('You realise far too late the dangers of swinging in unknown waters. You feel something tickling you feet, before it starts pulling you all the way down. GAME OVER.')
else:
    print('Wondering in the dark is a dangerous thing, you have ended up falling into a hole, you die. ')