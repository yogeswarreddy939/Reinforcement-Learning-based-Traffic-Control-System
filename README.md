
# Reinforcement Learning-based Traffic Control System 🚦

This project uses reinforcement learning to optimize traffic signal timing based on real-time traffic conditions. A Q-learning agent is trained to reduce congestion by maximizing vehicle throughput and minimizing waiting time. Computer vision (OpenCV) is used to analyze traffic congestion using sample video/image frames.

## 💡 Features

- Q-learning-based signal timing optimization
- Congestion analysis using image frame difference
- Simulated traffic environment
- Easy to extend with real-time video input

## 🧠 Technologies

- Python
- OpenCV
- Matplotlib
- Numpy

## 📁 Project Structure

- `traffic_env.py` – Simulated traffic environment
- `q_learning_agent.py` – Q-learning agent
- `simulate.py` – Main script to train and test
- `sample_traffic_data/` – Folder with sample traffic images

## ⚙️ Installation

```bash
git clone https://github.com/yourusername/traffic-control-rl.git
cd traffic-control-rl
pip install -r requirements.txt
