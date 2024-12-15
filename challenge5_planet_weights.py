earth_weight = float(input("Enter your weight on Earth (in kg): "))

planet_number = int(input("Enter the planet number (1-7): "))

if planet_number == 1:
    weight = earth_weight * 0.38
    print(f"Your weight on Mercury would be {weight:.2f} kg.")
elif planet_number == 2:
    weight = earth_weight * 0.91
    print(f"Your weight on Venus would be {weight:.2f} kg.")
elif planet_number == 3:
    weight = earth_weight * 0.38
    print(f"Your weight on Mars would be {weight:.2f} kg.")
elif planet_number == 4:
    weight = earth_weight * 2.53
    print(f"Your weight on Jupiter would be {weight:.2f} kg.")
elif planet_number == 5:
    weight = earth_weight * 1.07
    print(f"Your weight on Saturn would be {weight:.2f} kg.")
elif planet_number == 6:
    weight = earth_weight * 0.89
    print(f"Your weight on Uranus would be {weight:.2f} kg.")
elif planet_number == 7:
    weight = earth_weight * 1.14
    print(f"Your weight on Neptune would be {weight:.2f} kg.")
else:
    print("Invalid planet number.")
