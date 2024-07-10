"""
Keep the track of the search space in the list 
"""
def locate_card(cards,query):
    lo, hi  =  0, len(cards) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print("lo:", lo, "hi:", hi, "mid: ", mid, "mid_number:", mid_number)
        if mid_number == query:
            return mid
        elif mid_number < query:
            hi = mid - 1
        elif mid_number > query:
            lo = mid + 1
    
    return -1 

dict_tests = {
    "input": {
        "cards": [1,2,4,5,6,7,8],
        "query": 8
    }
}

results = locate_card(**dict_tests['input'])
print(results)