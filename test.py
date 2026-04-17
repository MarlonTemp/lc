def test(value, expected):
    if function(value).__eq__(expected):
        return True
    return False

def print_success(value, expected):
    if (test(value, expected)):
        print("SUCCESS")
        return True
    return False