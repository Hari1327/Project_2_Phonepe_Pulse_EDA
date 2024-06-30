import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px

# Set page config
st.set_page_config(
    page_title="Phonepe Pulse EDA",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Enable Altair dark theme
alt.themes.enable("dark")

# Function to get table names from the database
def get_table_names(cursor):
    cursor.execute("SHOW TABLES;")
    tables = cursor.fetchall()
    table_names = [table[0] for table in tables]
    return table_names

# Function to get column names
def get_column_names(cursor, table_name):
    query = f"DESCRIBE {table_name};"
    cursor.execute(query)
    columns = cursor.fetchall()
    column_names = [column[0] for column in columns]
    return column_names

# Connect to MySQL server and select the database
try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Hariharan@27",  # Consider using environment variables for credentials
        database="phonepe",
        port=3306
    )
    cursor = mydb.cursor()
except mysql.connector.Error as err:
    st.error(f"Error: {err}")
    st.stop()

# Get the table names from the database
table_names = get_table_names(cursor)

# Loop through each table name to fetch data
for table_name in table_names:
    column_names = get_column_names(cursor, table_name)
    query = f"SELECT * FROM {table_name};"
    cursor.execute(query)
    table_data = cursor.fetchall()
    df = pd.DataFrame(table_data, columns=column_names)
    globals()[f"{table_name}_df"] = df

# Close the cursor and connection
cursor.close()
mydb.close()

# Function to plot choropleth map
def plot_choropleth(df, geojson_url, location_column, color_column, title, color_theme):
    fig = px.choropleth(
        df,
        geojson=geojson_url,
        featureidkey='properties.ST_NM',
        locations=location_column,
        color=color_column,
        color_continuous_scale=color_theme,
        title=title,
        range_color=(0, 4000000)
    )
    fig.update_geos(visible=False, showcountries=False, showsubunits=False, projection_scale=6, center={"lat": 22, "lon": 78}, bgcolor='rgba(0,0,0,0)')
    return fig

# Function to plot heatmap
def plot_heatmap(df, x_column, y_column, color_column, color_theme):
    color_domain = [df[color_column].min(), df[color_column].max()]
    heatmap = alt.Chart(df).mark_rect().encode(
        x=alt.X(x_column, title="State"),
        y=alt.Y(y_column, title="Year"),
        color=alt.Color(color_column, scale=alt.Scale(domain=color_domain, scheme=color_theme), title="Insurance Count"),
        tooltip=[x_column, y_column, color_column]
    ).properties(
        width=600,
        height=400,
        title='Insurance Count Heatmap'
    )
    return heatmap

# Function to plot donut chart
def plot_donut_chart(df, value_column, title):
    fig = px.pie(df, names='States', values=value_column, hole=0.5, title=title)
    fig.update_traces(textinfo='percent+label')
    return fig

# Function to render the main page

def main_page():
    st.title("Insurance Data Analysis")
    col = st.columns((1.5, 4.5, 2), gap='medium')

    if 'aggregated_insurance_df' in globals():

            with col[1]:
                    year_list = list(aggregated_insurance_df["Years"].unique())
                    selected_year = st.selectbox('Select a year', year_list)
                    df_selected_year = aggregated_insurance_df[aggregated_insurance_df["Years"] == selected_year]
                    color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
                    selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
                    choropleth = plot_choropleth(
                        df_selected_year,
                        geojson_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                        location_column='States',
                        color_column='Insurance_count',
                        title=f'Insurance Count in {selected_year}', 
                        color_theme= selected_color_theme
                    )
                    st.plotly_chart(choropleth, use_container_width=True)

                    heatmap = plot_heatmap(
                        df_selected_year,
                        x_column='States',
                        y_column='Years',
                        color_column='Insurance_count',
                        color_theme= selected_color_theme
                    )
                    st.altair_chart(heatmap, use_container_width=True)

            with col[2]:
            #     donut_chart = plot_donut_chart(
            #         df_selected_year,
            #         value_column='Insurance_count',  # Replace with your actual column name for insurance amount
            #         title='Total Insurance Policies Purchased (Nos.)'
            # )
            #     st.plotly_chart(donut_chart, use_container_width=True)
                st.write('Total Insurance Policies Purchased (Nos.)')
                Total_Insurance_count = map_insurance_df.loc[map_insurance_df["Years"] == selected_year, "Transaction_count"].sum()
                st.write(Total_Insurance_count)
                Total_amount = map_insurance_df.loc[map_insurance_df["Years"] == selected_year, "Transaction_amount"].sum()
                st.write("Total Amount of Insurance")
                st.write(round(Total_amount),"Lakhs")
    else:
            st.error("aggregated_insurance_df not found in the database tables.")

# Function to render the second page
def second_page():
    st.title("Second Page")
    st.write("This is the second page of the Streamlit app!")

# Function to render the third page
def third_page():
    st.title("Third Page")
    st.write("This is the third page of the Streamlit app!")

# Dictionary to map page names to functions
pages = {
    "Insurance": main_page,
    "Transaction": second_page,
    "User": third_page,
}

# Sidebar for navigation
st.sidebar.title("Navigation")
selected_page = st.sidebar.radio("Go to", list(pages.keys()))

# Render the selected page
pages[selected_page]()