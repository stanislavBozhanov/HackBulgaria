def get_file_content(filename):
    return open(filename).read()


def get_lines(text):
    return text.split('\n')


def is_empty_line(line):
    return len(line.strip()) != 0


def get_file_name(filename):
    return filename.replace('.dsl', '.py')


def unline(line):
    return line + '\n'


def get_assertion(description, funcion_call, expected_value):
    assertions = {
        'False': {
            'assert_type': 'assertFalse',
            'asset_body': '{function_call}, {description}'
        }
    }


def test_line_test_case(line):
    test_parts = 
    test_case = """
    class {class_name}(unittest.TestCase):
        def {test_name}(self):
            self.{assert_type}()"""


def is_import(line):
    return line.startswith('import') or line.startswith('from')


def capitalize_word(word):
    return word[0].upper() + word[1:]


def construct_class_name(words):
    class_name = ""
    for word in words:
        class_name = class_name.join(capitalize_word(word))
    class_name = class_name.join('Tests')
    return class_name


def main():
    filename = 'is_prime_test.dsl'
    content = get_file_content(filename)
    lines = get_lines(content)
    non_empty_lines = list(filter(is_empty_line, lines))
    # print(non_empty_lines)
    # print(list(filter(is_import, non_empty_lines)))


if __name__ == '__main__':
    main()
