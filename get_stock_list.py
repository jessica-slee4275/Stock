    
import yfinance as yf
import pandas as pd

def get_sp500_list():
    # Use Wikipedia's S&P 500 page as a source
    url = "https://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
    sp500_table = pd.read_html(url)[0]
    return sp500_table["Symbol"].tolist()

# Fetch stock info for a list of tickers
def fetch_stock_data(tickers):
    data = []
    for ticker in tickers:
        try:
            stock = yf.Ticker(ticker)
            info = stock.info
            data.append({
                "Ticker": ticker,
                "Company": info.get("longName", "N/A"),
                "Market Cap": info.get("marketCap", 0),
                "Dividend Yield": info.get("dividendYield", 0) * 100  # Convert to percentage
            })
        except Exception as e:
            print(f"Error fetching data for {ticker}: {e}")
    return pd.DataFrame(data)
    
# Get the list of S&P 500 tickers    
sp500_tickers = get_sp500_list()
print(f"Retrieved {len(sp500_tickers)} S&P 500 tickers.")

# Fetch stock data
stock_data = fetch_stock_data(sp500_tickers)

# Filter and sort top 10 by market cap
top_market_cap = stock_data.nlargest(10, "Market Cap")[["Ticker", "Company", "Market Cap"]]
print("\nTop 10 Companies by Market Cap")
print(top_market_cap)

# Filter and sort top 10 by dividend yield
top_dividend_yield = stock_data.nlargest(10, "Dividend Yield")[["Ticker", "Company", "Dividend Yield"]]
print("\nTop 10 Companies by Dividend Yield")
print(top_dividend_yield)