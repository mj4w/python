"""
QUESTION 1: Alice has some cards with numbers written on them. She arranges the cards in decreasing order, and lays them out face down in a sequence on a table. She challenges Bob to pick out the card containing a given number by turning over as few cards as possible. Write a function to help Bob locate the card.
"""
# Sorted List [13,11,12,7,4,3,1,0]
"""
We need to write a program to find the position of a given number in a list of numbers arranged in decreasing order. We also need to minimize the number of times we access elements from the list.
"""
def locate_card(cards,query):
    
    position = 0
    while True:
        if cards[position] == query:
            return position
        
        position += 1
        
        if position == len(cards):
            return -1
    
object_dict = {
    'input': {
        'cards': [7,6,5,4,3,2,1],
        'query': 4
    }
}

## other approach
def locate_card(cards,query):
    position = 0
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

results = locate_card(**object_dict['input'])
print(results)