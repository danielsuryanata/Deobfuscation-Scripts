# Deobfuscate per row
# Mode == False -> the separator is '''
# Mode == True -> the separator is ','
def deobfuscateRow(Text, mode):
    Text = Text.lstrip("\(").rstrip("\)")

    # Read the order, put it into a list
    order = Text.split("-f")[0]
    order = order.rstrip(" ")
    order = order.lstrip("\"").rstrip("\"")
    order = order.replace("{", "")
    order = order.rstrip("}")
    listOrder = order.split("}")

    # Parse the actual input, place them in a dictionary
    input = Text.split("-f")[1]
    input = input.lstrip(" ").lstrip("'").rstrip("'")
    if(mode == False):
        tempList = input.split("'''")
    else:
        tempList = input.split("','")

    lengthTempList = len(tempList)
    i = 0
    dictInput = {}
    while (i < lengthTempList):
        dictInput[i] = tempList[i]
        i+=1

    # Read from order and match it to the dictionary
    finalString = ""
    for i in listOrder:
        finalString += dictInput[int(i)]

    return finalString
