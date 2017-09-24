"""
Supermarket Simulation
2016 Gregor Ulm

See provided readme.txt
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

customers = []
checkout  = []



def processCustomers(hour, minute):
  global customers, checkout

  result = []

  # e.g. if (0, True, x): interaction w/fridge; next step (0, False, x-1)

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


# simulation opening times of one business day
def oneDay():

  for hour in range(7, 22):

    # limit on numbers of customers?

    for minute in range(0, 60):

      # number of draws to get a customer
      n = random.randint(0, 5)

      for i in range(n):

        # new customer?
        val = random.random()

        if prob[hour] > val:

          # "time to live" (time spent in store)

          # customer:
          # goes to fridge: boolean
          # time spent in supermarket

          pre    = random.randint(2, 8)
          post   = random.randint(2, 8)
          fridge = random.random() < 0.5

          customers.append( (pre, fridge, post) )

      # each minute:
      processCustomers(hour, minute)

      # note: we ignore customers still in store after closing time, based on
      #       the assuption that the checkout lanes close on time



if __name__ == "__main__":


  for i in range(10):

    f = open("output/cashier_" + str(i) +".csv", "w")

    oneDay()

    for x in checkout:
      f.write(x + "\n")
    customers = []
    checkout = []

    f.close()