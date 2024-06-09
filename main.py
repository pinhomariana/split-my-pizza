import time

print("---Welcome to Split My Pizza---")
print("How many slices are in the pizza?")
pizza_total = float(input())
print("How many people are sharing?")
try:
  people = int(input())
except ValueError:
  print("You must enter a number")
  people = int(input())

slice_per_person = pizza_total // people
slices_remaining =  pizza_total % people

print(f"Total slice per person is {slice_per_person}. Remaining slices {slices_remaining}")

time.sleep(4)

print("What is the total bill?")
bill_total = float(input())

print("What percentage tip would you like to leave?")
tip_percentage = int(input())

bill_total = bill_total + (tip_percentage / 100) * bill_total

cost_per_person = bill_total / people

print(f"Total bill including tip is £{bill_total}")
print(f"Total cost per person is £{cost_per_person}")