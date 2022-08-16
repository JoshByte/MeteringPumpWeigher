# Josh Snyder
# Metering pump weight tracker

# The weight will be in grams
# The nominal value is 453.00
# Take the first weight
# Calculate 2% of the first weight
# Say what the weight has to be above and below
#   Check if the the next weight is within that 2% range
#       if yes then hold ontu both weights, and take the next, next reading
#       if next, next reading is within that 2% range, then calculate the average of the 3 readings
#       print to the console all three readings and the average reading

# Cant use a tuple because if the reading suddenly drops or jumps then I need to get rid of the old data and have the new reading take its place. A List will work fine.

TOLERANCE_WITHIN_WEIGHTS = 0.02 # percent

class Pump:
    def __init__(self, first_weight, second_weight, third_weight, tolerance_range, average):
        self.first_weight = first_weight
        self.second_weight = second_weight
        self.third_weight = third_weight
        self.tolerance_range = tolerance_range
        self.average = average
    
    def tellData(self):
        print(f"The first weight given was: {self.first_weight}")
        print(f"The second weight given was: {self.second_weight}")
        print(f"The third weight given was: {self.third_weight}")
        print(f"The tolerance range set was: {self.tolerance_range} percent")
        print(f"The average of the weights given was: {self.average}")
    
    def get_first_weight(self):
        print(self.first_weight)
    
    def get_second_weight(self):
        print(self.second_weight)

    def get_third_weight(self):
        print(self.third_weight)
    
    def get_tolerance_range(self):
        print(self.tolerance_range)
    
    def get_average(self):
        print(self.average)
    
    def set_first_weight(self, new_first_weight):
        self.first_weight = new_first_weight
    
    def set_second_weight(self, new_second_weight):
        self.second_weight = new_second_weight
    
    def set_third_weight(self, new_third_weight):
        self.third_weight = new_third_weight
    
    def set_tolerance_range(self, new_tolerance_range):
        self.tolerance_range = new_tolerance_range


def main():
    meteringpump_weights = []

    first_weight = float(input("Enter the first weight reading in grams: "))
    meteringpump_weights.append(first_weight)
    
    acceptable_weight_range = TOLERANCE_WITHIN_WEIGHTS * meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
    highest_acceptable_range = acceptable_weight_range + meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
    lowest_acceptable_range = meteringpump_weights[0] - acceptable_weight_range # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem

    print(f"The next readings have to be greater {first_weight - acceptable_weight_range} and less than {first_weight + acceptable_weight_range}\n")

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
        average_weight = (first_weight + second_weight + third_weight) / 3 # Algorithm to get the average of the 3 weights.
    else:
        print("The weight was not within the 2% allowed range. This will now be the first reading.")

    metering_pump_undertest = Pump(first_weight, second_weight, third_weight, TOLERANCE_WITHIN_WEIGHTS, average_weight)
    metering_pump_undertest.tellData()

if __name__ == '__main__':
    main()

# Instead of asking for 1st, 2nd, and 3rd weights I should only ask for the weight. There could be more than 3 weights if the pump is being a problem I could make a while loop that runs until my meteringpump_weights list has three
# acceptable values.