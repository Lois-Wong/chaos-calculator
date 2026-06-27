def calc_bac(alcohol_grams: float, weight_lb: float, sex: str):
    # BAC calculation based on the Widmark formula
    if sex == "male":
        r = 0.73
    elif sex == "female":
        r = 0.66
    else:
        raise ValueError("Invalid sex. Please specify 'male' or 'female'.")
    
    # calculate BAC
    # change alcohol grams to oz 
    alcohol_oz = alcohol_grams / 28.35
    bac = (alcohol_oz * 5.14) / (weight_lb * r) 

    return bac 


def calc_chaos_score(bac: float, caffeine_mg: float, sugar_g: float):
    if bac < 0.02:
        chaos_score = 0
    elif bac >= 0.02 and bac < 0.05:
        chaos_score = 1
    elif bac >= 0.05 and bac < 0.08:
        chaos_score = 2
    elif bac >= 0.08 and bac < 0.12:
        chaos_score = 3
    elif bac >= 0.12 and bac < 0.16:
        chaos_score = 4
    elif bac >= 0.16 and bac < 0.20:
        chaos_score = 5
    elif bac >= 0.20 and bac < 0.30:
        chaos_score = 6
    elif bac >= 0.30:
        chaos_score = 7 # danger zone

    return chaos_score
