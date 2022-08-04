# This is my test file before adding it to the main file.
# I want to see if I can run a while loop on the main function till I get three good readings in my list.

# I might be able to get rid a bunch of the code in main by just running a loop on the first_weight asking for weight until the list has 3 readings. That will clean up my main function.

TOLERANCE_WITHIN_WEIGHTS = 0.02 # percent

def main():
    meteringpump_weights = []

    while True:
        weight_in_grams = float(input("Enter the weight reading in grams: "))
        meteringpump_weights.append(weight_in_grams)
        if len(meteringpump_weights) == 3:
            print("All three weights have been saved. Here they are:\n")
            metering_pump_undertest = Pump(meteringpump_weights[0], meteringpump_weights[1], meteringpump_weights[2], TOLERANCE_WITHIN_WEIGHTS, average_weight)
            metering_pump_undertest.tellData()
            break
        else:
            acceptable_weight_range = TOLERANCE_WITHIN_WEIGHTS * meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            highest_acceptable_range = acceptable_weight_range + meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            lowest_acceptable_range = meteringpump_weights[0] - acceptable_weight_range # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem

            print(f"The next readings have to be greater {weight_in_grams - acceptable_weight_range} and less than {weight_in_grams + acceptable_weight_range}\n")
            continue
        
        

        second_weight = float(input("Enter the second reading in grams: "))
        if second_weight < highest_acceptable_range and second_weight > lowest_acceptable_range:
            print("Okay the second weight is within 2%. Move on to the next weight.\n")
            meteringpump_weights.append(second_weight)
        else:
            print("The weight has past the 2% allowed range. This will now be the first reading.")
            meteringpump_weights[0] = second_weight

        third_weight = float(input("Enter the third weight in grams: "))
        if third_weight < highest_acceptable_range and third_weight > lowest_acceptable_range:
            print("Okay the third weight is within 2%. All three readings have been saved.\n")
            meteringpump_weights.append(third_weight)
            average_weight = (weight_in_grams + second_weight + third_weight) / 3 # Algorithm to get the average of the 3 weights.
        else:
            print("The weight was not within the 2% allowed range. This will now be the first reading.")

        

if __name__ == '__main__':
    main()