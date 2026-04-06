import os
import requests

API_BASE_URL = os.getenv("API_BASE_URL", "https://cliff-openenv.hf.space")

task = "easy"

print(f"[START] task={task} env=cliff model=baseline")

rewards = []
success = False

res = requests.get(f"{API_BASE_URL}/reset")
state = res.json()["observation"]

for step in range(20):
    action = 1

    res = requests.get(f"{API_BASE_URL}/step", params={"action": action})
    data = res.json()

    reward = data["reward"]
    done = data["done"]

    rewards.append(f"{reward:.2f}")

    print(f"[STEP] step={step+1} action={action} reward={reward:.2f} done={str(done).lower()} error=null")

    if done:
        success = True
        break

print(f"[END] success={str(success).lower()} steps={len(rewards)} rewards={','.join(rewards)}")
