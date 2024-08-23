import os
from typing import Union, Dict

from langchain.tools import tool

class DirWriteTool:
    @tool("Create directory")
    def dir_write_tool(input: Union[Dict[str, Union[str, Dict]], str]) -> str:
        """Useful to create a directory with the given path.
        
        Args:
            input: Either a string representing the directory path,
                   or a dictionary containing a 'directory_path' key.
        
        Returns:
            A string confirming the directory has been created or describing an error.
        """
        try:
            if isinstance(input, dict):
                directory_path = input.get('directory_path')
                if isinstance(directory_path, dict):
                    directory_path = directory_path.get('title')
            elif isinstance(input, str):
                directory_path = input
            else:
                return f"Invalid input type. Expected str or dict, got {type(input)}"
            
            if not directory_path:
                return "No valid directory path provided."
            
            if not isinstance(directory_path, str):
                return f"Invalid directory path type. Expected str, got {type(directory_path)}"
            
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)
                return f"Directory '{directory_path}' has been created successfully."
            else:
                return f"Directory '{directory_path}' already exists."
        except Exception as e:
            return f"An error occurred: {str(e)}"