def read_file(filename, pr=False):
    file = open(filename, 'r')
    lines = file.readlines()

    if pr:
        count = 0
        for line in lines:
            count += 1
            print("Line{}: {}".format(count, line.strip()))

    return lines