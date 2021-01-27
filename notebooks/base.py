import numpy as np
import pandas as pd
import os

def load_files():
    # Files supplied by the competition for model training
    X_train = pd.read_csv('../../data/dengue_features_train.csv')
    y_train = pd.read_csv('../../data/dengue_labels_train.csv', usecols=['total_cases'])
    # Files supplied by the competition for submission
    X_test = pd.read_csv('../../data/dengue_features_test.csv')
    y_test = pd.read_csv('../../data/submission_format.csv')
    return X_train, y_train, X_test, y_test

def data_preprocess(df):
    # drop or encode categorical cols
    df_processed = df.drop('week_start_date', axis=1)
    df_processed['city'] = df_processed['city'].apply(lambda x : 1 if x=='iq' else 0)
    return df_processed

def create_submission_file(pipeline, X_test, y_test, filename_comment):
    next_file_id = generate_next_submission_fileid()
    X_test_processed = data_preprocess(X_test)
    y_submit_pred = np.rint(pipeline.predict(X_test_processed))
    y_test['total_cases'] = y_submit_pred
    y_test['total_cases'] = y_test['total_cases'].astype(int)
    y_test.to_csv(f'../../data/dengue_submission_{next_file_id}_{filename_comment}.csv', index = False)
    return y_submit_pred

def generate_next_submission_fileid():
    files_found = []
    for file in os.listdir("../../data"):
        if file.startswith("dengue_submission"):
            files_found.append(file[18:20])
    return f'{int(sorted(files_found).pop()) + 1 :02}'
