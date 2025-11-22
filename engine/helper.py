


import re


def extract_yt_term(command):
    # Define regular expression to capture song name
    pattern= r'play\s+(.*?)\s+on\s+youtube'
    # Use research to find match in command
    match= re.search(pattern,command,re.IGNORECASE)

    return match.group(1) if match else None 