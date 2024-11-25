import random

def send_message(guest_list):
    for guest in guest_list:
        print(f"Hello {guest.title()}, would you like to come to dinner?")

def send_apology(declined_list):
    for guest in declined_list:
        print(f"I'm so sorry {guest.title()}, but I don't have room at my table.")

# Initial guest list
guests = ['missy marrone', 'angie webster', 'caitlyn webster']
declined = []

# Initial invitations
send_message(guests)

# First guest cancellation
random_guest = random.choice(guests)
print(f"I'm so sorry, but {random_guest.title()} can't seem to make it!")
declined.append(guests.pop(guests.index(random_guest)))

# Add new guest
guests.append('nelson mandela')
send_message(guests)

print("You're not going to believe this! I found a bigger table!")

# Add more guests
guests.extend(['albert einstein', 'jean byrne', 'george webster'])
send_message(guests)

print("Okay, I was wrong, sorry guys! Only two people can come.")

# Remove guests randomly
while len(guests) > 2:
    random_guest = random.choice(guests)
    declined.append(guests.pop(guests.index(random_guest)))

send_message(guests)
send_apology(declined)

# Clear remaining guests
guests.clear()
print(guests)