def magaca():
    return input("Magaca saxib: ")
    
def age():
    return input("Imisa Jir aad tahay: ")
    
magac = magaca()

age = age()

print("There was a guy called ", magac)

if int(age) >= 18:
    print("What do you do for a living?")
else: 
    print("You're too young to play saxib.")
