# This is my test file before adding it to the main file.
# I want to see if I can run a while loop on the main function till I get three good readings in my list.

# I might be able to get rid a bunch of the code in main by just running a loop on the first_weight asking for weight until the list has 3 readings. That will clean up my main function.

TOLERANCE_WITHIN_WEIGHTS = 0.02 # percent

def main():
    meteringpump_weights = []

    while True:
        weight_in_grams = float(input("Enter the weight reading in grams: "))
        if len(meteringpump_weights) == 3:
            print("All three weights have been saved. Here they are:\n")
            metering_pump_undertest = Pump(meteringpump_weights[0], meteringpump_weights[1], meteringpump_weights[2], TOLERANCE_WITHIN_WEIGHTS, average_weight)
            metering_pump_undertest.tellData()
            break
        elif weight_in_grams <= highest_acceptable_range and weight_in_grams >= lowest_acceptable_range:
            print("The weight has past the 2% allowed range. This is now the first reading.")
            meteringpump_weights.clear() # This will empty the list of all items
            meteringpump_weights.append(weight_in_grams) # After having a clean list I will add this new weight as the "first one" or the one were gonna have the accepted range determined by.
        else:
            print("The weight has been saved. Can move on to the next weight.")
            meteringpump_weights.append(weight_in_grams)
            acceptable_weight_range = TOLERANCE_WITHIN_WEIGHTS * meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            highest_acceptable_range = acceptable_weight_range + meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            lowest_acceptable_range = meteringpump_weights[0] - acceptable_weight_range # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem

            print(f"The next readings have to be greater {weight_in_grams - acceptable_weight_range} and less than {weight_in_grams + acceptable_weight_range}\n")
            continue

if __name__ == '__main__':
    main()