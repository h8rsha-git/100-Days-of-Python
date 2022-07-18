
#strings are immutable in Python

# in-built functions
length = len("Sample String")

def format_name(f_name, l_name):
  ''' Takes the first and last name and format it to the title case version of the combined name'''
  if f_name == "" or l_name == "":
    return "Invalid Input"
    # to be noted - NO ERROR
    print("This will NOT be printed")
  # changes to title format
  formatted_f_name = f_name.title()
  formatted_l_name = l_name.title()
  return f"{formatted_f_name} {formatted_l_name}"

formatted_string = format_name("ANgeLa", "henDERsOn")
print(formatted_string)