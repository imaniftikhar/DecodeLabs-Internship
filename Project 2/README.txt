HEART DISEASE CLASSIFICATION PROJECT

OVERVIEW
This project builds a basic machine learning classification model to
predict the presence of heart disease in a patient based on clinical
attributes (age, cholesterol, blood pressure, chest pain type, etc.).
It is designed to run as a Kaggle Notebook.

DATASET
Source: https://www.kaggle.com/datasets/data855/heart-disease
The dataset contains patient clinical records with a target column
indicating whether heart disease is present (1) or not (0).

FILES
heart-disease-classification.ipynb
    Jupyter notebook containing the full workflow:
      1. Load and explore the dataset
      2. Clean and preprocess the data (handle missing values,
         encode categorical columns)
      3. Split data into training (80%) and testing (20%) sets
      4. Train a Logistic Regression baseline model
      5. Evaluate performance (accuracy, precision, recall, F1, ROC AUC)
      6. Train and compare a Random Forest model
      7. Plot feature importance to see which attributes matter most

HOW TO RUN
1. Go to Kaggle and create a new Notebook.
2. Upload heart-disease-classification.ipynb
   (File > Upload Notebook), or copy the cells into a new notebook.
3. Click "Add Data" and attach the dataset:
   data855/heart-disease
4. Run all cells from top to bottom (Run > Run All).

The notebook automatically searches /kaggle/input/ for the dataset's
CSV file, so it should work without editing the file path.


REQUIREMENTS
Standard Kaggle Notebook environment already includes everything
needed:
    - python 3.10+
    - pandas
    - numpy
    - matplotlib
    - seaborn
    - scikit-learn

No additional installation required.

RESULTS (EXAMPLE RUN)
----------------------
Logistic Regression and Random Forest were trained and compared.
On a typical run, Random Forest achieved approximately 82% accuracy
on the held-out test set. Exact results may vary slightly between
runs due to the train/test split and small dataset size (~300 rows).

Evaluation metrics reported in the notebook:
    - Accuracy
    - Precision
    - Recall
    - F1 Score
    - ROC AUC
    - Confusion Matrix
    - ROC Curve
    - Feature Importance (Random Forest)


POSSIBLE NEXT STEPS
    - Add k-fold cross-validation for a more reliable performance estimate
    - Tune hyperparameters with GridSearchCV / RandomizedSearchCV
    - Try additional models (XGBoost, SVM, Gradient Boosting)
    - Address class imbalance if present (e.g. class_weight, SMOTE)
    - Perform feature selection based on importance scores


AUTHOR / NOTES
Built as a beginner-friendly supervised learning classification
exercise: data handling, train/test splitting, model training, and
evaluation on a small clinical dataset.
