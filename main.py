from utils import load_file, filter_invalid_values, displayed_operations, displayed_sorted_operations

# Загрузить файл JSON с данными о транзакциях
data = load_file()

filtered_data = filter_invalid_values(data)

executed_operations = displayed_operations(filtered_data)

displayed_sorted_operations(executed_operations)