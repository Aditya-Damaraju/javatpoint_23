import math
train_speed = int(input("Enter the Speed of the train: "))
man_speed = int(input("Enter the Speed of the Man: "))
distance = int(input("Enter the distance of man from the train: "))
train_length = int(input("Enter the length of the train: "))
d = distance + train_length
relative_speed = train_speed - man_speed
r_s = relative_speed * 5/18
time = d / r_s
print("Time for crossing is: ", time, "seconds")
exit (0)
