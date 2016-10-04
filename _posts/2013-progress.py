arr = [lambda: i for i in range(4)]
brr = [lambda: i for i in range(3)]
print("I guess that you are "
      "running Python %d." % arr[0]())
