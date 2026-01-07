# CDC-x-Yhills

This project uses a hybrid workflow involving VS Code for data acquisition and Google Colab for preprocessing and model training, to efficiently handle large image and tabular datasets.

**Environment Setup**
VS Code is used for satellite image fetching due to better local file handling.
Google Colab is used for preprocessing and model training to leverage cloud compute and easier dependency management.
Ensure you have access to Google Drive, as intermediate datasets and generated files are shared through Drive.
google drive = https://drive.google.com/drive/folders/1peownNfh-7H4wy8KXhhR8rY72TeqJLfl

**Step-by-Step Execution Pipeline**
1.  Data Acquisition (VS Code) : 
        Import the train and test datasets provided in the problem statement.
        Open data_fetcher.py in VS Code.
        Update the excel_path variable to point to the train and test datasets respectively(if not a test_image.py file is also uploaded in google drive)
        Run the script to download satellite images using property coordinates.
        For this project:
        Training images are saved as mapbox_images folder and then converted to mapbox_images.zip 
        Test images are saved as test_mapbox_images folder and then converted to test_mapbox_images.zip
        Both ZIP files are uploaded to Google Drive for further processing.

2.  Image-to-CSV Conversion(colab) : 
        Using the provided script (available in Google Drive), convert the downloaded satellite images into CSV format.
        Each image is flattened and stored as pixel values in CSV files.
        Compress the generated CSV files into ZIP archives to reduce storage and transfer overhead.
        Upload these ZIP files to Google Drive(image_df.zip , test_image_final.zip are present in shared drive)

3.  Tabular Data Preprocessing(colab) : 
        Load the original training dataset from the problem statement.
        Run the preprocessing.ipynb notebook.
        This step performs:
          Data cleaning and anomaly correction
          Feature engineering
          Normalization of input features(output colum transformation is present in model training notebook itself)
       The processed outputs are saved as:
          train_new.csv
          test_new.csv
          These files are downloaded locally and uploaded to Google Drive.

4.  Dataset Loading in Google Colab :
       Open model_training.ipynb notebook.
       Mount Google Drive using the account where the project files are shared.
       Load:
         Preprocessed tabular datasets (train_new.csv, test_new.csv)
         Image datasets (CSV files extracted from ZIP archives,image_df.zip , test_image_final.zip)
       Unzip and verify that both image and tabular data are correctly loaded.

5.  Model Training and Prediction :
       After loading the datasets from google drive.
       Run the model_training.ipynb notebook in Colab.
       This notebook:
           Loads image and tabular data simultaneously
           Trains the multimodal neural network (ResNet-50 + MLP) and also XGBOOST(for only tabular dataset)
       Evaluates model performance on training and test sets
       Generates predictions for the test dataset

 6.  Submission Generation :
      The final cell in model_training.ipynb generates the submission.csv file.
      Download this file directly from Colab.
      This file contains the predicted house prices and serves as the final output of the project.

     
