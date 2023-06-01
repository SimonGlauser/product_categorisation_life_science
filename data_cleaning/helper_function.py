import string
import os

def remove_punctuation(old_string):
    """
    This function transforms a string into a string without punctuation
    Removed punctuation: !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
    :param old_string: string to transform
    :return: string without punctuation
    """
    if old_string is not None:
        new_string = old_string.translate(str.maketrans('', '', string.punctuation))
        return new_string

def get_filename(dir, ext):
    """
    This function appends all filepath to the variable filepath that are in the directory (dir) and have the extension (ext).
    :param dir: directory where the files are
    :param ext: extension of the files
    :return: filepath list variable
    """
    filepath = []
    for item in os.listdir(dir):
        if item.endswith(ext):
            filename = dir + "/" + os.path.basename(item)
            filepath.append(filename)
    return(filepath)

def transfrom_datatype(df, columnname):
    df = df.astype({columnname: int})
    return df
