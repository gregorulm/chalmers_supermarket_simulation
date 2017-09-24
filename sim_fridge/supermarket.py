"""
Supermarket Simulation with Fridge
2016 Gregor Ulm

See 'supermarket.py' in /sim_no_fridge for additional comments
"""

import random
# 1 minute 'ticks'

# probability/minute to get a new customer
prob = { 7 : 0.1 ,
         8 : 0.2 ,
         9 : 0.2 ,
        10 : 0.3 ,
        11 : 0.7 ,
        12 : 0.9 ,
        13 : 0.7 ,
        14 : 0.6 ,
        15 : 0.4 ,
        16 : 0.3 ,
        17 : 0.6 ,
        18 : 0.8 ,
        19 : 0.7 ,
        20 : 0.3 ,
        21 : 0.1  }

customers   = []
checkout    = []
fridgeUsers = []


def processCustomers(hour, minute):
  global customers, checkout

  result = []

  for (pre, fridge, post) in customers:
    if pre == 0:
      if post == 0:
        if minute < 10:
          tmp = str(hour) + ":0" + str(minute)
        else:
          tmp = str(hour) + ":" + str(minute)

        if hour < 10:
          checkout.append( "0" + tmp)
        else:
          checkout.append(tmp)

      else:
        result.append( (pre, fridge, post - 1) )

    if pre > 0:
      result.append( (pre - 1, fridge, post) )

  customers = result


def oneDay():

  global fridgeUsers

  for hour in range(7, 22):

    for minute in range(0, 60):

      n = random.randint(0, 5)

      for i in range(n):

        val = random.random()

        if prob[hour] > val:

          pre    = random.randint(2, 8)
          post   = random.randint(2, 8)
          fridge = random.random() < 0.5

          m = None
          h = None

          # time at fridge
          if fridge:
            if minute < 10:
              m = "0" + str(minute)
            else:
              m = str(minute)

            if hour < 10:
              h = "0" + str(hour)
            else:
              h = str(hour)

            fridgeUsers.append( h + ":" + m )

          customers.append( (pre, fridge, post) )


      processCustomers(hour, minute)


if __name__ == "__main__":


  for i in range(10):

    f = open("output/cashier_" + str(i) +".csv", "w")

    oneDay()

    for x in checkout:
      f.write(x + "\n")
    customers = []
    checkout = []


    g = open("output/cashier_fridge_" + str(i) +".csv", "w")

    for x in fridgeUsers:
      g.write(x + "\n")

    fridgeUsers = []


    f.close()
    g.close()