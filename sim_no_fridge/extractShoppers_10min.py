"""
Customer Aggregation
2016 Gregor Ulm

Purpose: aggregate customer numbers of 10 checkout lanes into
the number of customers across all lanes in each 10-minute slot
during opening hours.

"""

# input:  data for 10 checkout lanes
# output: CSV with time slot and corresponding number of customers


for i in range(10):

  with open("output/cashier_" + str(i) +".csv", "r") as f:
      content = f.readlines()

  customers = set()
  res       = dict()

  # ignore header
  content = content[1:]

  for line in content:
    tmp      = line.split(";")
    time     = tmp[0]  # "Uhrzeit"

    if len(time) == 4:
      time = "0" + time

    time = time.strip()

    if time not in res.keys():
      res[time] = 1

    else:
      res[time] += 1


  ### write output (aggregations)
  f = open("output/cashiers_aggregated.csv", "a")
  # market is open from 7.00 to 21.59

  allValues = []
  allTimes  = []

  for hour in range(7, 22):

    if hour < 10:
      hour = "0" + str(hour)

    for minute in range(0, 60):

      if minute < 10:
        minute = "0" + str(minute)

      timestamp = str(hour) + ":" + str(minute)

      if timestamp not in res.keys():
        allValues.append(0)

      else:  # record numbers of values associated with a given key
        allValues.append(res[timestamp])

      allTimes.append(timestamp)


  """
  At this point we have all customer numbers and timestamps in order, meaning
  that they can be easily aggreagated to 10 minute intervals, i.e. every
  ten-element interval in both lists corresponds to ten minutes.

  This could probably have been done in a more elegant way, but the chosen
  solution follows trivially from the existing code.
  """

  final = dict()

  def processLists(times, values, acc):

    assert len(times) == len(values)

    if len(times) == 0:
      return

    times_head , times_tail  = times[0] , times[1:]
    values_head, values_tail = values[0], values[1:]

    if times_head.endswith("9"):
      final[times_head] = acc + values_head
      return processLists(times_tail, values_tail, 0)

    else:
      return processLists(times_tail, values_tail, acc + values_head)


  processLists(allTimes, allValues, 0)



  ks = final.keys()
  ks.sort()
  for x in ks:
    f.write(x + "," + str(final[x]) + "\n")
  f.close()