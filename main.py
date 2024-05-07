from card import Card
import random
import math
import matplotlib.pyplot as plt
import itertools
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import statistics

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#CONSTANTS
CARDS_PICKED = 5
N = 10 # number of times to run draw simulation


def create_deck(*args):  # enter card type and then number of that card ex: copper,7,estate,3
    returndeck = []
    request = [*args]
    while len(request) > 1:
        for i in range(request.pop(1)):
            returndeck.append(request[0])
        request.pop(0)
    return returndeck



def calculate_probability_mathematically(num_of_copper_in_deck, num_cards_in_deck_f, num_of_copper_picked):
    permutation = math.factorial(CARDS_PICKED)/(math.factorial(num_of_copper_picked)*math.factorial(CARDS_PICKED-num_of_copper_picked))
    c = num_of_copper_in_deck
    n = num_cards_in_deck_f
    p = 1 #probability tracker
    for i in range(num_of_copper_picked):
        p = p * (c/n)
        c -= 1
        n -= 1
    for i in range(CARDS_PICKED-num_of_copper_picked):
        p = p * ((n-c)/(n))
        n -= 1

    return permutation*p

def calculate_probability_simply(kd,nd,kp): # kd is # of target card in deck, nd is # of cards in deck, kp is # of target card picked into hand
    answer = (math.comb(kd,kp)*math.comb(nd-kd,CARDS_PICKED-kp)/math.comb(nd,CARDS_PICKED))
    return answer

def print_copper_range(num_coppers_in_deck,num_cards_in_deck): #  compute probabilities using math!
    prob_2 = calculate_probability_mathematically(num_coppers_in_deck,num_cards_in_deck,2)
    prob_3 = calculate_probability_mathematically(num_coppers_in_deck, num_cards_in_deck, 3)
    prob_4 = calculate_probability_mathematically(num_coppers_in_deck, num_cards_in_deck, 4)
    prob_5 = calculate_probability_mathematically(num_coppers_in_deck, num_cards_in_deck, 5)
    print("Calculated: ")
    print("Percent of hands with 2 coppers:" + str(prob_2))
    print("Percent of hands with 3 coppers:" + str(prob_3))
    print("Percent of hands with 4 coppers:" + str(prob_4))
    print("Percent of hands with 5 coppers:" + str(prob_5))
    print(prob_2 + prob_3 + prob_4 + prob_5)

def print_cards(list):
    for card in list:
        print(card.name)

#def play_card(card):



def run_simulation():

    """
    #print deck to verify
    print()
    for i in range(len(deck)):  # print deck to verify create_deck works
        print(deck[i].name + ",", end =" ")
    print(" ")
    """
    sums = []
    average = 0
    N = int(entryN.get())
    #SIMULATE!
    for i in range(N):
        deck = create_deck(copper, int(entry3.get()), silver, int(entry4.get()), gold, int(entry5.get()), estate,
                           int(entry6.get()), laboratory, int(entry7.get()), village, int(entry8.get()), smithy,
                           int(entry9.get()))
        discard = []  # create discard pile
        hand = []
        random.shuffle(deck)
        actions = 1
        for i in range(5):
            hand.append(deck.pop(0))
        while actions > 0:
            if laboratory in hand:
                hand.remove(laboratory) #remove lab from hand
                if deck:
                    hand.append(deck.pop(0)) # pick a card
                if deck:
                    hand.append(deck.pop(0)) # pick another card

                discard.append(laboratory)
            if village in hand:
                hand.remove(village)  # remove lab from hand
                if(deck):
                    hand.append(deck.pop(0))  # pick a card
                actions += 1  # gain an action

                discard.append(village)

            if smithy in hand:
                hand.remove(smithy)  # remove lab from hand
                if deck:
                    hand.append(deck.pop(0))  # pick a card
                if deck:
                    hand.append(deck.pop(0))  # pick another card
                if deck:
                    hand.append(deck.pop(0))  # pick another card
                actions -= 1 # lose an action

                discard.append(smithy)

            no_actions = True
            for card in hand:
                if card.isAction:
                    no_actions = False




            if no_actions:
                break


        total = hand.count(copper) + hand.count(silver) * 2 + hand.count(gold) * 3
        sums.append(total)


    mean = sum(sums)/N
    #standard_deviation = statistics.stdev(sums)
    print(mean)
    #print(standard_deviation)

    #expected value
    label10 = tk.Label(root, text="Expected Value:")
    label10.grid(row=10, column=0, padx=10, pady=10)

    output10 = tk.Label(root, text=str(mean))
    output10.grid(row=10, column=1, padx=10, pady=10)

    #make graph
    num_0 = sums.count(0) / N
    num_1 = sums.count(1) / N
    num_2 = sums.count(2) / N
    num_3 = sums.count(3) / N
    num_4 = sums.count(4) / N
    num_5 = sums.count(5) / N
    num_6 = sums.count(6) / N
    num_7 = sums.count(7) / N
    num_8 = sums.count(8) / N
    num_9 = sums.count(9) / N
    num_10 = sums.count(10) / N

    print("Simulated with N = " + str(N) + ":")
    print("Percent of hands with 2 coppers:" + str(num_2))
    print("Percent of hands with 3 coppers:" + str(num_3))
    print("Percent of hands with 4 coppers:" + str(num_4))
    print("Percent of hands with 5 coppers:" + str(num_5))
    print(num_2 + num_3 + num_4 + num_5)

    # make graph
    names = ["0","1","2", "3", "4", "5","6","7","8","9","10"]
    values_simulation = [num_0,num_1,num_2, num_3, num_4,num_5,num_6,num_7,num_8,num_9,num_10]

    # Create the bar graph
    fig, ax = plt.subplots()

    # Plot a bar chart
    ax.grid(axis='y')
    ax.bar(names, values_simulation)

    title = "Simulated Probabilities for drawing x # of Coppers"
    ax.set_title(title)

    # Display the graph
    ax.set_xlabel('# of Coppers drawn')
    ax.set_ylabel("Frequency (%)")


    # Create a canvas to embed Matplotlib figure in Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()

    # Add the canvas to the Tkinter window using .grid()
    canvas.get_tk_widget().grid(row=0, column=2)












# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #create card types

    # money
    copper = Card("copper",1, 0, 0, 0, False)  # name, coin, actions, draws, vpoints, isAction):
    silver = Card("silver",2, 0, 0, 0, False)
    gold = Card("gold",3, 0, 0, 0, False)

    # VPs
    estate = Card("estate",0, 0, 0, 1, False)

    # Action Cards
    laboratory = Card("laboratory",0, 1, 2, 0, True)
    village = Card("village",0, 2, 1, 0, True)
    smithy = Card("smithy",0, 0, 3, 0, True)

    # CREATE DATA ENTRY WINDOW
    # Create the main window
    root = tk.Tk()
    root.title("Dominion Simulation:")

    # Create a labels
    label1 = tk.Label(root, text="Enter # of Each Type of Card in Deck:")
    label1.grid(row=0, column=0, padx=10, pady=10)

    label2 = tk.Label(root, text="Quantity:")
    label2.grid(row=0, column=1, padx=10, pady=10)

    label3 = tk.Label(root, text="Copper:")
    label3.grid(row=1, column=0, padx=10, pady=10)

    entry3 = tk.Entry(root)
    entry3.insert(0,"7")
    entry3.grid(row=1,column=1,padx=10,pady=10)

    label4 = tk.Label(root, text="Silver:")
    label4.grid(row=2, column=0, padx=10, pady=10)

    entry4 = tk.Entry(root)
    entry4.insert(0, "0")
    entry4.grid(row=2, column=1, padx=10, pady=10)

    label5 = tk.Label(root, text="Gold:")
    label5.grid(row=3, column=0, padx=10, pady=10)

    entry5 = tk.Entry(root)
    entry5.insert(0, "0")
    entry5.grid(row=3, column=1, padx=10, pady=10)

    label6 = tk.Label(root, text="Estate:")
    label6.grid(row=4, column=0, padx=10, pady=10)

    entry6 = tk.Entry(root)
    entry6.insert(0, "0")
    entry6.grid(row=4, column=1, padx=10, pady=10)

    label7 = tk.Label(root, text="Laboratory:")
    label7.grid(row=5, column=0, padx=10, pady=10)

    entry7 = tk.Entry(root)
    entry7.insert(0, "3")
    entry7.grid(row=5, column=1, padx=10, pady=10)

    label8 = tk.Label(root, text="Village:")
    label8.grid(row=6, column=0, padx=10, pady=10)

    entry8 = tk.Entry(root)
    entry8.insert(0, "0")
    entry8.grid(row=6, column=1, padx=10, pady=10)

    label9 = tk.Label(root, text="Smithy:")
    label9.grid(row=7, column=0, padx=10, pady=10)

    entry9 = tk.Entry(root)
    entry9.insert(0, "0")
    entry9.grid(row=7, column=1, padx=10, pady=10)

    labelN = tk.Label(root, text="Number of Trials:")
    labelN.grid(row=8, column=0, padx=10, pady=10)

    entryN = tk.Entry(root)
    entryN.insert(0, "10")
    entryN.grid(row=8, column=1, padx=10, pady=10)

    # Create a button to submit the input
    submit_button = tk.Button(root, text="Run", command=run_simulation)
    submit_button.grid(row=9, column=1, padx=10, pady=10)

    # Run the Tkinter event loop
    root.mainloop()
    
    # create deck

"""
    def run_simulation():
    deck = create_deck()
    for i in range(len(deck)):  # print deck to verify create_deck works
        print(deck[i].name + ",", end =" ")
    print(" ")
    discard = []  # create discard pile
    num_coppers_in_deck = deck.count(copper)
    num_laboratories_in_deck = deck.count(laboratory)
    num_cards_in_deck = len(deck)
    print(calculate_probability_simply(num_laboratories_in_deck,num_cards_in_deck,1))
    #  add action card functionality





    # compute draw statistics simulation
    num_of_coppers = []
    for i in range(N):
        random.shuffle(deck)
        hand = deck[:5]
        num_of_coppers.append(hand.count(copper))
    num_2 = num_of_coppers.count(2)/N
    num_3 = num_of_coppers.count(3)/N
    num_4 = num_of_coppers.count(4)/N
    num_5 = num_of_coppers.count(5)/N
    print("Simulated with N = " + str(N) + ":")
    print("Percent of hands with 2 coppers:" + str(num_2))
    print("Percent of hands with 3 coppers:" + str(num_3))
    print("Percent of hands with 4 coppers:" + str(num_4))
    print("Percent of hands with 5 coppers:" + str(num_5))
    print(num_2+num_3+num_4+num_5)
"""

"""
    #make graph
    names = ["2 Copper","3 Copper","4 Copper","5 Copper"]
    values_simulation = [num_2,num_3,num_4,num_5]
    values_probability = [prob_2,prob_3,prob_4,prob_5]
    bar_width = 0.35

    # Set the positions of the bars on the x-axis
    x = range(len(names))

    # Create the bar graph
    plt.bar(x, values_probability, width=bar_width, label='Calculated')
    plt.bar([i + bar_width for i in x], values_simulation, width=bar_width, label='Simulated')

    # Add labels and title
    title = "Calculated and Simulated Probabilities for drawing x # of Coppers with " + str(num_coppers_in_deck) + " coppers and " + str(num_cards_in_deck) + " total cards"
    plt.title(title)
    plt.xticks([i + bar_width / 2 for i in x], names)  # Centering x-tick labels

    # Add legend
    plt.legend()

    # Display the graph
    plt.xlabel('# of Coppers drawn')
    plt.ylabel("Frequency (%)")
    plt.show()



    #deck = create_deck(copper,7,estate,3)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
"""