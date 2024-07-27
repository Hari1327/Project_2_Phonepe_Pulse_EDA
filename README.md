### Phonepe Pulse Data Geo Visualization Project
## Overview
This project visualizes geographical data from Phoenpe Pulse. It provides an interactive map to analyze and understand spatial patterns and trends within the dataset.

### Features
- Interactive map visualization
- Multiple layers for different data types
- Customizable map styles
- Filtering and searching capabilities
- Tooltips and detailed information on hover
### Technologies Used

- **Python**: The core programming language used for developing the data extraction and processing scripts.
- **MySQL Database**: MySQL is a Relational Database Management System (RDBMS) whereas the structured Query Language (SQL) is the language used for handling the RDBMS using commands i.e Creating, Inserting, Updating and Deleting the data from the databases.
- **Pandas**: For data manipulation and transformation.
To install this package:
                
                pip install Pandas
- **mysql-connetor**: A MySQL database connector for Python, which is officially supported by Oracle. It provides a pure Python interface to MySQL databases, allowing you to connect to MySQL servers, execute SQL queries, and retrieve results.
To install this package:

               pip install mysql-connector-python
- **Streamlit** - Streamlit is an open-source Python library designed to create and share custom web applications for data science and machine learning projects with minimal effort. Its simplicity and focus on rapid prototyping make it a popular choice among data scientists and developers who need to quickly visualize and interact with data. Also you can download the data as csv file from the web application.
To install this package:
                pip install streamlit
### Installation
1. Clone the repository:
```
    git clone https://github.com/yourusername/phoenpe-pulse-geo-visualization.git](https://github.com/Hari1327/Project_2_Phonepe_Pulse_EDA.git
    cd phoenpe-pulse-geo-visualization
```
2. Install the necessary dependencies:
```
    pip install -r requirements.txt
```
3. Run the application:
```
    streamlit run python app.py
```
### Prerequisites
- Python 3.x installed on your system.
- MySQL installed and set up.
- Streamlit web application sign in 
### Usage
1. Load the dataset:

- Ensure your dataset is in the correct format and placed in the data directory.
- Start the application:
- Run python app.py to launch the application.
- Open your web browser and navigate to http://localhost:5000 to view the map.
2. Interact with the map:

- Use the controls to zoom in/out and move around the map.
- Select different layers to view various data points.
- Use the search and filter options to focus on specific areas or data points.
- Hover over data points to see detailed information.


### Project Structure

- Tranform.py: Conver the csv files into the dataframes 
- database.py: Contains functions for interacting dataframes with the MySQL database. 
- Main_page.py - contains the streamlit application settings. 
- requirements.txt: List of Python dependencies.

## Medium Article:
https://medium.com/@nuhari75/phonepe-pulse-data-visualization-and-exploration-e8a8a0f06d88

## Demo video: https://youtu.be/QMMGulWvc0U?si=xVNDhUIET_afg-IO
## License

[MIT](https://choosealicense.com/licenses/mit/)

License This project is licensed under the MIT License. See the LICENSE file for more details.
