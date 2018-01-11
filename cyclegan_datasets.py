"""Contains the standard train/test splits for the cyclegan data."""

"""The size of each dataset. Usually it is the maximum number of images from
each domain."""
DATASET_TO_SIZES = {
    'sunny2rainy_train': 1201,
    'sunny2rainy_test': 150
}

"""The image types of each dataset. Currently only supports .jpg or .png"""
DATASET_TO_IMAGETYPE = {
    'sunny2rainy_train': '.jpg',
    'sunny2rainy_test': '.jpg',
}

"""The path to the output csv file."""
PATH_TO_CSV = {
    'sunny2rainy_train': '/media/sunguofei/DATA1/road_data/processed/sunny2rainy_lake&mount_1_sunny_mode_1_train.csv',
    'sunny2rainy_test': '/media/sunguofei/DATA1/road_data/processed/sunny2rainy_unity_test.csv',
}
