import csv
import os
import re
import sys


REPLACER = r'(.*:)\s'
HEADER = ('product/productId', 'review/userId', 'review/profileName', 'review/helpfulness', 'review/score', 'review/time', 'review/summary', 'review/text')


def format_fraction(num):
    parts = num.split('/')
    if len(parts) != 2 or parts[1] == '0':
        return 0.0
    return float(parts[0]) / float(parts[1])


def format_to_csv(filepath):
    """
    Takes path to finefoods.txt and formats values into CSV
    and outputs to finefoods.csv
    """
    results = list()
    f = open(os.path.expanduser(filepath), 'r')
    out = open('finefoods.csv', 'wb')
    writer = csv.writer(out, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
    for line in f.xreadlines():
        if line == '\n':
            results[3] = format_fraction(results[3])
            results[4] = float(results[4])
            results[5] = int(results[5])
            writer.writerow(results)
            results = list()
            continue
        val = re.sub(REPLACER, '', line).strip()
        if line.startswith('product/') or line.startswith('review/'):
            results.append(val)
    out.close()
    f.close()


if __name__ == "__main__":
    if len(sys.argv) == 1:
        raise 'Please give path to file'
    format_to_csv(sys.argv[1])
