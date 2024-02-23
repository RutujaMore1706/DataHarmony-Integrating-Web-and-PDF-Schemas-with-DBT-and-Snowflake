from langchain_community.document_loaders.generic import GenericLoader
from langchain_community.document_loaders.parsers import GrobidParser
import json

def main():
    loader = GenericLoader.from_filesystem(
        "Archive_2/",
        glob="*",
        suffixes=[".pdf"],
        parser=GrobidParser(segment_sentences=False),
    )
    docs = loader.load()

    print(docs[3].page_content)
    # Check if there are at least four documents
    if len(docs) > 3:
        new_metadata = docs[3].metadata  # Extract metadata from the fourth document
        output_file = 'extracted_metadata.json'
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(new_metadata, f, ensure_ascii=False, indent=4)
    else:
        print("Not enough documents in the list. Can't access index 3.")

if __name__ == "__main__":
    main()
# print(docs)