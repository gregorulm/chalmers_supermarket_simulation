Simulation of Customer Movements in a Supermarket
Gregor Ulm, 2016
Chalmers University of Technology
Computer Science and Engineering Department
Distributed Computing and Systems Research Group

Brief description:
The Python code in this directory is a quirky simulation of a supermarket, in
which customers numbers follow a particular pattern over the day. There are
two versions, one with a fridge, i.e. a large-scale cooling cabinet, and one
without.

The high-level view is as follows: the store is open from 7:00 to 21:59. For
every minute of every hour in that interval, there is a set probability that a
new customer will enter the supermarket. A visit to the supermarket has at most
three phases: pre-fridge, fridge, and post-fridge. Some customers don't go to
the fridge. The duration of each phase is random. At the end of the sequence
just described, the visitor moves on to one of the checkout registers. Well, in
reality, the script runs ten sequential simulations, one for each checkout
register, but that does not affect the outcome in a meaningful way.

More formally, at the center of the simulation is a simple Markov process with
the states "start", "fridge", and "cashier". From "start", a customer can
transition to either "fridge" or "cashier", from "fridge" to only "cashier".
"Cashier" is the final state.

The final result is one CSV file for each checkout register, showing the
timestamp for each encountered customer. By collating those files, it can
be determined how many customers left the store in each 10-minute interval.
Thus, this simulation models high-level shopping behavior. The result was
used for further explorations, for instance predicting customer numbers
based on how many customers left the supermarket in the preceeding 10-minute
intervals.


Execution order:
1. supermarket.py
2. extractShoppers_10min.py
3. correlate.py
4. visualize.py

Files 3) and 4) are only available in /sim_fridge.
