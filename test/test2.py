import random

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
