This project uses a hybrid workflow involving VS Code for data acquisition and Google Colab for preprocessing and model training, to efficiently handle large image and tabular datasets.

*Environment Setup*
VS Code is used for satellite image fetching due to better local file handling.
Google Colab is used for preprocessing and model training to leverage cloud compute and easier dependency management.
Ensure you have access to Google Drive, as intermediate datasets and generated files are shared through Drive.
google drive = https://drive.google.com/drive/folders/1peownNfh-7H4wy8KXhhR8rY72TeqJLfl

## Project Execution Pipeline

### 1. Data Acquisition (VS Code)
- Import the train and test datasets provided in the problem statement.
- Open `data_fetcher.py` in VS Code.
- Update the `excel_path` variable to point to the train and test datasets respectively  
  (if required, a `test_image.py` file is also provided in Google Drive).
- Run the script to download satellite images using property coordinates.

**For this project:**
- Training images are saved in the `mapbox_images` folder and then compressed as `mapbox_images.zip`
- Test images are saved in the `test_mapbox_images` folder and then compressed as `test_mapbox_images.zip`
- Both ZIP files are uploaded to Google Drive for further processing.

---

### 2. Image-to-CSV Conversion (Google Colab)
- Using the provided script (available in Google Drive), convert the downloaded satellite images into CSV format.
- Each image is flattened and stored as pixel values in CSV files.
- Compress the generated CSV files into ZIP archives to reduce storage and transfer overhead.
- Upload these ZIP files to Google Drive:
  - `image_df.zip`
  - `test_image_final.zip`

---

### 3. Tabular Data Preprocessing (Google Colab)
- Load the original training dataset from the problem statement.
- Run the `preprocessing.ipynb` notebook.

This step performs:
- Data cleaning and anomaly correction
- Feature engineering
- Normalization of input features  
  (target column transformation is handled in the model training notebook)

**Outputs generated:**
- `train_new.csv`
- `test_new.csv`

These files are downloaded locally and uploaded to Google Drive.

---

### 4. Dataset Loading in Google Colab
- Open the `model_training.ipynb` notebook.
- Mount Google Drive using the account where the project files are shared.
- Load the following datasets:
  - Preprocessed tabular data: `train_new.csv`, `test_new.csv`
  - Image datasets (CSV files extracted from ZIP archives):
    - `image_df.zip`
    - `test_image_final.zip`
- Unzip and verify that both image and tabular data are correctly loaded.

---

### 5. Model Training and Prediction
- Run the `model_training.ipynb` notebook in Colab.
- This notebook:
  - Loads image and tabular data simultaneously
  - Trains the multimodal neural network (ResNet-50 + MLP)
  - Trains an XGBoost model for tabular-only comparison
  - Evaluates performance on training and test datasets
  - Generates predictions for the test dataset

---

### 6. Submission Generation
- The final cell in `model_training.ipynb` generates the `submission.csv` file.
- Download this file directly from Google Colab.
- This file contains the predicted house prices and serves as the final output of the project.
