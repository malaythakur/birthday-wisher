from twilio.rest import Client
import pandas as pd
import datetime
import os

# Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_ACCOUNT_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')
twilio_whatsapp_number = os.getenv('TWILIO_WHATSAPP_NUMBER')

def send_whatsapp_message(to_number, message):
    try:
        # Ensure the 'whatsapp:' prefix is correctly applied
        from_number = f'whatsapp:{twilio_whatsapp_number}'
        to_number = f'whatsapp:{to_number}'
        
        client = Client(account_sid, auth_token)
        message_response = client.messages.create(
            body=message,
            from_=from_number,
            to=to_number
        )
        print(f"Message sent to {to_number}: {message_response.body}")
        print(f"Message SID: {message_response.sid}")
    except Exception as e:
        print(f"Failed to send message to {to_number}: {e}")


def check_birthdays():
    print("Checking birthdays...")

    try:
        friends_data = pd.read_csv('friends_data.csv')
        print(f"Data loaded: {friends_data}")
    except Exception as e:
        print(f"Error loading CSV file: {e}")
        return

    # Get today's date in MM-DD format
    today = datetime.datetime.now().strftime("%m-%d")
    print(f"Today's date: {today}")

    found_birthday = False

    for index, row in friends_data.iterrows():
        friend_birthday = row['Birthday']
        friend_name = row['Name']
        friend_phone = row['PhoneNumber']

        if friend_birthday == today:
            found_birthday = True
            print(f"Today is {friend_name}'s birthday.")
            message = f"Happy Birthday, {friend_name} Bhai! 🎉 Party Hardd 🍷❤️🫂 - Malay"
            send_whatsapp_message(friend_phone, message)
        else:
            print(f"No birthday for {friend_name} today.")

    if not found_birthday:
        print("No birthdays found for today.")

# Run the birthday check
check_birthdays()
