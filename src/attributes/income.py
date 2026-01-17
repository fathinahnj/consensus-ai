INCOME_LEVELS = {
    "Poor": {
        "ratio": 0.233,
        "economic_anxiety": 0.78,
        "welfare_salience": 0.80,
        "status_quo_bias": 0.25
    },
    "Vulnerable": {
        "ratio": 0.536,
        "economic_anxiety": 0.65,
        "welfare_salience": 0.68,
        "status_quo_bias": 0.40
    },
    "MiddleUpper": {
        "ratio": 0.139,
        "economic_anxiety": 0.35,
        "welfare_salience": 0.42,
        "status_quo_bias": 0.65
    }
}

def get_income_attributes(income_level: str) -> dict:
  if income_level not in INCOME_LEVELS:
    raise ValueError(f"Unknown income level \"{income_level}\"")
    return INCOME_LEVELS[income_level]