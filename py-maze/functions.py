"""
Marleen & Evelyn
"""
import os # bibliotek för systemfunktioner
import msvcrt # bibliotek för Microsoft-funktioner
def clear(): # funktion som tömmer terminalen från all text
	os.system("cls")
def getch(): # funktion som väntar på första tangenttryckning
	return msvcrt.getch()
def xy(array, x, y, value): # funktion som vänder på x/y för inmatning till array
	array[y][x] = value
def text_left_right(width, left, right): # funktion som placerar två strängar till vänster och höger baserad på en viss bredd
	left_len = len(left)
	right_len = len(right)
	spacing = width - left_len - right_len
	return left + " "*spacing + right

W = 9 # antalet rutor i bredd man kan se
C = 4 # positionen i mitten där spelaren placeras

def print_map(player, terrain, pickup): # funktion som ritar ut hela spelplanen samt text runt
	x = player.get_x() 
	y = player.get_y() 
	map = [
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "], 
		["  ","  ","  ","  ","  ","  ","  ","  ","  "]
	]
	
	for t in terrain:
		tx = t.get_x() - x + C #
		ty = t.get_y() - y + C
		if tx >= 0 and tx < W and ty >= 0 and ty < W:
			xy(map, tx, ty, t.get_emoji())
	for t in pickup:
		tx = t.get_x() - x + C #
		ty = t.get_y() - y + C
		if tx >= 0 and tx < W and ty >= 0 and ty < W:
			xy(map, tx, ty, t.get_emoji())
	map[C][C] = "🔴"

	print(text_left_right(22, player.get_name().upper(), str(player.get_health())+"/"+str(player.get_max_health())))
	print("█"*(W*2+4))
	for i in range(W):
		print("██"+"".join(map[i])+"██")
	print("█"*(W*2+4))
	print(text_left_right(22, f"LEVEL {player.get_level()}", f"{player.get_gold()} G"))
# slutet på def print_map()