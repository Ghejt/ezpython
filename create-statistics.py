import math
def statistics():
#Initialize. Get datatype and file name.
    datatype = input("Enter data type (population or sample): ")
    datatype = datatype.lower()
    print("Create a text file with your data in this directory, seperating each entry with a new line.")
    file = input("Enter file name, including '.txt': ")
    numbers = []
#Read data and run functions.
    with open(file, 'r') as data:
        for line in data:
            numbers.append(line.strip())
    try:
        sortednumbers = sortedlist(numbers)
        median = middle(sortednumbers)
        average = mean(numbers)
        modes = mode(numbers)
        standard_deviation = stddev(numbers, datatype, average)
        variance = vari(standard_deviation)
#Create statistics file.
        with open('statistics', 'w') as statistics:
            statistics.write("Here are the statistics based off your %s data!\nSorted data: %s\nMedian: %s\nMean: %.5f\nMode(s): %s\nStandard Deviation: %.5f\nVariance: %.5f" % (datatype, sortednumbers, median, average, modes, standard_deviation, variance))
        print("Your file has been created. It is 'statistics.txt', located in this directory.")
    except:
            print("Something went wrong. Delete any whitespace and non-numbers in your data.")

#Sort data.
def sortedlist(numbers):
    numbers = [float(x) for x in numbers]
    numbers.sort()
    return numbers

#Calculate mean.
def mean(numbers):
    total = 0
    for number in numbers:
        total += float(number)
    mean = total/len(numbers)
    return mean

#Calculate median.
def middle(sortednumbers):
    middleval = len(sortednumbers)/2
    middle = 0
    if middleval.is_integer():
        middle = sortednumbers[int(middleval)]
    else:
        middleval = int(middleval)
        middle = (sortednumbers[middleval] + sortednumbers[middleval + 1])/2
    return middle

#Calculate mode.
def mode(numbers):
    occurences = {}
    for x in numbers:
        total = occurences.get(x, 0)
        occurences[x] = occurences.get(x, 0) + 1
    values = list(occurences.values())
    keys = list(occurences.keys())
    if (values[1:] == values[:-1]):
        mode = 'There is no mode in this data.'
    else:
        Max = []
        maxis = []
        pos = 0
        maxi = max(values)
        for x in values:
            if x == maxi:
                Max.append(keys[pos])
            pos += 1
        mode = str(Max)[1:-1]
    return mode

#Calculate standard deviation and variance.
def stddev(numbers, datatype, average):
    if datatype == 'population':
        numerator = 0
        for number in numbers:
            numerator += (float(number) - average)**2
        stddev = math.sqrt(numerator/len(numbers))
        return stddev
    elif datatype == 'sample':
        numerator = 0
        for number in numbers:
            numerator += (abs(float(number) - average))**2
        stddev = math.sqrt(numerator/(len(numbers) - 1))
        return stddev
    
def vari(standard_deviation):
    vari = standard_deviation**2
    return vari
