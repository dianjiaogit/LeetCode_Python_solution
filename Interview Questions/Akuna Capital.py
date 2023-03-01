# 1. Matching Engine

# Overview

 

# A matching engine is used by modern exchanges to match orders from market participants.

# An order is a simple request / offer to buy / sell something.

 

# I.E, if this was a fish market

# Someone may announce:

# "I will buy 5 fish, willing to pay up to $10 per fish"

# Someone else, less eager to buy fish may announce:

# "I will buy 5 fish, willing to pay up to $9 per fish"

# Finally, someone else, looking to sell fish:

# "I will sell 10 fish, for at least $8 per fish"

 

# The seller will first sell 5 fish to the buyer paying $10 per fish, then the next 5 to the buyer paying $9 per fish.

 

# In the event where 2 buyers offer the same amount of money for a fish, the buyer who offered first gets their fish first.

# This is known as price-time priority, where we first match according to price (sellers offering the lowest price, buyers offering the highest price), and then time (participants who offered first).

 

# Spec

 

# Orders will be delivered by the method new_order, defined in the scaffold below.

# It takes 4 parameters:

# is_buy: bool, denotes whether the order is a buy or a sell.

# price: int, the maximum / minimum price the participant is willing to buy / sell for.

# quantity: int, the quantity the participant is willing to buy / sell.

# id: str, a unique identifier for this order. This may be used to amend / cancel this order in the future.

 

# Once an order is in the market, 2 operations may be performed on it

# Cancel

# Relatively straightforward, removes an order from the matching engine.

# Note that an order may have already been partially or fully traded away.

# Modify

#  Changes an existing order's characteristics.

# All Charactersitics of an order may change, can change from a buy to a sell, price can change, qty can change.

# Even if a modify order does not actually modify an order, it still loses its time priority.

# This means if there are other orders with the same price, it is moved to the back of the queue.

 

# Cancel recieves 1 parameter:

# id: str, the unique identifier to remove.

# Modify recieves 4 parameters 

# id: str, a unique identifier to modify.

#  is_buy: bool, denotes whether the order is a buy or a sell.

# price: int, the maximum / minimum price the participant is willing to buy / sell for.

# quantity: int, the quantity the participant is willing to buy / sell.

 

# Note: for both of these, if there is no order with the specified id in the market (either never existed, was traded, or cancelled), the operation should be ignored.

 

# Output

 

# New Order

# When a new order is inserted, log the below:

# "INSERT {BUY | SELL} {NEW ORDER ID} {PRICE} {QUANTITY}"

 

# Note: We only log the quantity that remains after all trades may have occured.

# This means if, (continuing with the above fish market analogy) someone is willing to sell 5 fish for $8 & we are buying 8 fish for up to $10, we would first trade 5 of those fish, leaving 3 fish afterwards.

# In the event where no quantity remains after trades, no insertion should occur, so we shouldn't log one.

 

# Trade

# Following on from insertions, whenever a trade occurs, log it in this form:

# "TRADE {NEW ORDER ID} {OLD ORDER ID} {PRICE} {QUANTITY}" 

# Here, {NEW ORDER ID} refers to the id of the order that was just inserted. {OLD ORDER ID} refers to the id of the order that was already sitting in the market.

# {PRICE} Refers to the price the trade actually occured at, which is the price of the old order. In the example under inserts, we would log a price of $8.

# {QUANTITY} Refers to the quantity that traded in this trade. This will be the lesser of the quantity available from the old order & the quantity the new order is willing to buy. 

# In the insert example, the quantity that traded here would be 5.

 

# Cancel

# When an order is cancelled, log this:

# "CANCEL {ORDER ID} {QUANTITY}"

# Where {ORDER ID} is the id of the order being cancelled and {QUANTITY} is the remaining quantity of this order.

 

# Modify

# When an order is modified, log it as though it was cancelled and inserted afresh.

# This also includes any potential trades that may occur as a result of this new insertion.

 

# Implementation Notes

 

# Your code will be reviewed by a developer at akuna.

# Please keep your code neat and easily understandable.

# This doesn't mean your styling needs to be immaculate, just needs to be able to be easily understood by someone else.

# Note the worst case time complexity of each method in a comment (either above the method or at the bottom of your code).

# Include a short, 1 sentence explanation.

# There will never be an order with a price < 0 or > 100.

# You may use this to improve your code, but make a note of where you are using this assumption & calculate your time complexity as though you could have unlimited levels.

# You may assume all inputs are well formed, you do not need to handle cases where invalid inputs may be given.

# Do all of your development inside hackerrank - do not use an external editor.



from sys import stdin


class Engine:
    def __init__(self):
        self.seller_by_id = {}
        self.buyer_by_id = {}
        self.seller_by_price = {}
        self.buyer_by_price = {}

    def new_order(self, is_buy: bool, price: int, quantity: int, id: str):
        # Worst case time complexity is O(n)
        if is_buy:
            seller_prices = list(self.seller_by_price.keys())
            seller_prices.sort()
            for seller_price in seller_prices:
                if seller_price <= price:
                    for seller_id in self.seller_by_price[seller_price]:
                        seller_quantity = self.seller_by_price[seller_price][seller_id]
                        quantity_change = min(quantity, seller_quantity)
                        self.seller_by_price[seller_price][seller_id] -= seller_quantity - quantity_change
                        print(f"TRADE {id} {seller_id} {seller_price} {quantity_change}")
                        quantity = quantity - quantity_change
                        if quantity == 0:
                            return 0
            self.buyer_by_id[id] = [price, quantity]
            if price in self.buyer_by_price:
                self.buyer_by_price[price][id] = quantity
            else:
                self.buyer_by_price[price] = {id: quantity}
            print(f"INSERT BUY {id} {price} {quantity}")
        else:
            buyer_prices = list(self.buyer_by_price.keys())
            buyer_prices.sort()
            buyer_prices = buyer_prices[::-1]
            for buyer_price in buyer_prices:
                if buyer_price >= price:
                    for buyer_id in self.buyer_by_price[buyer_price]:
                        buyer_quantity = self.buyer_by_price[buyer_price][buyer_id]
                        quantity_change = min(quantity, buyer_quantity)
                        self.buyer_by_price[buyer_price][buyer_id] -= buyer_quantity - quantity_change
                        print(f"TRADE {id} {buyer_id} {buyer_price} {quantity_change}")
                        quantity = quantity - quantity_change
                        if quantity == 0:
                            return 0
            self.seller_by_id[id] = [price, quantity]
            if price in self.seller_by_price:
                self.seller_by_price[price][id] = quantity
            else:
                self.seller_by_price[price] = {id: quantity}
            print(f"INSERT SELL {id} {price} {quantity}")
            
            
    def modify(self, id: str, is_buy: bool, price: int, quantity: int):
        # Worst case time complexity is O(n)
        if id in self.buyer_by_id or id in self.seller_by_id:
            self.cancel(id)
            self.new_order(is_buy, price, quantity, id)
                

    def cancel(self, id: str):
        # Worst case time complexity is O(1)
        if id in self.buyer_by_id:
            price, quantity = self.buyer_by_id[id]
            self.buyer_by_id.pop(id)
            self.buyer_by_price[price].pop(id)
            print(f"CANCEL {id} {quantity}")
        elif id in self.seller_by_id:
            price, quantity = self.seller_by_id[id]
            self.seller_by_id.pop(id)
            self.seller_by_price[price].pop(id)
            print(f"CANCEL {id} {quantity}")
        

engine = Engine()
for msg in stdin:
    tokens = msg.split(" ")
    if tokens[0] in ["BUY", "SELL"]:
        engine.new_order(tokens[0] == "BUY", int(tokens[1]), int(tokens[2]), tokens[3].rstrip())
    elif tokens[0] == "MODIFY":
        engine.modify(tokens[1], tokens[2] == "BUY", int(tokens[3]), int(tokens[4]))
    elif tokens[0] == "CANCEL":
        engine.cancel(tokens[1].rstrip())