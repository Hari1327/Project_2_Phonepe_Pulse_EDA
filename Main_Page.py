import streamlit as st
import mysql.connector
import pandas as pd
import numpy as np
import altair as alt
import plotly.express as px
import git
import os
import Transform

# Set page config
st.set_page_config(
    page_title="Phonepe Pulse EDA",
    layout="wide",
    initial_sidebar_state="collapsed",
    page_icon="random",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# Inject custom CSS to reduce padding and margins
custom_css = """
<style>
    .block-container {
        padding-top: 0rem;
        padding-bottom: 0rem;
        padding-left: 1rem;
        padding-right: 1rem;
    }
    .main .block-container {
        max-width: 100%;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)


# Enable Altair dark theme
alt.themes.enable("dark")

REPO_URL = "https://github.com/PhonePe/pulse.git"
LOCAL_DIR = "C:/Users/Hari Haran/OneDrive/Desktop/GUVI/Project_1 _youtube_harvesting/Project_2_Phonepe Pulse Data Visualization and Exploration/pulse"
def update_repo():
    """Clone or fetch updates from the GitHub repository."""
    if not os.path.exists(LOCAL_DIR):
        git.Repo.clone_from(REPO_URL, LOCAL_DIR)
    else:
        repo = git.Repo(LOCAL_DIR)
        repo.remotes.origin.pull()
    Transform.ConvertAndInsert(LOCAL_DIR)


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

    # Group by State and sum the TransactionCount
    df_sum = df.groupby(location_column)[color_column].sum().reset_index()

    fig = px.choropleth(
        df_sum,
        geojson=geojson_url,
        featureidkey='properties.ST_NM',
        locations=location_column,
        color=color_column,
        color_continuous_scale=color_theme,
        title=title,
        range_color=(0, df_sum[color_column].max())
    )
    fig.update_geos(visible=False, showcountries=False, showsubunits=False, projection_scale=6, center={"lat": 22, "lon": 78}, bgcolor='rgba(0,0,0,0)')
    return fig

# Function to plot heatmap
def make_heatmap(input_df, input_y, input_x, input_color, input_color_theme):
    df_sum = input_df.groupby([input_x,"Years"])[input_color].sum().reset_index()
    x_axis_title = f"{input_color} (from {input_df['Years'].min()} to {input_df['Years'].max()})"
    heatmap = alt.Chart(df_sum).mark_rect().encode(
            y=alt.Y(f'{input_y}:O', axis=alt.Axis(title="Years", titleFontSize=18, titlePadding=15, titleFontWeight=900, labelAngle=0)),
            x=alt.X(f'{input_x}:O', axis=alt.Axis(title="States", titleFontSize=18, titlePadding=15, titleFontWeight=900)),
            color=alt.Color(f'max({input_color}):Q',
                             legend=alt.Legend(title="Registered Users"),
                             scale=alt.Scale(scheme=input_color_theme, domain=[0,df_sum[input_color].max()])),
            stroke=alt.value('black'),
            strokeWidth=alt.value(0.1),
        ).properties(width=600, height=380,
                    title=alt.TitleParams(
                    text=x_axis_title,  # Title text
                    fontSize=18,       # Title font size
                    fontWeight='bold', # Title font weight
                    anchor='middle',   # Title alignment
                    dy=-20             # Adjust vertical position
        )
        ).configure_axis(
        labelFontSize=10,
        titleFontSize=10
        ) 
    # height=300
    return heatmap

# Function to render the main page
def main_page():
    st.title("Insurance Data Analysis")
    col1, col2, col3 = st.columns((1.3, 3.5, 1.3))

    if 'map_insurance_df' in globals():
            
        with col1:
            if st.button('Update Data'):
                update_repo()
                st.success('Data has been updated successfully.')
            year_list = list(map_insurance_df["Years"].unique())
            selected_year = st.selectbox('Select a year', year_list)
            df_selected_year = map_insurance_df[map_insurance_df["Years"] == selected_year]
            color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
            selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
            selected_df = st.selectbox(
                                'Select the visulaize',
                                ('Transaction_count', 'Transaction_amount')
            )
            
            # Insurance Count
            st.write(f"Top 10 states with Highest Insurance {selected_df}")
            filtered_df = map_insurance_df[map_insurance_df["Years"] == selected_year]

            # Group by the relevant column and sum the 'Transaction_count'
            grouped_sum = filtered_df.groupby("States")[selected_df].sum()

            # Get the top 10 values
            top_10_sums = grouped_sum.nlargest(10)

            st.write(top_10_sums)

        with col2:
            choropleth = plot_choropleth(
                df_selected_year,
                geojson_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                location_column='States',
                color_column='Transaction_count',
                title=f'Insurance Count in {selected_year}', 
                color_theme=selected_color_theme
            )
            st.plotly_chart(choropleth, use_container_width=True)

            heatmap = make_heatmap(map_insurance_df, 'Years', 'States', 'Transaction_count', selected_color_theme)
            st.altair_chart(heatmap, use_container_width=True)

        with col3:
            st.write('Total Insurance Policies Purchased (Nos.)')
            total_insurance_count = map_insurance_df.loc[map_insurance_df["Years"] == selected_year, "Transaction_count"].sum()
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{total_insurance_count}</p>
                        """, unsafe_allow_html=True)
            total_amount = map_insurance_df.loc[map_insurance_df["Years"] == selected_year, "Transaction_amount"].sum()
            st.write("Total Insurance Amount")
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{round(total_amount)}</p>
                        """, unsafe_allow_html=True)
            aggregated_user = aggregated_user_df.sort_values(by='Percentage', ascending=True)
            bar_plot= px.bar(aggregated_user, x='Percentage', y='Brands', orientation='h', title='Brands by Percentage',width=100, height=500)
            st.plotly_chart(bar_plot, use_container_width=True)
            

        
    else:
        st.error("aggregated_insurance_df not found in the database tables.")



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# Function to render the second page
def second_page():
    st.title("Transaction Data Analysis")
    col1, col2, col3 = st.columns((1.3, 3.5, 1.3))

    if 'map_transaction_df' in globals():

        with col1:

            year_list = list(map_transaction_df["Years"].unique())
            selected_year = st.selectbox('Select a year', year_list)
            df_selected_year = map_transaction_df[map_transaction_df["Years"] == selected_year]
            color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
            selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
            selected_df = st.selectbox(
                                'Select the visulaize',
                                ('Transaction_count', 'Transaction_amount')
            )
            
            # Insurance Count
            st.write(f"Top 10 states with Highest Insurance {selected_df}")
            filtered_df = map_transaction_df[map_transaction_df["Years"] == selected_year]

            # Group by the relevant column and sum the 'Transaction_count'
            grouped_sum = filtered_df.groupby("States")[selected_df].sum()

            # Get the top 10 values
            top_10_sums = grouped_sum.nlargest(10)

            st.write(top_10_sums)
            
        with col2:
            choropleth = plot_choropleth(
                df_selected_year,
                geojson_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                location_column='States',
                color_column='Transaction_count',
                title=f'Transaction Count in {selected_year}', 
                color_theme=selected_color_theme
            )
            st.plotly_chart(choropleth, use_container_width=True)

            heatmap = make_heatmap(map_transaction_df, 'Years', 'States', 'Transaction_count', selected_color_theme)
            st.altair_chart(heatmap, use_container_width=True)

        with col3:
            st.write('Total Transactions')
            total_insurance_count = map_transaction_df.loc[map_transaction_df["Years"] == selected_year, "Transaction_count"].sum()
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{total_insurance_count}</p>
                        """, unsafe_allow_html=True)
            total_amount = map_transaction_df.loc[map_transaction_df["Years"] == selected_year, "Transaction_amount"].sum()
            st.write("Total Transaction Amount")
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{round(total_amount)}</p>
                        """, unsafe_allow_html=True)
            aggregated_user = aggregated_user_df.sort_values(by='Percentage', ascending=True)
            bar_plot= px.bar(aggregated_user, x='Percentage', y='Brands', orientation='h', title='Brands by Percentage',width=100, height=500)
            st.plotly_chart(bar_plot, use_container_width=True)

        
    else:
        st.error("aggregated_insurance_df not found in the database tables.")


#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# Function to render the third page
def third_page():
    st.title("Users Data Analysis")
    col1, col2, col3 = st.columns((1.3, 3.5, 1.3))

    if 'map_user_df' in globals():

        with col1:

            year_list = list(map_user_df["Years"].unique())
            selected_year = st.selectbox('Select a year', year_list)
            df_selected_year = map_user_df[map_user_df["Years"] == selected_year]
            color_theme_list = ['blues', 'cividis', 'greens', 'inferno', 'magma', 'plasma', 'reds', 'rainbow', 'turbo', 'viridis']
            selected_color_theme = st.selectbox('Select a color theme', color_theme_list)
            
            selected_user_type = st.selectbox(
                                'Select the user type to visualize',
                                ('RegisteredUser', 'AppOpens')
            )
            
            # Insurance Count
            st.write(f"Top 10 states with Highest Insurance {selected_user_type}")
            filtered_df = map_user_df[map_user_df["Years"] == selected_year]

            # Group by the relevant column and sum the 'Transaction_count'
            grouped_sum = filtered_df.groupby("States")[selected_user_type].sum()

            # Get the top 10 values
            top_10_sums = grouped_sum.nlargest(10)

            st.write(top_10_sums)
            
            
        with col2:
            
            # Group by 'Years' and 'States', then sum 'RegisteredUser' and 'AppOpens'
            map_user_df["total_user"] = map_user_df["RegisteredUser"] + map_user_df["AppOpens"]

            choropleth = plot_choropleth(
                df_selected_year,
                geojson_url="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                location_column='States',
                color_column = selected_user_type,
                title=f'{selected_user_type} in {selected_year}', 
                color_theme=selected_color_theme
            )
            st.plotly_chart(choropleth, use_container_width=True)

            heatmap = make_heatmap(map_user_df, 'Years', 'States', selected_user_type, selected_color_theme)
            st.altair_chart(heatmap, use_container_width=True)

        with col3:
            st.write('Total Registered Users')
            total_insurance_count = map_user_df.loc[map_user_df["Years"] == selected_year, "RegisteredUser"].sum()
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{total_insurance_count}</p>
                        """, unsafe_allow_html=True)
            total_amount = map_user_df.loc[map_user_df["Years"] == selected_year, "AppOpens"].sum()
            st.write("Total users thorugh App")
            st.markdown(f"""
                        <style>
                        .custom-color {{
                            color: crimson;
                            font-weight: 900;
                        }}
                        </style>
                        <p class="custom-color">{round(total_amount)}</p>
                        """, unsafe_allow_html=True)
            aggregated_user = aggregated_user_df.sort_values(by='Percentage', ascending=True)
            bar_plot= px.bar(aggregated_user, x='Percentage', y='Brands', orientation='h', title='Brands by Percentage',width=100, height=500)
            st.plotly_chart(bar_plot, use_container_width=True)
                            
    else:
        st.error("aggregated_insurance_df not found in the database tables.")


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
