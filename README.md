### **HSNP BENEFICIARY DATA CLEANING**
<img src="evansdim.jpg" alt="unsplash" width="949" height="400">
Photo by <a href="https://unsplash.com/@evans_dimsphoto?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Evans Dims</a> on <a href="https://unsplash.com/photos/a-small-child-standing-in-a-dirt-field-next-to-a-fence-OvKHanXCrOQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a>
  



<p>The Hunger Safety Net Programme (HSNP) is an unconditional Government cash transfer programme implemented by the National Drought Management Authority (NDMA) in eight poorest and arid counties, namely; Turkana, Wajir, Mandera, Marsabit, Garissa, Tana River, Isiolo, and Samburu.</p>

<p>HSNP is one of four cash transfer programmes under the National Safety Net Programme (NSNP) collectively called Inua Jamii. The other three programmes are;</p>

1) Older Persons Cash Transfer.
2) Cash Transfers for Orphans and Vulnerable Children.
3) Persons with Severe Disability Cash Transfer.

 

<p>The NDMA is responsible for implementing HSNP, while the Social Assistance Unit under the State Department of Social Protection in the Ministry of Labour and Social Protection manages the other three programmes.</p>

#### **Authors**:[Eugene Kuloba](https://github.com/eugenekuloba)
This repository contains Python code for cleaning and preprocessing the HSNP (Household Social and Natural Resource Profile) dataset. The code is designed to perform various data cleaning and transformation tasks to ensure the dataset's quality and consistency.

## Table of Contents

- [Introduction](#introduction)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
- [Usage](#usage)
  - [Running the Code](#running-the-code)
  - [Data Cleaning](#data-cleaning)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

## Introduction

The HSNP dataset cleaning code is designed to perform the following tasks:
- Reading an Excel file containing HSNP data
- Data understanding: displaying dataset statistics, checking for missing values, and duplicates
- Data cleaning: standardizing column names, correcting coordinate data, and filtering data by county
- Saving cleaned data in XLSX and CSV formats
- Optionally, concatenating multiple XLSX files into a single dataset

## Getting Started

### Prerequisites

Before running the code, ensure you have the following prerequisites installed:

- Python (version 3.10.12)
- Required Python libraries (listed in [requirements.txt](requirements.txt))

### Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/hsnp-dataset-cleaning.git
cd hsnp-dataset-cleaning
```
2. Install the required Python libraries:
```bash
pip install -r requirements.txt
```

## Usage
### Running the Code

```bash
python main.py
```
Follow the prompts to select the input Excel file and choose data cleaning options.

## Data Cleaning

The data cleaning process includes:

1. Standardizing column names
2. Correcting coordinate data
3. Filtering data by county
4. Saving cleaned data in XLSX and CSV formats

## Output
The cleaned dataset will be saved in the following formats:

1. XLSX files: cleaned_xlsx_data/county_name_cleaned.xlsx
2. CSV files: cleaned_csv_data/county_name_cleaned.csv
3. If you choose to concatenate multiple XLSX files, the concatenated dataset will be saved as concatenated_dataset.xlsx.

## Contributing

Contributions are welcome! If you'd like to contribute to this project, please follow these steps:

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## License
This project is licensed under the MIT License.

## Acknowledgments
Special thanks to the HSNP dataset contributors and maintainers for providing the data.
