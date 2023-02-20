ranges = []
first_number = 0
last_number = 0
range_count = 0


def check_ranges_on_array(array):
    global range_count
    for x in array:
        range_count += 1
        validate_range_value(x)
    write_range(first_number, last_number, range_count)
    return send_result(ranges)


def validate_range_value(value):
    global first_number
    global last_number
    global range_count
    if value > last_number:
        value_greater_last_number(value)
    else:
        first_number = value


def value_greater_last_number(value):
    global first_number
    global last_number
    global range_count
    if last_number != 0 and value - last_number >= last_number:
        write_range(first_number, last_number, range_count - 1)
        first_number = 0
        last_number = value
        range_count = 1
    manage_last_number(value)


def write_range(first_number, last_number, readings):
    global ranges
    data = {
        'range': str(first_number) + "-" + str(last_number),
        'readings': readings
        }
    ranges.append(data)


def manage_last_number(value):
    global first_number
    global last_number
    if (first_number == 0):
        first_number = last_number
    last_number = value


def send_result(ranges):
    rangeList = []
    keyList = list(ranges[0].keys())
    print(keyList[0] + ", " + keyList[1])
    for range in ranges:
        print(range["range"] + ", " + str(range["readings"]))
        rangeList.append([range["range"], range["readings"]])
    return rangeList
