import random

# Predefined lists of daily support messages
morning_messages = [
    "Good morning, love! Just reminding you that you’re amazing and capable of anything today. ❤️",
    "Morning, Fish! 🐟 I hope your day is as beautiful as your smile. 😊",
    "Good morning, my Smallie! Remember, you’ve got this, and I’m here for you always. 🌞",
    "Rise and shine, Witch! 🧙‍♀️ Let today be filled with happiness and laughter. ❤️",
]

afternoon_messages = [
    "Hey love, just checking in! Hope your day’s going well. Remember, I’m here for you anytime. ❤️",
    "Hi Smallie! 🐠 Just a little reminder that you’re doing great today. Keep shining! 🌟",
    "Hello, my amazing Witch! 🧙‍♀️ Sending you love and hugs to brighten your afternoon. ❤️",
    "Hey Fish! 🐟 Take a deep breath and remember you’re strong and incredible. 😊",
]

night_messages = [
    "Good night, my love. Rest well, and don’t forget I’m always here for you. Sweet dreams! ❤️",
    "Good night, Smallie! 🐠 May your dreams be as wonderful as you are. Sleep tight! 🌙",
    "Sleep well, my beautiful Witch! 🧙‍♀️ Tomorrow is a new day, and I’ll be right here for you. ❤️",
    "Good night, Fish! 🐟 Remember, you’re loved, and I’m always thinking of you. 💤",
]

# Function to generate a message
def generate_message(time_of_day):
    if time_of_day == "morning":
        return random.choice(morning_messages)
    elif time_of_day == "afternoon":
        return random.choice(afternoon_messages)
    elif time_of_day == "night":
        return random.choice(night_messages)
    else:
        return "Hello, love! Just wanted to let you know you’re amazing. ❤️"

# Example usage
time_of_day = input("Enter the time of day (morning, afternoon, night): ").strip().lower()
message = generate_message(time_of_day)
print("\nYour message:")
print(message)
