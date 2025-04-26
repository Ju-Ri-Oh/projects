import random

pcap_questions = [
    {
        'question': 'What is the result of the following code? \nprint(2 ** 3 ** 2 ** 1)',
        'options': ['512', '256', '64', 'The code is erroneous.'],
        'correct_answer': '512',
        'explanation': '2^3^2^1 is the same as 2^9, which is 512',
        'category': ['miscellaneous'],
        'subcategory': ['arithmetics']
    },
    {
        'question': 'What is the result of the following expression? \ni = 160 \nwhile len(str(i)) > 78: \n \ti *= 2 \nelse: \n \t i //= 2 \n print(i)',
        'options': ['80', '160', '320', 'The code is erroneous.'],
        'correct_answer': '80',
        'explanation': 'i is converted into a str with a length of 3. 3 is not greater than 78 so i is divided by 2. \n len(str(160) = 3. \n 3 is not > 72 \n else -> 160 // 2 = 80)',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
    {
        'question': 'What\'s the output of the following code? \n'
                'print("Juri\'s sister\'s name\'s \\"Svetlana\\"") \n'
                'print(\'Juri\\\'s sister\\\'s name\\\'s \\"Svetlana\\"\')',
        'options': ['Juri\'s sister\'s name\'s "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"', 'Juri\'s sister\'s name\'s "Svetlana"\nJuris sisters names "Svetlana"', 'Juris sisters names "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"', 'The code is erroneous.'],
        'correct_answer': 'Juri\'s sister\'s name\'s "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"',
        'explanation': 'Single \' and double quotes \" can be used interchangeably',
        'category': ['strings'],
        'subcategory': ['basic']
    },
    {
        'question': 'What is the result of the following code? \nn = 0\nwhile n < 4:\n\tn += 1\n \tprint(n, end=\" \")',
        'options': ['1 2 3 4', '0 1 2 3', '1 2 3', 'The code is erroneous.'],
        'correct_answer': '1 2 3 4',
        'explanation': 'n enters the loop with values of 0, 1, 2, 3 being smaller than 4 and then receives a value of +1 before being printed as 1, 2, 3, 4',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
    {
        'question': 'What is the result of the following code? \na = 0 \nb = 2\nc = len("PCAP")\na = b > c\nprint(a)\nprint(type(a))',
        'options': ['False \n <class "bool">', '4 \n <class "integer">', 'True\n <class "bool">', 'The code is erroneous.'],
        'correct_answer': 'False \n <class "bool">',
        'explanation': '"2 > 4" is False, therefore x is False and thus from class bool',
        'category': ['miscellaneous'],
        'subcategory': ['boolean']
    },
    {
        'question': 'What is the result of the following code? \nnum = 1\nnum2 = 0\nnum = num ^ num2\nnum2 = num ^ num2\nnum = num ^ num2\nprint(num)\n',
        'options': ['0', '1', '4', '2'],
        'correct_answer': '0',
        'explanation': 'This is a bitwise XOR operation, the values of num and num2 are swapped.',
        'category': ['miscellaneous'],
        'subcategory': ['XOR']
    },
    {
        'question': 'What is the result of the following code? \nc, b, a = 2, 1, 0\na, c = c, b\nb = b - c\na, b, c = b, c, a\nprint(a, b, c)',
        'options': ['0 1 2', '2 1 0', '1 2 0', '1 0 2'],
        'correct_answer': '0 1 2',
        'explanation': 'A simple series of variable assignments.',
        'category': ['miscellaneous'],
        'subcategory': ['variable assignment']
    },
    {
        'question': 'What is the result of the following code? \nx = 0\ny = x ** 0\nif y < x + 1:\n\tz = 1\nelif y == 1:\n\tz = 2\nelse:\n\tz = 3\nprint(x + y + z)',
        'options': ['3', '2', '4', '1.'],
        'correct_answer': '3',
        'explanation': 'a stays at 0. b is 1 because 0^0 is 1 which leads to c becoming 2. 0 + 1 + 2 = 3',
        'category': ['miscellaneous'],
        'subcategory': ['elif']
    },
    {
        'question': 'What do you call this: __ ?',
        'options': ['dunder', 'underscore', 'init', 'anaconda'],
        'correct_answer': 'dunder',
        'explanation': 'two consecutive underscores are called a dunder, for "D"ouble "UNDER"score',
        'category': ['miscellaneous'],
        'subcategory': ['basic']
    },
    {
        'question': 'What is the result of the following code? \nfor i in range(1, 4, 2): \n\tprint("*")',
        'options': ['*\n*', '*\n*\n*', '*\n*\n*\n*', 'The code is erroneous.'],
        'correct_answer': '*\n*',
        'explanation': 'There is two iterations, the index starts at 1, then is increased by 2 to the index 3. Since an index 5 doesn\'t exist the iteration ends.',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
        {
        'question': 'What is the result of the following code? \ni = 12\nwhile i > 0 :\n\ti -= 3\n\tprint(\"*\")\n\tif i <= 3:\n\t\tbreak\nelse:\n\tprint(\"*\")',
        'options': ['*', '* * *', '* * * *', 'The code is erroneous.'],
        'correct_answer': '* * *',
        'explanation': 'The loop is entered three times at i=12, i=9, i=6, each time it will be reduced by 3 and a star is printed. When i=6 becomes i=3 the if statement becomes true and the loop is ended via a break which means the else clause doesn\'t execute.',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
        {
        'question': 'What is the result of the following code? \ni = 12\nwhile i > 0 :\n\ti -= 3\n\tprint(\"*\")\n\tif i <= 3:\n\t\tpass\nelse:\n\tprint(\"*\")',
        'options': ['*', '* * *', '* * * * ', '* * * * *'],
        'correct_answer': '* * * * *',
        'explanation': 'The loop is entered four times at i=12, i=9, i=6, i=3 each time it will be reduced by 3 and a star is printed. When i=6 becomes i=3 the if statement becomes true but the loop continues due to a pass(other than break). Finally, since the loop completed without a break, the else statement executes for the fifth *',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
        {
        'question': 'What is the result of the following code? \nfor i in range(1, 4, 2): \n\tprint("*", end="**")\nprint("***")',
        'options': ['*********', '*****', '************', '******'],
        'correct_answer': '*********',
        'explanation': 'With a step count of 2, i enters the iteration twice, at 1 and at 3, both times one star gets printed plus another two stars at the end of the string for a total of 6. Finally three more stars are printed in the final statement for a total of 9',
        'category': ['miscellaneous'],
        'subcategory': ['loop']
    },
        {
        'question': 'What is the result of the following code? \nlst = ["A", "B", "C", 2, 4]\ndel lst[0:-2]\nprint(lst)',
        'options': ['2, 4', 'A, B, C', 'C, 2, 4', 'The code is erroneous.'],
        'correct_answer': '2, 4',
        'explanation': 'Everything between index 0 towards 2 to the left[-2] from the final index gets deleted',
        'category': ['miscellaneous'],
        'subcategory': ['list operations']
    },
        {
        'question': 'What is the result of the following code? \ns = "Hello, Python!"\nprint(s[-14:15])',
        'options': ['Hello, Python!', '!', 'IndexError: list index out of Range', 'ValueError'],
        'correct_answer': 'Hello, Python!',
        'explanation': 'Even though there is nothing to read in the negative index, everything towards the 15th index is read, which is the entire string.',
        'category': ['strings'],
        'subcategory': ['slicing']
    },

        {
        'question': 'What is an example of a "Factory-Function"?',
        'options': ['A function that creates objects of different classes based on input parameters.', 'A function used to manage the creation of complex objects or families of related objects.', 'A function that calculates and returns the factorial of a given number.', 'A function that relies on a staticmethod.'],
        'correct_answer': 'A function that creates objects of different classes based on input parameters.',
        'explanation': 'A factory function is a function that returns another function or object. It\'s often used to create instances of classes or to generate functions dynamically based on certain parameters or conditions',
        'category': ['OOP'],
        'subcategory': ['basic']
    },
    {
        'question': "What is the result of the following code? \nlst = { 'x': 3, 'y': 5, 'z': 7 }\nfor item in dict:\n\tprint(item)",
        'options': ['x\ny\nz', '3\n5\n7', "'x':1\n'y':2\n'z':3", 'The code is erroneous.'],
        'correct_answer': 'x\ny\nz',
        'explanation': 'If you iterate over a dictionary, you get only the keys, otherwise you need 2 iterables and access the dictionary via .items',
        'category': ['miscellaneous'],
        'subcategory': ['dict']
    },
    {
        'question': "What is the result of the following code? \ns = 'pcap'\nfor i in range(len(s)):\n\ti = s[i].upper()\nprint(s, end='')",
        'options': ['pcap', 'PCAP', 'PCA', 'The code is erroneous.'],
        'correct_answer': 'pcap',
        'explanation': 'The string s is not overwritten during the iteration, the original string is printed',
        'category': ['strings'],
        'subcategory': ['string iteration']
    },
    {
        'question': 'What is the result of the following code? \nlst = [i // i for i in range(0,5)]\nsum = 0\nfor n in lst:\n\tsum += n\nprint(sum)',
        'options': ['The code is erroneous.', '5', '4', '1'],
        'correct_answer': 'The code is erroneous.',
        'explanation': 'The first iterable of the range is 0 and 0 // 0 results in a ZeroDivisionError',
        'category': ['exceptions'],
        'subcategory': ['ZeroDivisionError']
    },
    {
        'question': "What is the result of the following code? \nlst = [[z for z in range(a)] for a in range(3)]\nfor y in lst:\n\tfor x in y:\n\t\tif x < 2:\n\t\t\tprint('*', end='')",
        'options': ['***', '*', '**', '****'],
        'correct_answer': '***',
        'explanation': 'List comprehension creates a list of lists: [[0], [0, 1], [0, 1, 2]] when ireated over, they are all smaller than 2, so three times the * gets printed',
        'category': ['miscellaneous'],
        'subcategory': ['list comprehension']
    },
    {
        'question': 'What is the result of the following code? \nlst = [2 ** a for a in range(0, 10)]\nprint(lst[-2])',
        'options': ['256', '1024', '512', '128'],
        'correct_answer': '256',
        'explanation': 'range(0,10) ends at index 9, lst[-2] accesses one index before the last(8), so 2^8 is being printed.',
        'category': ['miscellaneous'],
        'subcategory': ['list comprehension']
    },
    {
        'question': "What is the result of the following code? \nlst1 = '69,420'\nlst2 = lst1.split(',')\nlst3 = lst1.split('.')\nprint(len(lst1) < len(lst2), len(lst1) < len(lst3))",
        'options': ['False False', 'True True', 'True False', 'False True'],
        'correct_answer': 'False False',
        'explanation': '69,420 is not smaller than 69,420(when seperated by .) nor is it smaller than the first item of the list 69(when seperated by ,)',
        'category': ['strings'],
        'subcategory': ['string operation']
    },
    {
        'question': 'What is the result of the following code? \nfrom math import pi as a\nprint(pi)',
        'options': ['NameError', 'ValueError', 'ImportError', '3.141592653589'],
        'correct_answer': 'NameError',
        'explanation': 'pi was imported as xyz, so pi is not defined anywhere, printing an undefined variable results in a NameError',
        'category': ['exceptions'],
        'subcategory': ['NameError']
    },
    {
        'question': 'What is the result of the following code? \nfrom random import randint\nfor i in range(5):\n\tprint(random(1, 10))',
        'options': ['NameError', 'ImportError', 'ValueError', 'AttributeError'],
        'correct_answer': 'NameError',
        'explanation': 'random is the module name, not the function, random is not a defined variable here, resulting in a NameError',
        'category': ['exceptions'],
        'subcategory': ['NameError']
    },
    {
        'question': 'What is the result of the following code? \nc = 2\ndef a(c):\n\treturn 2 * c\n\nc = 2 + a(c)\nprint(a(c)) ',
        'options': ['12', '16', '8', '2'],
        'correct_answer': '12',
        'explanation': 'x = 2 + a(2)[4] = 6 -> a(6) = 12',
        'category': ['miscellaneous'],
        'subcategory': ['arithmetics']
    },
    {
        'question': 'What is the result of the following code? \ndef gen():\n\tlst = range(5)\n\tfor x in lst:\n\t\tyield x*x\n\nfor x in gen():\n\tprint(x, end="")',
        'options': ['014916', '01491625', '0', 'The code is erroneous.'],
        'correct_answer': '014916',
        'explanation': 'yield makes the function a generator function and replaces the return. It allows to produce a sequence of values. Hereby 0 through 4 are multiplied by themselves ',
        'category': ['miscellaneous'],
        'subcategory': ['list comprehension']
    },
    {
        'question': 'class A:\n\tdef a(self):\n\t\tprint("A", end="")\nclass B(A):\n\tdef a(self):\n\t\tprint("B", end="")\nclass C(B):\n\tdef b(self):\n\t\tprint("B", end="")\na = A()\nb = B()\nc = C()\na.a()\nb.a()\nc.b()',
        'options': ['ABB', 'ABC', 'AAB', 'AAA'],
        'correct_answer': 'ABB',
        'explanation': 'c calls function b of itself which prints B at the end, the b before that calls function a of itself which via polymoorphism has overwritten the inherited function a and a call its own function a BBA in reverse and ABB from a to c.',
        'category': ['OOP'],
        'subcategory': ['polymorphism']
    },
    {
        'question': 'What is the result of the following code? \ntry:\n\tprint("PCAP")\n\traise Exception\n\tprint(10/0)\nexcept Exception as err:\n\tprint("Error occured:", err)',
        'options': ['PCAP', 'ZeroDivisionError', 'Error occured: division by zero', 'PCAP\nError occured: division by zero'],
        'correct_answer': 'PCAP',
        'explanation': 'PCAP is printed before an exception is raised, then the exception is raised before the ZeroDivisionError occurs, which means it doesn\'t occur at all, it ends here.',
        'category': ['exceptions'],
        'subcategory': ['exception handling']
    },
    {
        'question': 'What is the result of the following code? \nclass CriticalError(Exception):\n\tdef __init__(self, message="CriticalError!!!"):\n\t\tException.__init__(self, message)\n\nraise CriticalError\nraise CriticalError("CriticalError!")',
        'options': ['CriticalError!!!', 'CriticalError!', 'CriticalError', 'None of these answers are correct.'],
        'correct_answer': 'CriticalError!!!',
        'explanation': 'The first raised exception is what amtters and it raised the exception CriticalError, which initializes the message "CriticalError!!!"',
        'category': ['exceptions'],
        'subcategory': ['error handling']
    },
    {
        'question': "What is the result of the following code? \nx = 'pcap'\ndef a(x,y):\n\tz = a[0] \n\treturn z \nprint(a(x))",
        'options': ['TypeError', 'pcap', 'ValueError', 'NameError'],
        'correct_answer': 'TypeError',
        'explanation': 'The function a expects two arguments, but only one is given. Since y is missing it is a TypeError',
        'category': ['exceptions'],
        'subcategory': ['TypeError']
    },
    {
        'question': 'What is the result of the following code? \nclass CriticalError(Exception):\n\tdef __init__(self, message="CriticalError!!!"):\n\t\tException.__init__(self, message)\n\nraise CriticalError("CriticalError!")',
        'options': ['CriticalError!', 'CriticalError!!!', 'CriticalError', 'None of these answers are correct.'],
        'correct_answer': 'CriticalError!',
        'explanation': 'CriticalError has message as a parameter, which allows a string to replace the default and this is given in the last line, the excemption gets raised with a new error message',
        'category': ['exceptions'],
        'subcategory': ['error handling']
    },
    {
        'question': 'Assuming that a file named text.txt is in the directory and the current path is set correctly; What is the result?\ntext = "Hello PCAP"\nfile = open(text.txt)\nprint(file.readlines())\nfile.close()',
        'options': ['AttributeError', 'NameError', 'SyntaxError', 'FiteNotFoundError'],
        'correct_answer': 'AttributeError',
        'explanation': 'text is a variable of type string, .txt accesses an attribute txt which does not exist for the variable.',
        'category': ['miscellaneous'],
        'subcategory': ['AttributeError']
    },
    {
        'question': 'Assuming text.md is in the same directory and the path is correct what\'s the result?\ntext = "Hello PCAP"\nfile = open("text.txt")\nprint(file.readlines())\nfile.close()',
        'options': ['FiteNotFoundError', 'SyntaxError', 'AttributeError', 'NameError'],
        'correct_answer': 'FiteNotFoundError',
        'explanation': 'While a text.md is in the directory, the required text.txt is not, resulting in a FileNotFoundError',
        'category': ['miscellaneous'],
        'subcategory': ['FileNotFoundError']
    },
    {
        'question': 'Assuming the file data.txt is NOT in the directory or the path is set incorrectly, what\'s the result of this?\nf = open("data.txt", "w")\nf.close()',
        'options': ['FiteNotFoundError', 'A file named data.txt will be created.', 'NameError', 'None of these options are correct.'],
        'correct_answer': 'None of these options are correct.',
        'explanation': 'There will be no error because the file is not getting read, but since nothing is actively being written, no file is created either, the code will run without any problems but not perform a meaningful action.',
        'category': ['miscellaneous'],
        'subcategory': ['input/output']
    },
    {
        'question': 'import random\nstring = “PCAP master”\nWhich option would pick a single character from the given string randomly.\nprint(random.sample(str))\nprint(random.choice(str))\nprint(random.get(str, 1))\nprint(random.random(str))',
        'options': ['print(random.choice(str))', 'print(random.sample(str))', 'print(random.get(str, 1))', 'print(random.random(str))'],
        'correct_answer': 'print(random.choice(str))',
        'explanation': 'choice will choose a random element of the string sequence, the other options don\'t apply here.',
        'category': ['modules and packages'],
        'subcategory': ['random choice']
    },
    {
        'question': 'What happens if random.seed() is used without a value in ()? \n',
        'options': ['It uses the system\'s current time', 'It becomes truly random', 'It will cause an error', 'It uses a default value of 0'],
        'correct_answer': 'It uses the system\'s current time',
        'explanation': 'If no value is given, random(seed) will use the current time of the operating system to determine a seed',
        'category': ['modules and packages'],
        'subcategory': ['random seed']
    },
    {
        'question': 'Which function is used to get 5 elements from the list below randomly in a way that each element of the list has a different probability of being selected?\n\nnumberList = [100, 200, 300, 400, 500]',
        'options': ['random.choices(numberList, weights=(10, 5, 15, 20, 50), k=5)', 'random.choice(numberList, weights=(10, 5, 15, 20, 50), k=5)', 'random.sample(numberList, weights=(10, 5, 15, 20, 50), k=5)', 'None of these options are correct.'],
        'correct_answer': 'random.choices(numberList, weights=(10, 5, 15, 20, 50), k=5)',
        'explanation': 'random.choices is used for weighting, choice is used for a single element.',
        'category': ['modules and packages'],
        'subcategory': ['random choice']
    },
    {
        'question': 'What is the random.seed() method used for?',
        'options': ['A pseudorandom number generator based on a certain value to be used across platforms', 'An algorithm designed to ensure that random numbers are evenly distributed across different platforms.', 'A method that guarantees unique random number sequences for every execution of the program.', '"A function used to generate truly random numbers without any underlying algorithmic basis.'],
        'correct_answer': 'A pseudorandom number generator based on a certain value to be used across platforms',
        'explanation': 'seed is a pseudorandom number generator. Pseudorandom because the randomness isn\'t truly random but rather based on a seed value.',
        'category': ['modules and packages'],
        'subcategory': ['random seed']
    },
    {
        'question': 'Which function of the random module should be used to capture and change the current state of the random generator?',
        'options': ['random.getstate()\nrandom.setstate(state)', 'random.currentstate()\nrandom.setcurrentstate(state)', 'random.snapshot()\nrandom.storestate(state)', 'random.capturestate()\nrandom.savestate(state)'],
        'correct_answer': 'random.getstate()\nrandom.setstate(state)',
        'explanation': 'random.getstate() is used to capture the current state of the random number generator.\nrandom.setstate(state) is used to set the state of the random number generator to the specified state.',
        'category': ['modules and packages'],
        'subcategory': ['random state']
    },
    {
        'question': 'Which function should be used to get 4 elements from the following list randomly\nlst = [10, 50, 60, 90, 95, 110, 150, 200, 400]',
        'options': ['random.sample(lst, 4)', 'random.choice(lst, 4)', 'random.choices(lst, 4)', 'random.randint(lst, 4)'],
        'correct_answer': 'random.sample(lst, 4)',
        'explanation': 'random.sample(lst, 4) is used to get 4 random elements of the list, the alternatives require weighting or are used for a singular element',
        'category': ['modules and packages'],
        'subcategory': ['random sample']
    },
    {
        'question': 'Select the correct method to get a list of files from a directory',
        'options': ['os.listdir()', 'os.listfiles()', 'os.getfiles()', 'os.list()'],
        'correct_answer': 'os.listdir()',
        'explanation': 'os.listdir() shows all files in the designated directory',
        'category': ['modules and packages'],
        'subcategory': ['os']
    },
    {
        'question': 'Which function gives you a character based on the designated ASCII number?',
        'options': ['chr(number)', 'char(number)', 'ascii(number)', 'ord(number)'],
        'correct_answer': 'chr(number)',
        'explanation': 'chr() is a built-in Python function that returns the string representing a character whose Unicode code point is the integer number',
        'category': ['strings'],
        'subcategory': ['unicode code point']
    },
    {
        'question': 'Which function is used to get the ASCII code of a character',
        'options': ['ord("character")', 'char("character")', 'chr("character")', 'ascii("character")'],
        'correct_answer': 'ord("character")',
        'explanation': 'ord() is a built-in Python function that returns the Unicode code point for a given character.',
        'category': ['strings'],
        'subcategory': ['unicode code point']
    },
    {
        'question': 'What is the result of the following code? \nstr_1 = str("PCAP")\nstr_2 = "PCAP"\nprint(str_1 == str_2)\nprint(str_1 is str_2)',
        'options': ['True\nFalse', 'True\nTrue', 'False\nFalse', 'False\nTrue'],
        'correct_answer': 'True\nFalse',
        'explanation': 'str_2 is a new string that copies the sequence of str_1, since they have the same sequence == results in true. The is statement refers to the memory location which given the fact that both are independently created variables must be different.',
        'category': ['strings'],
        'subcategory': ['string something']
    },
    {
        'question': 'What is the result of the following code? \nstr = "Beat"\nprint (str[:2] + " PCAP")',
        'options': ['Be PCAP', 'BePCAP', 'BeaPCAP', 'Bea PCAP'],
        'correct_answer': 'Be PCAP',
        'explanation': 'Index 0 to 2(exlusive) is Be and the space in the second string makes it "Be PCAP"',
        'category': ['strings'],
        'subcategory': ['slicing']
    },
    {
        'question': 'How to change this string:\n"i will beat the PCAP!" into:\n"I Will Beat The PCAP!"?',
        'options': ['title()', 'capitalize()', 'isupper()', 'upper()'],
        'correct_answer': 'title()',
        'explanation': 'title() capitalizes all first letters.',
        'category': ['strings'],
        'subcategory': ['string functions']
    },
    {
        'question': 'What is the result of the following code? \nprint("PCAP" > "PACP")\nprint("PCAP" < "PBAP")',
        'options': ['True\nFalse', 'False\nFalse', 'True\True', 'False\True'],
        'correct_answer': 'True\nFalse',
        'explanation': 'It\'s about the lexographical order, C>A and but C<B is false.',
        'category': ['strings'],
        'subcategory': ['string order']
    },
    {
        'question': 'What is the result of the following code? \nstr_1 = "Juri\'s bonus is 15000"\nstr_2 = "15000"\n\nprint(str_1.isdigit())\nprint(str_2.isdigit())',
        'options': ['False\nTrue', 'False\nFalse', 'True\nTrue', 'True\nFalse'],
        'correct_answer': 'False\nTrue',
        'explanation': 'The isdigit() function checks if all characters in the sequence are digits, hereby it doesn\'t matter that it is in a string and not an integer',
        'category': ['strings'],
        'subcategory': ['string function']
    },
    {
        'question': 'What is the result of the following code? \nstr_1 = "My isname isisis Harrison isis Ford"\nsubstr = "is"\nprint(str_1.count(substr, 4))',
        'options': ['6', '5', '7', '2'],
        'correct_answer': '6',
        'explanation': 'There is 7 "is" in the string but we are starting to count from index 4 which is the 5th character, so from sname, meaning that the first is not counted',
        'category': ['strings'],
        'subcategory': ['string count']
    },
    {
        'question': 'Which of the following statements accurately describes the immutability of strings in Python?',
        'options': ['Strings in Python are immutable, meaning once created, their contents cannot be changed.', 'Strings in Python are mutable, allowing direct modification of their contents.', 'While strings in Python are immutable, certain built-in functions allow direct modification of their contents.', 'Strings in Python are immutable, but their contents can be changed using the modify() method.'],
        'correct_answer': 'Strings in Python are immutable, meaning once created, their contents cannot be changed.',
        'explanation': 'In Python, strings are immutable, which means their contents cannot be modified after creation. This property is fundamental to how strings behave in Python and ensures data integrity and consistency. Attempting to directly modify a string will result in the creation of a new string object with the desired modifications.',
        'category': ['strings'],
        'subcategory': ['string basics']
    },
    {
        'question': 'What is the primary idea behind encapsulation in object-oriented programming?',
        'options': ['Encapsulating data within a class to prevent access from outside the class.', 'Hiding the implementation details of a class while providing a clear interface.', 'Restricting access to certain methods within a class.', 'Allowing multiple classes to inherit from a single superclass.'],
        'correct_answer': 'Hiding the implementation details of a class while providing a clear interface.',
        'explanation': 'The main purpose of encapsulation is to hide the internal state of an object from the outside world and to only allow access to it through well-defined interfaces (methods).',
        'category': ['OOP'],
        'subcategory': ['encapsulation']
    },
    {
        'question': 'In Python, what does the self parameter represent in a class method?',
        'options': ['A reference to the instance of the class itself.', 'A built-in function for creating instances of a class.', 'A special variable used for accessing class-level attributes.', 'A keyword indicating the start of a class definition.'],
        'correct_answer': 'A reference to the instance of the class itself.',
        'explanation': 'The instance or object of a class is referenced via self.',
        'category': ['OOP'],
        'subcategory': ['self']
    },
    {
        'question': 'What is the term used to describe the ability of a subclass to override a method defined in its superclass?',
        'options': ['Overriding', 'Encapsulation', 'Polymorphism', 'Inheritance'],
        'correct_answer': 'Overriding',
        'explanation': 'The term used to describe the ability of a subclass to override a method defined in its superclass is indeed "Overriding" (Option D). Polymorphism (Option B) refers to the ability of objects of different types to be treated as objects of a common superclass. While overriding is a form of polymorphism, not all polymorphism involves method overriding.',
        'category': ['OOP'],
        'subcategory': ['polymorphism']
    },
    {
        'question': 'What is the purpose of the __init__ method in a Python class?',
        'options': ['Initializing class attributes.', 'Defining class methods.', 'Creating instances of the class.', 'Inheriting from a superclass.'],
        'correct_answer': 'Initializing class attributes.',
        'explanation': 'The __init__ method is a special method in Python classes that is automatically called when a new instance of the class is created. It is primarily used to initialize the instance\'s attributes with initial values. This method allows you to define the initial state of the object when it is created.',
        'category': ['OOP'],
        'subcategory': ['constructor']
    },
    {
        'question': 'Which of the following statements about class variables in Python is true?',
        'options': ['Class variables are shared among all instances of the class.', 'Class variables cannot be modified after their initial assignment.', 'Class variables are accessible only within the class where they are defined.', 'Class variables are defined inside methods and belong to instances of the class.'],
        'correct_answer': 'Class variables are shared among all instances of the class.',
        'explanation': 'Class variables are defined within the class scope but outside of any methods. They are shared by all instances (objects) of the class.',
        'category': ['OOP'],
        'subcategory': ['inheritance']
    },
    {
        'question': 'In Python, what is the purpose of the super() function?',
        'options': ['It allows access to methods and properties of the superclass.', 'It returns the superclass of a class.', 'It defines a subclass within a class definition.', 'It creates a new instance of a class.'],
        'correct_answer': 'It allows access to methods and properties of the superclass.',
        'explanation': 'super(superclass) will allow the class to get access to the the properties of class it inherited from, for example it can use the constructor to set parameters.',
        'category': ['OOP'],
        'subcategory': ['inheritance']
    },
    {
        'question': 'What does the term "polymorphism" refer to in object-oriented programming?',
        'options': ['The ability of an object to take on multiple forms.', 'The restriction of access to certain methods within a class.', 'The act of defining a new class based on an existing class.', 'The process of hiding the implementation details of a class.'],
        'correct_answer': 'The ability of an object to take on multiple forms.',
        'explanation': 'Polymorphism is a fundamental concept in object-oriented programming (OOP) that allows objects to be treated as instances of their parent class or any of their subclasses interchangeably.',
        'category': ['OOP'],
        'subcategory': ['polymorphism']
    },
    {
        'question': 'Which keyword is used in Python to define a method that belongs to a class and not to its instances?',
        'options': ['staticmethod', 'class', 'self', 'object'],
        'correct_answer': 'staticmethod',
        'explanation': 'staticmethod is a method that only applies to the parent class and children classes won\'t inherit it.',
        'category': ['OOP'],
        'subcategory': ['staticmethod']
    },
    {
        'question': 'What is the result of the following code? \nclass Child:\n\tdef __init__(self):\n\t\tself.value = 100\n\nclass Parent(Child):\n\tdef __init__(self):\n\tsuper().__init__()\n\nobj = Parent()\nprint(obj.value)',
        'options': ['100', 'The code is erroneous.', 'None', 'Child class does not have a value attribute.'],
        'correct_answer': '100',
        'explanation': 'Parent inherits from child the constructor, which lets it receive the self.value attribute for its instances, so the new object created has a value of 100.',
        'category': ['OOP'],
        'subcategory': ['super()']
    },
    {
        'question': 'What is the result of the following code? \nclass A:\n\tdef __init__(self):\n\t\tprint("A\'s constructor")\n\nclass B(A):\n\tdef __init__(self):\n\t\tsuper().__init__()\n\t\tprint("B\'s constructor")\n\nobj = B()',
        'options': ['A\'s constructor, B\'s constructor', 'B\'s constructor', 'A\'s constructor', 'B\'s constructor, A\'s constructor'],
        'correct_answer': 'A\'s constructor, B\'s constructor',
        'explanation': 'super() is called first in the initialization of the new instance and will print the message from class A, then the print of class B is called.',
        'category': ['OOP'],
        'subcategory': ['inheritance']
    },

]

def sample_questions():
    modules_questions = [q for q in pcap_questions if 'modules and packages' in q['category']]
    exceptions_questions = [q for q in pcap_questions if 'exceptions' in q['category']]
    strings_questions = [q for q in pcap_questions if 'strings' in q['category']]
    oop_questions = [q for q in pcap_questions if 'OOP' in q['category']]
    miscellaneous_questions = [q for q in pcap_questions if 'miscellaneous' in q['category']]

    modules_sample = random.sample(modules_questions, 6) if len(modules_questions) >= 6 else []
    exceptions_sample = random.sample(exceptions_questions, 5) if len(exceptions_questions) >= 5 else []
    strings_sample = random.sample(strings_questions, 9) if len(strings_questions) >= 9 else []
    oop_sample = random.sample(oop_questions, 12) if len(oop_questions) >= 12 else []
    miscellaneous_sample = random.sample(miscellaneous_questions, 8) if len(miscellaneous_questions) >= 8 else []

    total_sample = modules_sample + exceptions_sample + strings_sample + oop_sample + miscellaneous_sample
    random.shuffle(total_sample)

    return total_sample

total_sample = sample_questions()
'''
    {
        'question': 'What is the result of the following code? \n',
        'options': ['', '', '', ''],
        'correct_answer': '',
        'explanation': '',
        'category': ['OOP'],
        'subcategory': ['']
    },
POTENTIAL FUTURE QUESTIONS

modules and packages
6. Choose the correct function from the following list to get the random integer between 99 to 200, which is divisible by 3.
 random.randrange(99, 200, 3)
 random.randint(99, 200, 3)
 random.random(99, 200, 3)

7. To Generate a random secure integer number, select all the correct options.
 random.SystemRandom().randint()
 random.System.randint()
 secrets.randbelow()

8. I want to generate a random secure hex token of 32 bytes to reset the password, which method should I use
 secrets.hexToken(32)
 secrets.hex_token(32)
 secrets.tokenHex(32)
 secrets.token_hex(32) 

9. To generate a random float number between 20.5 to 50.5, which function of a random module I need to use
 random.random(20.5, 50.5)
 random.uniform(20.5, 50.5)
 random.randrange(20.5, 50.5)
 random.randfloat(20.5, 50.5)

10. To generate a random secure Universally unique ID which method should I use
 uuid.uuid4()
 uuid.uuid1()
 uuid.uuid3()
 random.uuid()

 1. Select the correct access mode to open a file only for exclusive creation
 t
 w
 x
 a

2. Which method is used to sets the position of a file pointer
 ftell()
 fseek()
 tell()
 seek()

3. Select the incorrect file access mode
 r
 ab+
 rw+
 wb+

4. Select the correct output of the following code

fp.seek(5, 1)
 Move file pointer five characters ahead from the current position.
 Move file pointer five characters ahead from the beginning of a file.
 Move file pointer five characters behind from the current position.
 Move file pointer five characters behind ahead from the end of a file.

5. If the file is opened in write mode and already exists, it truncates the existing content and places the filehandle at the beginning of the file.
 True
 False

6. Select all true statements when a file is opened using the with statement
 The with statement simplifies exception handling
 The file is automatically closed after leaving the block, and all the resources that are tied up with the file are released.
 File reading and writing are faster using the with statement.

7. Select the correct method to write a list of lines to a file
 write(list)
 writelines(list)
 writelist(list)

8. Select the correct mode to open a file for appending as well as reading
 a+
 ar
 rw
 ar+

9. Select all correct methods to delete files in Python
 os.remove('file_path')
 os.rmfile('file_path')
 pathlib.Path('file_path').remove()
 os.unlink('file_path')

11. Select all correct methods to copy the source file’s content to the destination file
 shutil.copy()
 shutil.copy2(src_path, dst_path)
 shutil.copyfileobj()
 shutil.copyfile()

12. Which method is used to read file line by line
 read(1)
 readlines(1)
 readline()
 line()

'''