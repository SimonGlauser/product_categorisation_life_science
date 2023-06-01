import datetime
import time
import numpy as np
import pandas as pd
import joblib
from IPython.display import display
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import precision_recall_fscore_support, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC

np.set_printoptions(threshold=np.inf)

def read_data(path):
    df = pd.read_csv(path, header=0, index_col=0)
    data = df[["category", "group", "catalogNumber", "all_text", "supplier"]]
    data = data.set_index("catalogNumber")
    X = data["all_text"]
    y = data["group"]
    return X, y


def prepare_data(X, y):
    return train_test_split(X, y, test_size=0.20, stratify=y)


def run_classifiers(classifiers, X_train, y_train, X_test, y_test):
    models = pd.read_csv("results.csv", header=0, index_col=0)

    for idx, classifier in enumerate(classifiers):
        if idx == 0:
            continue

        print(f"#{classifier}")
        start_time = time.time()

        pipeline = Pipeline(
            steps=[
                ("preprocessor", preprocessor),
                ('classifier', LinearSVC()),
            ]
        )

        display(pipeline)
        pipeline.fit(X_train, y_train)

        y_pred = pipeline.predict(X_test)
        runtime = time.time() - start_time

        accuracy = accuracy_score(y_test, y_pred)
        precision, recall, fscore, _ = precision_recall_fscore_support(y_test, y_pred, average='weighted',
                                                                       labels=np.unique(y_pred))

        date = datetime.datetime.now()

        df_new_row = pd.DataFrame({
            'Model': [classifier.__class__.__name__],
            'Accuracy': [accuracy],
            'Precision': [precision],
            'Recall': [recall],
            'F1score': [fscore],
            'Runtime [s]': [round(runtime, 2)],
            'Date': [date]
        })

        print(df_new_row)

        models = pd.concat([models, df_new_row])
        models.to_csv("results.csv")

        return pipeline


def create_model(pipeline):
    joblib.dump(pipeline, 'LinearSVC.pkl', compress=1)


if __name__ == '__main__':
    X, y = read_data("csv_combined.csv")
    X_train, X_test, y_train, y_test = prepare_data(X, y)

    print("Preparation done")

    classifiers = [
        LogisticRegression(),
        LinearSVC(),
        MultinomialNB(),
        RandomForestClassifier(n_estimators=25),
        GradientBoostingClassifier(n_estimators=25),
    ]

    preprocessor = Pipeline([
        ("vect", CountVectorizer(ngram_range=(1, 2))),
        ("tfidf", TfidfTransformer()),
    ])

    preprocessor.fit_transform(X_train)

    pipeline = run_classifiers(classifiers, X_train, y_train, X_test, y_test)

    create_model(pipeline)

