
# Basic Rock Paper Scissors Game
# Name: Add Your Name Here
# Date: Add The Date Here

import random

"""
main.py
---------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.
This script allows a user to play a 3-round game of Rock, Paper, Scissors against the computer.
It uses the 'rich' library for colorful output.
"""

import random
from rich.console import Console
from rich.text import Text

# Create a Console object for rich output
console = Console()
"""
main.py (Starter Template)
-------------------------
Rock Paper Scissors game for CS101 Fall 2025 Lab 02.

Complete the TO-DOs to finish the game!
"""

import random
from rich.console import Console

console = Console()

choices = ['rock', 'paper', 'scissors']
num_to_choice = {'1': 'rock', '2': 'paper', '3': 'scissors'}

#: Implement this function to get and validate the user's choice.
def get_user_choice():
	"""Prompt the user for their choice and return 'rock', 'paper', or 'scissors'."""
	#: Use console.input and validate input (accept 1/2/3 or words)
	while True:
		user_input = console.input("[bold]Choose rock (1), paper (2), or scissors (3): [/bold]").strip().lower()
		if user_input in num_to_choice:
			user_choice = num_to_choice[user_input]
		else:
			user_choice = user_input
		if user_choice in choices:
			break
		else:
			console.print("[red]Invalid choice. Please try again.[/red]")
	
	return user_input, user_choice
	

#: Implement this function to randomly select the computer's choice.
def get_computer_choice():
	"""Randomly return 'rock', 'paper', or 'scissors'."""
	computer_choice = random.choice(choices)
	console.print(f"[magenta]Computer chose: {computer_choice}[/magenta]")
	
	return computer_choice

# : Implement this function to determine the winner of a round.
def determine_winner(user_choice, computer_choice, user_score, computer_score):
	"""Return 'user', 'computer', or 'tie' based on the choices."""
	if user_choice == computer_choice:
		console.print("[blue]It's a tie![/blue]")
	elif (
		(user_choice == 'rock' and computer_choice == 'scissors') or
		(user_choice == 'paper' and computer_choice == 'rock') or
		(user_choice == 'scissors' and computer_choice == 'paper')
	):
		console.print("[bold green]You win this round![/bold green]")
		user_score += 1
	else:
		console.print("[bold red]Computer wins this round![/bold red]")
		computer_score += 1
	
	return user_score, computer_score
	
	
	

# : Implement this function to print the round result with color.
def print_round_result(user_choice, computer_choice, user_score, computer_score): # winner
	"""Print the choices and the winner of the round using rich colors."""
	console.print("\n[bold underline]Game Over![/bold underline]")
	console.print(f"[cyan]Your score: {user_score}[/cyan]")
	console.print(f"[magenta]Computer score: {computer_score}[/magenta]")

	

# : Implement the main game loop.
def main():
	"""Main function to run the game for 3 rounds and print the final result."""
	user_score = 0
	computer_score = 0
	rounds = 3
	for round_num in range(1, rounds + 1):
		console.print(f"\n[bold yellow]Round {round_num} of {rounds}[/bold yellow]")

		# TODO: Get user and computer choices
		user_choice, user_choice = get_user_choice()
		computer_choice = get_computer_choice()
		# TODO: Determine winner
		user_score, computer_score = determine_winner(user_choice, computer_choice, user_score, computer_score)
		# TODO: Print round result
		print_round_result(user_choice, computer_choice, user_score, computer_score)
		# TODO: Update scores
		pass
	# TODO: Print final scores and announce the overall winner
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")
	elif user_score < computer_score:
		console.print("[bold red]Sorry, the computer wins the game.[/bold red]")
	else:
		console.print("[yellow]It's a tie game![/yellow]")
	if user_score > computer_score:
		console.print("[bold green]Congratulations, you win the game![/bold green]")

	

if __name__ == "__main__":
	main()

