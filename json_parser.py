def find_path(json_obj, target, path=None):
    """
    Recursively search for a value in a nested JSON object and return the path to the value.

    :param json_obj: The JSON object to search through.
    :param target: The target value to search for.
    :param path: The current path being checked (used in recursive calls).
    :return: The path to the target value as a list, or None if the value is not found.
    """
    if path is None:
        path = []

    # If json_obj is a dictionary, iterate over its items
    if isinstance(json_obj, dict):
        for key, value in json_obj.items():
            new_path = path + [key]
            if value == target:
                return new_path
            elif isinstance(value, (dict, list)):
                found_path = find_path(value, target, new_path)
                if found_path:
                    return found_path

    # If json_obj is a list, iterate over its elements
    elif isinstance(json_obj, list):
        for index, item in enumerate(json_obj):
            new_path = path + [index]
            if item == target:
                return new_path
            elif isinstance(item, (dict, list)):
                found_path = find_path(item, target, new_path)
                if found_path:
                    return found_path

    return None  # Return None if the target is not found
