from telegram_bot import app
app=app
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=False, port=5000)