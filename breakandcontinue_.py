for i in range(1, 100, 1):
    print(i ,end=" ")
    if (i==50):
           break
    else:
          print("Miss")
print("Thankyou")   



for i in [2, 3, 4, 6, 8, 0]:
      if(i%2!=0):
            continue
      print(i)
print("skip")