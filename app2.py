import collections

def checkEnteredValues(type, amount, products):
  isTypeCorrect = checkEnteredType(type, products)
  isAmountCorrect = checkEnteredAmount(amount)
  return isTypeCorrect and isAmountCorrect

def checkEnteredType(type, products):
  testProducts = [x.lower() for x in products]
  return type.lower() in testProducts

def checkEnteredAmount(amount):
  try:
    string_int = int(amount)
    return True
  except ValueError:
    return False

def createDescription(type, amount):
  if (amount > 1):
    return str(amount) + ' ' + type.lower() + 's'
  else:
    return str(amount) + ' ' + type.lower()

def addOrderToTable(table, type, amount):
  descr = createDescription(type, amount)
  table.append({ 'type': type, 'amount': amount, 'descr': descr })
  return table



products = ["Iphone", "Laptop", "Computer", "TV", "Mouse", "Keyboard"]
print("Available products: ", products)

table = collections.deque()

# add some default orders
table.append({ 'type': "Laptop", 'amount': 2, 'descr': '2 laptops' })
table.append({ 'type': "Mouse", 'amount': 5, 'descr': '5 mouses' })
table.append({ 'type': "TV", 'amount': 1, 'descr': '1 TV' })

productType = input("Enter type of product from the list above: ")
productAmount = input("Enter amount of wanted product: ")

if (checkEnteredValues(productType, productAmount, products)):
  table = addOrderToTable(table, productType, int(productAmount))
else:
  print("Order was not added - incorrect format")

print("Current version of table:")
for el in range(0, len(table)):
  print(table[el]['descr'])
