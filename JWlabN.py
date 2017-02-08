# this is a labyrinth text based adventure game. 

from random import randint
import time

player_lvl = 1
player_xp = 10 # current experience points
player_xp_cap = 10 # experience points - to next level
player_str = 3
player_dex = 4
player_int = 2
player_hp = 10 # hit point capacity
player_hp_dmg = 10	# current hit points
player_name = "Unknown"
player_class = "Unknown"
satchel = 100  # total units
satchel_used = 100
satchel_contents = []

loot_lvl_1_3 = ['Sturdy Stick', 'Extra Pack', 'Short Stick', 'Basic Gloves', 
'Spade', 'Rocks', 'Thick Shirt', 'Roll of String', 'Small Medallion']

loot_lvl_4_6 = ['3\' Pipe', 'Extra Large Pack', 'Madrona Wand', 'Fingerless Gloves',
'Shovel', 'Jagged Rocks', 'Leather T-Shirt', 'Short Rope', 'Big Medallion']

loot_lvl_7_9 = ['Sword', 'Duffel Bag', 'Oak Staff', 'Power Mitts',
'Balanced Pickaxe', 'Balanced Jagged Rocks', 'Leather Jacket', 'Long Rope',
'Intricate Medallion'] 

enemies_lvl_1_3 = ['Slime', 'Gnoll', 'Wolf', 'Bat', 'Goblin', 'Cat', 'Flannel Bag',
'Glowing Top Hat', 'Pair of Round Spectacles']

enemies_lvl_4_6 = ['Large Slime', 'Pack of Gnolls', 'Alpha Wolf', 'Ancient Bat', 
'Desperate Goblin', 'Mountain Cat', 'Self Closing Flannel Bag',
'Glowing Top Hat w/ Cane', 'Jagged Contacts']

enemies_lvl_7_9 = ['Shiny Mist', 'Floor of Marbles', 'Shrieking Box', 'Wall of Bats',
'Competetive Eater', 'Donald Trump', 'Mary Poppin\'s Bag of Horrors', 
'Badass Three Piece Suit w/ Hat & Cane', 'Eye Candy']

fathers_wisdom = ['If it\'s the easy way, it\'s probably the wrong way.', 
'Make soup, not war.', 'The fastest way to the end of any journey is slow running.',
'Life isn\'t fair.', 'When the going gets tough, stop and think about things.',
'Give it a little shake and see what falls out.',
'Talking is to be done silently.', 'When talking is silent, silence is golden.',
'Don\'t forget to drink water.', 'Just reach for it. Move!', 
'Club once in awhile, don\'t be a constant clubber.']

mothers_wisdom = ['Take garlic, son. And raw honey.',
'If you take ill, raw honey.', 'Don\'t shake hands with a troll',
'Raw garlic. Feel the burn.', 'Soak your bunions.',
'Never trust a woman with one eye.', 'Always trust a bearded wizard.',
'Can I look at your blackheads?', 'Let\'s go wash your face.', 'Eucalyptus oil.',
'Always use protection.', 'Milk baths are healing.']

prompt = "-> "

came_from = "Unknown"
first_time_first_room = True
first_time_secret_room = True
first_time_chamber_one = True
first_time_second_room = True
first_time_third_room = True
first_time_2nd_secret_room = True

def player_check():
	
	global player_lvl, player_xp, player_str, player_dex, player_int, player_hp
	global player_hp_dmg, player_name, player_class, satchel, satchel_contents
	
	player_hp_dmg = player_hp

	print "Would you like to see your stats or your inventory?"
	choice = raw_input(prompt)
	print " "
	
	if "tats" in choice:
		print """Here are your current stats:\n
		Name: %s, Class: %s
		Strength: %d
		Dexterity: %d
		Intelligence: %d
		Max Hit Points: %d
		Current Hit Points: %d""" % (player_name, player_class, player_str,
		player_dex, player_int, player_hp, player_hp_dmg)
		print " "
	
	elif "nvent" in choice:
	
		if satchel_contents == []:
			print "Your satchel has a capacity of %d and is empty!" % satchel
		
		else:
			print """Here is your current inventory:\n
			Satchel Capacity: %d
			Satchel's available space: %d
			Satchel Contents:
			%d %s""" % (satchel, satchel_used, satchel_contents[1], satchel_contents[0])
			print " "
	
	else:
		print "I'm not sure what you're looking for."

def equip(): #incomplete
	
	global player_str, player_dex, player_int, player_hp
	
	if player_class == "Wizard":
		print "What would you like to equip, good %s?" % player_class
		answer = raw_input(prompt)
	
	elif player_class == "Ninja":
		print "What would you like to equip, dear %s?" % player_class
		answer = raw_input(prompt)
	
	else:
		print "What would you like to equip, hybrid %s?" % player_class
		answer = raw_input(prompt) 

# incomplete def use(): 

def print_enemies_full():

	global enemies_lvl_1_3
	global enemies_lvl_4_6
	global enemies_lvl_7_9
	
	
	print "\nEnemies for Adventurers, Level 1 - 3: "
	for i in range(len(enemies_lvl_1_3)):
		print enemies_lvl_1_3[i]
	print '\n'
	
	print "Enemies for Adventurers, Level 4 - 6: "
	for i in range(len(enemies_lvl_4_6)):
		print enemies_lvl_4_6[i]
	print '\n'
	
	print "Enemies for Adventurers, Level 7 - 9: "
	for i in range(len(enemies_lvl_7_9)):
		print enemies_lvl_7_9[i]

def battle(enemy, enemy_name):
	
	#player list order: Hp, Str, Dex, Int, xp
	#enemy list order: Hp, MaxAttack, xp given, dex
		
	global player_xp, player_hp_dmg
	
	result = "No Hit."
	enemy_hp = enemy[0]
	enemy_attack = 0
	player_attack = 0
			
	
	if enemy[3] > player_dex:
		
		while player_hp_dmg > 0 and enemy_hp > 0:
			
			print "The %s attacks first!" % enemy_name
			time.sleep(2)
			
			enemy_attack = randint(0, enemy[1])
			precision = randint(1, 100)
		
			if precision >= 90:
		
				if precision == 100:
					result = "Unreal Critical Precision!" 
					enemy_attack += 3
				
				else: 
					result = "Critical Precision!" 
					enemy_attack += 2
			
			elif 75 < precision < 90:
				result = "Precision hit!" 
				enemy_attack += 1
			
			elif 30 < precision < 76:
				result = "Hit!"
			
			elif 10 < precision < 31:
				result = "Weak hit!"
				enemy_attack -+ 1
			
			elif 1 < precision <= 10:
			
				if precision == 2:
					result = "Glancing blow." 
					enemy_attack -= 3
				
				elif precision == 1:
					result = "Missed!"
					enemy_attack = 0
				
				else:
					result = "Contact."
					enemy_attack -= 2
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			if enemy_attack < 0:
				enemy_attack = 0
			
			print "The %s strikes you for: %d damage!" % (enemy_name, enemy_attack)
			time.sleep(2)
			
			player_hp_dmg -= enemy_attack
			
			print "You now have %s hit points.\n" % player_hp_dmg
			
			if player_hp_dmg <= 0:
				dead("The %s has defeated you!" % enemy_name)
			
			time.sleep(2)
			print "Now it's your turn to attack!"
			time.sleep(2)
			
			# First attack algorithm:
			# player_attack = x + y + j
			
			# Second attack algorithm:
			# modifier = randint(1, 3)
			# player_attack = (x + y + j) / modifier
	
			# updated attack algorithm:
			x = player_str
			y = player_dex 
			j = player_int
			order = [x, y, j]
			order.sort()
			x = order[0] / 3
			y = order[1] / 2
			j = order[2]
			player_attack = x + y + j
			
			balance = randint(1, 3)
			
			if balance == 1:
				print "Perfectly balanced attack."
			
			elif balance == 2:
				print "Well balanced attack"
				player_attack = player_attack / 2
			
			elif balance == 3:
				print "Off balance attack"
				player_attack = player_attack / 3
			
			else:
				print "This should not ever print. Ever."
			
			precision = randint(1, 100)
			
			if precision >= 90:
			
				if precision == 100:
					result = "Unreal Critical Precision!" 
					player_attack += 3
				
				else: 
					result = "Critical Precision!" 
					player_attack += 2
			
			elif 75 < precision < 90:
				result = "Precision hit!" 
				player_attack += 1
			
			elif 30 < precision < 76:
				result = "Hit!"
			
			elif 10 < precision < 31:
				result = "Weak hit!"
				player_attack -+ 1
			
			elif 1 < precision <= 10:
			
				if precision == 2:
					result = "Glancing blow." 
					player_attack -= 3
				
				elif precision == 1:
					result = "Miss!"
					player_attack = 0
				
				else:
					result = "Contact."
					player_attack -= 2
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			print "You strike the %s for: %d damage!" % (enemy_name, player_attack)
			time.sleep(2)
			
			enemy_hp -= player_attack
			
			print "The %s now has %d hit points.\n" % (enemy_name, enemy_hp)
			time.sleep(2)
			
			if enemy_hp <= 0:
				print "Your enemy fades to dust."
				break
			
		if player_hp_dmg <= 0:
			dead("You've been slain by the %r" % enemy)
	
	else:
		
		while player_hp_dmg > 0 and enemy_hp > 0:
			
			print "You attack!"
			
			time.sleep(2)
		
			x = player_str
			y = player_dex 
			j = player_int
			order = [x, y, j]
			order.sort()
			x = order[0] / 3
			y = order[1] / 2
			j = order[2]
			player_attack = x + y + j
			
			balance = randint(1, 3)
			
			if balance == 1:
				print "Perfectly balanced attack."
			
			elif balance == 2:
				print "Well balanced attack"
				player_attack = player_attack / 2
			
			elif balance == 3:
				print "Off balance attack"
				player_attack = player_attack / 3
			
			else:
				print "This should not ever print. Ever."
			
			precision = randint(1, 100)
			
			if precision >= 90:
			
				if precision == 100:
					result = "Unreal Critical Precision!" 
					player_attack += 3
			
				else: 
					result = "Critical Precision!" 
					player_attack += 2
			
			elif 75 < precision < 90:
				result = "Precision hit!" 
				player_attack += 1
			
			elif 30 < precision < 76:
				result = "Hit!"
			
			elif 10 < precision < 31:
				result = "Weak hit!"
				player_attack -+ 1
			
			elif 1 < precision <= 10:
			
				if precision == 2:
					result = "Glancing blow." 
					player_attack -= 3
			
				elif precision == 1:
					result = "Miss!"
					player_attack = 0
			
				else:
					result = "Contact."
					player_attack -= 2
			
			else:
				result = "This shouldn't ever print."
				
			print result
			
			print "You strike the %s for: %d damage!" % (enemy_name, player_attack)
			
			enemy_hp -= player_attack
			
			print "The %s now has %d hit points.\n" % (enemy_name, enemy_hp)
			
			time.sleep(2)
			
			if enemy_hp <= 0:
			
				print "You're enemy fades to dust."
				break 
				
			print "Now it's the %s\'s turn!" % enemy_name
			
			time.sleep(2)
			
			enemy_attack = randint(0, enemy[1])
			precision = randint(1, 100)
		
			if precision >= 90:
		
				if precision == 100:
					result = "Unreal Critical Precision!" 
					enemy_attack += 3
		
				else: 
					result = "Critical Precision!" 
					enemy_attack += 2
		
			elif 75 < precision < 90:
				result = "Precision hit!" 
				enemy_attack += 1
		
			elif 30 < precision < 76:
				result = "Hit!"
		
			elif 10 < precision < 31:
				result = "Weak hit!"
				enemy_attack -+ 1
		
			elif 1 < precision <= 10:
			
				if precision == 2:
					result = "Glancing blow." 
					enemy_attack -= 3
			
				elif precision == 1:
					result = "Miss!"
					enemy_attack = 0
			
				else:
					result = "Contact."
					enemy_attack -= 2
			
			else:
			
				result = "This shouldn't ever print."
				
			print result
			
			if enemy_attack < 0:
				enemy_attack = 0
			
			print "The %s strikes you for: %d damage!" % (enemy_name, enemy_attack)
			player_hp_dmg -= enemy_attack
			
			print "You now have %s hit points.\n" % player_hp_dmg
			
			time.sleep(2)		
			
			if player_hp_dmg <= 0:
				dead("You've been defeated by the %s." % enemy_name)
			
		if player_hp_dmg <= 0:
			dead("You've been DEFEATED by the %s" % enemy_name)
			
	
	print "You win!\n"
	
	print "You've gained %d experience points!\n" % enemy[2]
	
	time.sleep(2)
	
	player_xp -= enemy[2]
	
	if player_xp <= 0:
		level_up()
		player_xp = player_xp_cap
	
	print "You have %d experience points to gain before you level up.\n" % player_xp

def enemy_encounter():
	
	global player_hp, player_xp, enemies_lvl_1_3, enemies_lvl_4_6, enemies_lvl_7_9
	global player_lvl
	
	x = randint(0, 8)
	
	if 0 < player_lvl <= 3:
		
		enemy = enemies_lvl_1_3[x]
		enemy_name = enemy
		#Enemy form: (hp, max_attack, gives_xp, dex)
		if x == 0:
			enemy = (6, 4, 3, 1) #slime 14
		
		elif x == 1:
			enemy = (6, 5, 4, 5) #gnoll 20
		
		elif x == 2:
			enemy = (6, 6, 5, 6) #wolf 23
		
		elif x == 3: 
			enemy = (4, 4, 5, 10) #bat 23
		
		elif x == 4:
			enemy = (6, 5, 5, 6) #goblin 22
		
		elif x == 5:
			enemy = (3, 3, 3, 8) #cat 17
		
		elif x == 6:
			enemy = (6, 3, 3, 1) #flannel_bag 13
		
		elif x == 7:
			enemy = (10, 2, 5, 2) #glowing_top_hat 19
		
		else:
			enemy = (5, 3, 2, 2) #round_spectacles() 12
	
	elif 3 < player_lvl <= 6:
		
		enemy = enemies_lvl_4_6[x]
		enemy_name = enemy
		
		if x == 0:
			enemy = (9, 7, 6, 2) #lg_slime 24
		
		elif x == 1:
			enemy = (10, 10, 10, 8) #gnoll_pack 38
		
		elif x == 2:
			enemy = (9, 9, 7, 7) #alpha_wolf 32
		
		elif x == 3: 
			enemy = (6, 10, 8, 12) #ancient_bat 36
		
		elif x == 4:
			enemy = (4, 12, 6, 6) #desperate_goblin 28
		
		elif x == 5:
			enemy = (6, 6, 6, 10) #mountain_cat 28
		
		elif x == 6:
			enemy = (5, 10, 6, 3) #self_closing_flannel_bag 24
		
		elif x == 7:
			enemy = (10, 8, 6, 2) #glowing_top_hat_w_cane 26
		
		else:
			enemy = (6, 8, 5, 3) #jagged_contacts 22
	
	elif 6 < player_lvl <= 9:
		
		enemy = enemies_lvl_7_9[x]
		enemy_name = enemy
	
		if x == 0:
			enemy = (12, 15, 12, 8) #shiny_mist 47
		
		elif x == 1:
			enemy = (13, 2, 10, 18) #floor_of_marbles 43
		
		elif x == 2:
			enemy = (8, 14, 9, 5) #shrieking_box 36
		
		elif x == 3: 
			enemy = (12, 12, 12, 5) #wall_of_bats 41
		
		elif x == 4:
			enemy = (18, 5, 9, 3) #competetive_eater 35
		
		elif x == 5:
			enemy = (10, 15, 14, 1) #donald_trump 40
		
		elif x == 6:
			enemy = (15, 18, 14, 4) #mary_poppins_bag_of_horrors 51
		
		elif x == 7:
			enemy = (12, 13, 14, 11) #badass_3_suit_hat_cane 50
		
		else:
			enemy = (1, 20, 15, 20) #eye_candy 56
	
	else:
		return "Did not work!"
	
	print "You've run into an enemy!" 
	print "It's a %s" % enemy_name
	
	print "Are you going to fight or flee?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		player_check()
		
		print "Are you going to fight or flee?"
		choice = raw_input(prompt)
		print " "
	
	if "ight" in choice: 
	
		print "You and the %s fight!" % enemy_name
		battle(enemy, enemy_name)
	
	else: 
	
		if enemy[3] > player_dex:
			dead("""Wow, you're slow. As you turn around and expose your neck,
			the %s attacks and it kills ya.""" % enemy_name) 
		
		else:
			print "Because of your superior quickness, you escape." 

def level_up():
	
	global player_lvl, player_xp_cap, player_str, player_dex, player_int, player_hp
	global player_hp_dmg
	
	print "You've leveled up! Congrats, that's awesome!\n" 
	time.sleep(4)
	
	print """These are your old stats:
	Level: %d
	Strength: %d
	Dexterity: %d
	Intelligence: %d
	Hit Points: %d""" % (player_lvl, player_str, player_dex, player_int, player_hp)
	
	player_lvl += 1
	player_xp_cap *= 2
	player_xp = player_xp_cap
	
	if player_class == "Wizard":
		
		player_str += randint(0, 1)
		player_dex += randint(0, 1)
		player_int += randint(2, 4)
	
	elif player_class == "Ninja":
		
		player_str += randint(0, 2)
		player_dex += randint(1, 4)
		player_int += randint(0, 1)
	
	else:
		player_str += randint(0, 3)
		player_dex += randint(0, 3)
		player_int += randint(0, 3)
	
	player_hp += randint(2, 5)
	player_hp_dmg = player_hp
	time.sleep(3)
	
	print """These are your new stats: 
	Level: %d
	Strength: %d
	Dexterity: %d
	Intelligence: %d
	Hit Points: %d""" % (player_lvl, player_str, player_dex, player_int, player_hp)

def start():
	
	global first_time_secret_room, first_time_first_room, came_from
	
	first_time_secret_room = True
	first_time_first_room = True
	
	print "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n"
	print "\n\n\t\tLabryinth of the Lost Sons\n\n\n"
	
	time.sleep(2)
	print "Thanks for playing.\n"
	print "At any time type 'player' to see your stats or inventory."
	print "\n\n\n"
	time.sleep(2)
	
	print """You awaken. It feels like you shouldn't be here or you're lost. 
	It's a strange feeling. You get up and look around you. You see barren 
	fields and a grey sky.\n"""
	time.sleep(3)
	
	print """You turn around and there is a high concrete wall stretching far 
	in either direction. It seems like forever.\n"""
	time.sleep(3)
	
	print """There is thin rectangular opening in the concrete and sitting next 
	to the opening is an old woman. You approach the woman and she sees you."""
	time.sleep(3)
	
	print "\nOld Woman: 'I see you're awake. You came out of nowhere it seems.'\n"
	
	build_character()
	
	print "Old Woman: 'Are you on a quest? Or just hanging out? Or What?'"
	
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Old Woman: 'Are you on a quest? Or just hanging out?'"
		answer = raw_input(prompt)
		print " "
	
	if "uest" in answer: 
		
		print "'Oh, a quest, eh?" 
		time.sleep(2)
		print "This labryinth holds great treasure. And danger. Did I mention danger?"
		print "Are you willing to proceed?'"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			player_check()
			
			print "Are you willing to proceed?'"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision: 
			print "'Best luck in there!'"
			came_from = "South"
			first_intersection()
		
		else:
			dead("The old woman rises up in a fury and one-punch kills you.")
	
	elif "ang" in answer:
		
		print """'You're so cool. I wish any one of my twelve sons were as cool 
		as you are. Are you single?"""
		time.sleep(1)
		
		print "Just kidding. It's fine. I didn't mean it anyway."
		
		time.sleep(2)
		print """Speaking of my kids... I lost them.
		They're in the labrynth and I'm certain they're being held prisoner
		or lost somewhere...""" 
		time.sleep(1)
		print "Woe is me!! I have the gout."
		
		print "Will you help me?'"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			
			player_check()
			
			print "Will you help me?'"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision:
			print "'Oh, thank you! Send them back to me when you've found them."
			print "Good luck!'"
			came_from = "South"
			first_intersection()
		
		elif "Ye" in decision:
			print "Oh, I knew I could trust you."
			print "Send them back safely!"
			came_from = "South"
			first_intersection()
		
		elif "YE" in decision:
			print "My hero!! Oh, I love a man that does what's right."
			print "I look forward to seeing you all real soon."
			print "Good luck now, ya hear?" 
			came_from = "South"
			first_intersection()
		
		else: 
			print "'I curse you then! May death be upon your door!'\n\n\n.\n..\n..."
			print "You walk awkwardly past the woman and into the labrynth."
			print "The wall of the labryinth breaks for no apparent reason."
			dead("The wall falls on you and the woman laughs as you perish.")
	
	else: 
		print "'That doesn't suprise me."
		print "I think whatever you're looking for is in this labryinth."
		print "There's some pretty sweet loot and basically no danger."
		print "Are you going to enter the labryinth?'"
		
		decision = raw_input(prompt)
		print " "
		
		while decision == "player":
			
			player_check()
			
			print "Are you going to enter the labryinth?'"
			decision = raw_input(prompt)
			print " "
		
		if "ye" in decision: 
			print "'Best luck in there, you mysterious %s'" % player_class
			came_from = "South"
			first_intersection()
		
		else:
			dead("The old woman starts to sing and\nsuddenly your head explodes.")

def build_character():

	global player_name, player_class, player_str, player_dex, player_int
								
	print "'What, may I ask, is your name sweet traveler?'"
	player_name = raw_input(prompt)
	print " "
	
	while player_name == "player":
		
		player_check()
		
		print "'What, may I ask, is your name sweet traveler?'"
		player_name = raw_input(prompt)
		print " "
	
	print "'And what type of a hero are you, %s?'" % player_name
	print "\t 1. Pro Wizard"
	print "\t 2. Master Ninja"
	print "\t 3. Amatuer Wizard, decent Ninja"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "'And what type of a hero are you, %s?'" % player_name
		print "\t 1. Pro Wizard"
		print "\t 2. Master Ninja"
		print "\t 3. Amatuer Wizard, decent Ninja"
		choice = raw_input(prompt)
		print " "
	
	if "1" in choice:
		
		player_class = "Wizard"
		player_str = 1
		player_dex = 2
		player_int = 6
	
	elif "2" in choice:
		
		player_class = "Ninja"
	
	else:
		player_class = "Wizard/Ninja"
		player_str = 3
		player_dex = 3
		player_int = 3
	
	print "'Ahh, %s the %s! Exciting!'" % (player_name, player_class)
	print "'Jeez. I haven't seen a %s in ages...'""" % player_class
	time.sleep(2)
	
	print "'Actually, I haven't seen anyone in ages."
	print "You look really good. Seriously, have you looked at yourself lately?'"
	print " "
	time.sleep(2)
	
	print "Type 'player' to check yourself out." 
	choice2 = raw_input(prompt)
	print " "
	
	if "player" in choice2: 
		
		player_check()
	
	else:
		
		print "Or not..."

def first_intersection():

	global came_from
	
	print " "
	print "The hallway is dark but enough light is present to see around." 
	print "You may choose to travel North, West, or East."
	print "You came from the %s." % came_from
	print "Which direction do you choose?" 
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "Which direction do you choose?" 
		choice = raw_input(prompt)
		print " "
	
	if "est" in choice:
		
		print "You go West and come to an elbow leading North."
		time.sleep(2)
		
		print """You follow the elbow and are in a corridor that smells like dust 
		and decay."""
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		time.sleep(2)
		print "As you walk you see a 6 inch bookcase on your left."
		print "There is a Red Book, a Green Book, and a Blue Book."
		print "Do you move on or do you inspect a book?"
		
		choice2 = raw_input(prompt)
		print " "
		
		while choice2 == "player":
			
			player_check()
			
			print "Do you move on or do you inspect a book?"
			choice2 = raw_input(prompt)
			print " "
		
		if "move" in choice2:
			
			print "You go around the corner and come to another intersection."
			came_from = "West"
			chance = randint(1, 100)
			
			if chance <= 60:
				enemy_encounter()
			second_intersection()
		
		elif "inspect" in choice2:
			secret_room_1()
		
		else: 
			print "I wish I was human! Then I could understand you!"
			dead("A wave of sound comes and crushes your skull.")
							
	elif "ast" in choice:
		
		print """You follow the path East, which comes to an elbow that
		heads North. You follow that path and come to another intersection."""
		came_from = "South"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		third_intersection()
		
	else: 
		print "You head North and come to a T intersection, branching West and East."
		came_from = "South"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		second_intersection()

def secret_room_1():

	global came_from, player_int, player_dex, player_str, first_time_secret_room
		
	print "Interesting. You're curious. I like that."
	print "Which one book would you like to inspect?"
	print "1. Red Book"
	print "2. Green Book"
	print "3. Blue Book"
			
	choice3 = raw_input(prompt)
	print " "
	
	while choice3 == "player":
		
		player_check()
		
		print "Which one book would you like to inspect?"
		print "1. Red Book"
		print "2. Green Book"	
		print "3. Blue Book"
		choice3 = raw_input(prompt)
		print " "
			
	if "1" in choice3:
		
		print """
		You take the Red Book off the shelf and read the title; 
		'Making Friends with Blood Pacts' 
		by 'Glungoral the Witty' 
		You flip through the book, finding it boorish. You put the book back and
		can now decide to go North or South in the corridor."""
		came_from = "West"
		
		choice = raw_input(prompt)
		print " "
		
		while choice == "player":
			
			player_check()
			
			print "Would you like to go North or South in the corridor?"
			choice = raw_input(prompt)
			print " "
		
		if "orth" in choice:
			second_intersection()
		
		else:
			first_intersection()
						
	elif "2" in choice3:
		print """
		You take the Green book off the shelf and read the title; 
		'Pushing Past Your Own Insecurities for Fun and Profit!' 
		by 'Mungorak the Pleasant'
		You flip through the book and it quickly becomes your favorite, but you've
		got no time to read, so you put the book back and can now decide to go North 
		or South in the corridor."""
		came_from = "West"
		
		choice = raw_input(prompt)
		print " "
		
		while choice == "player":
			player_check()
			
			print "Would you like to go North or South in the corridor?"
			choice = raw_input(prompt)
			print " "
		
		if "orth" in choice:
			print "You go North."
			second_intersection()
		
		else:
			print "You go South."
			first_intersection()
			
	elif "3" in choice3:
		print """
		As you attempt to take the Blue Book off the shelf, you feel it
		stick and then click mechanically into place as it comes forward. The book 
		gets sucked back onto the shelf and a panel in the wall moves aside,
		revealing a passageway."""
		time.sleep(5)
		print "Do you enter the passageway?" 
				
		choice4 = raw_input(prompt)
		print " "
		
		while choice4 == "player":
			
			player_check()
			
			print "Do you enter the passageway?"
			choice4 = raw_input(prompt)
			print " "
				
		if "ye" in choice4:
			came_from = "West"
			
			print "The passageway is short and leads to a secret room!"
			
			if !first_time_secret_room:
				print "You're standing in the secret room you hung out in earlier."
				time.sleep(2)
				print "You remember the good times you had, then you turn around"
				print "and leave the room because there's nothing in there anymore." 
				print "Do you go North or South?"
				choice1 = raw_input(prompt)
				print " "
				
				while choice1 == "player":
					
					player_check()
					
					print "Do you go North or South?"
					choice1 = raw_input(prompt)
					print " "
						
				if "orth" in choice1:
					print "North you go!"
					second_intersection()
				
				else: 
					print "South it is!"
					first_intersection()
			
			while first_time_secret_room:
				
				first_time_secret_room = False
				enemy_encounter()
				
				print """
				Now that you stand victorious, you notice there is a shaft
				of light highlighting a sweet looking chocolate danish on a narrow 
				pedestal.\n"""
				time.sleep(3)
				
				print "\nYou examine it closely.\n"
				time.sleep(3)
				
				print "You don't want to put it in your satchel (messy!)."
				time.sleep(2)
				
				print "And it smells so good! You must eat it or leave it."
				time.sleep(2)
				
				print "Eat it or leave it?"
				choice5 = raw_input(prompt)
				print " "
		
				while choice5 == "player":
					
					player_check()
			
					print "Do you eat the danish?"
					choice5 = raw_input(prompt)
					print " "
					
				if "eat" in choice5:
					print "You've never tasted anything so delicious and fresh!"
					
					if player_class == "Wizard":
						
						player_int += 1
						print "The danish expands your brain by five percent."
						print "Your intelligence has grown by one. It is now %d." % player_int
						time.sleep(3)
						print "You leave the secret room."
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
						while choice1 == "player":
							player_check()
							print "Do you go North or South?"
							choice1 = raw_input(prompt)
							print " "
							
						if "orth" in choice1:
							print "North you go!"
							second_intersection()
						
						else: 
							print "South it is!"
							first_intersection()
							
					elif player_class == "Ninja":
						
						player_dex += 1
						print "The danish hones your muscles and heightens your quickness."
						print "Your dexterity has grown by one. It is now %d." % player_dex
						time.sleep(3)
						print "You leave the secret room."
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
						while choice1 == "player":
							
							player_check()
							
							print "Do you go North or South?"
							choice1 = raw_input(prompt)
							print " "
							
						if "orth" in choice1:
							print "North you go!"
							second_intersection()
						
						else: 
							print "South it is!"
							first_intersection()	
					else:
						
						player_str += 1
						print "Suddenly you flex and feel more power."
						print "Your strength has grown by one. It is now %d." % player_str
						time.sleep(3)
						print "You leave the secret room."
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
						while choice1 == "player":
							
							player_check()
							
							print "Do you go North or South?"
							choice1 = raw_input(prompt)
							print " "
							
						if "orth" in choice1:
							print "North you go!"
							second_intersection()
						
						else: 
							print "South it is!"
							first_intersection()
							
				else:
					print "You back away from the danish... slowly back away."
					time.sleep(4)
					print "Phew! That thing looked too delicious to be of any use!"
					print "Do you go North or South?"
					choice1 = raw_input(prompt)
					print " "
					
					while choice1 == "player":
						
						player_check()
						
						print "Do you go North or South?"
						choice1 = raw_input(prompt)
						print " "
						
					if "orth" in choice1:
						print "North you go!"
						second_intersection()
					
					else: 
						print "South it is!"
						first_intersection()
			 	
		elif "no" in choice4:
			print """
			Yeah, who in their right mind would go in there!? It's probably 
			haunted or something. Definitely worth avoiding. You leave the panel and
			can now decide to go North or South in the corridor."""
			came_from = "West"
			
			choice2 = raw_input(prompt)
			print " "
			
			while choice2 == "player":
				
				player_check()
				
				print "Would you like to go North or South in the corridor?"
				choice2 = raw_input(prompt)
				print " "
			
			if "orth" in choice2:
				print "You go North."
				second_intersection()
			
			else:
				print "You go South."
				first_intersection()
				
		else: 
			dead("Standing. Waiting. The floor opens and you fall into eternity.")
			
	else: 
		print "I wish I knew what you chose, but... you cryptic!"
		time.sleep(3)
		dead("""Standing and waiting, suddenly the floor 
		opens up and you fall onto some well made spikes.""")

def second_intersection():

	global came_from
	global player_hp

	print "You are at an intersection that has passageways to the South, West, and East"
	print "You came from the %s." % came_from
	print "Which way do you go?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
		
		print "Which way do you go?"
		choice = raw_input(prompt)
		print " "
	
	if "outh" in choice:
		print "You move South."
		came_from = "North"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		first_intersection()
	
	elif "ast" in choice:
		print "You move East"
		came_from = "West"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		third_intersection()
	
	elif "est" in choice:
		print "You go West and come to an elbow leading South."
		time.sleep(2)
		print """You follow the elbow and are in a corridor that smells like dust 
		and decay."""
		time.sleep(2)
		print "As you walk you see a 6 inch bookcase on your right."
		print "There is a Red Book, a Green Book, and a Blue Book."
		print "Do you move on or do you inspect a book?"
		
		choice2 = raw_input(prompt)
		print " "
		
		while choice2 == "player":
			
			player_check()
			
			print "Do you move on or do you inspect a book?"
			choice2 = raw_input(prompt)
			print " "
		
		if "move" in choice2:
			print "You go around the corner and come to another intersection."
			came_from = "West"
			chance = randint(1, 100)
			
			if chance <= 50:
				enemy_encounter()
			first_intersection()
		
		elif "inspect" in choice2:
			secret_room_1()
	
	elif "orth" in choice:
		print "You try to head North, but run into the concrete wall."
		player_hp -= 1
		print "You lost a hit point! you now have %d hit points." % player_hp
		chance = randint(1, 100)
	
		if chance <= 50:
			enemy_encounter()
		second_intersection()
	else:
		dead("triggering dead")

def third_intersection():

	global came_from
	global player_hp
	
	print """You are at an intersection with passageways to the South, West, and
	East. \nThere is a door along the wall to the South/West."""
	print "You came from %s." % came_from
	print "Which way do you go?"
	
	choice = raw_input(prompt)
	print " "
	
	while choice == "player":
		
		player_check()
	
		print "Which way do you go?"
		choice = raw_input(prompt)
		print " "
			
	if "door" in choice:
	
		first_room()
	
	elif "outh" in choice:
		print "You head South, turn a corner to going West, and"
		print "Come to another intersection."
		came_from = "East"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		first_intersection()
	
	elif "est" in choice:
		print "You head West and come to another intersection."
		came_from = "East"
		chance = randint(1, 100)
		
		if chance <= 50:
			enemy_encounter()
		second_intersection()
	
	elif "ast" in choice:
		print "You head East... and the hallway turns slightly and"
		print "you head up some stone stairs. Upon reaching the top,"
		print "a great chamber comes into view!"
		came_from = "Southwest"
		
		first_chamber()
	
	elif "orth" in choice:
		print "You try to head North, but run into the concrete wall."
		player_hp -= 1
		print "You lost a hit point! you now have %d hit points." % player_hp
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		third_intersection()
	
	else:
		dead("Triggering DEATH")
	
	third_intersection()

def first_room():
	
	global satchel, satchel_contents, came_from, first_time_first_room
	came_from = "The Room"
	
	while first_time_first_room:
	
		first_time_first_room = False
	
		print "You open the door and step into a room full of rubies!"
		time.sleep(2)
		print "Rubies each occupy 1 unit of space in your satchel."
		print "How many do you take?"
	
		choice = int(raw_input(prompt))
		print " "
		
		while choice == "player":
			
			player_check()
			
			print "How many do you take?"
			choice = int(raw_input(prompt))
			print " "
				
		if 0 < choice <= satchel:
			
			print "You put %d rubies in your bag." % choice
			
			satchel_contents.append("Rubies")
			satchel_contents.append(choice)
			satchel = satchel - choice
			time.sleep(2)
			
			print "Your satchel contains %r" % satchel_contents
			print "You have %d units of space left in your satchel." % satchel
			
			third_intersection()
		else:
			print "Your greed angers a nearby enemy!"
			
			enemy_encounter()
			
			print "You stand victorious."
			time.sleep(2)
			
			print "How many rubies do you take?"
			choice = int(raw_input(prompt))
			print " "
	
			while choice == "player":
				
				player_check()
			
				print "How many do you take?"
				choice = int(raw_input(prompt))
				print " "
				
			if 0 < choice <= satchel:
				
				print "You put %d rubies in your bag." % choice
				
				satchel_contents.append("Rubies")
				satchel_contents.append(choice)
				satchel = satchel - choice
				
				print "Your satchel contains %r" % satchel_contents
				print "You have %d units of space left in your satchel." % satchel
				
				third_intersection()
			
			else:
				print "You temporarily lose memory and wake up in the hallway."
				
				third_intersection()
					
	print "You stand in the familiar doorway. All of the rubies have vanished."
	time.sleep(3)
	print """You sniff and cry a little, then you get over it and get back to 
	the hallway."""
	
	third_intersection()

def first_chamber():

	global came_from, first_time_chamber_one
	
	print "The chamber before you is a grand open chamber."
	print "There are doors exiting the chamber in all directions."
	print "You came from the %s." % came_from
	
	if first_time_chamber_one:
		print "You see an older boy chained to a chair in the middle of the chamber."
	
	else: 
		print "You are alone in the chamber."
	
	print "What would you like to do? Approach the boy or take a door?" 
	answer = raw_input(prompt)
	print " " 
	
	while answer == "player":
		player_check()
		
		print "What would you like to do? Approach the boy or take a door?"
		answer = raw_input(prompt)
	
	if "boy" in answer:
		
		print "You approach the boy."
		time.sleep(1)
		print "He looks up at hearing your footsteps."
		time.sleep(1)
		print "'Hello there! I haven't seen anyone in so long, I don't even"
		print "know how I'm still alive.'"
		time.sleep(2)
		print "'Are you here to help me?'"
		
		answer1 = raw_input(prompt)
		
		while answer1 == "player":
			
			player_check()
			
			print "'Are you here to help me?'"
			answer1 = raw_input(prompt)
			print " "
			
		if "ye" in answer1:
			print "'Wonderful! My chains are secured to the ground by stone.'"
			print "'Are you able to free me?'"
			answer2 = raw_input(prompt)
			print " " 
			
			while answer2 == "player":
				player_check()
				
				print "'Are you able to free me?'"
				answer2 = raw_input(prompt)
				print " "
				
			if "ye" in answer2:
				print "'Excellent! I'm waiting'"
			
			else:
				print "'Oh well, maybe later.'" 
		
		else: 
			print "That's okay. I kind of like this chair anyway. I do miss"
			print "being able to scratch my ear though."

	elif "door" in answer:
		
		print "Which door would you like to take?"
		
		came_from = "Chamber"
		
		print """
		1. West
		2. Northwest
		3. North
		4. Northeast
		5. East
		6. Southeast
		7. South
		8. Southwest"""
		
		answer3 = raw_input(prompt)
		
		while answer3 == "player":
			
			player_check()
			
			print "Which door would you like to take?"
			print """
			1. West
			2. Northwest
			3. North
			4. Northeast
			5. East
			6. Southeast
			7. South
			8. Southwest"""
			
			answer3 = raw_input(prompt)
		
		if answer3 == "1":
			print "You go through the west leading door and arrive shortly"
			print "at a T-intersection."
			
			sixth_intersection()
		
		elif answer3 == "2":
			print "You go through the northwest leading door."
			print "It leads you down a stone stairway."
			
			seventh_intersection()
		
		elif answer3 == "3":
			print "You go through the north leading door."
			
			twelfth_intersection()
		
		elif answer3 == "4":
			print "You go through the northeast leading door."
			
			vendor_room()
		
		elif answer3 == "5":
			print "You go through the east leading door and arrive at a four way"
			print "intersection."
			
			eighth_intersection()
		
		elif answer3 == "6":
			print "You go through the southeast leading door."
			
			third_room()
		
		elif answer3 == "7":
			print "You go through the south leading door and come to a"
			print "T-intersection."
			
			fourth_intersection()
		
		elif answer3 == "8":
			print "You go through the southwest leading door and walk down some"
			print "stone steps."
			
			third_intersection()
		
		else: 
			print "You're still in the chamber." 
			
			first_chamber()
	
	else: 
		first_chamber()
		
def fourth_intersection():

	global came_from
	
	print "You are at an intersection that branches West, East, and North,"
	print "You came from the %s." % came_from
	
	print "Which way do you go?"
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "est" in answer:
		print "You head west and..."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "...you come to a large room!" 
		came_from = "East"
		second_room()
	elif "ast" in answer:
		print "You head east and..."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "...you come to another intersection."
		came_from = "West"
		fifth_intersection()
	else: 
		print "You head north and..."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "... you enter the chamber." 
		came_from = "South"
		first_chamber()

def fifth_intersection():
	
	global came_from
	
	print "You are at an intersection that branches West, East, and South,"
	print "You came from the %s." % came_from
	
	print "Which way do you go?"
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
		
	if "outh" in answer:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You find yourself in a small dead end. In the floor, centered to"
		print "the back wall, stands a small pedestal with a circular top."
		time.sleep(2)
		
		print "You cannot find any way to interact with the pedestal so you turn"
		print "back around."
		came_from = "South"
		fifth_intersection()
	elif "ast" in answer: 
		print "You abruptly come upon the edge of a pit." 
		time.sleep(2)
		print "You can see the other side, though it is quite a distance." 
		print "There is tree trunk hanging over the labryinth wall."
		time.sleep(2)
		print "The trunk is well above you and in between the path you stand on"
		print "and the path across the pit."
		print "Do you do something or go back?"
		to_do = raw_input(prompt)
		if "back" in to_do:
			came_from = "East"
			fifth_intersection()
	else:
		print "You head West and..."
		came_from = "West"
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "...you come to another intersection."
		fourth_intersection()

def sixth_intersection():

	global came_from
	
	print "You can see that both the North and the South paths turn a"
	print "corner heading in the same direction."
	print "You came from %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "outh" in answer:
		print "You head South, turning the corner to the West." 
		time.sleep(2)
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You walk along a narrow corridor until you reach an elbow heading"
		print "North. Now you walk and stop between two walls." 
		time.sleep(2)
		print "On your left the wall is blank. On the right there are three"
		print "protruding circles." 
		print "You can go North or South or examine the wall."
		answer1 = raw_input(prompt)
		while answer1 == "player":
			player_check()
			
			print "You can go North or South or examine the wall."
			answer1 = raw_input(prompt)
		
		if "xamin" in answer1:
			print "Looking more closely, you see that the circles move, but you"
			print "you cannot make odds or ends of it." 
			sixth_intersection()
		elif "outh" in answer1: 
			print "You go South."
			sixth_intersection()
		else:
			print "You go North."
			sixth_intersection()
	elif "orth" in answer: 
		print "You head North, turning the corner to the West." 
		time.sleep(2)
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You walk along a narrow corridor until you reach an elbow heading"
		print "South. Now you walk and stop between two walls." 
		time.sleep(2)
		print "On your right the wall is blank. On the left there are three"
		print "protruding circles." 
		print "You can go North or South or examine the wall."
		answer1 = raw_input(prompt)
		while answer1 == "player":
			player_check()
			
			print "You can go North or South or examine the wall."
			answer1 = raw_input(prompt)
		
		if "xamin" in answer1:
			print "Looking more closely, you see that the circles move, but you"
			print "you cannot make odds or ends of it." 
		elif "outh" in answer1: 
			print "You go South."
			chance = randint(1, 100)
			if chance <= 50:
				enemy_encounter()
			sixth_intersection()
		else:
			print "You go North."
			chance = randint(1, 100)
			if chance <= 50:
				enemy_encounter()
			sixth_intersection()
	else: 
		sixth_intersection()

def seventh_intersection():

	global came_from
	
	print "Heading down the stone steps, you come to an intersection." 
	print "the intersection goes West or North."
	print "You came from the %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "est" in answer: 
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head West and shortly come to a dead end. It's different than"
		print "a normal dead end, because the top of the wall at this dead end"
		print "is much shorter than the walls surrounding it."
		time.sleep(2)
		print "You can't do anything at this time so you go back to the intersection."
		seventh_intersection()
	elif "orth" in answer:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head North and come to another intersection."
		came_from = "South"
		eleventh_intersection()
	else:
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You head back up the stairs."
		came_from = "Northwest"
		first_chamber()

def eighth_intersection():

	global came_from
	
	print "You stand in a four-way intersection."
	print "You can go North, South, East, or West."
	print "You came from the %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "orth" in answer:
		print "You head North."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You've come to another intersection."
		came_from = "South"
	elif "outh" in answer:
		print "You head South."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "The corridor turns an elbow to the east." 
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "The corridor turns into a dead end. The wall at the end has"
		print "an intricately carved inlay on the wall, centered by a hollow"
		print "circular form." 
		print "You can't seem to do anything, so you turn around and go back."
		came_from = "South"
		eighth_intersection()
	elif "ast" in answer:
		print "You head East and enter a long room."
		enemy_encounter()
		fourth_room()
	else:
		print "You head West."
		first_chamber()

def ninth_intersection():

	global came_from
	
	print "You stand at a three-way intersection."
	print "You can go North, South, or East."
	print "You came from the %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "ast" in answer:
		print "You head East and immediately the corridor takes you South."
		print "You come to a dead end with a portrait hanging on the wall."
		print "The portrait is of the old woman you saw at the beginning of"
		print "the labryinth."
		came_from = "East"
		ninth_intersection()
	elif "orth" in answer:
		print "You head North."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You find yourself at the back of a Grand Hallway."
		grand_hallway()
	else:
		print "You head South."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		eighth_intersection()
		
# incomplete def tenth_intersection():

def eleventh_intersection():
	
	global came_from
	
	print "You stand at an intersection that leads North, East, or South."
	print "You came from the %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "orth" in answer:
		print "You approach the mouth of a cave!" 
		print "Do you go into the cave?"

		answer1 = raw_input(prompt)
		print " "
		
		while answer1 == "player":
			player_check()
			
			print "Do you go into the cave?"
			answer1 = raw_input(prompt)
			print " "
		
		if "ye" in answer1:
			came_from = "South"
			battle_cave()
		else: 
			eleventh_intersection()
	elif "ast" in answer: 
		print "You head East along a long corridor."
		time.sleep(2)
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		print "You come to a large intersection."
		came_from = "West"
		twelfth_intersection()
	else: 
		print "You head South."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		came_from = "North"
		seventh_intersection
	
def twelfth_intersection():

	global came_from
	
	print "The large intersection holds an immense Grand Hallway to the East."
	print "You may go East to the hallway or North or South."
	print "You came from the %s." % came_from
	chance = randint(1, 100)
	if chance <= 50:
		enemy_encounter()
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " "
	
	if "ast" in answer:
		print "You find yourself in the Grand Hallway."
		chance = randint(1, 100)
		if chance <= 80:
			enemy_encounter()
		grand_hallway()
	elif "outh" in answer:
		print "You head South."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		came_from = "North"
		first_chamber()
	else:
		print "That part of the labryinth hasn't been coded yet."
		chance = randint(1, 100)
		if chance <= 50:
			enemy_encounter()
		twelfth_intersection()		

def second_room():

	global came_from
	came_from = "East"
	
	print "You enter a large room full of caskets." 
	print "You came from the %s." % came_from
	enemy_encounter()
	print "You try to open the caskets and see that they are all"
	print "made of solid stone." 
	
	print "You exit the room and come to an intersection."
	came_from = "West"
	fourth_intersection()

def third_room():
	
	global came_from
	
	print "The door you took leads directly into a small room."
	print "You came from the %s." % came_from
	enemy_encounter()
	print "There is some sweet art in this room. Dang. Good stuff." 
	print "You head back to the chamber."
	came_from = "Southeast"
	first_chamber()
	
def fourth_room():
	
	print "In the fourth room."
	eighth_intersection() #incomplete
	
def vendor_room():

	global came_from
	
	print "You enter a triangle shaped room.\n"
	print "You see an old man sitting behind a wooden shelf in the far corner of"
	print "the room. He's crotcheting." 
	time.sleep(2)
	print "You step forward to talk to him." 
	
	came_from = "Northeast"
	first_chamber()
	
def battle_cave():

	global came_from
	count = 0
	
	print "You enter the cave." 
	print "It stinks like death and you hear living sounds beyond the darkness."
	print "You can only see about five feet in front of you."
	print "Do you go forward?"
	answer = raw_input(prompt)
	
	while answer == "player":
		player_check()
		
		print "Do you go forward?"
		answer = raw_input(prompt)
	
	while "ye" in answer:
		print "You move forward."
		enemy_encounter()
		count += 1
		if count == 4:
			print "You have come across one of the Old Woman's Sons!"
		print "Do you go forward?"
		answer = raw_input(prompt)
	
		while answer == "player":
			player_check()
			
			print "Do you go forward?"
			answer = raw_input(prompt)
	while count > 0:
		print "You move back toward the entrance."
		enemy_encounter()
		count -= 1
	
	eleventh_intersection()

# incomplete ritual_room()

def grand_hallway():
	
	global came_from
	
	print "There are ornately carved pillars lining the North and South walls"
	print "and you see an exit at the Southeast end of the Hallway." 
	print "Would you like to go West or South?"
	print "You came from the %s." % came_from
	print "Which way do you go?" 
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Which way do you go?"
		answer = raw_input(prompt)
		print " " #incomplete
		
def dead(why):
	
	print why, "\nWeak effort, dying so soon. Better luck next time."
	print "Would you like to play again? y or n?"
	
	answer = raw_input(prompt)
	print " "
	
	while answer == "player":
		player_check()
		
		print "Would you like to play again? y or n?"
		answer = raw_input(prompt)
		print " "
		
	if "y" in answer:
		start()
	else: 
		exit(0)

start()


#def print_wisdom(parent):
#	
#	if parent == "Dad":
#		print "Length of entries: %d" % len(fathers_wisdom)
#		for i in 
#			print fathers_wisom[i]
#			
#	else: 
#		print "Mom Road."
#	
#print_wisdom(Dad)
