from func.lottery_number_extractor import lottery_number_extract
from func.lottery_number_input import lottery_number_input
from func.lottery_number_check import lottery_number_check

# chosen_numbers = lottery_number_input()
chosen_numbers = [3, 10, 24, 33, 38, 45]
winning_numbers = lottery_number_extract()

print(chosen_numbers)
print(winning_numbers)
lottery_number_check(chosen_numbers, winning_numbers)
