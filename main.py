import os  # For accessing the other python code in this folder.
import inspect  # For converting source code to string.

# Make a list of all files in the c(urrent) w(orking) d(irectory).
files = os.listdir(os.getcwd())
# The files with solutions to Project Euler problems are all the python files that are not this file.
solutions = filter(lambda filename: filename.endswith('.py') and filename != 'main.py',
                   files)
# Strip of the last three characters of the filenames ('.py'), by slicing the strings from beginning up to the third last character.
solutions = map(lambda filename: filename[:-3], solutions)
# Import the solution files as Python modules.
solutions = map(lambda module_name: __import__(module_name), solutions)
# Decorate the solutions with their Project Euler problem numbers using list comprehension.
solutions = [(solution.problem_no, solution) for solution in solutions]
# Sort by problem number.
solutions = sorted(solutions)
# Undecorate.
solutions = [solution for (_, solution) in solutions]


# Removes the first line of a string.
def prettify(func_str):
    # Split the string into a list using the newline character ('\n') as a separator.
    lines = func_str.split('\n')
    # Return all but the first line, joined together in one string with newline characters.
    return '\n'.join(lines[1:])

print 'Press Enter to continue...'
for sol in solutions:
    raw_input()  # Wait for user input.
    print 'Problem no.', sol.problem_no, '\n'
    print '"'+sol.description+'"', '\n'
    raw_input()
    print 'Solution:'
    print '    '+str(sol.solve())
    raw_input()
    print 'Code:'
    print prettify(inspect.getsource(sol.solve))
    print '------------------'
raw_input()  # Wait for input before shutting down.
