import json
from utils import filter_invalid_values

# Загрузка данных из JSON-файла
with open('operations.json', 'r') as file:
    data = json.load(file)
# Фильтрация выполненных операций и сортировка по дате
filtered_items = filter_invalid_values(data)
executed_operations = [op for op in filtered_items if op['state'] == 'EXECUTED']
sorted_executed_operations = sorted(executed_operations, key=lambda value: value['date'], reverse=True)
display_operations = sorted_executed_operations[:5]
for operation in display_operations:
    print(f"{operation['date']} {operation['description']}")
    masked_card = ' '.join([operation.get('from', "***")[-8:-4], operation.get('from', "*** ")[-4:]])
    masked_account = f"*** {operation['to'][-4:]}"
    print(f"{masked_card} -> {masked_account}")
    operationAmount = operation['operationAmount']
    amount = operationAmount['amount']
    currency = operationAmount['currency']['name']
    print(f"{amount} {currency}")
