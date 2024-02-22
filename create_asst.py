from instructions import asst_name, asst_file_path, asst_model, asst_instructions
from functions import create_assistant

'''
Calls function to create a new assistant if needed. Passes in assistant name, file(s), 
model and instructions from instructions.py file. Prints the Assistant ID and File ID
upon successful creation.
'''
file, assistant = create_assistant(asst_name, asst_file_path, asst_model, asst_instructions)
print(file.id, assistant.id)
