import yfinance as yf
import pandas as pd
import pandas_datareader as pdr
import plotly.graph_objects as go
from datetime import datetime
from pandas_datareader import data as pdrd
from pandas_datareader._utils import RemoteDataError
from pandas_datareader.data import Options
from datetime import timedelta
import plotly.offline as plo
import plotly.io as pio
pio.renderers.default = 'browser'
import kaleido
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import argparse as argparse

parser = argparse.ArgumentParser(prog="Artic Fox Indicators & Backtesting", description="An app for your web browser that allows you to try out and backtest different trading strategies.", epilog="If you know your yesterday, your tomorrow is stronger.")
parser.add_argument('--symbol', help="The name of the symbol you wish to pull up and analyze.")
parser.add_argument('--daterange', help="The range of time that your backtesting will be across two dates separated by a hyphen format: MM/DD/YYYY.", required = True)
"""
parser.add_argument('strategy',help="The strategy that the user selects from a set of...") #TODO: enter varients and the designations
parser.add_argument('indicators', help="A binary number that corresponds to which indicators to add.")
"""
args = parser.parse_args()
symbol = args.symbol
if(symbol == None):
    #TODO: finish the section that tests the exception cases for the symbols provided
    exit(0) 
"""try("sneed"):
                   #TODO: test except for symbol being listed on NYSE and/or NASDAQ
    return 0
except:
    return "Bollucks"
"""
if(args.daterange == None):
    #TODO: finish test and except
    exit(0)
"""
if(args.strategy == None):
    #TODO: finish the test and except
    exit(0)
"""

daterange = args.daterange.split("-")
print(daterange)
st = datetime.strptime(daterange[0], '%m/%d/%Y')
en = datetime.strptime(daterange[1], '%m/%d/%Y')
print(daterange)
def chartData(symbol, chart):
    image_output_path = "temp.png"
    c = canvas.Canvas(f"{symbol} Report")
    c.setTitle(f"{symbol} Price Action")
    chart.write_image(image_output_path)
    c.drawImage(image_output_path,x=-20, y=250)
    c.save()

stockData = pdr.DataReader(symbol, 'stooq', st, en)
yearlyHigh = 0
yearlyLow = stockData.High.values[0]
for y in range(len(stockData)):
    if(stockData.High.values[y] > yearlyHigh):
        yearlyHigh = float(stockData.High.values[y])
    elif(stockData.Low.values[y] < yearlyLow):
        yearlyLow = float(stockData.Low.values[y])
diffYearly = yearlyHigh-yearlyLow

# Reset index to make 'Date' a column
stockData.reset_index(inplace=True)

# Create candlestick chart
graph = go.Figure(data=[go.Candlestick(x=stockData['Date'],
                                    open=stockData['Open'],
                                    high=stockData['High'],
                                    low=stockData['Low'],
                                    close=stockData['Close'])])
# Update layout
graph.update_layout(
        title=f"{symbol} Stock Price Movement",
        xaxis_rangeslider_visible=False,
        xaxis_title="Date Range",
        yaxis_title="Price",
        
)
image_output_path = "temp_plot.png"
pio.write_image(graph, image_output_path)


