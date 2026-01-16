# --- Plane Destinations, Travel Times & Prices ---

# Travel time (minutes)
travel_times = {
    "lagos": 60,
    "abuja": 90,
    "port harcourt": 80,
    "ibadan": 70
}

# Base ticket prices (Naira)
base_prices = {
    "lagos": 60000,
    "abuja": 120000,
    "port harcourt": 80000,
    "ibadan": 50000
}

print("=== PLANE TICKET BOOKING SYSTEM ===\n")

# --- Passenger Information ---
name = input("Enter passenger full name: ")

# Age requirement
age = int(input("Enter passenger age: "))

# If passenger is too young, require an adult
if age < 16:
    print("Passenger is under 16 years old.")
    guardian_age = int(input("Enter accompanying adult's age (must be 18+): "))
    
    if guardian_age < 18:
        print("Cannot process booking: Guardian must be 18 or older.")
        exit()
    else:
        print("Guardian verified. Proceeding...\n")

# Destination input
destination = input("Enter destination: ").lower()

# Validate destination
if destination not in travel_times:
    print("Destination not available for booking.")
    exit()

# Ticket class
ticket_type = input("Enter ticket type (Economy / Business / First Class): ").lower()

# Number of passengers
num_passengers = int(input("Enter number of passengers: "))

# Pet option
has_pet = input("Are you travelling with a pet? (yes/no): ").lower()

# Travel date
travel_date = int(input("Enter travel date (1 - 31): "))

# Restrict 13th
while travel_date == 13:
    print("Flights are banned on the 13th. Choose another date.")
    travel_date = int(input("Enter a new travel date (1 - 31): "))

print(f"Travel date confirmed: {travel_date}\n")

# Weather condition
weather = input("Enter current weather (clear/rainy/stormy/foggy): ").lower()

# Weather restrictions
if weather in ["stormy", "foggy"]:
    print("Flight cannot take off due to unsafe weather conditions.")
    exit()
else:
    print(f"Weather is safe for travel: {weather}\n")

# --- Ticket Type & Price ---
ticket_prices = {
    "economy": 50000,
    "business": 120000,
    "first class": 250000
}

# Validate ticket choice
if ticket_type in ticket_prices:
    base_price = ticket_prices[ticket_type]
    print(f"{ticket_type.title()} ticket selected. Base price: ₦{base_price}")
else:
    print("Invalid ticket type selected.")
    exit()

# Pet fee
pet_fee = 10000 if has_pet == "yes" else 0
if pet_fee > 0:
    print(f"Pet fee applied: ₦{pet_fee}")

# Total cost calculation
total_cost = (base_price + pet_fee) * num_passengers
print(f"Total cost for {num_passengers} passenger(s): ₦{total_cost}\n")

# --- Ticket Summary ---
print("====================================")
print("             PLANE TICKET")
print("====================================")
print(f"Passenger Name       : {name}")
print(f"Age                  : {age}")
print(f"Destination          : {destination.title()}")
print(f"Ticket Type          : {ticket_type.title()}")
print(f"Travelling With Pet? : {'Yes' if has_pet == 'yes' else 'No'}")
print(f"Weather Status       : {weather.title()}")
print(f"Travel Date          : {travel_date}")
print(f"Passengers           : {num_passengers}")
print("------------------------------------")
print(f"Total Cost           : ₦{total_cost}")
print("====================================")
print("        BOOKING SUCCESSFUL")
print("====================================")
print("Thank you for booking with us. Have a pleasant flight!")