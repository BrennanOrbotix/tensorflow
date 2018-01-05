import csv
import argparse
import os

def squish_csv():
    print('squishing csv ' + csv_file_path)
    field_names = []
    data = []
    if os.path.exists(csv_file_path):
        print(csv_file_path + ' exists')
        with open(csv_file_path) as csv_file:
            contents = csv.DictReader(csv_file)
            field_names = contents.fieldnames
            data = [line for line in contents]

    if data:

        final_categories = {}
        for row in data:
            for key in row:
                value = row[key]
                if is_float(value):
                    if final_categories.has_key(key):
                        final_categories[key] += float(value)
                    else:
                        final_categories[key] = float(value)

        sorted_categories = sorted(final_categories.iteritems(), key=lambda (k, v): (v, k))

        lowest_categories = []
        category_len = len(sorted_categories)
        if category_len <= category_count:
            return

        i = 0

        while i < category_len - category_count:
            lowest_categories.append(sorted_categories[i])
            i += 1

        for row in data:
            for category in lowest_categories:
                row.pop(category[0])
                if category[0] in field_names:
                    field_names.remove(category[0])

        with open(csv_file_path, 'wb') as csv_file:
            results_writer = csv.DictWriter(
                csv_file,
                delimiter=',',
                quotechar='\'',
                quoting=csv.QUOTE_MINIMAL,
                fieldnames=field_names
            )

            results_writer.writeheader()
            results_writer.writerows(data)

def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--category_count',
        type=int,
        default=7,
        help='Desired number of category columns'
    )
    parser.add_argument(
        '--csv_file_path',
        type=str,
    )

    args = parser.parse_args()

    csv_file_path = args.csv_file_path
    category_count = args.category_count
    squish_csv()