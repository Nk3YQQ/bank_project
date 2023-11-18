from src.logger import setup_logger
from src.masks import mask_card, mask_count
from src.utils import get_transaction_on_rub, get_transactions

logger = setup_logger()

if __name__ == "__main__":
    mask_card("4000001234567899")
    mask_count("40817810099910004312")

    transactions = get_transactions("../data/operations.json")
    amount_in_rub = get_transaction_on_rub(transactions[0])
