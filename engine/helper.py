import re


def extract_yt_term(command):
    # Define regular expression to capture song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    # Use research to find match in command
    match= re.search(pattern,command,re.IGNORECASE)

    return match.group(1) if match else None 


def remove_words(input_string, words_to_remove):
    # split input string to words
    words= input_string.split()

    # removbe unwanted words
    filtered_words= [word for word in words if word.lower() not in words_to_remove]

    # join words in string
    result_string= ' '.join(filtered_words)

    return result_string
