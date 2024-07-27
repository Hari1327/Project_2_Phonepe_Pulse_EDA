# Project_2_Phonepe_Pulse_EDA
Project_2_Phonepe_Pulse_EDA


### Overview

This project aims to extract data from a specific YouTube channel using its Channel ID and store the extracted data in a SQL database. The main objective is to facilitate data analysis and reporting by systematically organizing and storing the channel's data. This includes retrieving video details, statistics, and other relevant metadata to provide insights into the channel's performance and content trends.
### Features
- **Channel Data Extraction**: Fetch detailed information about videos from a specified YouTube channel using the Channel ID.
- **Data Warehousing**: Store the extracted data in a SQL database for efficient querying and analysis.
- **Automated Data Pipeline**: Set up an automated process to regularly update the database with the latest data from the channel.
- **Data Analysis Ready**: Organize the data in a structured format, making it easy to perform various data analysis tasks.
### Technologies Used

- **Python**: The core programming language used for developing the data extraction and processing scripts.
- **YouTube Data API v3**: Utilized to fetch data from the YouTube channel. For accessing this API you have to install a python pacakge called *'google-api-python-client'*

    To install this package:

            pip install google-api-python-client
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
If you want you can install the packages sepeartely by above given command (or) you can also run below requirement file to install all the packages.
### Installation
Install the pytohn package that you needed for this project are provide in the *requirement.txt* file. Execute the requiremnt text in the cmd prompt or in terminal if you are using mac. By using the below command.

            pip install -r requirements.txt
### Prerequisites
- Python 3.x installed on your system.
- A Google Cloud Project with YouTube Data API enabled.
- API Key from the Google Developer Console and paste it in *Harvest.py* python file.
- MySQL installed and set up your hostame, User ID and password in *Warehouse.py* python file.
- Streamlit web application sign in 
### Usage
To clone a GitHub repository, you can use the *git clone* command

```
    git clone https://github.com/Hari1327/Project_1_Youtube_Data_Harvesting_and_Data_Warehousing.git
```
To run this Streamlit application run the below command
```python
    streamlit youtube_app.py

```


### Project Structure

- Harvest.py: Main script to extract data from the YouTube channel. 
- Warehouse.py: Contains functions for interacting with the SQL database. 
- YouTube_app.py - contains the streamlit application settings. 
- requirements.txt: List of Python dependencies.  
Contributions - - - Contributions are welcome! If you have any suggestions or improvements, feel free to create a pull request or open an issue.

## Meidum Article
https://medium.com/@nuhari75/youtube-data-harvesting-and-warehousing-506dc545e745
## License

[MIT](https://choosealicense.com/licenses/mit/)

License This project is licensed under the MIT License. See the LICENSE file for more details.
