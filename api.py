from fastapi import FastAPI
from env import CliffEnv
from tasks import get_tasks

app = FastAPI()
env = None

@app.get("/")
def home():
    return {"message": "API is running"}

@app.api_route("/reset", methods=["GET", "POST"])
def reset(task_name: str = "easy"):
    global env
    task = next(t for t in get_tasks() if t["name"] == task_name)
    env = CliffEnv(task["rows"], task["cols"], task["cliffs"])
    state = env.reset()

    return {
        "observation": state,
        "reward": 0.0,
        "done": False,
        "info": {}
    }

@app.api_route("/step", methods=["GET", "POST"])
def step(action: int = 0):
    global env
    state, reward, done, info = env.step(action)

    return {
        "observation": state,
        "reward": float(reward),
        "done": bool(done),
        "info": info if info else {}
    }
