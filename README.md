# Discord Bot Project

## Description
This project is a Discord bot developed using Python. It integrates with MongoDB for data storage. The bot includes various commands to manage job applications, including adding, displaying, and (soon)updating job statuses. This is intended for your own private discord server, use in a public one at your own risk. 


### Prerequisites
- Python 3.8 or higher
- pip (Python package installer)

## Installation Steps
1. Clone the repository:
    git clone https://github.com/reddynamo/discord-bot.git
    cd discord-bot

2. Create and activate a virtual environment:
    -On Windows
    python -m venv venv
    venv\Scripts\activate

    -On macOS/Linux
    python3 -m venv venv
    source venv/bin/activate

3. Install the dependencies:
    pip install -r requirements.txt

4. Create a `.env` file:
    cp .env.example .env

5. Fill in the `.env` file with your own values:
    
    DISCORD_TOKEN=your_discord_token_here
    YOUR_USER_ID=your_user_id_here
    MONGODB_URI=your_mongodb_uri_here
    

## Usage
1. Run the bot:
    python main.py
    
2. Interacting with the bot:
    Use the commands defined in the bot to manage job applications in your discord server.

