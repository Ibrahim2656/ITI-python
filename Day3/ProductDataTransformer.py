"""
4) Product Data Transformer (lambda, map, filter, zip)
   - Ask user for a list of product names (comma-separated).
   - Ask user for a list of product prices (comma-separated).
   - Process them by:
        - Pairing product with price.
        - Filtering out items where price <= 0.
        - Transforming each pair into a dictionary {"product": name, "price": price, "discounted": price * 0.9}.
   - Save the final result as JSON into "products.json".
   - Print a preview of the first 5 results.
"""

import json

def validate_names(user_input: str):
    names = [name.strip() for name in user_input.split(",") if name.strip()]
    return names if names else None

def validate_prices(user_input: str , expected_count:int):
    parts=[p.strip() for p in user_input.split(",")]
    if len(parts) != expected_count:
        return  None, f"You must enter exactly {expected_count} prices."
    
    prices=[]
    for i,p in enumerate(parts,1):
        try:
            prices.append(float(p))
        except ValueError:
            return None,f"Price #{i} ('{p}') is invalid!"
        
    
    return prices,None
    

def product_data_transformer():
    # Step 1: Get valid product names
    while True:
        names_input=input("Enter product names (comma-separated):")
        names= validate_names(names_input)
        if names is None:
            print("Invalid input! Enter at least one product name.")
        else:
            break
    # Step 2: Get valid product prices
    while True:
        prices_input=input("Enter product prices (comma-separated): ")
        prices,error=validate_prices(prices_input,len(names))
        if error:
            print(error)
        else:
            break
    
    # Step 3: Pair names and prices
    paired=list(zip(names,prices))
    
    # Step 4: Filter out items where price <= 0
    filtered = list(filter(lambda x:x[1] > 0,paired))
    
    # Step 5: Transform into dictionaries with discounted price
    transformed=list(map(lambda x:{
        "product":x[0],
        "price":x[1],
        "discounted": round(x[1] * 0.9, 2)
    },filtered))

    
    # Step 6: Save as JSON
    json_file="products.json"
    with open(json_file,"w") as f:
        json.dump(transformed,f,indent=4)
        
    # Step 7: Print preview of first 5 results
    print(f"✅ Product data saved into {json_file}. Preview (first 5 items):")
    for item in transformed[:5]:
        print(" ", item)
    

