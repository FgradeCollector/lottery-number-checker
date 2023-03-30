def lottery_number_check(chosen_numbers, winning_numbers):
    winner_numbers_string = winning_numbers['당첨번호']
    for i in winner_numbers_string:
        trans = i
        print(type(trans))
    """
    bonus_number = winning_numbers['보너스번호']
    check_winner_numbers = []
    check_bonus_number = [False]
    for check in chosen_numbers:
        if check in winner_numbers:
            check_winner_numbers.append(True)
    for check in bonus_number:
        if check in winner_numbers:
            check_bonus_number[0] = True
    print(check_winner_numbers)
    print(check_bonus_number)
    if check_winner_numbers.count(True) == 6:
        print("1등 입니다!")
    if check_winner_numbers.count(True) == 5 and check_bonus_number[0]:
        print("2등 입니다!")
    if check_winner_numbers.count(True) == 5 and not check_bonus_number[0]:
        print("3등 입니다!")
    if check_winner_numbers.count(True) == 4:
        print("4등 입니다!")
    if check_winner_numbers.count(True) == 3:
        print("5등 입니다!")
    else:
        print("꽝 입니다.")
        """
