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

