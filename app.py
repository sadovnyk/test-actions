from typing import List, Dict

def filter_active_users(users: List[Dict]) -> List[Dict]:
    """Фільтрує активних користувачів."""
    return [u for u in users if u.get("is_active", False)]

def calculate_average_age(users: List[Dict]) -> float:
    """Обчислює середній вік списку користувачів."""
    if not users:
        return 0.0
    total_age = sum(u.get("age", 0) for u in users)
    return round(total_age / len(users), 2)

if __name__ == "__main__":
    raw_data = [
        {"id": 1, "name": "Олена", "age": 24, "is_active": True},
        {"id": 2, "name": "Тарас", "age": 30, "is_active": False},
        {"id": 3, "name": "Ірина", "age": 28, "is_active": True},
        {"id": 4, "name": "Максим", "age": 22, "is_active": True},
    ]

    active = filter_active_users(raw_data)
    avg_age = calculate_average_age(active)

    print(f"Активних користувачів: {len(active)}")
    print(f"Середній вік активних: {avg_age}")