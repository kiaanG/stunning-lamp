import random
response= input("do you want to role a dice")

def die(response):
   while response== "y":  
      num= random.randint(1, 6)
      print(num)

   if response=="n":
      print("[-----]")
      print("[     ]")
      print("[  0  ]")
      print("[     ]")
      print("[-----]")

die(response)