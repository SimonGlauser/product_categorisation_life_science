# Import Packages
import pandas as pd
# Import Helperfunctions
from helper_function import get_filename

def combine_csv(filepath):
    df_list = []
    for file in filepath:
        if file.split('.')[0].split('/')[1] == "idt" or file.split('.')[0].split('/')[1] == "lubioscience":
            continue
        df_list.append(pd.read_csv(file, dtype={'supplier_id': int, 'supplier': str, 'catalogNumber': str, 'title': str, 'description': str, 'category_id': int, 'category': str, 'group_id': int, 'group': str, 'general_info': str, 'host': str, 'application': str, 'isotype': str, 'reactivity': str, 'synonym': str, 'gene_symbol': str, 'gene_description': str}))
        print(f"{file.split('.')[0].split('/')[1]} done")
    df = pd.concat(df_list)
    print(df.shape)
    df.to_csv("data_clean/csv_combined.csv")

def main():
    filepath = get_filename("data_csv", ".csv")
    combine_csv(filepath)

if __name__ == '__main__':
   main()