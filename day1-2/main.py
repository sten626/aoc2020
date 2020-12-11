import math

def parseFile(file):
  numbers = []
  with open(file) as f:
    for line in f:
      numbers.append(int(line))

  return numbers

def findNumbersWithSum(numbers, target_sum, total_numbers, chosen=None):
  if chosen is None:
    chosen = []

  sum_so_far = sum(chosen)

  if len(chosen) + 1 == total_numbers:
    # Last level
    for number in numbers:
      if sum_so_far + number == target_sum:
        result = chosen[:]
        result.append(number)

        return result
    
    return None

  for i in range(len(numbers)):
    number = numbers[i]
    result = findNumbersWithSum(numbers[i+1:], target_sum, total_numbers, chosen=[*chosen, number])

    if result:
      return result

def main():
  numbers = parseFile('./input.txt')
  result = findNumbersWithSum(numbers, 2020, 3)
  product = 1

  for number in result:
    product *= number

  print(product)
  
if __name__ == "__main__":
  main()