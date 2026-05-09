def estimate_rodent_population(
    humidity,
    vegetation,
    precipitation
):

    rodent_score = (
        humidity * 0.4 +
        vegetation * 0.4 +
        precipitation * 0.2
    )

    return min(round(rodent_score, 2), 100)