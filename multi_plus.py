# Дан массив целых чисел. Нужно найти сумму элементов с четными индексами (0-й, 2-й, 4-й итд), затем перемножить эту сумму и последний элемент исходного массива. Не забудьте, что первый элемент массива имеет индекс 0.

# Для пустого массива результат всегда 0 (ноль).

# Входные данные: Список (list) целых чисел (int).

# Выходные данные: Число как целочисленное (int).
def multi_plus(array):
  thesum = 0
  for el in array:
    if array.index(el) % 2 == 0:
      thesum += el
  if array == []:
    return 0
  array = thesum * array[-1]
  return array

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    print('Example:')
    print(multi_plus([0, 1, 2, 3, 4, 5]))

    assert multi_plus([0, 1, 2, 3, 4, 5]) == 30, "(0+2+4)*5=30"
    assert multi_plus([1, 3, 5]) == 30, "(1+5)*5=30"
    assert multi_plus([6]) == 36, "(6)*6=36"
    assert multi_plus([]) == 0, "An empty array = 0"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")
