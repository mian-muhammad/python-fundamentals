"name_lib.py"
def name_length(name):
    "name_length"
    return len(name)

def upper_case_name(name):
    "upper_case_name"
    return name.upper()


def lower_case_name(name):
    "lower_case_name"
    return name.lower()

if __name__ == "__main__":
    name = "Nina"
    length = name_length(name)
    upper_case = upper_case_name(name)
    print(f"The length is {length} and the uppercase version is: {upper_case}")
