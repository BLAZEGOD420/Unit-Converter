def tableToDict(file):
    f = open(file, 'r')
    lines = f.readlines()
    dict = {}
    for line in lines:
        split = line.split(' = ')
        start = ''
        end = ''
        conversion = ''
        for char in split[0]:
            if char.isalpha():
                start += char
        for char in split[1]:
            if char.isalpha() and char != '.':
                end += char
            else:
                conversion += char
        dict[start] = [float(conversion), end]
    return dict


def converter(value, start, end, table):
    # first convert to meters or inches, f or c, etc
    x = table[start][0] * float(value)
    if table[end][1] == table[start][1]:
        # if no conversions to a different system of measurement is needed, just divide
        return x / table[end][0]
    elif start == end:
        return value
    else:
        # convert to a different system of measurement
        x *= table[table[start][1]][0]
        # divide
        return x/table[end][0]


amount = input("starting amount: ")
startingUnit = input("starting unit (abbreviated): ")
targetUnit = input("target unit (abbreviated): ")

distanceConversions = tableToDict('distanceConversionTable.txt')
timeConversions = tableToDict('timeConversionTable.txt')
massConversions = tableToDict('massConversionTable.txt')
volumeConversions = tableToDict('volumeConversionTable.txt')

if (startingUnit in distanceConversions) and (targetUnit in distanceConversions):
    print("{}{} = {:.10f}{}".format(amount, startingUnit, converter(amount, startingUnit, targetUnit,
                                                                    distanceConversions), targetUnit))
elif (startingUnit in timeConversions) and (targetUnit in timeConversions):
    print("{}{} = {:.10f}{}".format(amount, startingUnit, converter(amount, startingUnit, targetUnit,
                                                                    timeConversions), targetUnit))
elif (startingUnit in massConversions) and (targetUnit in massConversions):
    print("{}{} = {:.10f}{}".format(amount, startingUnit, converter(amount, startingUnit, targetUnit,
                                                                    massConversions), targetUnit))
elif (startingUnit in volumeConversions) and (targetUnit in volumeConversions):
    print("{}{} = {:.10f}{}".format(amount, startingUnit, converter(amount, startingUnit, targetUnit,
                                                                    volumeConversions), targetUnit))
else:
    print("not possible")
