# Import Packages
import os
from zipfile import ZipFile
from xml.etree import ElementTree
import csv
# Import Helperfunctions
from helper_function import remove_punctuation
from helper_function import get_filename


def get_xml(filepath):
    """
    This function unzips .xml files from the data/2022 folder to the data_cleaning/data_xml folder.
    :return:.xml files in the folder /data_xml
    """
    for file in filepath:
        with ZipFile(file, 'r') as zipObj:
            listOfFileNames = zipObj.namelist()
            for fileName in listOfFileNames:
                if fileName.endswith('.xml'):
                    os.chdir("data_xml")
                    zipObj.extract(fileName)
                    os.chdir("../")
    print("all xml extracted")


def extract_csv(counter):
    """
    This function extracts the information from th xml file and creates a csv file
    :param counter: counter for development
    :return: .csv files in the folder /data_csv
    """
    for file in os.listdir("data_xml"):
        # if counter in range(0,5):
        #     counter += 1
        #     continue
        # if counter == 6:
        #     break
        csvname = file.split(".")[0]
        xml = ElementTree.parse(f"data_xml/{file}")
        csvfile = open(f"data_csv/{csvname}.csv", 'w', newline='', encoding='utf-8')
        csvfile_writer = csv.writer(csvfile)
        csvfile_writer.writerow(
            ["supplier_id", "supplier", "catalogNumber", "title", "description", "category_id", "category", "group_id",
             "group", "general_info", "application", "host", "isotype", "reactivity", "synonym", "gene_symbol", "gene_description"])
        for product in xml.findall("product"):
            application, reactivity, synonym, general_info, host, isotype, gene_symbol, gene_description = None, None, None, None, None, None, None, None
            if (product):
                supplier = product.find("supplier")
                supplier_id = supplier.attrib["id"]
                supplier = supplier.text
                catalogNumber = product.find("catalogNumber")
                if product.find("title") is not None:
                    title = remove_punctuation(product.find("title").text)
                else:
                    title = None
                if product.find("description") is not None:
                    description = remove_punctuation(product.find("description").text)
                else:
                    description = None
                category = product.find("category")
                category_id = category.attrib["id"]
                category = category.text
                group = product.find("group")
                group_id = group.attrib["id"]
                group = group.text
                for attributes in product.findall("attributes"):
                    if (attributes):
                        for attribute in attributes.findall("attribute"):
                            if attribute.attrib["key"] == "generalInfo":
                                general_info = remove_punctuation(attribute.text)
                                if general_info is None or general_info == description:
                                    general_info = None
                for lists in product.findall("lists"):
                    if (lists):
                        for list in lists.findall("list"):
                            if list.attrib["key"] == "application":
                                application = []
                                for item in list.findall("item"):
                                    application.append(remove_punctuation(item.find("value").text))
                                application = " ".join(application)
                            if list.attrib["key"] == "host":
                                host = []
                                for item in list.findall("item"):
                                    host.append(remove_punctuation(item.find("value").text))
                                host = " ".join(host)
                            if list.attrib["key"] == "isotype":
                                isotype = []
                                for item in list.findall("item"):
                                    isotype.append(remove_punctuation(item.find("value").text))
                                isotype = " ".join(isotype)
                            if list.attrib["key"] == "reactivity":
                                reactivity = []
                                for item in list.findall("item"):
                                    reactivity.append(remove_punctuation(item.find("value").text))
                                reactivity = " ".join(reactivity)
                for synonyms in product.findall("synonyms"):
                    if (synonyms):
                        synonym = []
                        for value in synonyms.findall("value"):
                            synonym.append(remove_punctuation(value.text))
                        synonym = " ".join(synonym)
                for genes in product.findall("genes"):
                    if (genes):
                        gene_symbol = []
                        gene_description = []
                        for gene in genes.findall("symbol"):
                           for symbol in gene.findall("symbol"):
                               gene_symbol.append(remove_punctuation(symbol.find("value").text))
                           gene_symbol = " ".join(gene_symbol)
                           for gene_description in gene.findall("description"):
                               gene_description.append(remove_punctuation(gene_description.find("value").text))
                           gene_description = " ".join(gene_description)

                csv_line = [supplier_id, supplier, catalogNumber.text, title, description,
                            category_id, category, group_id, group, general_info, application, host, isotype, reactivity, synonym, gene_symbol, gene_description]
                csvfile_writer.writerow(csv_line)
        csvfile.close()
        print(f"csv for {csvname} done")
        counter += 1

def main():
    filepath = get_filename("../data/2022", ".zip")
    #get_xml(filepath)
    extract_csv(0)

if __name__ == '__main__':
   main()

