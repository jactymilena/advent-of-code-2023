from utils.reader import read_file

rows = read_file('inputs/day-1.txt')
val_digits_w = [ 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
val_digits = {}
for i, w in enumerate(val_digits_w):
    val_digits[str(i + 1)] = val_digits_w[i]

row_digits = []
s = 0
buff = ''

for row in rows:
    for d in row:
        buff += d
        for v in val_digits:
            if v in buff or val_digits[v] in buff:
                if len(row_digits) == 2:
                    row_digits.pop()
                row_digits.append(v)
                buff = buff[-1]

    s += int(''.join(row_digits) if len(row_digits) == 2 else row_digits[0]*2)
    row_digits.clear()

print(s)
