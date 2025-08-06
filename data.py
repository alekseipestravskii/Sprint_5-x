def get_test_data():
    return {
        "valid": generate_registration_data(),  # Функция для генерации валидных данных
        "invalid_password": {
            "name": "Test User",
            "email": "test@example.com",
            "password": "12345"
        },
        "empty_password": {
            "name": "Test User",
            "email": "test@example.com",
            "password": ""
        }
    }
