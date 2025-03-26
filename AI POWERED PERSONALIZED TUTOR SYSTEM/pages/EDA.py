import streamlit as st
import nbformat
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import io
import sys
from contextlib import redirect_stdout

# Streamlit title
st.title("📓 Exploratory Data Analysis")

# Load a specific notebook file
def load_notebook(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        notebook_content = f.read()
    return nbformat.reads(notebook_content, as_version=4)

# Function to display notebook content
def display_notebook(notebook):
    output_buffer = io.StringIO()

    # Execute and display cells
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            st.markdown(cell.source)
        elif cell.cell_type == "code":
            st.code(cell.source)

            # Redirect standard output to the buffer
            with redirect_stdout(output_buffer):
                try:
                    # Execute the code dynamically
                    exec(cell.source, globals())

                    # Display graphs (if any)
                    if plt.get_fignums():
                        st.pyplot(plt.gcf())
                        plt.close() 

                except Exception as e:
                    st.error(f"Error executing cell: {e}")

            # Display the captured output
            output = output_buffer.getvalue()
            if output.strip():  
                st.text(output)

            # Clear the buffer for the next cell
            output_buffer.truncate(0)
            output_buffer.seek(0)

# Load and display the fixed "Goal0_EDA.ipynb" file
st.subheader("About Us")
notebook = load_notebook("Goal0_EDA.ipynb")
display_notebook(notebook)