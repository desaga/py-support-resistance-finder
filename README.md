# py-support-resistance-finder

Here's a Python script using the **yfinance** and **pandas** libraries to identify support and resistance levels over one year.
The script will download historical stock price data, calculate the support and resistance levels, and plot them.

1. **Local Minima and Maxima:** The script uses **argrelextrema** from **scipy.signal** to find local minima and maxima, which helps identify significant peaks and troughs.
2. **Filter Close Levels:** The script ensures that detected levels are not too close to each other by checking the minimum distance between levels.
3. **Filter Based on Distance:** The script filters the levels further based on a minimum percentage distance between them to keep only the most significant ones.

This approach helps reduce unimportant levels and retain only the significant support and resistance levels.
Adjust the **window** and **distance** parameters to fine-tune the sensitivity and filtering of levels.

### **window**
The window parameter defines the number of periods to look for local minima and maxima. A reasonable range for this parameter depends on the time frame of your analysis:

_Short-term analysis_ (e.g., intraday, daily): A smaller window (e.g., 5 to 20 periods) is appropriate.
_Medium-term analysis_ (e.g., weekly, monthly): A moderate window (e.g., 20 to 50 periods) is suitable.
_Long-term analysis_ (e.g., yearly): A larger window (e.g., 50 to 100 periods) might be more effective.
A typical value for a one-year daily analysis might be around 20 to 50 periods.

### **distance**
The distance parameter defines the minimum percentage distance between support and resistance levels to filter out closely spaced levels. A reasonable range for this parameter also depends on the volatility of the stock and the time frame:

_Low volatility stocks:_ A smaller distance (e.g., 0.5% to 1%) might be appropriate.
_High volatility stocks:_ A larger distance (e.g., 1% to 3%) might be necessary.
For a one-year daily analysis, a distance of around 1% to 2% is often reasonable.

_Example Reasonable Values
Short-term analysis: window = 10, distance = 0.01 (1%)
Medium-term analysis: window = 20, distance = 0.02 (2%)
Long-term analysis: window = 50, distance = 0.03 (3%)_

### **ticker**
You can change the **ticker** variable to the desired stock symbol.
