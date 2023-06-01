import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import regexp
word_tokenizer = regexp.WhitespaceTokenizer()
nltk.download('stopwords')
stop = stopwords.words('english')
new_stopwords = ["nan"]
stop.extend(new_stopwords)
porter = PorterStemmer()

df = pd.read_csv("csv_combined.csv", header=0, index_col=0)

def preprocess_column(x, prefix):
    if isinstance(x, str):
        x = [prefix + i for i in x.split()]
    else:
        x = []
    return ' '.join(x)

def preprocess_text(text):
    ''' The function to remove punctuation,
    stopwords and apply stemming'''
    tokenized_text = [word.lower() for word in word_tokenizer.tokenize(text) if word.lower() not in stop]
    tokenized_text = [porter.stem(word) for word in tokenized_text]
    return " ".join(tokenized_text)

def preprocess_data(df):
    df['title'] = df['title'].astype(str)
    df['description'] = df['description'].astype(str)
    df['general_info'] = df['general_info'].astype(str)
    df['synonym'] = df['synonym'].astype(str)
    df["application_text"] = df["application"].apply(lambda x: preprocess_column(x, "application"))
    df["host_text"] = df["host"].apply(lambda x: preprocess_column(x, "host"))
    df["isotype_text"] = df["isotype"].apply(lambda x: preprocess_column(x, "isotype"))
    df["reactivity_text"] = df["reactivity"].apply(lambda x: preprocess_column(x, "reactivity"))
    df["all_text"] = df["title"] + " " + df["description"] + " " + df["general_info"] + " " + df["application_text"] + " " + df["host_text"] + " " + df["isotype_text"] + " " + df["reactivity_text"] + " " + df["synonym"]
    df["all_text"] = df["all_text"].apply(preprocess_text)
    df = df.drop(["application_text", "host_text", "isotype_text", "reactivity_text"], axis='columns')
    return df

df = preprocess_data(df)


df.to_csv("csv_combined_cleaned.csv")
df["all_text"].sample(20)



# Remove groups with less than 5 products
def group_cleaning(df, minimum_groupssize):
    """
    function to remove small groups with less products than set
    :param dataframe to be cleaned, minimim_groupsize limit
    :return: dataframe with small groups removed
    """
    ls = pd.DataFrame(df["group"].value_counts())
    ls = ls[ls["group"]<minimum_groupssize]
    values = ls.index.tolist()
    for i in values:
        df.drop(df[df["group"] == i].index, inplace = True)
    return df


df_groups = pd.read_csv("csv_combined_cleaned.csv", header=0, index_col=0)
gf_groups_cleaned = group_cleaning(df_groups, 10)
gf_groups_cleaned = gf_groups_cleaned.dropna(subset=['all_text'])
gf_groups_cleaned.to_csv("csv_combined.csv")