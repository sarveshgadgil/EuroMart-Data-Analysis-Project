# EuroMart Data Analysis Project

Welcome to the EuroMart Data Analysis Project! This project aims to demonstrate an end-to-end data analysis workflow, from importing data from Excel into a MySQL database using Python to generating insightful reports using Power BI.

## Overview

EuroMart is a fictional company, and the dataset used in this project represents its sales data. The project consists of the following components:

- `import_data_to_mysql.py`: Python script to import data from the provided Excel file into a MySQL database.
- `EuroMart Data Store.xlsx`: Excel file containing sales data for EuroMart.
- `EuroMart.pbix`: Power BI report file for visualizing and analyzing the EuroMart sales data.

## Getting Started

To get started with the project, follow these steps:

1. **Clone the Repository**: Clone this repository to your local machine using the following command:

    ```
    git clone https://github.com/your-username/EuroMart-Data-Analysis.git
    ```

2. **Setup MySQL Database**: Ensure you have a MySQL database set up where you want to import the data. Update the database connection details (host, username, password, database name) in the `import_data_to_mysql.py` script.

3. **Import Data**: Execute the `import_data_to_mysql.py` script to import the data from the Excel file into your MySQL database:

    ```
    python import_data_to_mysql.py
    ```

4. **Open Power BI Report**: Open the `EuroMart.pbix` file in Power BI to explore the sales data visually.

## Data Analysis Process

- The Python script `import_data_to_mysql.py` utilizes the pandas library to read data from the Excel file and pymysql library to connect to the MySQL database and insert the data.
- The `EuroMart.pbix` Power BI report provides various visualizations and insights into the EuroMart sales data, allowing stakeholders to analyze performance and trends effectively.

## Contributing

Contributions to the project are welcome! If you have suggestions for improvements, feature requests, or find any issues, please open an issue or submit a pull request.

