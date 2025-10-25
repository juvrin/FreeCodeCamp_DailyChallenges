import heapq
import json

def favorite_songs(playlist):
    max1 = max2 = float('-inf')
    title1 = ''
    title2 = ''
    # Loop through each number in list
    for p in playlist:
    
        # If the current number is greater 
        # than largest found so far
        if p['plays'] > max1:
        
            # Update second largest to the previous largest
            max2 = max1  
            title2 = title1

            # Update largest to the current number
            max1 = p['plays']     
            title1 = p['title']

        # If current number is less than largest
        # but greater than second largest
        elif p['plays'] > max2 and p['plays'] != max1:
        
            # Update second largest to current number
            max2 = p['plays']
            title2 = p['title'] 

    result_list = [title1,title2]
    return result_list


# test = favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]) 
# print(test)

#### OPTION 2
def favorite_songs(playlist):
    plays = []
    title1 = ""
    title2 = ""

    #Find top two most played
    for p in playlist:
        plays.append(p['plays'])

    top_two = heapq.nlargest(2, plays) 

    #Retrieve titles of those
    for p in playlist:
        if p['plays'] == top_two[0]:
            title1 = p['title']
        elif p['plays'] == top_two[1]:
            title2 = p['title']
    
    output = [f"\"{title1}\", \"{title2}\""]
    return output

test = favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ])
print(test)


