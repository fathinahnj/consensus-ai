EDUCATION_LEVELS = {
    "PrimaryAndLower": {
        "ratio": 0.238,
        "cognitive_complexity": 0.30,
        "issue_based_reasoning": 0.30,
        "authority_deference": 0.70
    },
    "SecondaryLevel": {
        "ratio": 0.61,
        "cognitive_complexity": 0.50,
        "issue_based_reasoning": 0.50,
        "authority_deference": 0.50
    },
    "University": {
        "ratio": 0.148,
        "cognitive_complexity": 0.75,
        "issue_based_reasoning": 0.75,
        "authority_deference": 0.25
    }
}

def get_education_attributes(education_level: str) -> dict:
    return EDUCATION_LEVELS[education_level]