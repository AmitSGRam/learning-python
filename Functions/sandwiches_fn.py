def order_sandwiches(quantity, *items):
    print(f"\nMaking {quantity} sandwich(es) with the following items:")
    for item in items:
        print(f"\t{item}")

order_sandwiches(5, "cheese burst")
order_sandwiches(3, "grilled chicken","big mac")
order_sandwiches(1, "pork","cheese", "onion")