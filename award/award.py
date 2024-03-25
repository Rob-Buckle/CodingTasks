# program to determin qualifying times for athletes
swim_time = int(input("Enter your swim time in minutes:"))
cycle_time = int(input("Enter your clycle time in minutes:"))
run_time = int(input("Enter your run time in minutes:"))

sum = swim_time + cycle_time + run_time
print(f"Total time:", sum)


#Calculate the awards using if and elif statements to determin award given
if sum <= 100:
    print(f"AwardAchieved: Provincial Colours")
elif sum in range(101,106):
    print(f"Award Achieved: Half Provincial Colours")
elif sum in range(106,111):
    print(f"Award Achieved: Provincial Scroll")
elif sum > 110:
    print("No Award")



