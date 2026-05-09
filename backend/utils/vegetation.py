def get_vegetation_index(lat, lon):

    vegetation_score = (
        (abs(lat) + abs(lon)) % 100
    )

    return round(vegetation_score, 2)