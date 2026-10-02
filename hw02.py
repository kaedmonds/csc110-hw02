# Kathryn Edmonds

# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    # ADD a Docstring for this function
    """the purpose of this section is to get the user to input two integers, in order to then compute several functions with them later on."""
    # the return shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    num_one = input("give me x: ")
    a = int(num_one)
    num_two = input("give me y: ")
    b = int(num_two)
    return a, b 
    
    #computer should store and return the two integers given by the user

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    # ADD a Docstring for this function
    """The purpose of this section is to compute the functions with the stored integers from earlier -- first they are multiplied and added, then the result of the multiplication is divided by the result of the addition"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    x = a * b
    y = a + b
    
    print("mult result:" ,x)
    print("add result:" ,y)
    
    z = x / y
    return z

    # function of x/y labeled z for ease and organization
    # stored value is the value of the multiplication divided by the addition
    
# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, z):
    # ADD a Docstring for this function
    """The purpose of this section is to create a nicely formatted way of printing the values that were inputted and computed. no actual computation is being done here, it's purely for formatting"""
    # the pass shown below is a placeholder to make sure this runs
    # TODO: complete the function instead of the line shown below
    
    print(16 * '*')
    print("RESULTS:")
    print("first number:" ,a)
    print("second number:" ,b)
    print("multadd result:", z)
    print(16 * '=')
    
    # only print commands because of formatting
    # should print the given integers and the final computation of the multiplication result / the addition result
    

def main ():
    # ADD a Docstring for this function
    """purpose of this section is to call the above sections to run them. The code should run by asking the user for two integers, and then printing their multiplication result, addition result, and the result of the two divided by each other"""
    # Task 1.2:
    #  Add one line below to call read_two_ints (note that it returns two values)
    #  the call should provide no arguments
    #  store the returned values into two variables: x and y

    x, y = read_two_ints()
    
    # calling the first section of code
    
    

    # Task 2.2:
    #  Add one line below to call multadd (note that it returns one value)
    #  the call should provide the arguments x, and y you obtained above;
    #  store the returned value in a variable called xy_multadd

    xy_multadd = compute_multadd(x,y)
    
    # calling the second section of code
    # calling it xy_multadd so the computer knows the values for later

    # Task 3.2:
    #  Complete The line below to call print_fancy
    #  the call should provide the arguments x, y, and xy_multadd you obtained above;

    print_fancy(x, y, xy_multadd)
    
    #calling the third section of code


    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
