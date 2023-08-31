# modules/etherscan/models.py

class EthereumWallet:
    def __init__(self, address, balance, transactions=None):
        self.address = address  # The Ethereum wallet address.
        self.balance = balance  # Current balance of the wallet in Ether.
        self.transactions = transactions if transactions else []  # List of transactions associated with this wallet.

    def add_transaction(self, transaction):
        """
        Add a new transaction to the wallet's transaction history.
        """
        self.transactions.append(transaction)

    def get_balance_in_wei(self):
        """
        Convert and return the balance in Wei. (1 Ether = 10^18 Wei)
        """
        return self.balance * (10**18)

    def __repr__(self):
        return f"<EthereumWallet(address={self.address}, balance={self.balance} ETH)>"

class Transaction:
    def __init__(self, from_address, to_address, value, timestamp, txn_hash, status):
        self.from_address = from_address  # Sender's address.
        self.to_address = to_address  # Recipient's address.
        self.value = value  # Amount of Ether transferred in the transaction.
        self.timestamp = timestamp  # Timestamp of the transaction.
        self.txn_hash = txn_hash  # Unique transaction hash.
        self.status = status  # Status of the transaction (e.g., "success", "failed").

    def __repr__(self):
        return f"<Transaction(from={self.from_address}, to={self.to_address}, value={self.value} ETH, status={self.status})>"
