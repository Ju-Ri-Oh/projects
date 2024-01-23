pcap_questions = [
    {
        'question': 'What is the result of the following code? \n print(2 ** 3 ** 2 ** 1)',
        'options': ['512', '256', '64', 'The code is erroneous.'],
        'correct_answer': '512',
        'explanation': '2^3^2^1 is the same as 2^9, which is 512',
        'categories': ['basic']
    },
    {
        'question': 'What is the result of the following expression? \n i = 160 \n while len(str(i)) > 78: \n \t i *= 2 \n else: \n \t i //= 2 \n print(i)',
        'options': ['80', '160', '320', 'The code is erroneous.'],
        'correct_answer': '80',
        'explanation': 'i is converted into a str with a length of 3. 3 is not greater than 78 so i is divided by 2. \n len(str(160) = 3. \n 3 is not > 72 \n else -> 160 // 2 = 80)',
        'categories': ['basic', 'loop']
    },
    {
        'question': 'What\'s the output of the following code? \n'
                'print("Juri\'s sister\'s name\'s \\"Svetlana\\"") \n'
                'print(\'Juri\\\'s sister\\\'s name\\\'s \\"Svetlana\\"\')',
        'options': ['Juri\'s sister\'s name\'s "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"', 'Juri\'s sister\'s name\'s "Svetlana"\nJuris sisters names "Svetlana"', 'Juris sisters names "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"', 'The code is erroneous.'],
        'correct_answer': 'Juri\'s sister\'s name\'s "Svetlana"\nJuri\'s sister\'s name\'s "Svetlana"',
        'explanation': 'Single \' and double quotes \" can be used interchangeably',
        'categories': ['basic']
    },
    {
        'question': 'What is the result of the following code? \n "n = 0\n" "while n < 4:\n" \t"n += 1\n" \t"print(n, end=\" \")"',
        'options': ['1 2 3 4', '0 1 2 3', '1 2 3', 'The code is erroneous.'],
        'correct_answer': '1 2 3 4',
        'explanation': 'n entwers the loop with values of 0, 1, 2, 3 being smaller than 4 and then receives a value of +1 before being printed as 1, 2, 3, 4',
        'categories': ['basic', 'loop']
    },
    {
        'question': 'What is the result of the following code? \n a = 0 \nb = 2\nc = len("PCAP")\na = b > c\nprint(a)\nprint(type(a))',
        'options': ['False \n <class "bool">', '4 \n <class "integer">', 'True\n <class "bool">', 'The code is erroneous.'],
        'correct_answer': 'False \n <class "bool">',
        'explanation': '"2 > 4" is False, therefore x is False and thus from class bool',
        'categories': ['basic']
    },
    {
        'question': 'What is the result of the following code? \nnum = 1\nnum2 = 0\nnum = num ^ num2\nnum2 = num ^ num2\nnum = num ^ num2\nprint(num)\n',
        'options': ['0', '1', '4', '2'],
        'correct_answer': '0',
        'explanation': 'This is a bitwise XOR operation, the values of num and num2 are swapped.',
        'categories': ['basic', 'XOR']
    },
    {
        'question': 'What is the result of the following code? \n c, b, a = 2, 1, 0\na, c = c, b\nb = b - c\na, b, c = b, c, a\nprint(a, b, c)',
        'options': ['0 1 2', '2 1 0', '1 2 0', '1 0 2'],
        'correct_answer': '0 1 2',
        'explanation': 'A simple series of variable assignments.',
        'categories': ['basic']
    },
    {
        'question': 'What is the result of the following code? \nx = 0\ny = x ** 0\nif y < x + 1:\n\tz = 1\nelif y == 1:\n\tz = 2\nelse:\n\tz = 3\nprint(x + y + z)',
        'options': ['3', '2', '4', '1.'],
        'correct_answer': '3',
        'explanation': 'a stays at 0. b is 1 because 0^0 is 1 which leads to c becoming 2. 0 + 1 + 2 = 3',
        'categories': ['basic', 'elif']
    },
    {
        'question': 'What do you call this: __ ?',
        'options': ['dunder', 'underscore', 'init', 'anaconda'],
        'correct_answer': 'dunder',
        'explanation': 'two consecutive underscores are called a dunder, for "D"ouble "UNDER"score',
        'categories': ['basic']
    },
    {
        'question': 'What is the result of the following code? \n',
        'options': ['', '', '', 'The code is erroneous.'],
        'correct_answer': '',
        'explanation': '',
        'categories': ['']
    },


]
