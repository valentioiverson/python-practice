def count_substring(string, sub_string):
    count = 0
    for i in range(len(string)):
        if string[i: i + len(sub_string)] == sub_string:
            count += 1
        elif len(sub_string) < len(string) - i:
            continue
    return count

