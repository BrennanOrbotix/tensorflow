import os
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image_dir",
        type=str
    )
    parser.add_argument(
        "--csv_suffix",
        type=str,
        default='-label_results.csv'
    )
    args = parser.parse_args()
    image_dir = args.image_dir
    csv_suffix = args.csv_suffix

    category = image_dir.rstrip('/')

    csv_name = category + csv_suffix

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.jpg'):
                os.system('python label_image.py --graph=/tmp/output_graph.pb ' +
                          '--labels=/tmp/output_labels.txt --input_layer=Mul ' +
                          '--output_layer=final_result --input_mean=128 ' +
                          '--input_std=128 --image=' + image_dir + file +
                          ' --csv_name=' + csv_name)

    os.system('python squish_results_csv.py --category_count=7 --csv_file_path=' + csv_name)
