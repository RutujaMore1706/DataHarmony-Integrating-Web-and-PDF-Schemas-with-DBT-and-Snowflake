from bs4 import BeautifulSoup
import lxml.etree as ET  # Use lxml's etree for full XPath support
import pandas as pd
import json
import os

FILENAME_MAPPING = {
    '2024-l1-topics-combined-2.grobid.tei.xml': {
        'content_csv': 'grobid_content_2024_l1_topics_combined_2.csv',
        'metadata_csv': 'grobid_metadata_2024_l1_topics_combined_2.csv'
    },
    '2024-l2-topics-combined-2.grobid.tei.xml': {
        'content_csv': 'grobid_content_2024_l2_topics_combined_2.csv',
        'metadata_csv': 'grobid_metadata_2024_l2_topics_combined_2.csv'
    },
    '2024-l3-topics-combined-2.grobid.tei.xml': {
        'content_csv': 'grobid_content_2024_l3_topics_combined_2.csv',
        'metadata_csv': 'grobid_metadata_2024_l3_topics_combined_2.csv'
    }
}

class ContentPDFClass:
    @staticmethod
    def extract_content(xml_file_path):
        with open(xml_file_path, 'r', encoding='UTF-8') as file:
            soup = BeautifulSoup(file, 'xml')  # Use 'xml' parser
        return {
            "title": soup.title.get_text(strip=True) if soup.title else '',
            "abstract": soup.abstract.get_text("\n", strip=True) if soup.abstract else '',
            "body": soup.body.get_text("\n", strip=True) if soup.body else '',
            "back": soup.back.get_text("\n", strip=True) if soup.back else ''
        }

class MetadataPDFClass:
    def __init__(self, xml_file_path):
        self.tree = ET.parse(xml_file_path)
        self.root = self.tree.getroot()
        self.namespaces = {
            'tei': 'http://www.tei-c.org/ns/1.0',
            'xlink': 'http://www.w3.org/1999/xlink'
        }

    def extract_first_item(self, xpath_result):
        if xpath_result:
            # Clean and return the first item
            return xpath_result[0].replace('\n', '').replace('\t', '').strip()
        else:
            return "No Data"

    def extract_abstract(self):
        # Extracting all <div> elements within <abstract>
        abstract_divs = self.root.xpath('//tei:profileDesc/tei:abstract/tei:div', namespaces=self.namespaces)
        abstract_texts = []
        for div in abstract_divs:
            # For each <div>, extract <head> text (if present) and all <p> text, and combine them
            head_text = " ".join(div.xpath('./tei:head/text()', namespaces=self.namespaces)).strip()
            p_texts = " ".join(div.xpath('./tei:p/text()', namespaces=self.namespaces)).strip()
            div_text = (head_text + " " + p_texts).strip()
            abstract_texts.append(div_text)
        return " ".join(abstract_texts)

    def extract_metadata(self):
        metadata_dict = {
            "Title": self.extract_first_item(self.root.xpath('//tei:titleStmt/tei:title[@level="a" and @type="main"]/text()', namespaces=self.namespaces)),
            "Publisher": self.extract_first_item(self.root.xpath('//tei:publicationStmt/tei:publisher/text()', namespaces=self.namespaces)),
            "AvailabilityStatus": self.extract_first_item(self.root.xpath('//tei:availability/@status', namespaces=self.namespaces)),
            "BiblicalReference": self.extract_first_item(self.root.xpath('//tei:back//tei:listBibl/text()', namespaces=self.namespaces)),
            "AppInfoDescription": self.extract_first_item(self.root.xpath('//tei:application/tei:desc/text()', namespaces=self.namespaces)),
            "Abstract": self.extract_abstract(),
        }
        return metadata_dict

def process_files(input_dir, output_dir):
    for xml_filename, paths in FILENAME_MAPPING.items():
        xml_file_path = os.path.join(input_dir, xml_filename)
        content_data = ContentPDFClass.extract_content(xml_file_path)
        metadata_data = MetadataPDFClass(xml_file_path).extract_metadata()

        # Save content and metadata to CSV
        content_csv_path = os.path.join(output_dir, 'content', 'csv', paths['content_csv'])
        metadata_csv_path = os.path.join(output_dir, 'metadata', 'csv', paths['metadata_csv'])
        
        pd.DataFrame([content_data]).to_csv(content_csv_path, index=False)
        pd.DataFrame([metadata_data]).to_csv(metadata_csv_path, index=False)

if __name__ == "__main__":
    input_dir = 'GROBID/xml'
    output_dir = 'parsed_into_schema'
    process_files(input_dir, output_dir)
