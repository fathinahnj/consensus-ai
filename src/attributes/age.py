AGE_GROUPS = {
    "GenZ": {
        "ratio": 0.2494,
        "digital_exposure": 0.48
    },
    "Millennial": {
        "ratio": 0.3344,
        "digital_exposure": 0.40
    },
    "GenX": {
        "ratio": 0.2705,
        "digital_exposure": 0.32
    },
    "Boomer": {
        "ratio": 0.1308,
        "digital_exposure": 0.22
    },
    "PreBoomer": {
        "ratio": 0.0149,
        "digital_exposure": 0.12
    }
}

def get_age_attributes(age_group: str) -> dict:
    if age_group not in AGE_GROUPS:
        raise ValueError(f"Unknown age group \"{age_group}\"")
    
    return AGE_GROUPS[age_group]