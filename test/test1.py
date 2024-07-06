from datetime import datetime, timedelta

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
