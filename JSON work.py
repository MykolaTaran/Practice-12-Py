import json

def load_data_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return []

def save_data_to_file(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)

def display_json_content(file_path):
    data = load_data_from_file(file_path)
    print(json.dumps(data, indent=2))

def add_record(file_path, record):
    data = load_data_from_file(file_path)
    data.append(record)
    save_data_to_file(file_path, data)

def remove_record(file_path, field_name, field_value):
    data = load_data_from_file(file_path)
    data = [record for record in data if record.get(field_name) != field_value]
    save_data_to_file(file_path, data)

def search_by_field(file_path, field_name, field_value):
    data = load_data_from_file(file_path)
    result = [record for record in data if record.get(field_name) == field_value]
    return result

def find_min_max_salary(file_path):
    data = load_data_from_file(file_path)
    if not data:
        return None, None
    
    min_salary_record = min(data, key=lambda x: x.get('salary'))
    max_salary_record = max(data, key=lambda x: x.get('salary'))
    
    return min_salary_record['name'], max_salary_record['name']

# Приклад використання:
file_path = 'employees.json'

# Відображення вмісту JSON файлу
print("The contents of the JSON file:")
display_json_content(file_path)

# Додавання нового запису
new_record = {'name': 'Radionova', 'salary': 49200, 'position': 'cartographer', 'sex': 'female'}
add_record(file_path, new_record)
print("\nA new entry has been added:")
display_json_content(file_path)

# Пошук даних за полем
search_result = search_by_field(file_path, 'name', 'Ivanov')
print("\Search result by last name 'Ivanov':")
print(json.dumps(search_result, indent=2))



# Знайдення прізвища осіб з найменшою та найбільшою зарплатою
min_salary, max_salary = find_min_max_salary(file_path)
print("\nLast name with the lowest salary:", min_salary)
print("Surname with the highest salary:", max_salary)
