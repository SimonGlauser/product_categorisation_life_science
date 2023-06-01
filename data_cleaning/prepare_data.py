import pandas as pd

def import_file(file):
    df = pd.read_csv(file, engine="pyarrow")
    print(df.shape)
    print(df.info())
    print(df['supplier'].value_counts())
    print(df.sample())

def main():
    import_file("data_clean/csv_combined.csv")



if __name__ == '__main__':
    main()