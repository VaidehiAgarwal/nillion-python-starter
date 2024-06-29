from nada_dsl import *

def secure_auction_system():
    # Define parties
    auctioneer = Party(name="Auctioneer")
    bidder1 = Party(name="Bidder1")
    bidder2 = Party(name="Bidder2")
    
    # Input bids from each bidder (using SecretInteger)
    bid1 = SecretInteger(Input(name="bid1", party=bidder1))
    bid2 = SecretInteger(Input(name="bid2", party=bidder2))
    
    # Compute the maximum bid
    max_bid = bid1.max(bid2)
    
    # Determine the winning bidder
    winner = If(max_bid == bid1, "Bidder1",
                Else("Bidder2"))
    
    # Return results as outputs
    return [
        Output(max_bid, "max_bid", party=auctioneer),
        Output(winner, "winner", party=auctioneer)
    ]
