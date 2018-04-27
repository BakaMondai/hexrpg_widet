import ticket_parser as tp
import config

def main():
    stock = tp.stock_access(config.payload)
    tp.parse_data(stock)
