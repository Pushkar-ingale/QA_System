# from llama_index.core import SimpleDirectoryReader
# import sys
# from exception import customexception
# from logger import logging

# def load_data(data):
#     """
#     Load PDF documents from a specified directory.

#     Parameters:
#     - data (str): The path to the directory containing PDF files.

#     Returns:
#     - A list of loaded PDF documents. The specific type of documents may vary.
#     """
#     try:
#         logging.info("data loading started...")
#         loader = SimpleDirectoryReader("Data")
#         documents=loader.load_data()
#         logging.info("data loading completed...")
#         return documents
#     except Exception as e:
#         logging.info("exception in loading data...")
#         raise customexception(e,sys)



    
import os
import sys
from llama_index.core import SimpleDirectoryReader
from exception import customexception
from logger import logging
import shutil

def load_data(uploaded_file):
    """
    Load PDF documents from the specified directory, and save uploaded file to the 'Data' folder.

    Parameters:
    - uploaded_file: The file uploaded by the user.

    Returns:
    - A list of loaded PDF documents.
    """
    try:
        # Define the directory where the file will be saved
        data_directory = "Data"
        
        # Check if the 'Data' directory exists, and create it if it doesn't
        if not os.path.exists(data_directory):
            logging.info(f"Creating directory: {data_directory}")
            os.makedirs(data_directory)

        # Save the uploaded file to the 'Data' directory
        file_path = os.path.join(data_directory, uploaded_file.name)

        # Write the uploaded file to the 'Data' directory
        with open(file_path, "wb") as f:
            shutil.copyfileobj(uploaded_file, f)
        
        logging.info(f"File saved to {file_path}")

        # Load the documents from the 'Data' folder
        loader = SimpleDirectoryReader(data_directory)
        documents = loader.load_data()
        logging.info(f"Data loading completed. {len(documents)} documents loaded.")
        
        return documents

    except Exception as e:
        logging.error(f"Exception in loading data: {str(e)}")
        raise customexception(f"Error in loading data: {str(e)}", sys)
