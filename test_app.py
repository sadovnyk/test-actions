import pytest
from app import filter_active_users, calculate_average_age

SAMPLE_DATA = [
    {"id": 1, "name": "Тест 1", "age": 20, "is_active": True},
    {"id": 2, "name": "Тест 2", "age": 40, "is_active": False},
    {"id": 3, "name": "Тест 3", "age": 30, "is_active": True},
]

def test_filter_active_users():
    active = filter_active_users(SAMPLE_DATA)
    assert len(active) == 2
    assert all(u["is_active"] for u in active)

def test_calculate_average_age():
    active = filter_active_users(SAMPLE_DATA)
    avg = calculate_average_age(active)
    assert avg == 25.0

def test_calculate_average_age_empty():
    assert calculate_average_age([]) == 0.0