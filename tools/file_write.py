import json
import os
from typing import Dict, Union

from langchain.tools import tool

class FileWriteTool:
    @tool("Write file")
    def file_write_tool(input: Union[Dict[str, str], str]) -> str:
        """Useful to write content to a file with the given filename.
        
        Args:
            input: Either a JSON string or a dictionary containing 'filename' and 'content' keys.
        
        Returns:
            A string confirming the file has been written or describing an error.
        """
        try:
            if isinstance(input, str):
                input_dict = json.loads(input)
            elif isinstance(input, dict):
                input_dict = input
            else:
                return f"Invalid input type. Expected str or dict, got {type(input)}"
            
            filename = input_dict.get('filename')
            content = input_dict.get('content')
            
            if not filename or not content:
                return "Both 'filename' and 'content' must be provided."
            
            with open(filename, 'w') as file:
                file.write(content)
            return f"File '{filename}' has been written successfully."
        except json.JSONDecodeError:
            return "Invalid JSON string provided."
        except Exception as e:
            return f"An error occurred: {str(e)}"