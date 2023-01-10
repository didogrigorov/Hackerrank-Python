def swap_case(s):
    new_str = ""
    for el in s:
        if el.islower():
            new_el = el.upper()
            new_str += new_el
        elif el.isupper():
            new_el = el.lower()
            new_str += new_el
        elif not el.isalpha() or el.isdigit() or el.isspace():
            new_str += el

    return new_str