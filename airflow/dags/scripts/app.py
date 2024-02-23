from pydantic import BaseModel, HttpUrl, Field, field_validator, ValidationError
from pathlib import Path
import re
import csv
from typing import List, Optional
import os  # For directory operations

class Topic(BaseModel):
    Name_of_the_topic: str
    Year: Optional[str] = Field(default="N/A")
    Level: Optional[str] = Field(default="N/A")
    Introduction_Summary: Optional[str] = Field(default="N/A")
    Learning_Outcomes: Optional[str] = Field(default="N/A")
    Link_to_the_Summary_Page: Optional[HttpUrl] = Field(default="N/A")
    Link_to_the_PDF_File: Optional[HttpUrl] = Field(default="N/A")

    @field_validator('Year')
    def validate_year(cls, v):
        if not re.match(r"^\d{4}$", v) and v != "N/A":
            raise ValueError('Year must be a four-digit number or "N/A"')
        return v

class URLClass:
    def __init__(self, csv_file_path: str):
        self.csv_file_path = csv_file_path
        self.output_dir = 'file'  # Name of the directory to save the cleaned file
        self.output_file_name = 'cleaned_extracted.csv'  # Name of the cleaned file
    
    def clean_and_validate_csv(self) -> List[Topic]:
        valid_rows = []
        errors = []
        with open(self.csv_file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                try:
                    if row['Link_to_the_PDF_File'] and not row['Link_to_the_PDF_File'].startswith("http"):
                        row['Link_to_the_PDF_File'] = f"https://www.cfainstitute.org{row['Link_to_the_PDF_File']}"
                    topic = Topic.parse_obj(row)
                    valid_rows.append(topic)
                except ValidationError as e:
                    errors.append({'row': row, 'error': str(e)})
        
        # Ensure the output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Define the full path for the cleaned CSV file
        cleaned_csv_path = os.path.join(self.output_dir, self.output_file_name)
        
        # Write the valid rows to the cleaned CSV, overwriting any existing file
        with open(cleaned_csv_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=Topic.__fields__.keys())
            writer.writeheader()
            for topic in valid_rows:
                writer.writerow(topic.dict())
        
        return valid_rows, errors

# Usage
def main():
    csv_file_path = Path(__file__).parents[1] / 'scripts/CSV/extracted_updated.csv'
    url_class_instance = URLClass(str(csv_file_path))
    valid_topics, validation_errors = url_class_instance.clean_and_validate_csv()
    print(f"Valid rows: {len(valid_topics)}, Validation errors: {len(validation_errors)}")

if __name__ == "__main__":
    main()