##### ASSIGNMENT STARTS HERE #####


#%%
# First Assignment
'''
1: Please create a program which inputs two years and outputs the years as well as the difference
between them!

Your output should look like:

Year 1: 2025
Year 2: 2028
Difference: 3
'''


#%%
# Second Assignment

'''
2: Please create a program which collects an input as fahrenheit and outputs the 
temperature in celsius

Your output should look like:

Fahrenheit: 25
Celsius: -3.89
'''


#%%
# Third Assignment

'''

3: Please create a program which collects an input as US Dollars and converts the output to Euros 
given the exchange rate on 1/19/25 as 1 USD = 0.97 Euro

Your output should look like:
USD: 1
EU: 0.97

'''


##### ASSIGNMENT ENDS HERE #####



#Assignment_One

# Function to calculate the difference between two years
def year_difference(year1, year2):
    return abs(year1 - year2)

# Input two years from the user
year1 = int(input("Enter the first year: "))
year2 = int(input("Enter the second year: "))

# Calculate the difference
difference = year_difference(year1, year2)

# Output the years and the difference
print(f"The difference between the two years is: {difference} years")



#Assignment_Two

# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

# Input from user
fahrenheit = float(input('Enter temperature in Fahrenheit: '))

# Convert to Celsius
celsius = fahrenheit_to_celsius(fahrenheit)

# Output the result
print(f"The temperature in Celsius is: {celsius:.2f}°C")


#Assignment_Three

# Function to convert USD to EUR
def usd_to_euro(usd, exchange_rate=0.97):
    return usd * exchange_rate

# Input amount in USD
usd = float(input("Enter amount in US Dollars (USD): "))

# Convert to Euros
euros = usd_to_euro(usd)

# Output the result
print(f"{usd} USD is equivalent to {euros:.2f} Euros.")