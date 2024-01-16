try:
	import os
except ImportError as e:
	print(f"Import error: {e}")

class Guard:
	def Idle():
		print("Guard is on patrol.")
	def Panic():
		print("Guard is in a panic.")
	def Alert():
		print("Guard is on alert.")
	def CollectItem():
		print("Guard picks up item on the ground.")
	def SeeMurder():
		print("Guard sees you kill someone.")
		Guard.Panic()
	def SeeKnockout():
		print("Guard sees you knockout someone.")
		Guard.Panic()

class Ghost:
	def Idle():
		print("Ghost is milling around.")
	def Panic():
		print("Ghost is running away.")
		Guard.Panic()
	def SeeMurder():
		print("Ghost sees you kill someone.")
		Ghost.Panic()
	def SeeKnockout():
		print("Ghost sees you knockout someone.")
		Ghost.Panic()

class Innocent:
	def Idle():
		print("Innocent is walking around.")
	def Panic():
		print("Innocent is in a panic.")
		print("Innocent is running away.")
		Guard.Panic()
	def SeeMurder():
		print("Innocent sees you kill someone.")
		Innocent.Panic()
	def SeeWeapon():
		print("Innocent sees weapon on the ground.")
		print("Innocent informs the guard.")
		Guard.CollectItem()
	def SeeKnockout():
		print("Innocent sees you knockout someone.")
		Innocent.Panic()

class Player:
	def InputCommand():
		while True:
			print("Action to take:")
			print("[1: Pull out weapon] [2: Knock out NPC(stealth)] [3: Knock out NPC(public)]")
			print("[4: Kill an NPC]     [5: Drop weapon]            [6: Exit]")
			command = int(input("-> "))
			Player.Action(command=command)
	def Action(command):
		if command == 1:
			os.system("clear")
			print("You pull out your gun.")
			Guard.Alert()
			Innocent.Panic()
			Ghost.Panic()
		elif command == 2:
			os.system("clear")
			print("You knock out an NPC.")
			print("No one has witnessed your deed.")
		elif command == 3:
			os.system("clear")
			Innocent.SeeKnockout()
			Ghost.SeeKnockout()
			Guard.SeeKnockout()
		elif command == 4:
			os.system("clear")
			Innocent.SeeMurder()
			Ghost.SeeMurder()
			Guard.SeeMurder()
		elif command == 5:
			os.system("clear")
			print("You drop a weapon")
			Innocent.SeeWeapon()
		elif command == 6:
			quit()
		else:
			os.system("clear")
			print("Invalid command.")

Player.InputCommand()