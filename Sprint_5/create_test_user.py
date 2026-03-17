from browser import get_chrome_driver
from helpers import UserHelper
import os


def update_data_file(user_data):
    """Обновление файла data.py с новыми данными пользователя"""
    data_file = "data.py"
    
    if not os.path.exists(data_file):
        print("❌ Файл data.py не найден")
        return False
    
    # Читаем текущий файл
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Обновляем данные пользователя
    # Ищем и заменяем строки с данными пользователя
    lines = content.split('\n')
    new_lines = []
    
    for line in lines:
        if 'EXISTING_USER_EMAIL =' in line:
            new_lines.append(f'    EXISTING_USER_EMAIL = "{user_data["email"]}"')
        elif 'EXISTING_USER_PASSWORD =' in line:
            new_lines.append(f'    EXISTING_USER_PASSWORD = "{user_data["password"]}"')
        elif 'EXISTING_USER_NAME =' in line:
            new_lines.append(f'    EXISTING_USER_NAME = "{user_data["name"]}"')
        else:
            new_lines.append(line)
    
    # Записываем обратно
    with open(data_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    print("✅ Файл data.py обновлен")
    return True


def main():
    """Основная функция"""
    print("=" * 60)
    print("🚀 СОЗДАНИЕ ТЕСТОВОГО ПОЛЬЗОВАТЕЛЯ")
    print("=" * 60)
    
    # Создаем драйвер
    driver = get_chrome_driver()
    
    try:
        # Используем хелпер для регистрации
        helper = UserHelper(driver)
        user_data = helper.register_new_user()
        
        print(f"\n📧 Email: {user_data['email']}")
        print(f"🔑 Пароль: {user_data['password']}")
        print(f"👤 Имя: {user_data['name']}")
        
        # Сохраняем в файл для резервного копирования
        helper.save_user_to_file(user_data, "test_user.json")
        
        # Обновляем data.py
        update_data_file(user_data)
        
        print("\n✅ Пользователь успешно создан и данные обновлены!")
        print("\nТеперь можно запускать тесты:")
        print("  pytest -v")
        
    except Exception as e:
        print(f"\n❌ Ошибка: {e}")
        
    finally:
        driver.quit()
        print("\n🛑 Браузер закрыт")
        print("=" * 60)


if __name__ == "__main__":
    main()