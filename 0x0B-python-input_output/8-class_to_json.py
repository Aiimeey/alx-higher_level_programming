def class_to_json(obj):
    result = {}
    for key, value in obj.__dict__.items():
        if isinstance(value, (list, dict, str, int, bool)):
            result.update({key: value})
    return result
