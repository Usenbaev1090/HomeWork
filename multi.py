#Дано положительное целое число. Вам необходимо подсчитать произведение всех цифр в этом числе, за исключением нулей.

#Для примера: Дано число 123405. Результат будет: 1*2*3*4*5=120 (не забудьте исключить нули).

def multi(number: int) -> int:
  multiply = 1
  for i in str(number):
    if i != "0":
      multiply *= int(i)
  number = multiply
  return number

if __name__ == '__main__':
    print('Example:')
    print(multi(123405))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert multi(123405) == 120
    assert multi(999) == 729
    assert multi(1000) == 1
    assert multi(1111) == 1
    print("Cool!")
