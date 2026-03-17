from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import joblib
import math

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load("models/model.pkl")


# -----------------------------
# Queue Observer
# -----------------------------
def observe_queue():

    return {
        "queue_length": random.randint(5,25),
        "arrival_rate": random.randint(2,8),
        "service_time": random.randint(2,5),
        "open_counters": random.randint(1,4)
    }


# -----------------------------
# ML Wait Prediction
# -----------------------------
def predict_wait(queue):

    X = [[
        queue["queue_length"],
        queue["arrival_rate"],
        queue["service_time"],
        queue["open_counters"]
    ]]

    wait = model.predict(X)[0]

    return round(wait,2)


# -----------------------------
# AI Forecast Engine
# -----------------------------
def forecast_wait(current_wait):

    return {
        "next_10_min": round(current_wait * random.uniform(0.9,1.2),2),
        "next_20_min": round(current_wait * random.uniform(1.0,1.4),2),
        "next_30_min": round(current_wait * random.uniform(1.1,1.6),2)
    }


# -----------------------------
# Congestion Detection
# -----------------------------
def detect_congestion(queue):

    q = queue["queue_length"]

    if q < 8:
        return "LOW"
    elif q < 15:
        return "MEDIUM"
    else:
        return "HIGH"


# -----------------------------
# Staff Recommendation
# -----------------------------
def recommend_staff(queue):

    q = queue["queue_length"]

    if q < 8:
        return 2
    elif q < 15:
        return 3
    else:
        return 4


# -----------------------------
# Queue Optimization
# -----------------------------
def optimize_queue(queue):

    q = queue["queue_length"]
    counters = queue["open_counters"]

    if q > 15:
        return "Open additional counter"

    elif q < 5 and counters > 1:
        return "Reduce one counter"

    else:
        return "Current setup optimal"


# -----------------------------
# Simple Distance
# -----------------------------
def distance(a,b):

    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)


# -----------------------------
# Branch Recommendation
# -----------------------------
def recommend_branch(user_location):

    branches = {
        "Branch A": (13.0827,80.2707),
        "Branch B": (13.0500,80.2120),
        "Branch C": (13.1200,80.3000)
    }

    wait_times = {
        "Branch A": 10,
        "Branch B": 6,
        "Branch C": 15
    }

    best_branch = None
    best_score = 999

    for name,coords in branches.items():

        dist = distance(user_location,coords)

        score = dist + wait_times[name]

        if score < best_score:
            best_score = score
            best_branch = name

    return best_branch


# -----------------------------
# AI Customer Assistant
# -----------------------------
def assistant(question, result):

    q = question.lower()

    wait = result["predicted_wait_time"]
    congestion = result["congestion"]

    if "wait" in q:
        return f"Estimated waiting time is {wait} minutes."

    if "busy" in q or "congestion" in q:
        return f"Queue congestion level is {congestion}"

    if "visit" in q:
        if congestion == "LOW":
            return "This is a good time to visit."
        else:
            return "Queues are busy now. Consider visiting later."

    return "I can answer questions about wait time or congestion."


# -----------------------------
# Queue Simulation
# -----------------------------
def simulate_customers(n=500):

    customers = []

    for i in range(n):

        customers.append({
            "customer_id": i+1,
            "service_time": random.randint(2,6),
            "queue_length": random.randint(1,25)
        })

    return customers


# =============================
# API ENDPOINTS
# =============================

@app.get("/queue-status")
def queue_status():

    queue = observe_queue()

    wait = predict_wait(queue)

    return {
        "queue_length": queue["queue_length"],
        "arrival_rate": queue["arrival_rate"],
        "predicted_wait_time": wait
    }


@app.get("/forecast")
def forecast():

    queue = observe_queue()

    wait = predict_wait(queue)

    future = forecast_wait(wait)

    return future


@app.get("/congestion")
def congestion():

    queue = observe_queue()

    level = detect_congestion(queue)

    return {"congestion_level": level}


@app.get("/staff-plan")
def staff():

    queue = observe_queue()

    staff = recommend_staff(queue)

    return {"recommended_counters": staff}


@app.get("/optimization")
def optimization():

    queue = observe_queue()

    decision = optimize_queue(queue)

    return {"decision": decision}


@app.get("/best-branch")
def best_branch():

    user_location = (13.0827,80.2707)

    branch = recommend_branch(user_location)

    return {"recommended_branch": branch}


@app.get("/simulate")
def simulate():

    data = simulate_customers(500)

    return {
        "customers_simulated": len(data),
        "sample": data[:5]
    }


@app.get("/ask-ai")
def ask_ai(question: str):

    queue = observe_queue()

    wait = predict_wait(queue)

    congestion = detect_congestion(queue)

    result = {
        "predicted_wait_time": wait,
        "congestion": congestion
    }

    answer = assistant(question,result)

    return {"response": answer}