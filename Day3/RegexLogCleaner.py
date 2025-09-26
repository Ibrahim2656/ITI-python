"""
2) Regex Log Cleaner
   - Create a file called "access.log" with 10 fake log lines
     (mix valid emails and invalid strings).
   - Use regex to extract all valid emails.
   - Save them into "valid_emails.txt".
   - Print how many unique emails were found.
"""

import re
import os
from DecoratorsTask import log_time


@log_time
def regex_log_cleaner():
    log_filename="access.log"
    if not os.path.exists(log_filename):
        fake_logs = [
        "User login: john.doe@example.com",
        "Invalid entry: @nope.com",
        "Another email: alice99@mail.org",
        "Broken string: hello@@test",
        "Contact: bob_smith@company.co.uk",
        "Random text without email",
        "Signup: test.user123@gmail.com",
        "Garbage: !!!@@##",
        "Reach me at: sarah.connor@skynet.net",
        "weird but valid: my-email+test@domain.io"
    ]
        with open(log_filename,"w") as f:
            for line in fake_logs:
                f.write(line+"\n")
                
    with open(log_filename,"r") as f:
        logs=f.read()
    
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    emails=re.findall(email_pattern,logs)
    
    unique_emails = sorted(set(emails))
    
    vaild_file="valid_emails.txt"
    
    with open(vaild_file,"w") as f :
        for email in unique_emails:
            f.write(email+"\n")
    
    print("\n Regex log Cleaner Finished.")
    print(f"Found {len(unique_emails)} unique valid emails.")
    print(f"Saved into {vaild_file}\n")
    print("Extracted Emails:")
    for email in unique_emails:
        print(" -",email)