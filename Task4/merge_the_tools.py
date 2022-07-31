def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        unique_string = ""
        for j in string[i:i+k]:
            if(j not in unique_string):
                unique_string += j
        print(unique_string)
        
