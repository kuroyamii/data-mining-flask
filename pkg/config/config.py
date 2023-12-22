# from imagekitio import ImageKit
import dotenv
import os
import csv
import hashlib


# def init_imagekit_client(public_key, private_key, url):
#     imagekit = ImageKit(
#         public_key=public_key,
#         private_key=private_key,
#         url_endpoint=url
#     )
#     return imagekit


# def init_env_variables():

#     class EnvVariables:
#         def __init__(self):
#             self.imagekit_public_key = os.getenv("IMAGEKIT_PUBLIC_KEY"),
#             self.imagekit_private_key = os.getenv("IMAGEKIT_PRIVATE_KEY"),
#             self.imagekit_endpoint_url = os.getenv("IMAGEKIT_ENDPOINT_URL"),

#     env = EnvVariables()
#     return env


def load_csv_data():
    file_path = __file__
    file_path = os.path.join(os.path.dirname(file_path), "data.csv")

    first = True
    with open(file_path, 'r', encoding='UTF8', newline='') as f:
        csvreader = csv.reader(f)
        dataset = {}
        for row in csvreader:
            if first:
                first = False
                continue
            if row[1] not in dataset:
                dataset[row[1]] = {}

            if row[2] not in dataset[row[1]]:
                dataset[row[1]][row[2]] = [row[0]]
            else:
                dataset[row[1]][row[2]].append(row[0])
        return dataset

def hash_value(value):
    return hashlib.sha256(value.encode('utf-8')).hexdigest()

def load_condition_data():
    file_path = __file__
    file_path = os.path.join(os.path.dirname(file_path),"../../condition_data.csv")

    first = True
    with open(file_path, 'r', encoding='UTF8', newline='') as f:
        csvreader = csv.reader(f)
        conditions = {}
        for row in csvreader:
            if first:
                first = False
                continue
            concat = row[0]+row[1]+row[2]+row[3]
            key = hash_value(concat)
            upperwears = row[4].split(";")
            bottomwears = row[5].split(";")
            footwears = row[6].split(";")
            conditions[key] = {
                "upperwear": upperwears,
                "bottomwear": bottomwears,
                "footwear": footwears,
            }

        return conditions

