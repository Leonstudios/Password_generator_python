import random

print("Password generator started! Press ctrl+c to exit.")

while True:
  howLong = input("How long do you want your password to be ? 8-73:  ")
  lower = "abcdefghijklmnopqrstuvwxz"
  upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  numbers = "0123456789"
  special = "!@#$%^&*()_+"
  string = lower + upper + numbers + special
  length = int(howLong)
  password = "".join(random.sample(string,length))
  if length >= 8 and length <= 73:
   print("Your generated password is : " + password)
