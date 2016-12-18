#Best solutions:
#1.
def filter_list(l):
  'return a new list with the strings filtered out'
  return [x for x in l if type(x) is not str]

#2.
def filter_list(l):
  'return a new list with the strings filtered out'
  return [i for i in l if not isinstance(i, str)]

#3.My code :)
def filter_list(l):
  string_holder = [string for string in l if type(string) == str]
  print string_holder
  for each in string_holder:
  	l.remove(each)
  return l



