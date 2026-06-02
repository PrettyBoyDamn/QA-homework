numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("numbers:", numbers[0], numbers[-1])
cell_count = len(numbers)
numbers += [cell_count]
print("numbers with cell count: ", numbers[0], numbers[-1], cell_count)