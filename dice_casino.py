from random import randint
import time

print("Welcome to the Dice game \n")
print("Your goal is to guess higher or lower will the sum of 3 dices will be \n")
print("#########################################################################")

while True:
	dice_1 = 0
	dice_2 = 0
	dice_3 = 0
	player_score = 0
	player_credits = 5
	while player_credits > 0:
		print("Your options are: Lower than 10, Higher than 10, 3 Exactly or Three Sixes \n")
		print(f"Right now you have {player_credits} credits left. Choose wisely \n")
		user_choice = input("What's your guess? (L, H, 3 or 18) ")
		if user_choice == "exit":
			print(f"Bye! See ya again. You ended with {player_score} win points in this session and {player_credits} credits left")
			break
		elif user_choice not in ["L", "l", "H", "h", "3", "18", "exit"]:
			print("Try inputing something else next time.")
			continue
		print("Here goes")
		time.sleep(2)
		dice_1 = randint(1, 6)
		print(f"First dice gives {dice_1}")
		dice_2 = randint(1, 6)
		time.sleep(1)
		print(f"Second dice shows {dice_2}")
		dice_3 = randint(1, 6)
		time.sleep(0.5)
		print(f"Third dice strikes with {dice_3}")
		time.sleep(1)
		total = dice_1 + dice_2 + dice_3
		print(f"The sum is {total}. Your choice was: {user_choice}")
		if user_choice in ["L", "l"] and total > 10:
			print("You lost this time! -1 credit\n")
			player_credits -=1;
			time.sleep(1)
		elif user_choice in ["H","h"] and total < 10:
			print("Not your lucky day, mate! -1 credit\n")
			player_credits -=1;
			time.sleep(1)
		elif user_choice == "3" and total != 3:
			print("No, this is a loss. -1 credit \n")
			player_credits -=1;
			time.sleep(1)
		elif user_choice == "18" and total != 18:
			print("Nope, but that was a risky try. -1 credit\n")
			player_credits -=1;
			time.sleep(1)
		elif user_choice in ["L", "l"] and total < 10:
			print("Congrats! You win this round. 1 credit awarded! \n")
			player_credits +=1;
			time.sleep(1)
			player_score += 1;
		elif user_choice in ["H", "h"] and total > 10:
			print("Yes! A solid win! 1 credit awarded! \n")
			player_credits +=1;
			time.sleep(1)
			player_score += 1;
		elif user_choice == "3" and total == 3:
			print("Pinpoint win! 3 credits awarded! \n")
			player_credits +=3;
			time.sleep(1)
			player_score += 3;
		elif user_choice == "18" and total == 18:
			print("Could this even happen?! You win 3 credits awarded!\n")
			player_credits +=3;
			time.sleep(1)
			player_score += 3;
		elif user_choice in ["L","l", "H","h", "3", "18"] and total == 10:
			print("Welcome to the Blind zone! Casino wins. Just because. -2 credit")
			player_credits -=2;
			time.sleep(1)
	if player_credits <= 0:
		print(f"Unfortunately you've lost all your credits. Your player score for this session is {player_score} points")
		time.sleep(3)
		print("Goodbye. See you again in our casino")
	break

	