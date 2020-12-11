def parseFile(file):
  numbers = []
  with open(file) as f:
    for line in f:
      numbers.append(int(line))

  return numbers

def main():
  numbers = parseFile('./input.txt')
  first, second = findNumbersWithSum(numbers, 2020)
  product = first * second
  print(product)

def findNumbersWithSum(numbers, sum):
  firstNumber = numbers.pop(0)
  secondNumber = findNumberWithSum(firstNumber, numbers, sum)

  return (firstNumber, secondNumber) if secondNumber else findNumbersWithSum(numbers, sum)
  
def findNumberWithSum(firstNumber, otherNumbers, sum):
  for number in otherNumbers:
    if firstNumber + number == sum:
      return number

  return None

if __name__ == "__main__":
  main()