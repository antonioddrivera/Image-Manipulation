import subprocess
matlab_executable = r'C:\Program Files\MATLAB\R2023b\bin\matlab.exe'


# --------------------------------------Matlab 1 Section -------------------------------------------------------------


print("--------------------Running MATLAB 1 CODE FROM Python------------------------------")
# Set up MATLAB environment
# Runs the first matlab program to read the image and create input.txt to hold the unsigned chars
matlab_process = subprocess.run([matlab_executable, "-batch", "run('mprog1.m'); pause(10);"], capture_output=True)


# --------------------------------------------C Section --------------------------------------------------------------


# Grab the data from input.txt
print("-----------------------Running C CODE FROM Python-------------------------")

# Compile the C program
subprocess.run(["gcc", "cprog.c", "-o", "CProg"])

# Execute the C program with input from input.txt
with open('input.txt', 'r') as file:
    input_data = [value for line in file for value in line.split()]

# create a list of the arguments
# Found that this works better then input_data directly
char_list = []
for x in input_data:
    char_list.append(x)

# Use subprocess to run the C program
process = subprocess.run([".\CProg"] + char_list, capture_output=True, text=True)

# Capture and print the output
output_variable = process.stdout.strip()

# Write the output into a seperate output which mprog2.m will use
with open('c_output.txt', 'w') as f:
    f.write(process.stdout)


# --------------------------------------Haskell Section -------------------------------------------------------------


print("-----------------------Running Haskell CODE FROM Python-------------------------")
# Compiles the Haskell program
subprocess.run(['ghc', 'hprog.hs'])
# Runs the haskell program with input.txt as the arguement
process = subprocess.run(['./hprog'] + [str(x) for x in char_list], text=True, capture_output=True)
# Strip the result to get only the numbers
result = process.stdout.strip()

# Write the output into a seperate output which mprog2.m will use
with open('haskell_output.txt', 'w') as f:
    f.write(process.stdout)


# ---------------------------------------Prolog Section -------------------------------------------------------------


print("-----------------------Running Prolog CODE FROM Python-------------------------")
# Creates a version of char_list that prolog will be able to use
prolog_input = "[" + ",".join(map(str, char_list)) + "]."
# Compile and run the prolog code
process = subprocess.run(['swipl', '-q', '-g', 'main', '-t', 'halt', 'plprog.pl'], input=prolog_input, capture_output=True, text=True)

# Remove square brackets from the output
prolog_output = process.stdout.strip("[]")

# Write the output into a seperate output which mprog2.m will use
with open('prolog_output.txt', 'w') as f:
    f.write(prolog_output)


# --------------------------------------Matlab 2 Section ------------------------------------------------------------


print("-----------------------Running MatLab 2 CODE FROM Python-------------------------")

# Load the matlab code 
with open('mprog2.m', 'r') as file:
    matlabcode = file.read() 

# Set up MATLAB environment 
matlab_process = subprocess.run([matlab_executable, "-batch", "run('mprog2.m'); pause(inf);"], capture_output=True)