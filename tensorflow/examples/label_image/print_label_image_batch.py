import os
import argparse


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--image_dir",
        type=str
    )
    image_dir = parser.parse_args().image_dir

    for root, dirs, files in os.walk(image_dir):
        for file in files:
            if file.endswith('.jpg'):
                os.system('python label_image.py --graph=/tmp/output_graph.pb ' +
                          '--labels=/tmp/output_labels.txt --input_layer=Mul ' +
                          '--output_layer=final_result --input_mean=128 ' +
                          '--input_std=128 --image=' + image_dir + file +
                          ' --category=' + image_dir)
