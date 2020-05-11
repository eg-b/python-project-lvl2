before = {
  "common": {
    "setting1": "Value 1",
    "setting2": "200",
    "setting3": 'true',
    "setting6": {
      "key": "value"
    },
    "site": {
      "base": "hexlet.io",
      "base2": "hexlet.io"
    }
  },
  "group1": {
    "baz": "bas",
    "foo": "bar"
  },
  "group2": {
    "abc": "12345"
  }
}

after = {
  "common": {
    "setting1": "Value 1",
    "setting3": 'true',
    "setting4": "blah blah",
    "setting5": {
      "key5": "value5"
    },
    "site": {
      "base2": "hexlet.io"
    }
  },

  "group1": {
    "foo": "bar",
    "baz": "bars"
  },

  "group3": {
    "fee": "100500"
  }
}

def compare(file1_data, file2_data):
    diff = {}
    data1_set, data2_set = file1_data.keys(), file2_data.keys()
    unchanged, updated = set(), set()
    removed = data1_set - data2_set
    added = data2_set - data1_set

    for k in data1_set & data2_set:
        if file1_data[k] == file2_data[k]:
            unchanged.add(k)
        else:
            if type(file1_data[k]) == dict and type(file2_data[k]) == dict:
                children = compare(file1_data[k], file2_data[k])
                diff.update({k + ' changed': children})
            else:
                updated.add(k)
    for k in removed:
        value = {}
        if type(file1_data[k]) == dict:
            for key in file1_data[k]:
                value.update({f'{key} removed': file1_data[k][key]})
        else:
            value = file1_data[k]
        diff.update({k + ' removed': value})
    for k in added:
        value = {}
        if type(file2_data[k]) == dict:
            for key in file2_data[k]:
                value.update({f'{key} added': file2_data[k][key]})
        else:
            value = file2_data[k]
        diff.update({k + ' added': value})
    for k in unchanged:
        value = {}
        if type(file1_data[k]) == dict:
            for key in file1_data[k]:
                value.update({f'{key} unchanged': file1_data[k][key]})
        else:
            value = file1_data[k]
        diff.update({k + ' unchanged': value})
    for k in updated:
        diff.update(
            {k + ' changed_from_to': (file1_data[k], file2_data[k])})
    return diff


#print(compare(before, after))
'''
{'common changed':
     {'site changed': 
          {'base removed': 'hexlet.io', 
           'base2 unchanged': 'hexlet.io'},
      'setting6 removed':
          {'key': 'value'},
      'setting2 removed': '200',
      'setting5 added': {'key5': 'value5'},
      'setting4 added': 'blah blah', 
      'setting3 unchanged': 'true',
      'setting1 unchanged': 'Value 1'}, 
 'group1 changed':
     {'foo unchanged':
          'bar', 'baz changed_from_to': ('bas', 'bars')}, 
 'group2 removed':
     {'abc': '12345'}, 
 'group3 added': 
     {'fee': '100500'}}
'''
'''
{'common changed':
     {'site changed':
          {'base removed': 'hexlet.io',
           'base2 unchanged': 'hexlet.io'},
      'setting2 removed': '200', 
      'setting6 removed': {'key removed': 'value'}, 
      'setting5 added': {'key5 added': 'value5'},
      'setting4 added': 'blah blah',
      'setting1 unchanged': 'Value 1',
      'setting3 unchanged': 'true'},
 'group1 changed':
     {'foo unchanged': 'bar',
      'baz changed_from_to': ('bas', 'bars')},
 'group2 removed': {'abc removed': '12345'},
 'group3 added': {'fee added': '100500'}}

'''