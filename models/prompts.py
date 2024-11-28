from langchain_core.prompts import ChatPromptTemplate

# Fixed PROMPT
def read_file_to_string(filepath):
  """Reads the contents of a file and returns them as a string.

  Args:
    filepath: The path to the file.

  Returns:
    A string containing the file's contents, or None if the file does not exist.
  """
  try:
    with open(filepath, 'r') as file:
      file_content = file.read()
    return file_content
  except FileNotFoundError:
    print(f"Error: File not found at {filepath}")
    return None

HTML_FORMAT = read_file_to_string("models/prompts/html_format.txt")
REQUIREMENTS = read_file_to_string("models/prompts/requirments.txt")
USER_PROMPT = read_file_to_string("models/prompts/user_prompt.txt")


def get_prompt(document, database, language):
    prompt_template = ChatPromptTemplate([
        ("system", "You are a helpful report generator capable of creating reports in multiple languages."),
        ("user", USER_PROMPT)
    ])

    full_prompt = {
        "language": language,
        "htmlformat": HTML_FORMAT,
        "requirements": REQUIREMENTS,
        "database": database,
        "document": document,
    }

    return prompt_template, full_prompt

# Ultility functions


  
