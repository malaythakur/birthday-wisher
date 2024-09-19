from twilio.rest import Client
import pandas as pd
import datetime
import os

# Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

# Send WhatsApp message function
def send_whatsapp_message(to_number, message):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=twilio_whatsapp_number,
        to=f'whatsapp:+{to_number}'
    )
    print(f"Message sent to {to_number}: {message.body}")

# Checks birthdays and sends WhatsApp messages
def check_birthdays():
    # Load data from CSV file
    friends_data = pd.read_csv('friends_data.csv')

    # Get today's date in MM-DD format
    today = datetime.datetime.now().strftime("%m-%d")

    # Iterate over the rows in the CSV file
    for index, row in friends_data.iterrows():
        friend_birthday = row['Birthday']
        friend_name = row['Name']
        friend_phone = row['PhoneNumber']

        # Check if today is the friend's birthday
        if friend_birthday == today:
            # Create the birthday message
            message = f"Happy Birthday, {friend_name} Bhai! 🎉 Party Hardd 🍷❤️🫂 - Malay"
            # Send WhatsApp message
            send_whatsapp_message(friend_phone, message)

# Run the birthday check
check_birthdays()
