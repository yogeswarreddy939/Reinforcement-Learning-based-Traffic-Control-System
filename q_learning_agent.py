
import cv2
import os
import numpy as np
from traffic_env import TrafficEnvironment
from q_learning_agent import QLearningAgent

env = TrafficEnvironment()
agent = QLearningAgent()

def estimate_congestion(frame):
    # simple brightness-based estimation (mock method)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    congestion_score = np.mean(gray)
    return int(30 - congestion_score // 10)  # simulate vehicle count

frames_path = "sample_traffic_data/traffic_frames"
frame_files = sorted(os.listdir(frames_path))

for epoch in range(20):
    print(f"Epoch {epoch+1}")
    for frame_file in frame_files:
        path = os.path.join(frames_path, frame_file)
        frame = cv2.imread(path)
        if frame is None:
            continue

        vehicle_count = estimate_congestion(frame)
        state = env.get_state(vehicle_count)
        action = agent.choose_action(state)
        reward = env.get_reward(state, action)
        next_state = state  # assume same next state for now

        agent.update(state, action, reward, next_state)

        print(f"Frame: {frame_file}, Vehicles: {vehicle_count}, State: {state}, Action: {action}, Reward: {reward}")

print("\nFinal Q-table:")
print(agent.q_table)
