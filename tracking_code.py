import yfinance as yf

energy = ['XOM', 'PBR', 'ET', 'CVX', 'CLR']
finan = ['BAC', 'MS', 'C', 'MA', 'JPM', 'V']
rstate = ['PLD', 'WELL', 'EQR', 'SBAC', 'O', 'VTR']
tech = ['STX', 'FTV', 'HPQ', 'XRX', 'AMD']
hcare = ['WBA', 'PFE', 'CNC', 'INCY', 'TFX']
mat = ['ECL', 'VALE', 'GOLD', 'MT', 'SUZ']
indus = ['GE', 'ABB', 'CSX', 'EMR', 'DAL']

period = "1d"

data = yf.download(energy, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('energyfund.csv')

data = yf.download(finan, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('financefund.csv')

data = yf.download(rstate, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('realestatefund.csv')

data = yf.download(tech, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('technologyfund.csv')

data = yf.download(hcare, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('healthcarefund.csv')

data = yf.download(mat, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('materialsfund.csv')

data = yf.download(indus, period=period, group_by="ticker", auto_adjust = True)
data.to_csv('industrialfund.csv')