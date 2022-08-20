# Convert SCREAMING_SNAKE_CASE String to camelCase
# Using split() + join() + title() + map()

# Нужно для интересного* апи Битрикс24, который в документации даёт поля в SCREAMING_SNAKE_CASE, а по факту возвращает в camelCase
# Это также отдельная программа, которая запускается через CLI с указанием имени файла
import re

def screaming_snake_to_camel(string):
    return "".join([s.capitalize() if idx != 0 else s for idx, s in enumerate(string.lower().split('_'))])

def camel_case_to_screaming_snake(string):
    return "_".join(re.findall(r'(?:[A-Z]|[a-z])(?:[a-z]+|[A-Z]*(?=[A-Z]|$))', string)).upper()

if (__name__ == "__main__"):
    def change_case(matchobj):
        return screaming_snake_to_camel(matchobj.group())


    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument("input", help='Путь к входному файлу для преобразования')
    parser.add_argument("output", default="OVERWRITE", help='Путь к файлу, куда записываем результат. ВНИМАНИЕ! По умолчанию перезаписывает input файл')

    args = parser.parse_args()
    if args.output == 'OVERWRITE':
        args.output = args.input

    with open(args.input, 'r') as inp:
        case_before = inp.read()
        case_after = re.sub(r"\b([A-Z]+)+(_[A-Z]+)*\b", change_case, case_before)

    with open(args.output, 'w') as out:
        out.write(case_after)