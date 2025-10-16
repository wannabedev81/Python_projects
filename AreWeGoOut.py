temperature = 5

is_raining = False

if temperature >= 25:
    print("Let us go hiking, the weather is good.")
elif temperature < 25 and is_raining:
    print("It is cold and wet, no outdoor activity today.")
elif 20 < temperature < 25 and not is_raining:
    print("Okay, let's go out but dress warm.")
else:
    print("No activities outside today.")

