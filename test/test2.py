from datetime import datetime, timedelta
import random
import re

# Перше завдання
def get_days_from_today(date_str):
    try:
        input_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        
        today = datetime.now().date()
        
        days_diff = (today - input_date).days
        
        return days_diff
    
    except ValueError:
        print("Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'.")
        return None
    
if __name__ == "__main__":
    date_str = "2021-10-09"
    days = get_days_from_today(date_str)
    
    if days is not None:
        print(f"Кількість днів між {date_str} і сьогодні: {days}")

# Друге завдання
def get_numbers_ticket(min_num, max_num, quantity):
    if min_num < 1 or max_num > 1000 or min_num >= max_num or quantity < 1 or quantity > (max_num - min_num + 1):
        return []
    
    numbers = []
    
    while len(numbers) < quantity:
        random_number = random.randint(min_num, max_num)
        
        if random_number in numbers:
            continue
        
        numbers.append(random_number)
    
    numbers.sort()
    
    return numbers

if __name__ == "__main__":
    min_num = 1
    max_num = 49
    quantity = 6
    lottery_numbers = get_numbers_ticket(min_num, max_num, quantity)
    print("Ваші лотерейні числа:", lottery_numbers)

#Третє завдання
def normalize_phone(phone_number):
    normalized_number = re.sub(r'\D', '', phone_number)
    
    if normalized_number.startswith('380') and len(normalized_number) == 12:
        normalized_number = '+' + normalized_number
    elif normalized_number.startswith('0') and len(normalized_number) == 10:
        normalized_number = '+38' + normalized_number[1:]
    elif not normalized_number.startswith('+'):
        normalized_number = '+38' + normalized_number
    
    return normalized_number

if __name__ == "__main__":
    raw_numbers = [
        "067\\t123 4567",
        "(095) 234-5678\\n",
        "+380 44 123 4567",
        "380501234567",
        "    +38(050)123-32-34",
        "     0503451234",
        "(050)8889900",
        "38050-111-22-22",
        "38050 111 22 11   ",
    ]
    
    sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
    print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
