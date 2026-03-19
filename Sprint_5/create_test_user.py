from browser import get_chrome_driver
from helpers import UserHelper
import os


def update_data_file(user_data):
    """Обновление файла data.py с новыми данными пользователя"""
    data_file = "data.py"
    
    if not os.path.exists(data_file):
        return False
    
    with open(data_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
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
    
    with open(data_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(new_lines))
    
    return True


def main():
    """Основная функция"""
    driver = get_chrome_driver()
    
    try:
        helper = UserHelper(driver)
        user_data = helper.register_new_user()
        helper.save_user_to_file(user_data, "test_user.json")
        update_data_file(user_data)
    except Exception as e:
        pass  # В реальном проекте здесь может быть логирование в файл
    finally:
        driver.quit()


if __name__ == "__main__":
    main()