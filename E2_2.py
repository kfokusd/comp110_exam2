import math
## must NOT import other modules 
## ONLY allowed to use math.sqrt() function from math module

# Function: process_expenses()
# - One parameter, filename (csv format)
# - This function returns a 2-items tuple: 1st item is a dictionary, and 2nd item is a list
# - Dictionary:
# - >>Read the csv file and create a dictionary with key of the "Category" field in the csv file
# - >>The values of the dictionary is the total "Amount" for such "Category"
# - List:
# - >>The list contains all of the "Amount" values from the csv file
#

# TODO: Implement this function
# End of process_Expenses()


# Function: computeAvg()
# - One parameter: a list with values
# - Returns the average of all values from the list
#
# TODO: Implement this function
# End of computeAvg()


# Function: computeSum()
# - One parameter: a list with values
# - Returns the sum of all values from the list
#
# TODO: Implement this function
# End of computeSum()


# Function: computeStdDev()
# - One parameter: a list with values
# - Compute the Standard Deviation from the list
# - Returns the value of standard deviation
#
# TODO: Implement this function
# End of computeStdDev()



#process_expenses()                                 # TODO: Need to uncomment and modify this line
print("\n\nExpenses based on Categories:")          # DO NOT change this line
#for i in dict:                                     # TODO: Need to uncomment this line
#    print("{:30s}: ${:.2f}".format(i, dict[i]))    # TODO: Need to uncomment this line


print("\n\nExpenses Stats:")
nAvg = 0.0                                          # TODO: Need to modify this line
nSum = 0.0                                          # TODO: Need to modify this line
nStddev = 0.0                                       # TODO: Need to modify this line
print("Total: ${:.2f}".format(nSum))
print("Average Expense: ${:.2f}".format(nAvg))
print("Standard Deviation: ${:.2f}".format(nStddev))


#Expected Output:
#Expenses based on Categories:
#Fee                           : $1852.00
#Appliance Supplies            : $517.33
#Utilities                     : $4397.92
#HOA                           : $30146.00
#Insurance                     : $2959.86
#Permits & License             : $472.00
#Legal & Prof. Fees            : $1938.00
#Cleaning & Maintenance        : $1176.87
#Repairs - Plumbing            : $3692.10
#Property Taxes                : $19695.89
#Refund (Deposit)              : $4251.27
#Repairs - Misc                : $1802.47
#Advertising                   : $219.99
#Repairs - A/C                 : $290.00
#Return of Capital             : $25000.00
#Remodeling                    : $333.26
#
#
#Expenses Stats:
#Total: $98744.96
#Average Expense: $421.99
#Standard Deviation: $689.93
