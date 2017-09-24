"""
Script for computing correlations (number of customers vs. energy cost)
2016 Gregor Ulm
"""

customers = []
energy    = []

with open("output/aggregated_cashier.csv", "r") as f:
  content = f.readlines()

for line in content:
  line = line.strip()
  (_, n) = line.split(",")
  customers.append(int(n))



with open("output/aggregated_cashier_fridges.csv", "r") as g:
  content = g.readlines()


for line in content:
  line = line.strip()
  (_, n) = line.split(",")
  energy.append(n)


assert len(customers) == len(energy)


h = open("output/correlate_raw.csv", "w")

for i in range(len(customers)):
  h.write( str(customers[i]) + "," + str(energy[i]) + "\n" )



f.close()
g.close()
h.close()