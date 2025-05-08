"""
TRE-I-RAD
Kod skriven av Evelyn Fluttershy
"""

import random # slumpa tal, används av motståndaren
import os # används för att rensa skärmen med clr/clear

# START PÅ EGNA FUNKTIONER #

def skriv_bräde(a): # matar ut brädet i 3 rader från en array
	for i in range(0,9,3): # i = 0, 3, 6
		print(f"[{symbol(a,i)}|{symbol(a,i+1)}|{symbol(a,i+2)}]")
def tomt_bräde(): # returnerar en blank array som motsvarar ett tomt bräde
	return [-1,-1,-1,-1,-1,-1,-1,-1,-1]
def symbol(a,i): # matar ut rätt symbol från en array och index
	if a[i] == -1:
		return super(i+1) # -1 representerar tom ruta, skriv ut liten siffra för index 1-9
	elif a[i] == 0:
		return "X" # 0 representerar spelare 1: X
	elif a[i] == 1:
		return "O" # 1 representerar spelare 2: O
	else: # om annat värde, skriv ut ett frågetecken
		return "?"
def super(n): # omvandlar en int 0-9 till upphöjd siffra
	a = ["⁰","¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹"]
	if (n < 10):
		return a[n] # returnerar upphöjd siffra
	else:
		return n # om talet är 10 eller högre, skriv ut talet
def hitta_två(a,s): # hitta två där det finns en tredje ledig ruta för tre i rad, samt vilken spelare den kollar efter. Giltiga mönster är XX_, X_X, _XX
	i = -1 # initialvariable, ingen två i rad
	for n in range(0,9,3): # checka varje rad om det är två i rad och stoppa/avsluta
		if a[n] == s and a[n] == a[n+1] and a[n+2] == -1: # om A = B, placera på C
			i = n+2
		elif a[n] == s and a[n] == a[n+2] and a[n+1] == -1: # om A = C, placera på B
			i = n+1
		elif a[n+1] == s and a[n+1] == a[n+2] and a[n] == -1: # om B = C, placera på A
			i = n
	for n in range(0,3,1): # checka varje kolumn om det är två i rad och stoppa/avsluta
		if a[n] == s and a[n] == a[n+3] and a[n+6] == -1: # om A = B, placera på C
			i = n+6
		elif a[n] == s and a[n] == a[n+6] and a[n+3] == -1: # om A = C, placera på B
			i = n+3
		elif a[n+3] == s and a[n+3] == a[n+6] and a[n] == -1: # om B = C, placera på A
			i = n
	if a[0] == s and a[0] == a[4] and a[8] == -1: # checkar diagonal \, om A = B, placera på C
		i = 8
	elif a[0] == s and a[0] == a[8] and a[4] == -1: # checkar diagonal \, om A = C, placera på B
		i = 4
	elif a[4] == s and a[4] == a[8] and a[0] == -1: # checkar diagonal \, om B = C, placera på A
		i = 0
	elif a[2] == s and a[2] == a[4] and a[6] == -1: # checkar diagonal /, om A = B, placera på C
		i = 6
	elif a[2] == s and a[2] == a[6] and a[4] == -1: # checkar diagonal /, om A = C, placera på B
		i = 4
	elif a[4] == s and a[4] == a[6] and a[2] == -1: # checkar diagonal /, om B = C, placera på A
		i = 2
	if i != -1:
		return i+1 # +1 för att omvandla från array 0-8 till 1-9
	else:
		return -1 # returnera -1 om två i rad inte kunde hittas
def hitta_vinnare(a):
	v = -1 # initialvariable, ingen vinnare
	for i in range(0,9,3): # checka varje rad om alla är samma och inte -1
		if a[i] != -1 and a[i] == a[i+1] and a[i] == a[i+2]:
			v = a[i]
	# > for i in range(0,9,3):
	for i in range(0,3,1): # checka varje kolumn om alla är samma och inte -1
		if a[i] != -1 and a[i] == a[i+3] and a[i] == a[i+6]:
			v = a[i]
	# > for i in range(0,3,1):
	if a[0] != -1 and a[0] == a[4] and a[0] == a[8]: # checka diagonal \ om alla är samma och inte -1
		v = a[0]
	if a[2] != -1 and a[2] == a[4] and a[2] == a[6]: # checka diagonal / om alla är samma och inte -1
		v = a[2]
	return v
def print_tr(obj,s,h=[],e=[]): # skriver ut text enligt språk s, ersätter text från h[] med e[], där h och e är valfria
	ö = obj.get(s, obj.get("en", "")) # hämta sträng från obj för språk s om det finns, annars hämta från engelska
	for i in range(len(h)): # gå igenom arrayen för h för vad som ska ersättas
		ö = ö.replace(str(h[i]),str(e[i])) # ersätt h[] med e[], ser till att båda är strängar
	print(ö) # skriver ut texten
def input_tr(obj,s,h=[],e=[]): # begär inmatning enligt språk s, ersätter text från h[] med e[], där h och e är valfria
	ö = obj.get(s, obj.get("en", "")) # hämta sträng från obj för språk s om det finns, annars hämta från engelska
	for i in range(len(h)): # gå igenom arrayen för h för vad som ska ersättas
		ö = ö.replace(str(h[i]),str(e[i])) # ersätt h[] med e[], ser till att båda är strängar
	return input(ö).strip() # kör input, returnerar värdet, tar också bort tomt utrymme före och efter
def getch(): # enkelt namn på att vänta på input
	input_tr(s_tryckfortsätt,språk)
def clear(): # enkelt namn på att rensa skärmen
	if os.name == 'nt': # Windows
		os.system('cls')
	else: # Linux, Mac
		os.system('clear')

# SLUT PÅ EGNA FUNKTIONER #
# START PÅ ÖVERSÄTTNINGAR #
# dessa är objekt som innehåller översättningar #
# varje objekt representerar en sträng, indexet i objektet representerar språk #

s_tryckfortsätt = {"sv":"Tryck på Enter för att fortsätta ...","en":"Press Enter to continue ...","de": "Drücken Sie die Eingabetaste, um fortzufahren ...","es": "Presiona Enter para continuar ...","ja": "Enterキーを押して続行……"}
s_svårighetA = {"sv":"Välj svårighetsgrad","en":"Choose difficulty","de": "Wählen Sie den Schwierigkeitsgrad","es": "Elige la dificultad","ja": "難易度を選択"}
s_svårighetB = {"sv":"1/L/lätt | 2/M/mellan | 3/S/svårt | 0/M/människa","en":"1/E/easy | 2/M/medium | 3/H/hard | 0/U/user","de": "1/E/einfach | 2/M/mittel | 3/S/schwierig | 0/B/benutzer","es": "1/F/fácil | 2/M/medio | 3/D/difícil | 0/U/usuario","ja": "１／Ｅ／簡単 | ２／Ｍ／普通 | ３／Ｈ／難しい | ０／Ｕ／ユーザー"}
s_svårighet_ogiltig = {"sv":"Ogiltig svårighetsgrad","en":"Invalid difficulty","de": "Ungültiger Schwierigkeitsgrad","es": "Dificultad no válida","ja": "無効な難易度"}
s_spelareS = {"sv":"spelare","en":"player","de": "Spieler","es": "jugador","ja": "プレイヤー"}
s_spelareD = {"sv":"datorn","en":"computer","de": "Computer","es": "computadora","ja": "コンピュータ"}
s_spelareA = {"sv":"spelare A","en":"player A","de": "Spieler A","es": "jugador A","ja": "プレイヤーＡ"}
s_spelareB = {"sv":"spelare B","en":"player B","de": "Spieler B","es": "jugador B","ja": "プレイヤーＢ"}
s_spelarnamn = {"sv":"Ange spelarnamn: ","en":"Enter username: ","de": "Geben Sie den Spielernamen ein: ","es": "Ingresa el nombre del jugador: ","ja": "ユーザー名を入力："}
s_spelarnamnA = {"sv":"Ange namn på spelare A: ","en":"Enter name of player A: ","de": "Geben Sie den Namen von Spieler A ein: ","es": "Ingresa el nombre del jugador A: ","ja": "プレイヤーＡの名前を入力："}
s_spelarnamnB = {"sv":"Ange namn på spelare B: ","en":"Enter name of player B: ","de": "Geben Sie den Namen von Spieler B ein: ","es": "Ingresa el nombre del jugador B: ","ja": "プレイヤーＢの名前を入力："}
s_poängställning = {"sv":"{P1} {S1} - {S2} {P2}","en":"{P1} {S1} vs {S2} {P2}","de": "{P1} {S1} - {S2} {P2}","es": "{P1} {S1} - {S2} {P2}","ja": "{P1} {S1} 対 {S2} {P2}"}
s_spelaredrag = {"sv":"{P} gör det första draget","en":"{P} makes the first move","de": "{P} macht den ersten Zug","es": "{P} hace el primer movimiento","ja": "{P}が最初の手を打ちます"}
s_ruta = {"sv":"Ange en ruta (1-9): ","en":"Pick a square (1-9): ","de": "Wählen Sie ein Feld (1-9): ","es": "Elige un cuadro (1-9): ","ja": "マスを選択 (1-9)："}
s_spelarevinner = {"sv":"{P} vinner","en":"{P} wins","de": "{P} gewinnt","es": "{P} gana","ja": "{P}の勝利"}
s_ingenvinner = {"sv":"Ingen vinner","en":"No one wins","de": "Niemand gewinnt","es": "Nadie gana","ja": "勝者なし"}

# SLUT PÅ ÖVERSÄTTNINGAR #

# START PÅ HUVUDLOOP #

# hämta språk #
språk = ""
clear() # rensa skärmen
print("Sprache | Language | Idioma | Språk | 言語")
while(språk == ""): # loopa tills användaren anger giltig inmatning
	print("Deutch (de) | English (en) | español (es) | svenska (sv) | 日本語 (ja)")
	språk = input(": ").strip().lower() # ter en input, tar bort tomma symboler före och efter

	if (språk == "de" or språk == "1" or språk == "deutch"): # tyska
		språk = "de"
	elif (språk == "en" or språk == "2" or språk == "english"): # engelska
		språk = "en"
	elif (språk == "es" or språk == "3" or språk == "español"): # spanska
		språk = "es"
	elif (språk == "sv" or språk == "4" or språk == "svenska"): # svenska
		språk = "sv"
	elif (språk == "ja" or språk == "5" or språk == "日本語"): # svenska
		språk = "ja"
	else:
		clear() # rensa skärmen
		print("Ungültiger Sprache | Invalid language | Idioma no válida | Ogiltigt språk | 無効な言語")
		språk = ""
# > while(språk == ""):

# hämta svårighetsgrad #
nivå = -1
clear() # rensa skärmen
print_tr(s_svårighetA,språk) # skriver ut översättning
while(nivå == -1): # loopa tills användaren anger giltig inmatning
	print_tr(s_svårighetB,språk) # skriver ut översättning
	nivå = input(": ").strip().lower()[:1] # tar en input, tar bort tomma symboler före och efter, gör till små bokstäver, tar ut endast första tecknet; "Svår" blir "s"

	if (nivå == "1" or nivå == "l" or nivå == "e" or nivå == "f" or nivå == "１" or nivå == "Ｅ"):
		nivå = 1 # anger lättaste svårighetsgrad
	elif (nivå == "2" or nivå == "m" or nivå == "２" or nivå == "Ｍ"):
		nivå = 2 # anger medelsvår svårighetsgrad
	elif (nivå == "3" or nivå == "s" or nivå == "h" or nivå == "d" or nivå == "３" or nivå == "Ｈ"):
		nivå = 3 # anger svåraste svårighetsgrad
	elif (nivå == "0" or nivå == "m" or nivå == "u" or nivå == "b" or nivå == "０" or nivå == "Ｕ"):
		nivå = 0 # anger att det är en människa
	else:
		clear() # rensa skärmen
		print_tr(s_svårighet_ogiltig,språk) # skriver ut översättning
		nivå = -1
# > while(nivå == -1):

# börja spelet #
plan = tomt_bräde()
poäng = [0,0]
nästa_drag = 0
clear() # rensa skärmen
if nivå == 0: # om det är två spelare
	spelare = [s_spelareA[språk],s_spelareB[språk]] # ange standardnamnen från s_spelareA och s_spelareB
	spelare_input = input_tr(s_spelarnamnA,språk) # tar en input, text från översättning
	if (spelare_input != ""):
		spelare[0] = spelare_input
	spelare_input = input_tr(s_spelarnamnB,språk) # tar en input, text från översättning
	if (spelare_input != ""):
		spelare[1] = spelare_input
else: # om det är spelare mot datorn
	spelare = [s_spelareS[språk],s_spelareD[språk]] # ange standardnamnen från s_spelareS och s_spelareD
	spelare_input = input_tr(s_spelarnamn,språk) # tar en input, text från översättning
	if (spelare_input != ""):
		spelare[0] = spelare_input

while(1): # primär loop för varje omgång
	clear() # rensa skärmen
	print_tr(s_poängställning,språk,["{P1}","{S1}","{S2}","{P2}"],[spelare[0],poäng[0],poäng[1],spelare[1]]) # skriver ut översättning, ersätter placeholders {} med namn och poäng
	print_tr(s_spelaredrag,språk,["{P}"],[spelare[nästa_drag]]) # skriver ut översättning, ersätter placeholder {P} med spelarens namn
	getch() # vänta på Enter
	while(1): # sekundär loop för varje drag
		clear() # rensa skärmen
		skriv_bräde(plan) # rita ut brädet
		i = -1 # variabel för vilket ruta spelaren väljer
		if nästa_drag == 0: # om det är spelare 1 (användaren), utför detta block
			i = input_tr(s_ruta,språk)[:1] # tar en input, text från översättning, tar ut endast första tecknet
			if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
				i = int(i) # kollar om input är giltigt och anger som en int
			else:
				i = -1 # annars blir det -1 och det är inte giltigt
		# > if nästa_drag == 0:
		elif nästa_drag == 1: # om det är spelare 2 (dator), utför detta block
			if nivå == 1: # lätt
				while(i == -1): # fortsätt så länge i är -1
					i = random.randint(1,9) # slumpa ruta
					if plan[i-1] != -1: # om rutan är upptagen
						i = -1 # återställ till -1
			elif nivå == 2: # mellan
				while(i == -1): # fortsätt så länge i är -1
					i = hitta_två(plan,0) # funktion för att stoppa användaren (spelare: 0)
					if i == -1: # om den inte kan stoppa spelaren
						i = hitta_två(plan,1) # funktion för att få tre i rad (spelare: 1)
					if i == -1: # om den inte kan stoppa spelaren eller få tre i rad
						i = random.randint(1,9) # slumpa ruta
					if plan[i-1] != -1: # om rutan är upptagen
						i = -1 # återställ till -1
			elif nivå == 3: # svår
				while(i == -1): # fortsätt så länge i är -1
					i = hitta_två(plan,1) # funktion för att att få tre i rad (spelare: 1)
					if i == -1: # om den inte kan få tre i rad
						i = hitta_två(plan,0) # funktion för stoppa användaren (spelare: 0)
					if i == -1: # om den inte kan få tre i rad eller stoppa spelaren
						if plan[0] == -1 and plan[1] == -1 and plan[2] == -1 and plan[3] == -1 and plan[4] == -1 and plan[5] == -1 and plan[6] == -1 and plan[7] == -1 and plan[8] == -1:
							i = 1 # prioritera övre vänstra hörnet om brädet är tomt
						elif plan[0] == -1 and plan[1] == -1 and plan[2] == -1 and plan[3] == -1 and plan[4] == 0 and plan[5] == -1 and plan[6] == -1 and plan[7] == -1 and plan[8] == -1:
							i = 1 # prioritera övre vänstra hörnet om brädet om motståndaren har placerat i mitten
						elif plan[4] == -1:
							i = 5 # annars placera i mitten om den är ledig
						elif plan[1] == -1:
							i = 2 # annars placera övre ruta om den är ledig
						elif plan[3] == -1:
							i = 4 # annars placera vänstre ruta om den är ledig
						elif plan[7] == -1:
							i = 8 # annars placera undre ruta om den är ledig
						elif plan[5] == -1:
							i = 6 # annars placera högre ruta om den är ledig
						else:
							i = random.randint(1,9) # slumpa ruta
					if plan[i-1] != -1: # om rutan är upptagen
						i = -1 # återställ till -1
			elif nivå == 0: # om spelare 2 är en människa
				i = input_tr(s_ruta,språk)[:1] # tar en input, text från översättning, tar ut endast första tecknet
				if i == "1" or i == "2" or i == "3" or i == "4" or i == "5" or i == "6" or i == "7" or i == "8" or i == "9":
					i = int(i) # kollar om input är giltigt och anger som en int
				else:
					i = -1 # annars blir det -1 och det är inte giltigt
			else: # error-correction, om ogiltig svårighetsgrad på något sätt har valts
				i = -1 # variabel för vilket ruta spelaren väljer
				for n in range(9): # går igenom brädet i ordning från 0 till 8
					if plan[n] == -1: # om rutan är ledig
						i = n+1 # ange att rutan som blir vald är den första lediga rutan
						break # avsluta att gå igenom alla rutor
				# > for n in range(9):
		# > if nästa_drag == 1:
		if i != -1 and plan[i-1] == -1: # om inmatning är giltig och rutan är tom
			plan[i-1] = nästa_drag # ange rutan att bli spelaren som gör draget
			v = hitta_vinnare(plan) # kolla och spara om någon har vunnit
			if (v != -1):
				poäng[v] += 1 # ge ett poäng till vinnaren
				nästa_drag = 1-v # anger att spelaren som förlorar börjar nästa runda
				clear() # rensa skärmen
				skriv_bräde(plan) # rita ut brädet
				print_tr(s_spelarevinner,språk,["{P}",spelare[v]]) # skriver ut översättning, ersätter placeholder {P} med spelarens namn
				print_tr(s_poängställning,språk,["{P1}","{S1}","{S2}","{P2}"],[spelare[0],poäng[0],poäng[1],spelare[1]]) # skriver ut översättning, ersätter placeholders {} med namn och poäng
				getch() # vänta på Enter
				plan = tomt_bräde() # töm spelplanen
				break # avsluta loopen för denna runda, vilket kommer påbörja en ny runda
			elif plan[0] != -1 and plan[1] != -1 and plan[2] != -1 and plan[3] != -1 and plan[4] != -1 and plan[5] != -1 and plan[6] != -1 and plan[7] != -1 and plan[8] != -1:
				nästa_drag = 1-nästa_drag # invertera variabeln (flippa 0 och 1)
				clear() # rensa skärmen
				skriv_bräde(plan) # rita ut brädet
				print_tr(s_ingenvinner,språk) # skriver ut översättning
				print_tr(s_poängställning,språk,["{P1}","{S1}","{S2}","{P2}"],[spelare[0],poäng[0],poäng[1],spelare[1]]) # skriver ut översättning, ersätter placeholders {} med namn och poäng
				getch() # vänta på Enter
				plan = tomt_bräde() # töm spelplanen
				break # avsluta loopen för denna runda, vilket kommer påbörja en ny runda
			nästa_drag = 1-nästa_drag # invertera variabeln (flippa 0 och 1)
		# > if i != -1 and plan[i-1] == -1:
	# > while(1):
# > while(1):

# SLUT PÅ HUVUDLOOP #