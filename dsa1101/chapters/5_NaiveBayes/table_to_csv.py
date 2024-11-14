def table_to_csv(table, y_s, y_name):
  for x_s in table:
    for x in table[x_s]:
      if len(table[x_s][x]) != len(y_s):
        raise Exception('Inconsistent number of rows and cols!')
  total = {}
  for x_s in table:
    cat_data = list(table[x_s].values())
    for i in range(len(cat_data[0])):
      cur_sum = sum(r[i] for r in cat_data)
      if y_s[i] not in total:
        total[y_s[i]] = cur_sum
      elif total[y_s[i]] != cur_sum:
        raise Exception('Within category sum not consistent!')

  with open('data.csv', 'w') as output:
    headers = ','.join(table.keys())
    headers += f',{y_name}\n'
    output.write(headers)

    rows = []
    row_num = 0
    for y_idx in range(len(y_s)):
      y = y_s[y_idx]
      start_num = row_num
      rows.extend([[f'{y}']]*total[y])
      for x_s in table:
        row_num = start_num
        for x in table[x_s]:
          for i in range(row_num, row_num + table[x_s][x][y_idx]):
            rows[i].insert(0, x)
          row_num += table[x_s][x][y_idx]
      
    rows = [','.join(r) for r in rows]
    output.write('\n'.join(rows))
    output.write('\n')

train = {
  'long': {
    'long': [200, 20, 100],
    'not long': [300, 280, 100]
  }, 
  'sweet': {
    'sweet': [100, 100, 50],
    'not sweet': [400, 200, 150]
  },
  'yellow': {
    'yellow': [200, 180, 50],
    'not yellow': [300, 120, 150]
  }
}

y = ['banana', 'orange', 'other']

table_to_csv(train, y, 'fruit_name')
