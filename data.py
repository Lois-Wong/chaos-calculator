# alcohol_contentt : abv
# alcohol_grams : grams of alcohol in the drink
# sugar : grams 
# caffeine : mg 

# each key is 1 drink 

drinks = [
    {"name": "beer", "alcohol_content": 5.0, "alcohol_grams": 14.0, "sugar": 0.0, "caffeine": 0.0},
    {"name": "red_wine", "alcohol_content": 13.0, "alcohol_grams": 19.5,"sugar": 1.0, "caffeine": 0.0},
    {"name": "white_wine", "alcohol_content": 11.0, "alcohol_grams": 16.5, "sugar": 1.4, "caffeine": 0.0},
    {"name": "gin", "alcohol_content": 46.0, "alcohol_grams": 20.24, "sugar": 0.0, "caffeine": 0.0},
    {"name": "vodka", "alcohol_content": 40.0, "alcohol_grams": 17.6, "sugar": 0.0, "caffeine": 0.0},
    {"name": "hugo_spritz", "alcohol_content": 9.0, "alcohol_grams": 12.5, "sugar": 11.0, "caffeine": 0.0},
    {"name": "aperol_spritz", "alcohol_content": 9.0, "alcohol_grams": 12.5, "sugar": 13.0, "caffeine": 0.0},
    {"name": "espresso", "alcohol_content": 0.0, "alcohol_grams": 0.0, "sugar": 0.0, "caffeine": 64.0},  
] 

# index is the chaos schore; stages[0] is nothing 
stages = [
    {"name": "nothing here", "description": "No chaos detected."},
    {"name": "eh", "description": "Bare minimum chaos detected."},
    {"name": "happiness has entered the chat", "description": "Moderate chaos detected :)."},
    {"name": "let's goooo", "description": "Chaotic happiness has entered the chat"},
    {"name": "chaos mode activated", "description": "Approaching diminishing returns."},
    {"name": "going to regret this tomorrow", "description": "Past diminishing returns"},
    {"name": "ultimate chaos mode activated", "description": "Maximum chaos detected - time to get water :)"},
    {"name": "danger zone", "description": "Too much chaos"}
]