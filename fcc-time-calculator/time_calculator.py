def add_time(start, duration, extra = None):
  a = start.split(":")
  b = a[1].split(" ")
  a[1] = b[0]
  a.append(b[1])

  a[0] = int(a[0])
  a[1] = int(a[1])
  a[2] = a[2].upper()

  b = duration.split(":")

  b[0] = int(b[0])
  b[1] = int(b[1])

  c0 = a[0]+b[0]
  c1 = a[1]+b[1]

  while c1 >= 60:
    c1 -= 60
    c0 += 1
  
  days = 0
  while c0 > 12:
    c0 -= 12
    if a[2] == "AM":
      a[2] = "PM"
    elif a[2] == "PM":
      days += 1
      a[2] = "AM"
  if c0 == 12:
    days += 0.5
    if a[2] == "AM":
      a[2] = "PM"
    elif a[2] == "PM":
      a[2] = "AM"
  
  days = round(days)
  answer = str(c0)+":"
  if len(str(c1)) == 1:
    answer += "0"
  answer += str(c1)+" "+a[2]
  if extra != None:
    extra = extra.capitalize()
    for i in range(days):
      if extra == "Sunday":
        extra = "Monday"
      elif extra == "Monday":
        extra = "Tuesday"
      elif extra == "Tuesday":
        extra = "Wednesday"
      elif extra == "Wednesday":
        extra = "Thursday"
      elif extra == "Thursday":
        extra = "Friday"
      elif extra == "Friday":
        extra = "Saturday"
      elif extra == "Saturday":
        extra = "Sunday"
    answer += ", "+extra
  if days == 0:
    None
  elif days == 1:
    answer += " (next day)"
  else:
    answer += " ("+str(days)+" days later)"
  return answer
