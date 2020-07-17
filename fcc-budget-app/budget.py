class Category:
  def __init__(self, category):
    self.category = category
    self.ledger = []

  def deposit(self, amount, description = ""):
    self.ledger.append({
      "amount": float(amount),
      "description": description
    })

  def get_deposits(self):
    deposits = 0
    for entry in self.ledger:
      temp = entry.get("amount")
      if temp > 0:
        deposits += temp
    return deposits

  def get_balance(self):
    balance = 0
    for entry in self.ledger:
      balance += entry.get("amount")
    return balance

  def check_funds(self, amount):
    balance = self.get_balance()
    return balance >= amount

  def withdraw(self, amount, description = ""):
    check_funds = self.check_funds(amount)
    if check_funds:
      self.ledger.append({
        "amount": float(amount*-1),
        "description": description
      })
    return check_funds

  def get_withdrawls(self):
    withdrawls = 0
    for entry in self.ledger:
      temp = entry.get("amount")
      if temp < 0:
        withdrawls -= temp
    return withdrawls

  def transfer(self, amount, budget):
    check_funds = self.check_funds(amount)
    if check_funds:
      self.withdraw(amount, "Transfer to "+budget.category)
      budget.deposit(amount, "Transfer from "+self.category)
    return check_funds

  def __str__(self):
    answer = ""
    for i in range(int((30 - len(self.category))/2)):
      answer += "*"
    answer += self.category
    for i in range(int((30 - len(self.category))/2)):
      answer += "*"
    for entry in self.ledger:
      description = entry.get("description")[0:23]
      amount = "{:.2f}".format(entry.get("amount"))[0:7]
      answer += "\n"+description
      for i in range(30 - len(description) - len(amount)):
        answer += " "
      answer += amount
    answer += "\nTotal: "+str(self.get_balance())
    return answer


def create_spend_chart(categories):
  total = 0
  answer = "Percentage spent by category\n"
  for c in categories:
      total += c.get_withdrawls()
  for i in range(10, -1, -1):
    for j in range(3 - len(str(i*10))):
      answer += " "
    answer += str(i*10)+"|"
    for c in categories:
      percentage = c.get_withdrawls()*100/total
      if int(percentage) >= i*10:
        answer += " o "
      else:
        answer += "   "
    answer += " \n"
  answer += "    "
  for i in range(len(categories)):
    answer += "---"
  answer += "-"
  m = 0
  for c in categories:
    m = max(m, len(c.category))
  for i in range(m):
    answer += "\n    "
    for c in categories:
      try:
        answer += " "+c.category[i]+" "
      except:
        answer += "   "
    answer += " "
  print(answer)
  return answer