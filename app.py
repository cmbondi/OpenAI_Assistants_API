from openai import OpenAI
from functions import create_new_thread, add_message, run_thread, get_response

# Hard code assistant ID after assistant creation to set the assistant for the app
assist_id = "asst_IgOO223FMpfKBoKoWuj1U742"

# Create a new thread for the current conversation
thread_id = create_new_thread()

if __name__ == "__main__":
    # While loop to keep asking for user input until the word exit is entered
    while True:
        question = input("Enter your question (enter exit to end): ")
        if "exit" in question.lower():
            print("Thanks, have a nice day!ex")
            break
        # Add the user_input to the message thread
        message = add_message(thread_id, question)
        # Run the message thread against the assistant
        run = run_thread(assist_id, thread_id)
        # Get the response from the AI along with annotations
        annotations,message_content = get_response(run,thread_id)
        # Display the AI reply to the user
        print(message_content)
