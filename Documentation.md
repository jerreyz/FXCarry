# FXCarry

# Futures Carry

## A. Contracts 

- EURODOLLAR [ED]

>How the Eurodollar futures contract works
For example, if on a particular day an investor buys a single three-month contract at 95.00 (implied settlement LIBOR of 5.00%):
> - if at the close of business on that day, the contract price has risen to 95.01 (implying a LIBOR decrease to 4.99%), US\$25 will be paid into the investor's margin account;
> - if at the close of business on that day, the contract price has fallen to 94.99 (implying a LIBOR increase to 5.01\%), US$25 will be deducted from the investor's margin account.  
> - On the settlement date, the settlement price is determined by the actual LIBOR fixing for that day rather than a market-determined contract price.
> - contract is cash settled

- The Euro/US dollar (EUR/USD) futures contract
> - EURUSD 125000 notional [EC]
> - EURO FX E-mini EURUSD 62500 notional [EE]
> - E-micro EURUSD  12500 notional[EU]

- S&P 500 [ES]
> - Cash settled
> - $50 x S&P 500 Index



## B. Continuous Futures contracts

1.  __Panama method__

This method alleviates the "gap" across multiple contracts by shifting each contract such that the individual deliveries join in a smooth manner to the adjacent contracts. Thus the open/close across the prior contracts at expiry matches up.

- Forwards panama canal method, aka first-true method
>  Shift successive contracts up or down by a constant amount so as to eliminate jumps, working forwards from the oldest contract in your history. The price of the oldest contract will therefore be "true"; all others will be adjusted.

- Backwards panama canal method,aka last-true method.   
> Shift successive contracts up or down by a constant amount so as to eliminate jumps, working backwards from the current contract. The price of the current continuous contract will be "true" and match market prices; however, you will need to recalculate your entire history on every roll date, which may be impractical.

The key problem with the Panama method includes the introduction of a trend bias, which will introduce a large drift to the prices.
This can lead to negative data for sufficiently historical contracts. In addition there is a loss of the relative price differences due to an absolute shift in values.  

2. __Backwards Ratio __
> Instead of shifting contracts up or down, in this method we multiply contracts by a constant factor so as to eliminate jumps, working backwards from the current contract. As with the backwards panama canal method, this method necessitates full historical recalculation on every roll date.

### Which roll date and price adjustment should I use?


- If you are using continuous contracts for economic forecasting or regression, you should use "first day of month" as your roll date rule, and "calendar-weighted rolling" as your price adjustment rule. These two choices are perfectly deterministic, predictable, and smooth; furthermore they do not contaminate any economic aspects of the price history.

- If you are using continuous contracts for chart-based technical analysis, you should use "open interest switch" as your roll date rule. Technical analysis depends on finding patterns in trader group dynamics, and hence a popularity-based roll measure is appropriate. For your price adjustment rule, you can use either "backwards panama" with a linear y-axis, or "backwards ratio" with a logarithmic y-axis, depending on your preferred flavor of technical analysis. (Although some traders claim that "unadjusted" prices are more appropriate, since they correspond more closely with psychological perceptions of support, resistance etc.)

- If you are using continuous contracts for back-testing trading strategies, you should use a roll date rule that corresponds exactly to your trading strategy. If you always roll on the expiry date, use "last trading day". If you always roll on the first of the month, use "first day of month". If you roll when everybody else rolls (for benchmarking or liquidity reasons), use "open interest switch". As for prices: if you trade based on a constant number of contracts, you should use "backwards Panama" as your price adjustment rule. If you trade based on a constant value of the underlying commodity, you should use "backwards ratio" for your price adjustment rule, and be sure to calculate PL using relative (percentage) changes not absolute (price) changes.

- For example, sophisticated technical traders often use open-interest-switch-roll and unadjusted-prices (code: 'ON') in order to make buy/sell decisions; this splicing method combines maximum liquidity with accurate nominal prices, and thus matches well with mass psychology. But when it comes to back-testing their buy/sell decisions, they use first-of-month-roll and calendar-weighted-prices, since that gives the most accurate, unbiased estimate of historical PL. So the same spreadsheet or backtester can in fact incorporate different roll/price rules, depending on where they're being used. This kind of advanced analysis is simply not possible without the SCF database, unless you're willing to invest huge amounts of time to build your own custom histories.

Here are some examples of what not to do. If you're trading Fed Funds or Eurodollar futures, an open-interest-switch rule is inappropriate, because most of the "action" is in the back contracts. If you're back-testing a trading strategy, you should not use unadjusted prices, because that will introduce artifical PL from roll date jumps. If you're trading a commodity with heavy contango or backwardation, you should not use Panama canal shifts, because they will lead to negative prices. If you're trading equities or currencies, you should never look at the #2 or #3 contracts, because they are utterly illiquid. And so on.


## B. Futures Roll Yield 

$$F_t RollYield = R_t_{F_{t,T}}$$
