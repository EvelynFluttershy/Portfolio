"""
Marleen & Evelyn
"""
class Item: # klass för alla saker i spelet
	def __init__(self, x, y, type, subtype):
		self.x = x
		self.y = y
		self.type = type
		self.subtype = subtype
	def get_x(self): # ger x-värdet
		return self.x 
	def get_y(self): # ger y-värdet
		return self.y
	def get_type(self):
		return self.type
	def get_subtype(self):
		return self.subtype
	def get_emoji(self):
		emoji = {"player":"🔴", "tree":"🌳", "crown":"👑" } 
		try:
			return emoji[self.subtype] # om en emoji finns för denna subtype, returnera det
		except:
			return "❓" # ifall det inte finns en bestämd emoji, returnera denna emoji istället
	def delete(self):
		self.x = -1000
		self.y = -1000

class Player(Item): # spelaren
	def __init__(self, x, y, name):
		super().__init__(x, y, "player", "player")
		self.name = name
		self.level = 1
		self.health = 100
		self.max_health = 100
		self.gold = 0
	def get_name(self):
		return self.name
	def get_level(self):
		return self.level 
	def get_health(self):
		return self.health
	def get_max_health(self):
		return self.max_health
	def get_gold(self):
		return self.gold
	def move(self, x:int, y:int, terrain, pickup):
		target = None
		target_x = self.x +x
		target_y = self.y +y
		for t in terrain:
			if t.get_x() == target_x and t.get_y() == target_y:
				target = t
		for t in pickup:
			if t.get_x() == target_x and t.get_y() == target_y:
				target = t
		if target == None:
			self.x += x
			self.y += y
		elif target.get_type() == "pickup":
			self.x += x
			self.y += y
			self.gold += target.get_gold()
			target.delete()

class Terrain(Item): # objekt i världen
	def __init__(self, x, y, subtype):
		super().__init__(x, y, "terrain", subtype) 

class Pickup(Item): # objekt man kan plocka upp
	def __init__(self, x, y, subtype, gold):
		super().__init__(x, y, "pickup", subtype)
		self.gold = gold
	def get_gold(self):
		return self.gold