<<<<<<< HEAD
# feedback-bot-aiogram
Feedback bot written on Aiogram library
=======
# Feedback Bot (aiogram)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![aiogram](https://img.shields.io/badge/aiogram-3.20-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Telegram bot built with **aiogram 3.20** and **Tortoise ORM** 
to handle user feedback, supports all types of messages, 
and manage user bans.

## Features
- Supports all types of Telegram messages (text, images, etc.).
- Admin commands to ban/unban users.
- Flexible database support with Tortoise ORM (PostgreSQL, SQLite, etc.).
- Asynchronous architecture.
- Easy to extend with custom commands.

## Prerequisites
- Python 3.8 or higher
- Telegram Bot Token (from [@BotFather](https://t.me/BotFather))
- Your telegram ID (can find it in [@username_to_id_bot](https://t.me/username_to_id_bot))
- PostgreSQL or SQLite database

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/quvvii/feedback-bot-aiogram.git
   cd feedback-bot-aiogram
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Create a `.env` file in the project root with the following content:
   ```env
   TELEGRAM_BOT_TOKEN=
   TELEGRAM_ADMIN_ID=
   DATABASE_URL=sqlite://db.sqlite3 
   # For PostgreSQL: DATABASE_URL=postgresql://user:password@localhost:5432/dbname
   ```

## Usage
1. Run the bot locally:
   ```bash
   python -m tgbot
   ```
   
2. Available commands:

   **Admin Commands**:
   - `/start`: Pings the bot.
   - `[Reply to message]`: Sends a response to the user's question.
   - `/ban [user_id/reply]`: Bans a user from using the bot.
   - `/unban [user_id/reply]`: Unbans a user.

   **User Interaction**:
   - Users can send any type of message (text, images, etc.), which will be forwarded to the admin.
   - Admins can reply directly to user messages via the bot.


3. Screenshots:

   **User view**:

   ![User](https://i.ibb.co/23QTZ51Q/photo-2025-06-29-15-41-07-2.jpg)

   **Admin view**:

   ![Admin](https://i.ibb.co/twC0SXTm/photo-2025-06-29-15-41-23.jpg)

## License
This project is licensed under the [MIT License](LICENSE).
>>>>>>> 64727da (First commit)
