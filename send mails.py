import smtplib as s  # Import the smtplib library to handle email sending
ob = s.SMTP("smtp.gmail.com", 587)  # Establish connection to Gmail's SMTP server using port 587
ob.ehlo()  # Identify the client to the server (SMTP handshake)
ob.starttls()  # Start TLS encryption for security
ob.login("trishlaverma2004@gmail.com", "Write Your App Password")  # Login to the Gmail account (replace with a valid app password for security)

# Defining email subject and body
subject = "test python"  
body = "this is a mail for test python code"

# Format the email message with subject and body
message = "subject: {}\n\n{}".format(subject, body)

# List of email recipients
listadd = ["trishalavermahtn@gmail.com", "khushi0308htn@gmail.com", "anilrayhtn12@gmail.com"]

# Send the email to the recipient list
ob.sendmail("trishlaverma2004@gmail.com", listadd, message)

print("mail sent")  # Confirmation that the email has been sent

ob.quit()  # Close the SMTP connection


