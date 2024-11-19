import re

def parse_date(input_text):
    date_regex = r"\d{4}-\d{2}-\d{2}"
    return re.findall(date_regex, input_text)