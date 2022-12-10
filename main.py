def plex(num): # add all the digits of a number together
    output = 0
    print(" > Plexing " + str(num) + "...")
    first = True
    for i in range(len(str(num)) - 1): # Iterate over digits 
        if output != 0: # Do not print "0 + i" 
            print(str(output) + " + " + str(num)[i] + " = ", end='') # print current equation
        output = output + int(str(num)[i]) # add current total with current digit
        if first == True: # Do not print output for first iteration (0 + i)
            first = False
        else:
            print(str(output)) # print equation sum

    print(str(output) + " + " + str(num)[-1] + " = ") # print final equation
    output = output + int(str(num)[-1]) # Add final number
    print("Output: " + str(output)) # print final summ
    return output

def plex_to_dp(num, dp): # plex until specific number decimal points
    print(" > Plexing " + str(num) + " to " + str(dp) + " decimal point(s)...")
    while len(str(num)) != int(dp):
        num = plex(num)
    return num

def cumulate(num): # add all numbers that make up a number
    output = 0
    print(" > Culumating " + str(num) + "...")
    for i in range(num + 1):
        output = output + i
    print("Output: " + str(output))
    return output

def ticCount(num): #WIP
    print(2**(num-1))

def quasiphonize(num):
    print(" > Quasiphonizing " + str(num) + "...")
    num = str(num)
    #num = num.replace("0", "eiaoung")
    num = num.replace("0", "y") # using "y" as an all purpose vowel
    num = num.replace("1", "gl")
    num = num.replace("2", "dt")
    num = num.replace("3", "zx")
    num = num.replace("4", "skr")
    num = num.replace("5", "ktt")
    num = num.replace("6", "tch")
    num = num.replace("7", "pb")
    num = num.replace("8", "mnm")
    num = num.replace("9", "tn")
    print(num)
    return num
