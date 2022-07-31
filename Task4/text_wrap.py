

def wrap(string, max_width):
    temp = ""
    for i in range(0,len(string),max_width):
        temp += string[i:i+max_width] + "\n"
    return temp