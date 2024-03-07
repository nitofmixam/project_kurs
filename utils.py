import json
import datetime
from datetime import datetime


def load_file():
    with open('operations.json', 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def filter_invalid_values(items):
    filtered_items = []
    for item in items:
        if item is None or item == {} or item == []:
            continue
        else:
            filtered_items.append(item)
    return filtered_items


def displayed_operations(filtered_items):
    executed_operations = [op for op in filtered_items if op['state'] == 'EXECUTED']
    sorted_executed_operations = sorted(executed_operations, key=lambda value: value['date'], reverse=True)
    display_operations = sorted_executed_operations[:5]
    return display_operations


def displayed_sorted_operations(display_operations):
    for operation in display_operations:
        date = datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f')
        date_str = date.strftime("%d.%m.%Y")
        print(f"{date_str} {operation['description']}")
        masked_card = ''.join([operation.get('from', "***")[-8:-4], operation.get('from', "***")[-5:]])
        masked_account = f"*** {operation['to'][-4:]}"
        print(f"{masked_card} -> {masked_account}")
        operationAmount = operation['operationAmount']
        amount = operationAmount['amount']
        currency = operationAmount['currency']['name']
        print(f"{amount} {currency}")