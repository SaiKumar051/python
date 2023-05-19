num = int(input("enter temperature in celsius: "))


if num <= -273.15:
  print("the tempa is invalid")

elif num<= 0 and num >= -273.15:
   print("tempa is beloe freezing")

elif num> 0 and num <= 100:
    print("temp is in normal range")

else:
   print('temp is above boiling')
