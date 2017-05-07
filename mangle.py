import csv
import string
import numpy as np

conv = dict(zip('KMGT', (3, 6, 9, 12)))
# idea from http://stackoverflow.com/questions/9932656/formatting-kilo-mega-gig-data-in-numpy-record-array
def de_humanize(value):
    if value[-1] in conv:
        value = '{}e{}'.format(value[:-1], conv[value[-1]])
    return float(value)

def parse_netflow_csv(path):
    rows_array = []
    with open(path, "rt", encoding="utf-8") as csvfile:
        rows = csv.reader(csvfile, delimiter=',')
        for row in rows:
            row[0] = float(row[0])
            for i in [1, 2, 3, 4, 5, 6]:
                row[i] = de_humanize(row[i])
            rows_array.append(row)
    return rows_array

def compose_dict(rows):
    """Dict for a single label"""
    length = len(rows)
    data = {} 
    data['duration'] = np.zeros((1, length))
    data['flows']    = np.zeros((1, length))
    data['packets']  = np.zeros((1, length))
    data['bytes']    = np.zeros((1, length))
    data['pps']      = np.zeros((1, length))
    data['bps']      = np.zeros((1, length))
    data['bpp']      = np.zeros((1, length))
    for i in range(length):
        data['duration'][0][i] = rows[i][0]
        data['flows'][0][i] = rows[i][1]
        data['packets'][0][i] = rows[i][2]
        data['bytes'][0][i] = rows[i][3]
        data['pps'][0][i] = rows[i][4]
        data['bps'][0][i] = rows[i][5]
        data['bpp'][0][i] = rows[i][6]
    return data

def aggregate_netflow_csv(*paths):
    """XXX"""
    rows_array = []
    labels_array = []
    labels_dict ={}
    numeric_labels_array = []
    numeric_label = 0
    for path in paths:
        slabel = path.split("/")[-1]
        label = slabel.rstrip(".csv")
        numeric_label += 1
        labels_dict[numeric_label] = label
        with open(path, "rt", encoding="utf-8") as csvfile:
            rows = csv.reader(csvfile, delimiter=',')
            for row in rows:
                row[0] = float(row[0])
                for i in [1, 2, 3, 4, 5, 6]:
                    row[i] = de_humanize(row[i])
                rows_array.append(row)
                labels_array.append(label)
                numeric_labels_array.append(numeric_label)
    np_array = np.array(rows_array)
    #print rows_array
    #print np_array
    return np_array, labels_array, numeric_labels_array, labels_dict

# vim: tabstop=4 softtabstop=4 shiftwidth=4 expandtab
