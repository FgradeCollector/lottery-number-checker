def lottery_number_input():
    numbers = []
    orders = ("첫", "두", "세", "네", "다섯", "여섯")
    order = 0

    for numb in orders:
        chosen_number = int(input(f'{numb} 번째 숫자를 입력하세요.:'))
        while chosen_number > 45 or chosen_number < 1:
            print("1과 45사이의 숫자를 입력해주세요.")
            chosen_number = int(input(f'다시 {numb} 번째 숫자를 입력하세요.:'))
        while order >= 1 and chosen_number in numbers:
            print("이전 숫자와 중복되지 않는 숫자를 입력해주세요.")
            chosen_number = int(input(f'다시 {numb} 번째 숫자를 입력하세요.:'))
            while chosen_number > 45 or chosen_number < 1:
                print("1과 45사이의 이전 숫자와 중복되지 않는 숫자를 입력해주세요.")
                chosen_number = int(input(f'다시 {numb} 번째 숫자를 입력하세요.:'))
        numbers.append(chosen_number)
        order += 1

    numbers.sort()

    return numbers
