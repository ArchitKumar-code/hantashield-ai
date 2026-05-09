def get_flood_risk(precipitation):

    if precipitation > 80:
        return 90

    elif precipitation > 50:
        return 70

    elif precipitation > 20:
        return 40

    return 10