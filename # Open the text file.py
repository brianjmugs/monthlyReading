# Open the text file
with open('text_file.txt', 'r') as f:
  # Read the contents of the file into a list of lines
  lines = f.readlines()

# Determine the number of lines per section
lines_per_section = len(lines) // 10

# Iterate over the sections
for i in range(10):
  # Create a new file for the current section
  with open('section_{}.txt'.format(i), 'w') as f:
    # Write the lines for the current section to the file
    f.writelines(lines[i*lines_per_section:(i+1)*lines_per_section])