# This is my test file before adding it to the main file.
# I want to see if I can run a while loop on the main function till I get three good readings in my list.

# I might be able to get rid a bunch of the code in main by just running a loop on the first_weight asking for weight until the list has 3 readings. That will clean up my main function.

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

meteringpump_weights = []

def main():

    while True:

        weight_in_grams = float(input("Enter the weight reading in grams: "))
        if len(meteringpump_weights) != 3:

            print("All three weights have been saved. Here they are:\n")
            average_weight = (meteringpump_weights[0] + meteringpump_weights[1] + meteringpump_weights[2]) / len(meteringpump_weights) # Did the length of the list rather than have a magic number.
            metering_pump_undertest = Pump(meteringpump_weights[0], meteringpump_weights[1], meteringpump_weights[2], TOLERANCE_WITHIN_WEIGHTS, average_weight)
            metering_pump_undertest.tellData()
            break
        elif weight_in_grams <= highest_acceptable_range and weight_in_grams >= lowest_acceptable_range:
            print("The weight has past the 2% allowed range. This is now the first reading.")
            meteringpump_weights.clear() # This will empty the list of all items
            meteringpump_weights.append(weight_in_grams) # After having a clean list I will add this new weight as the "first one" or the one were gonna have the accepted range determined by.
            continue
        else:
            print("The weight has been saved. Can move on to the next weight.")
            meteringpump_weights.append(weight_in_grams)

            # I wonder if theres a cleaner way to have the next 3 lines. Also the placement feels weird
            acceptable_weight_range = TOLERANCE_WITHIN_WEIGHTS * meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            highest_acceptable_range = acceptable_weight_range + meteringpump_weights[0] # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem
            lowest_acceptable_range = meteringpump_weights[0] - acceptable_weight_range # Changed to list index 0 no longer the first weight. If the first weight is replaced then this would be a problem

            print(f"The next readings have to be greater {weight_in_grams - acceptable_weight_range} and less than {weight_in_grams + acceptable_weight_range}\n")
            continue

if __name__ == '__main__':
    main()