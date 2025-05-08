"""
Marleen & Evelyn
"""
from classes import *
from functions import *

# här initieras värden #
clear() # för att tömma skärmen när spelet först startar
print("Name your character:")
var = input("> ").strip()
player = Player(50, 50, var) # skapar ett objekt för spelaren
terrain = [ # en lista över alla träd
	Terrain(45, 48, "tree"),
	Terrain(45, 51, "tree"),
	Terrain(46, 46, "tree"),
	Terrain(47, 52, "tree"),
	Terrain(48, 44, "tree"),
	Terrain(49, 55, "tree"),
	Terrain(51, 56, "tree"),
	Terrain(52, 44, "tree"),
	Terrain(53, 46, "tree"),
	Terrain(53, 55, "tree"),
	Terrain(54, 49, "tree"),
	Terrain(54, 51, "tree")
]
pickup = [ # en lista över alla kronor
	Pickup(46, 54, "crown", 250),
	Pickup(47, 48, "crown", 250),
	Pickup(48, 56, "crown", 250),
	Pickup(52, 46, "crown", 250),
	Pickup(55, 53, "crown", 250)
]

# här körs spelet
while True:
	clear()
	print_map(player, terrain, pickup)
	var = getch() # vänta på att en knapp trycks
	if var == b"w": # upp, tangent W
		player.move( 0, -1, terrain, pickup)
	elif var == b"s": # ned, tangent S
		player.move( 0,  1, terrain, pickup)
	elif var == b"a": # vänster, tangent A
		player.move(-1,  0, terrain, pickup)
	elif var == b"d": # höger, tangent D
		player.move( 1,  0, terrain, pickup)