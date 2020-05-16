import re

class regexReplace:
  pattern = 'Fill with regex pattern'
  string_to_change = '''Multiline string'''
  values_replace = ['Value','Value','...']
  result_string = ''
  for i in range(0, len(values_replace)):
    result_string = re.sub(pattern, values_replace[i], string_to_change)
    print(str(result_string))
