import mysql.connector
import pandas as pd
import streamlit as st

# Function to fetch available bus names for the dropdown
def fetch_busnames():
    # MySQL connection setup
    db_config = {
        'host': 'localhost',        # Change to your MySQL host
        'user': 'root',             # Change to your MySQL username
        'password': 'SR#442roy',    # Change to your MySQL password
        'database': 'redbusextract' # Database where your table exists
    }
    
    # Establishing MySQL connection
    conn = mysql.connector.connect(**db_config)

    query = "SELECT DISTINCT busname FROM detailbusroutedata"  # Fetch unique busnames
    busnames = pd.read_sql(query, conn)
    conn.close()
    
    return busnames['busname'].tolist()  # Return list of busnames

# Function to fetch data for a specific busname
def fetch_data_for_bus(busname):
    db_config = {
        'host': 'localhost',        # Change to your MySQL host
        'user': 'root',             # Change to your MySQL username
        'password': 'SR#442roy',    # Change to your MySQL password
        'database': 'redbusextract' # Database where your table exists
    }
    
    # Establishing MySQL connection
    conn = mysql.connector.connect(**db_config)

    query = f"SELECT * FROM detailbusroutedata WHERE busname = '{busname}'"
    df = pd.read_sql(query, conn)
    conn.close()
    
    return df

# Streamlit app
def main():
    st.title("Bus Route Data")

    # Fetch available busnames
    busnames = fetch_busnames()

    # Dropdown menu for selecting busname
    selected_bus = st.selectbox("Select a Bus", busnames)

    if selected_bus:
        # Fetch data for the selected bus
        data = fetch_data_for_bus(selected_bus)

        # Display data in a table format
        st.write(f"### Data for {selected_bus}")
        st.dataframe(data)  # Display the data in an interactive table

if __name__ == "__main__":
    main()
