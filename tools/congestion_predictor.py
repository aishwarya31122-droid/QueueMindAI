def forecast_congestion(history):

    if len(history) < 3:
        return "Not enough data"

    if history[-1] > history[-2] > history[-3]:
        return "High congestion expected soon"

    return "Queue stable"