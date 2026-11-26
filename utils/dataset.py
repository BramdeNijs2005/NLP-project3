# Here we load our dataset
import kagglehub
import pandas as pd
import os
from preprocessing import preprocess_data

def get_dataset(data_location):

    if os.path.exists(f"{data_location}training.csv"):
        training_df = pd.read_csv(f"{data_location}/training.csv")
        validation_df = pd.read_csv(f"{data_location}/validation.csv")
        testing_df = pd.read_csv(f"{data_location}/testing.csv")
        return training_df, validation_df, testing_df
    else:
        if not os.path.exists(f".data/full_dataset/goemotions_1.csv"):
            _ = kagglehub.dataset_download(
                "debarshichanda/goemotions",
                path="./data/goemotions", #TODO needs editing based on where the data comes from
                output_dir="./data/full_dataset"
            )


        path_to_set_1 = "/kaggle/input/goemotions/data/full_dataset/goemotions_1.csv"
        path_to_set_2 = "/kaggle/input/goemotions/data/full_dataset/goemotions_2.csv"
        path_to_set_3 = "/kaggle/input/goemotions/data/full_dataset/goemotions_3.csv"
        paths = [path_to_set_1, path_to_set_2, path_to_set_3]

        dataset = pd.concat(
            [pd.read_csv(path, delimiter=',') for path in paths],
            ignore_index=True
        )

        dataset = dataset.loc[
            dataset["example_very_unclear"] == False,
            ["text", "example_very_unclear", "admiration",
             "amusement", "anger", "annoyance", "approval", "caring",
             "confusion", "curiosity", "desire", "disappointment",
             "disapproval", "disgust", "embarrassment", "excitement",
             "fear", "gratitude", "grief", "joy", "love", "nervousness",
             "optimism", "pride", "realization", "relief", "remorse",
             "sadness", "surprise", "neutral"]
        ].copy()

        dataset.to_csv("./data/full_dataset/full_dataset.csv", index=False)

        preprocess_data()


