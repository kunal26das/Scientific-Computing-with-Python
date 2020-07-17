def arithmetic_arranger(problems, solve = False):
  flag1 = False
  flag2 = False
  flag3 = False
  flag4 = False

  if len(problems) > 5:
    flag1 = True
  for i in range(len(problems)):
    if " + " in problems[i]:
      problems[i] = problems[i].split(" + ")
      for j in range(len(problems[i])):
        try:
          if len(problems[i][j]) > 4:
            flag4 = True
            break
          problems[i][j] = int(problems[i][j])
        except:
          flag3 = True
          break
      problems[i].append("+")
      if solve:
        problems[i].append(problems[i][0] + problems[i][1])
    elif " - " in problems[i]:
      problems[i] = problems[i].split(" - ")
      for j in range(len(problems[i])):
        try:
          if len(problems[i][j]) > 4:
            flag4 = True
            break
          problems[i][j] = int(problems[i][j])
        except:
          flag3 = True
          break
      problems[i].append("-")
      if solve:
        problems[i].append(problems[i][0] - problems[i][1])
    elif " * " in problems[i]:
      flag2 = True
      break
    elif " / " in problems[i]:
      flag2 = True
      break

  if flag1:
    return "Error: Too many problems."
  elif flag2:
    return "Error: Operator must be '+' or '-'."
  elif flag3:
    return "Error: Numbers must only contain digits."
  elif flag4:
    return "Error: Numbers cannot be more than four digits."

  answer = ""
  for i in range(len(problems)):
    answer += "  "
    if len(str(problems[i][0])) < len(str(problems[i][1])):
      for x in range(len(str(problems[i][1])) - len(str(problems[i][0]))):
        answer += " "
    answer += str(problems[i][0])
    if i < len(problems) - 1:
      answer += "    "
  answer += "\n"

  for i in range(len(problems)):
    answer += problems[i][2]+" "
    if len(str(problems[i][0])) > len(str(problems[i][1])):
      for x in range(len(str(problems[i][0])) - len(str(problems[i][1]))):
        answer += " "
    answer += str(problems[i][1])
    if i < len(problems) - 1:
      answer += "    "
  answer += "\n"

  for i in range(len(problems)):
    answer += "--"
    for j in range(max(len(str(problems[i][0])), len(str(problems[i][1])))):
      answer += "-"
    if i < len(problems) - 1:
      answer += "    "

  if solve:
    answer += "\n"
    for i in range(len(problems)):
      for j in range(2 + max(len(str(problems[i][0])), len(str(problems[i][1]))) - len(str(problems[i][3]))):
        answer += " "
      answer += str(problems[i][3])
      if i < len(problems) - 1:
        answer += "    "

  print(answer, end=' ')
  return answer