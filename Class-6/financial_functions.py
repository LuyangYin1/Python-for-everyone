import yfinance as yf


def get_stock_data(ticker_symbol):
    """
    Retrieves financial stock data for a given ticker symbol using yfinance.

    Args:
        ticker_symbol (str): The ticker symbol of the stock (e.g., "AAPL", "GOOG").

    Returns:
        pandas.DataFrame: A DataFrame containing historical stock data,
                         or None if an error occurs.
    """
    try:
        stock = yf.Ticker(ticker_symbol)
        data = stock.history()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None


if __name__ == "__main__":
    symbol = "AAPL"  # Replace with the desired stock symbol
    stock_data = get_stock_data(symbol)

    if stock_data is not None:
        print(f"Stock data for {symbol}:")
        print(stock_data)
