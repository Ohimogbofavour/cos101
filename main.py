
def calculate_force(mass,acceleration):
     force = mass * acceleration
     return force

def calculate_velocity(speed,time):
    velocity = speed/time
    return velocity



def maim():
    print('formula calculator')
    print('---------------------')

    while True:
        print('chose from the options below')
        print("a" : force= mass * acceleration  )
        print('b')
        print('c')
        print('d')

        choice = input("enter the letter of your chosen formula")

         if choice == "a":
            mass = float(input("enter mass(kg):"))
            acceleration = float(input("enter acceleration (m/s^2):"))
            force = calculate_force(mass,acceleration)
            print(f"force:{force} N")

        elif choice == "b":
            speed = float(input("enter speed:"))
            time = float(input("enter time(s):"))
            velocity = calculate_velocity(speed,time)
            print(f"velocity:{velocity}")










