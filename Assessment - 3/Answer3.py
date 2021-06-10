def count_substring(string, sub_string):
    l=len(sub_string)
    num = 0
    for i in range(1, len(string)-1):
        if string[i-1:i+l-1] == sub_string :
            num += 1
    return num
