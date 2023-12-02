file = open("day8_digits_input.txt")
lines = file.readlines()

result = 0
digits = []

one = ''
four = ''
seven = ''
eight = ''

fiveParts = []
sixParts = []


for i in range(len(lines)) :
    line = lines[i].strip().split("|")
    patterns = line[0].split(" ")
    output = line[1].split(" ")
            
    fiveParts = []
    sixParts = []

    for j in range(len(patterns)) :
        digit = patterns[j]
        length = len(digit)

        if length == 2 :
            one = digit
        elif length == 4 :
            four = digit
        elif length == 3 :
            seven = digit
        elif length == 7 :
            eight = digit
        elif length == 5 :
            fiveParts.append(digit)
        elif length == 6 :
            sixParts.append(digit)
    
    zero = ''
    two = ''
    three = ''
    five = ''
    six = ''
    nine = ''

    for k in range(len(fiveParts)) :
        guess = fiveParts[k]
        # is three?
        count = 0
        for letter in guess :
            for element in one :
                if letter == element :
                    count = count + 1

        if count == 2 :
            three = guess
        else :
            # is five
            count = 0
            for letter in guess :
                for element in four :
                    if letter == element :
                        count = count + 1
            
            if count == 3 :
                five = guess
            else :
                two = guess          

    for k in range(len(sixParts)) :
        guess = sixParts[k]

        # is nine?
        count = 0
        for letter in guess :
            for element in four :
                if letter == element :
                    count = count + 1

        if count == 4 :
            nine = guess
        else :
            # is zero?
            count = 0
            for letter in guess :
                for element in one :
                    if letter == element :
                        count = count + 1
            
            if count == 2 :
                zero = guess
            else :
                six = guess          
    
    digits = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    number = 0

    for j in range(len(output)) :
        value = output[j]

        for k in range(len(digits)) :
            digit = digits[k]

            count = 0
            for letter in value :
                for element in digit :
                    if letter == element :
                        count = count + 1
            # print(k, digit, value)
            if count == len(value) and count == len(digit) :
                number = number * 10 + k

    result = result + number

print(result)
