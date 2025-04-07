from exchangelib import Credentials, Account, Message, Mailbox, HTMLBody
from exchangelib.configuration import Configuration

def send_email_via_exchange(
    username,
    password,
    email_from,
    email_to,
    subject,
    body,
    server='outlook.office365.com',
    use_html=False,
    cc_recipients=None,
    bcc_recipients=None,
    attachments=None
):
    """
    Send an email using Microsoft Exchange/Office 365.
    
    Args:
        username (str): Your Exchange username (usually your email)
        password (str): Your Exchange password
        email_from (str): Sender email address
        email_to (list): List of recipient email addresses
        subject (str): Email subject
        body (str): Email body content
        server (str): Exchange server URL (default: outlook.office365.com)
        use_html (bool): Whether to send as HTML (default: False)
        cc_recipients (list): List of CC email addresses (optional)
        bcc_recipients (list): List of BCC email addresses (optional)
        attachments (list): List of file paths to attach (optional)
    """
    # Set up credentials and configuration
    credentials = Credentials(username=username, password=password)
    config = Configuration(server=server, credentials=credentials)

    # Create account object
    account = Account(
        primary_smtp_address=email_from,
        config=config,
        autodiscover=False,
        access_type='delegate'
    )

    # Create the message
    message = Message(
        account=account,
        subject=subject,
        body=HTMLBody(body) if use_html else body,
        to_recipients=[Mailbox(email_address=email) for email in email_to]
    )

    # Add CC recipients if provided
    if cc_recipients:
        message.cc_recipients = [Mailbox(email_address=email) for email in cc_recipients]

    # Add BCC recipients if provided
    if bcc_recipients:
        message.bcc_recipients = [Mailbox(email_address=email) for email in bcc_recipients]

    # Add attachments if provided
    if attachments:
        for file_path in attachments:
            with open(file_path, 'rb') as f:
                file_content = f.read()
            message.attach(filename=file_path.split('/')[-1], content=file_content)

    # Send the message
    message.send()

    print("Email sent successfully!")

# Example usage
if __name__ == "__main__":
    # Replace these with your actual credentials and details
    YOUR_EMAIL = "your.email@example.com"
    YOUR_PASSWORD = "your_password"
    RECIPIENT_EMAIL = "recipient@example.com"
    
    send_email_via_exchange(
        username=YOUR_EMAIL,
        password=YOUR_PASSWORD,
        email_from=YOUR_EMAIL,
        email_to=[RECIPIENT_EMAIL],
        subject="Test Email from Python",
        body="<h1>Hello from Python!</h1><p>This is a test email.</p>",
        use_html=True,
        cc_recipients=["cc@example.com"],
        # bcc_recipients=["bcc@example.com"],
        # attachments=["/path/to/file.pdf"]
    )
