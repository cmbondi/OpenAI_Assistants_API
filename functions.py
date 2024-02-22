# Functions for OpenAI Assistants API
from openai import OpenAI

'''Initialize OpenAI client - no arguments if API key set as system environment variable
otherwise must be added here with api_key="YOUR_API_KEY" argument. NEVER HARD CODE IT!
'''
client = OpenAI()

def create_assistant(asst_name, asst_file_path, asst_model, asst_instructions):
    # Add a file to upload for assistant if needed
    file = client.files.create(
        file=open(asst_file_path, "rb"),
        purpose='assistants'
    )

    # Create the Assistant with data passed in with function call
    assistant = client.beta.assistants.create(
        name=asst_name,
        instructions=asst_instructions,
        model=asst_model,
        tools=[{"type": "retrieval"}, {"type": "code_interpreter"}],
        file_ids=[file.id]
    )

    # Return the new file and assistant objects
    return file, assistant

def create_new_thread():
    # Function to create a new thread or conversation
    thread = client.beta.threads.create()
    return thread.id

def add_message(thread_id, question):
    ''' 
    Function to add a new message to an existing thread/conversation. Takes an existing
    thread ID and the content of the question passed with the function call.
    '''
    message = client.beta.threads.messages.create(
    thread_id=thread_id,
    role="user",
    content=question
    )
    return message

def run_thread(assist_id, thread_id):
    '''
    Runs the thread with the AI model passing in the Assistant ID to run it with and
    the existing thread ID
    '''
    run = client.beta.threads.runs.create(
        thread_id=thread_id,
        assistant_id=assist_id
    )
    return run

def get_response(run, thread_id):
    '''
    Get the response to the question from running it. First checks if run state is "completed"
    and keeps retrieving the run status until it is completed.
    '''
    while run.status != "completed":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread_id,
            run_id=run.id
        )
    # Gets the list of messages in the thread including the latest response from the last run
    messages = client.beta.threads.messages.list(
        thread_id=thread_id
    )

    # Stores the content of the AI response
    message_content = messages.data[0].content[0].text.value

    # Returns them
    return message_content
        