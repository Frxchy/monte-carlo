#-Lucas Michellys-------------------------------------------------------------------------------------------------------
#-lmichell@ucsc.edu-----------------------------------------------------------------------------------------------------
#-Programming Assignment 7----------------------------------------------------------------------------------------------
#-Takes user input on details of a dice and calculates frequencies/probabilities and tabulates results------------------

import random

def throwdice(m, k, rng):
    L = []
    for i in range(m):
        roll = rng.randrange(1,k+1)
        L.append(roll)
    return tuple(L)
# end throwdice(m, k, rng)

def main(SEED=237):

    print()  # prints blank line
    m = int(input("Enter the number of dice: "))  # get number of dice
    print()  # prints blank line
    while m < 1:
        print("The number of dice must be at least 1")
        m = int(input("Please enter the number of dice: "))
        print()  # prints blank line
    # end while
    k = int(input("Enter the number of sides on each die: "))  # get number of sides on each die
    print()  # prints blank line
    while k < 2:
        print("The number of sides on each die must be at least 2")
        k = int(input("Please enter the number of sides on each die: "))
        print()  # prints blank line
    # end while
    c = int(input("Enter the number of trials to perform: "))  # get number of trials to perform
    print()  # prints blank line
    while c < 1:
        print("The number of trials must be at least 1")
        c = int(input("Please enter the number of trials to perform: "))
        print()  # prints blank line
    # end while
    rng = random.Random(SEED)  # create a random number generator

    sum = []
    for num in range(m, ((m*k)+1)):
        sum.append(num)
    # end for
    frequency = ((m*k)+1)*[0]  # creates a list range from user input
    for i in range(c):
        s = 0
        t = throwdice(m, k, rng)  # calls throwdice function
        for j in range(len(t)):
            s += t[j]
        frequency[s] += 1
        # end for
    #print(frequency)
    # end for

    relativeFrequency = []
    experimentalProbability = []
    for i in range(0, len(frequency)):
        relativeFrequency.append(frequency[i]/c)  # calculates relative frequency
        experimentalProbability.append(relativeFrequency[i]*100)  # calculates experimental probability
       # end for
    #print(relativeFrequency)
    #print(experimentalProbability)

    f1 = "{0:<9}{1:<14}{2:<22}{3:>25}"
    f2 = 70 * "-"
    f3 = "{0:>4}{1:>11}{2:>18.5f}{3:>21.2f} %"
    print(f1.format(" Sum", "Frequency", "Relative Frequency", "Experimental Probability"))
    print(f2)
    for i in range(m, len(frequency)):
        print(f3.format(i, frequency[i], relativeFrequency[i], experimentalProbability[i]))
    # end for
# end main
if __name__=='__main__':

    main()

# end if
