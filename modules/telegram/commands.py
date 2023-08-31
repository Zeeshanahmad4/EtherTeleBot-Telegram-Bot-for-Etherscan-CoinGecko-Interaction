# modules/telegram/commands.py

from modules.etherscan.api import get_wallet_data

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="🚀 EtherTeleBot Started! Type /monitor_wallet <your_wallet_address> to monitor a wallet.")

def monitor_wallet(update, context):
    if not context.args:
        context.bot.send_message(chat_id=update.effective_chat.id, text="❌ Please provide a wallet address. Usage: /monitor_wallet <your_wallet_address>")
        return

    wallet_address = context.args[0]
    data = get_wallet_data(wallet_address)
    
    if 'result' in data:
        balance_in_ether = int(data['result']) / (10**18)
        response_message = f"💼 Wallet: {wallet_address}\n💰 Balance: {balance_in_ether:.4f} ETH"
    else:
        response_message = "❌ Error fetching data. Ensure the provided wallet address is correct."

    context.bot.send_message(chat_id=update.effective_chat.id, text=response_message)

