# Create three strings using three different methods. Save your result to result_string_1, result_string_2,
# result_string_3 variables

result_string_1 = 'December'
result_string_2 = str(56)
result_string_3 = input()
print(result_string_1)
print(result_string_2)
print(result_string_3)



# Enter your first and  last name. Join them together with a space in
# between. Save a result in a variable result_full_name and
# save the length of the whole name in result_full_name_length variable.

first_name = "Dana"
last_name = "Iurco"
result_full_name = first_name + ' ' + last_name
result_full_name_length =len(result_full_name)
print(result_full_name)
print(result_full_name_length)


# Enter the capital city of California State in lower case. Change the case to title case.
# Save the result in result_ca_capital variable

result_ca_capital = "los angeles"
result_ca_capital = result_ca_capital.title()
print(result_ca_capital)


# Enter the name of our planet. Change the case to upper case. Save the result in
# result_planet variable
planet = "earth"
result_planet = planet.capitalize()
print(result_planet)
