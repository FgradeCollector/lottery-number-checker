from bs4 import BeautifulSoup
import requests


def lottery_number_extract():
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin"
    request = requests.get(url, headers={"User-Agent": "number"})

    if request.status_code == 200:
        soup = BeautifulSoup(request.text, "html.parser")
        round = soup.find('option', selected=True).string
        numb = soup.find_all("span", class_="ball_645")
        numbers = []
        for number in numb:
            numbers.append(number.string)
        winner_numbers = numbers[0:6]
        bonus_number = numbers[-1]
        round_info = {'회차': round,
                      '당첨번호': winner_numbers, '보너스번호': bonus_number}

        return round_info
    else:
        print("Can't print numbers")
