from bokeh.plotting import figure, show, output_file
from bokeh.models import ColumnDataSource, HoverTool
import yfinance as yf
import pandas as pd

def plot_dividend_with_hover(ticker_symbol):
    # Fetch stock data
    stock = yf.Ticker(ticker_symbol)
    dividends = stock.dividends

    if dividends.empty:
        print(f"No dividend history available for {ticker_symbol}.")
        return

    # Prepare data
    dividends_df = dividends.reset_index()
    dividends_df.columns = ["Date", "Dividend"]
    source = ColumnDataSource(dividends_df)

    # Set up output file
    output_file(f"dividend_history-{ticker_symbol}.html")

    # Create a Bokeh figure
    p = figure(
        title=f"Dividend History for {ticker_symbol}",
        x_axis_type="datetime",
        width=800,
        height=400  
    )

    # Add line
    p.line(x="Date", y="Dividend", source=source, line_width=2, legend_label="Dividend")

    # Add hover tool
    hover = HoverTool(
        tooltips=[
            ("Date", "@Date{%F}"),
            ("Dividend", "@Dividend{0.00}%")
        ],
        formatters={
            "@Date": "datetime"
        },
        mode="vline"
    )
    p.add_tools(hover)

    # Customize the plot
    p.xaxis.axis_label = "Date"
    p.yaxis.axis_label = "Dividend Amount"
    p.legend.location = "top_left"

    # Show the plot
    show(p)

plot_dividend_with_hover("MSFT")
