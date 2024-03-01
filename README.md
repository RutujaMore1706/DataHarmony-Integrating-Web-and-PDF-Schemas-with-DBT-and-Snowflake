
## Project Title

Development and Validation of Data Management Schemas for Web and PDF Content Analysis With DBT and Snowflake Integration







## Problem Statement

In the evolving landscape of data management and analysis, efficiently organizing, validating, and transforming data from diverse sources like webpages and PDF documents into actionable insights remains a significant challenge. This project aims to design a comprehensive data management system that addresses these challenges through the creation of structured Python classes for webpage URLs and PDF content. The system will leverage Pydantic for schema validation to ensure data integrity and cleanliness. Furthermore, it will explore the integration of DBT (Data Build Tool) with Snowflake for sophisticated data transformation workflows, enabling the generation of summarized data tables for enhanced analytical purposes. This approach seeks to not only streamline data validation processes but also optimize data analysis and reporting capabilities, catering to potential applications ranging from academic research to business intelligence. The project will include rigorous testing to validate the functionality and reliability of the designed schemas and transformation workflows, setting a foundation for scalable and efficient data management strategies.



## Project Goals


## Part 1

    1. Design and implement the URLClass in Python to represent the schema for the Assignment 2 (Part 1) CFA webpages, ensuring adherence to defined guidelines.
    2. Develop two PDFClasses, MetaDataPDFClass, and ContentPDFClass, in Python to represent the schema for the Grobid output.
    3. Utilize the provided schema for Part 1 and create schemas for Part 2 (PDFClass).
    4. Implement data and schema validation using Pydantic 2, ensuring the integrity and cleanliness of the data.
    5. Generate "clean" CSV files from validated data.
    6. Construct 5 pass and 5 fail test cases for each of the three classes using Pytest to demonstrate validation success and failure scenarios.
    7. Utilize existing code structures such as Grobid data loader and URL data loader classes as starter code or refer to Grobid Data classes example.
    8. Prepare for Part 2 using DBT by understanding the documentation and redoing the tutorial with the "clean CSV" files created in Part 1.

## Part 2:

    1. Load the clean data from Part 1 into Snowflake.
    2. Utilize DBT to create transformation workflows.
    3. Develop a summary table with the schema: Level, Topic, Year, Number of articles, Min Length (Summary), Max Length (Summary), Min Length (Learning outcomes), Max Length (Learning outcomes).
    4. Design the summary table model in a flexible and efficient manner.
    5. Materialize the summary table into a new table within Snowflake.
    6. Write tests to validate the new columns and ensure data accuracy.
    7. Document the model thoroughly for future reference and understanding.
    8. Commit and deploy the model, following best practices outlined in DBT documentation.
    9. Establish separate Test and Production environments, including corresponding databases/tables in Snowflake.
    10. Considerations for Test and Production environments include data isolation, access controls, version control, and deployment strategies.
## Codelab

[![codelabs](https://img.shields.io/badge/codelabs-4285F4?style=for-the-badge&logo=codelabs&logoColor=white)](https://codelabs-preview.appspot.com/?file_id=1H-NznhIh2AqN8jsjyq399n_NODPnIhcgUE6CWyrsULI#5)


## Technologies Used

[![Python](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)](https://www.python.org/)
[![Snowflake](https://img.shields.io/badge/Snowflake-387BC3?style=for-the-badge&logo=snowflake&logoColor=light)](https://www.snowflake.com/)
[![Pydantic](https://img.shields.io/badge/Pydantic-339933?style=for-the-badge&logo=python&logoColor=white)](https://pydantic-docs.helpmanual.io/)
[![Beautiful Soup](https://img.shields.io/badge/Beautiful%20Soup-59666C?style=for-the-badge&logo=python&logoColor=blue)](https://www.crummy.com/software/BeautifulSoup/)
[![DBT](https://img.shields.io/badge/DBT-F2AFA6?style=for-the-badge&logo=dbt&logoColor=white)](https://www.getdbt.com/)
[![Grobid](https://img.shields.io/badge/Grobid-007396?style=for-the-badge&logo=java&logoColor=white)](https://github.com/kermitt2/grobid)
[![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apache-airflow&logoColor=white)](https://airflow.apache.org/)




##  Prerequisites 


**Part 1:**

**General Software Prerequisites:**

1. **Python:** Install Python programming language (version 3.x) from the official Python website or using package managers like Anaconda.

2. **Snowflake Account:** Sign up for a Snowflake account or gain access to an existing account with appropriate permissions.

3. **DBT (Data Build Tool):** Install DBT for data transformation and modeling.

   ```
   pip install dbt
   ```

6. **Git:** Install Git version control system for managing project codebase.

   - Download and install Git from the official website: [Git](https://git-scm.com/)

**Specific Software Prerequisites for Part 1:**

1. **PDF Data Extraction Tools:** Depending on the chosen method for extracting metadata and content from PDF files, you might need additional libraries or tools such as PyPDF2, pdfplumber, or others. Install the relevant libraries as needed.

   ```
   pip install PyPDF2
   ```

**Specific Software Prerequisites for Part 2:**

1. **Snowflake Client:** Install Snowflake Python client for connecting to Snowflake from Python scripts.

   ```
   pip install snowflake-connector-python
   ```

2. **Snowflake CLI (Command Line Interface):** Install Snowflake CLI for running SQL commands and managing Snowflake resources from the command line.

   - Download and install Snowflake CLI from the official Snowflake documentation: [Snowflake CLI](https://docs.snowflake.com/en/user-guide/snowsql-install-config.html)

3. **DBT Setup:** Configure DBT to connect to Snowflake by specifying connection details in the profiles.yml file.

4. **Test Environment Setup:** Set up separate test and production environments within Snowflake as per project requirements.

Ensure that all software prerequisites are installed and configured properly before starting the project to avoid any issues during development and execution.
 

 

 

 

 

 

 

 
## Project Structure




```
Assignment3
├── CSV
│   └── extracted_updated.csv
├── Updated_CSV
│   └── cleaned_extracted.csv
├── Validation.py
├── Webscrapper.py
├── airflow-dbt-cloud
│   ├── Dockerfile
│   ├── LICENSE
│   ├── README.md
│   ├── archive
│   │   ├── dbt_cloud_example.py
│   │   ├── dbt_cloud_example_single_tenant.py
│   │   ├── dbt_cloud_provider_example.py
│   │   ├── dbt_cloud_smart_reruns.py
│   │   ├── dbt_cloud_utils.py
│   │   ├── example-dag-advanced.py
│   │   ├── example-dag-basic.py
│   │   └── run_results_parser.py
│   ├── dags
│   │   ├── dbt_cloud_provider_eltml.py
│   │   └── example-dag.py
│   ├── images
│   │   ├── airflow_api_token_variable.png
│   │   ├── dbt_cloud_api_token.png
│   │   ├── dbt_cloud_api_token_connection.png
│   │   ├── dbt_cloud_provider_verify_success.png
│   │   ├── turn_on_dag.png
│   │   ├── verify_dbt_cloud_job_success.png
│   │   ├── verify_dbt_cloud_job_success_provider.png
│   │   └── verify_job_success.png
│   ├── include
│   ├── packages.txt
│   ├── plugins
│   ├── requirements.txt
│   └── tests
│       └── dags
│           └── test_dag_integrity.py
├── execute_commands.py
├── grobid_step
│   ├── Archive_2
│   │   ├── 2024-l1-topics-combined-2.pdf
│   │   ├── 2024-l2-topics-combined-2.pdf
│   │   └── 2024-l3-topics-combined-2.pdf
│   ├── GROBID
│   │   ├── txt
│   │   │   ├── Grobid_RR_2024-l1-topics-combined-2.grobid.tei_combined.txt
│   │   │   ├── Grobid_RR_2024-l2-topics-combined-2.grobid.tei_combined.txt
│   │   │   └── Grobid_RR_2024-l3-topics-combined-2.grobid.tei_combined.txt
│   │   └── xml
│   │       ├── 2024-l1-topics-combined-2.grobid.tei.xml
│   │       ├── 2024-l1-topics-combined-2_408.txt
│   │       ├── 2024-l2-topics-combined-2.grobid.tei.xml
│   │       ├── 2024-l2-topics-combined-2_408.txt
│   │       ├── 2024-l3-topics-combined-2.grobid.tei.xml
│   │       └── 2024-l3-topics-combined-2_408.txt
│   ├── grobid_parsing.py
│   ├── parsed_into_schema
│   │   ├── content
│   │   │   ├── csv
│   │   │   │   ├── grobid_content_2024_l1_topics_combined_2.csv
│   │   │   │   ├── grobid_content_2024_l2_topics_combined_2.csv
│   │   │   │   └── grobid_content_2024_l3_topics_combined_2.csv
│   │   │   └── json
│   │   │       ├── 2024-l1-topics-combined-2.grobid.tei.json
│   │   │       ├── 2024-l2-topics-combined-2.grobid.tei.json
│   │   │       └── 2024-l3-topics-combined-2.grobid.tei.json
│   │   └── metadata
│   │       ├── csv
│   │       │   ├── grobid_metadata_2024_l1_topics_combined_2.csv
│   │       │   ├── grobid_metadata_2024_l2_topics_combined_2.csv
│   │       │   └── grobid_metadata_2024_l3_topics_combined_2.csv
│   │       └── json
│   │           ├── 2024-l1-topics-combined-2.grobid.tei.json
│   │           ├── 2024-l2-topics-combined-2.grobid.tei.json
│   │           └── 2024-l3-topics-combined-2.grobid.tei.json
│   └── requirements.txt
├── pytests
│   ├── test_content.py
│   ├── test_metadata.py
│   └── test_topic.py
├── requirements.txt
└── snowflake_transfer
    ├── requirements.txt
    └── snowflake.py

```


## Architectural Diagram


![Diagram Description](./diagrams/diagram.png)
## How to run Application locally


To run the application locally from scratch, follow these steps:

1. **Clone the Repository**: Clone the repository onto your local machine.

   ```bash
   git clone <repository_url>
   ```

2. **Create a Virtual Environment**: Set up a virtual environment to isolate project dependencies.

   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**: Activate the virtual environment.

   - **Windows**:

     ```bash
     venv\Scripts\activate
     ```

   - **Unix or MacOS**:

     ```bash
     source venv/bin/activate
     ```

4. **Install Requirements**: Install the required dependencies listed in `requirements.txt`.

   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Notebook Script**: Execute the `run_notebook.sh` shell script to run the application.

   ```bash
   bash run_notebook.sh
   ```

By following these steps, you will be able to run the application locally from scratch. Ensure that Docker Desktop is installed and running before hosting the Grobid server.
## Team Information and Contribution 

Name           | NUID          |
---------------|---------------|
Anirudh Joshi  | 002991365     |      
Nitant Jatale  | 002776669     |      
Rutuja More    | 00272782      |      
