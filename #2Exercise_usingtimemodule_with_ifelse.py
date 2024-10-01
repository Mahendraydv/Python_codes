import time 
timestamp = time.strftime('%a, %d %b %Y, %H:%M:%S: ')
print(timestamp)
if('%H:%M:%S:' >= '%00:%00:%00' < '%11:%59:%59'):
    print("Good Morining Sir")
elif('%H:%M:%S:' >= '%12:%00:%00' < '%16:%59:%59'):
    print("Good Afternoon Sir")   
elif('%H:%M:%S:' >= '%17:%00:%00' < '%00:%00:%00'):
    print("Good Night Sir")

