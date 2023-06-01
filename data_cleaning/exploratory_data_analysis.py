# Import Packages
import pandas as pd
pd.set_option('display.width', 400)
from collections import Counter
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
sns.color_palette("ch:s=.25,rot=-.25", as_cmap=True)
sns.set_style("darkgrid")
font = {'fontname':'Times New Roman'}
plt.rc("font", size=12)

def eda(file):
    df = pd.read_csv(file, engine="pyarrow")
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(df.info())
        print(df.shape)
        print(df['supplier'].value_counts())

def eda_category(file):
    df = pd.read_csv(file, engine="pyarrow")
    print("file imported")
    data = dict(Counter(df.category))
    df_category = pd.DataFrame.from_dict(data, orient='index', columns=["category_count"])
    df_category = df_category.sort_values("category_count", ascending=False)
    print(df_category)
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df_category, x=df_category.index, y="category_count", linewidth=0)
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.yticks([250000, 500000, 750000, 1000000, 1250000, 1500000])
    plt.ticklabel_format(style='sci', axis='y')
    plt.xlabel('$1^{st}$-level Categorisation')
    plt.ylabel('Frequency')
    legend_1 = mpatches.Patch(color="#1f77b4", label='Antibodies')
    legend_2 = mpatches.Patch(color='#ff7f0e', label='Proteins, Peptides and Small Molecules')
    legend_3 = mpatches.Patch(color='#2ca02c', label='Molecular Biology')
    legend_4 = mpatches.Patch(color="#d62728", label='Assay Kits')
    legend_5 = mpatches.Patch(color="#9467bd", label='Lab Reagents & Chemicals')
    legend_6 = mpatches.Patch(color="#8c564b", label='Genomics & NGS')
    legend_7 = mpatches.Patch(color="tab:pink", label='Cell Culture')
    legend_8 = mpatches.Patch(color="#7f7f7f", label='Protein Purification & Analysis')
    legend_9 = mpatches.Patch(color="#bcbd22", label='Instruments & Equipment')
    legend_10 = mpatches.Patch(color="#17becf", label='Services')
    plt.legend(handles=[legend_1, legend_2, legend_3, legend_4, legend_5, legend_6, legend_7, legend_8, legend_9, legend_10])
    plt.tight_layout()
    plt.savefig('../figures/1_level_categorisation.pdf', format="pdf", bbox_inches="tight")
    plt.show()
    plt.close()


def eda_group(file):
    df = pd.read_csv(file, engine="pyarrow")
    print("file imported")
    data = dict(Counter(df.group))
    df_group = pd.DataFrame.from_dict(data, orient='index', columns=["category_count"])
    df_group = df_group.sort_values("category_count", ascending=False)
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df_group, x=df_group.index, y="category_count", linewidth=0)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.yticks([250000, 500000, 750000, 1000000, 1250000])
    plt.ticklabel_format(style='sci', axis='y')
    plt.xlabel('$2^{nd}$-level Categorisation')
    plt.ylabel('Frequency')
    plt.savefig('../figures/2_level_categorisation.pdf', format="pdf", bbox_inches="tight")
    plt.show()
    plt.close()

def eda_supplier(file):
    df = pd.read_csv(file, engine="pyarrow")
    print("file imported")
    data = dict(Counter(df.supplier))
    df_supplier = pd.DataFrame.from_dict(data, orient='index', columns=["category_count"])
    df_supplier = df_supplier.sort_values("category_count", ascending=False)
    plt.figure(figsize=(8, 4))
    sns.barplot(data=df_supplier, x=df_supplier.index, y="category_count", linewidth=0)
    plt.tight_layout()
    plt.tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
    plt.yticks([250000, 500000, 750000, 1000000])
    plt.ticklabel_format(style='sci', axis='y')
    plt.xlabel('Supplier')
    plt.ylabel('Frequency')
    plt.savefig('../figures/supplier_overview.pdf', format="pdf", bbox_inches="tight")
    plt.show()
    plt.close()

def main():
    eda("data_clean/csv_combined.csv")
    eda_category("data_clean/csv_combined.csv")
    eda_group("data_clean/csv_combined.csv")
    eda_supplier("data_clean/csv_combined.csv")

if __name__ == '__main__':
    main()