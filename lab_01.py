""" LAB #1
    08/25/2025

    Student 1: Daniel, Mccray
    Student 2: Jimmy, Le
    Description: Our first Lab demonstrating the usage of using input methods and logic
    to create a simple guessing game from 1-100
"""

import random
from check_input import get_int_range



         


def main():
    
   low_number = 1
   high_number = 100


   """  
   RANDOM NUMBER GRADE
   # ? Gen the random number from ranges 1-100 inclusively. 
   # ? ONLY ONCE at the beggining of the function
   """
   random_number = random.randint(1, 100)
   
   # Uncomment for debugging
   # print(random_number)
   
   # ? Create a counter to keep track of the attempts
   counter = 0
   
   print("--- Guessing Game Has Started ---")
  
   # * Uses a while loop until the user’s guesses correct
   while True:
      
      # ? Use check_input module to ensure proper range enforcement until correct input
      current_input = get_int_range("Please enter a number (1-100): ", low_number, high_number)
            
      # ? count the valid guesses immediately to include correct guess
      counter += 1
      
      # ? Uses if statements to check high or too low.
      if current_input == random_number:
         print(f"Congratulations, you did it in {counter} attempts.")
         break
      elif current_input < random_number:
          print(f"Too low! Guess again ({low_number}-{high_number})")
      elif current_input > random_number:
         print(f"Too high! Guess again ({low_number}-{high_number})")
     
      
      """
      Because get_int_range enforces input correction, 
      we can safely increment the counter without having to worry
      """
    
    
    



main()
