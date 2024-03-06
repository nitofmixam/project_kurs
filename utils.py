def filter_invalid_values(items):
    filtered_items = []
    for item in items:
        if item is None or item == {} or item == []:
            continue
        else:
            filtered_items.append(item)
    return filtered_items
