import sys

if __name__ == "__main__":
    s = sys.stdin.readline().strip()
    left = 0
    right = len(s) - 1
    insert = 0 
    while left <= right and insert < 3:
        if s[left] != s[right]:     
            if insert == 0:
                temp_s = s
                temp_left = left
                temp_right = right
                s = s[0:left] + s[right] + s[left:] 
                right += 1
            elif insert == 1:
                left = temp_left
                right = temp_right
                s = temp_s[0:(right + 1)] + temp_s[left] + temp_s[(right + 1):]
                right += 1
            insert += 1
        else:
            left += 1
            right -= 1

    if insert == 3:
        print "NA"
    elif insert == 0:
        s = s[0:left] + s[left-1] + s[left:]    
        print s
    else:
        print s
