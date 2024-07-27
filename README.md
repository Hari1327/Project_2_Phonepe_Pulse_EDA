# Project_2_Phonepe_Pulse_EDA

## Phoenpe Pulse Data Geo Visualization Project
## Overview
This project visualizes geographical data from Phoenpe Pulse using a Streamlit application. It provides an interactive map to analyze and understand spatial patterns and trends within the dataset. The data is managed using MySQL.

## Features
- Interactive map visualization
- Multiple layers for different data types
- Customizable map styles
- Filtering and searching capabilities
- Tooltips and detailed information on hover
- Data management with MySQL

## Installation
1. Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/phoenpe-pulse-geo-visualization.git
cd phoenpe-pulse-geo-visualization
Install the necessary dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the MySQL database:

Install MySQL on your system if it’s not already installed.
Create a new database for the project.
Run the provided SQL scripts in the sql directory to create the necessary tables and populate them with initial data.
Configure the database connection:

Update the config.py file with your MySQL database credentials.
Run the Streamlit application:

bash
Copy code
streamlit run app.py
Usage
Load the dataset:

Ensure your dataset is in the correct format and imported into the MySQL database.
Modify the config.py file to point to your database if necessary.
Start the application:

Run streamlit run app.py to launch the application.
Open your web browser and navigate to the URL provided by Streamlit to view the map.
Interact with the map:

Use the controls to zoom in/out and move around the map.
Select different layers to view various data points.
Use the search and filter options to focus on specific areas or data points.
Hover over data points to see detailed information.
Data
The dataset used for this project should include the following fields:

latitude: Latitude of the data point
longitude: Longitude of the data point
attribute1: Description of the first attribute
attribute2: Description of the second attribute
...
Ensure your dataset is cleaned and formatted correctly before loading it into the database.

Customization
You can customize the map styles, data layers, and other settings by modifying the config.py file and the Streamlit scripts. Detailed comments and documentation within the codebase should help guide your customizations.

Contributing
Contributions are welcome! Please follow these steps to contribute:

Fork the repository
Create a new branch (git checkout -b feature/your-feature)
Commit your changes (git commit -m 'Add some feature')
Push to the branch (git push origin feature/your-feature)
Open a Pull Request
License
This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments
Thanks to the Phoenpe Pulse team for providing the data.
Special thanks to all the contributors and the open-source community.
