import time
import random

class SimpleAIAgent:
    def __init__(self, name, goal):
        self.name = name
        self.goal = goal
        self.knowledge = []
        self.received_messages = []

    def perceive(self, environment_data):
        # In a real system, this would involve complex perception
        # For this simulation, we'll just add it to knowledge
        self.knowledge.append(environment_data)
        print(f"[{self.name}] Perceived: {environment_data}")

    def decide(self):
        # Simple decision logic: if goal is met, stop. Otherwise, communicate.
        if self.goal in self.knowledge:
            print(f"[{self.name}] Goal '{self.goal}' achieved! Halting.")
            return None # Stop
        else:
            # Decide to send a message based on current knowledge
            message_content = f"Seeking information about '{self.goal}'. Current knowledge: {self.knowledge[-1] if self.knowledge else 'None'}"
            return message_content

    def act(self, message_content, other_agents):
        if message_content:
            print(f"[{self.name}] Sending message: '{message_content}'")
            # Simulate sending message to a random other agent
            if other_agents:
                recipient = random.choice([agent for agent in other_agents if agent.name != self.name])
                recipient.receive_message(self.name, message_content)
        else:
            print(f"[{self.name}] No action needed.")

    def receive_message(self, sender_name, message_content):
        print(f"[{self.name}] Received message from {sender_name}: '{message_content}'")
        self.received_messages.append((sender_name, message_content))
        # Agents can update their knowledge based on received messages
        self.knowledge.append(f"Message from {sender_name}: {message_content}")

def run_simulation(agents, environment_updates, max_steps=5):
    for step in range(max_steps):
        print(f"\n--- Simulation Step {step + 1} ---")

        # 1. Environment updates
        if step < len(environment_updates):
            update = environment_updates[step]
            for agent in agents:
                agent.perceive(update)

        # 2. Agents decide and act
        messages_to_send = {}
        for agent in agents:
            decision = agent.decide()
            if decision is not None:
                messages_to_send[agent.name] = decision

        # Distribute messages (simulating network communication)
        for agent in agents:
            if agent.name in messages_to_send:
                agent.act(messages_to_send[agent.name], agents)

        time.sleep(1) # Slow down simulation for readability

if __name__ == "__main__":
    # Define agents with their goals
    agent1 = SimpleAIAgent("Alpha", "Find the Red Ball")
    agent2 = SimpleAIAgent("Beta", "Find the Blue Box")
    agent3 = SimpleAIAgent("Gamma", "Find the Red Ball")

    all_agents = [agent1, agent2, agent3]

    # Simulate environmental changes over time
    # These are simple strings representing observations
    environment_changes = [
        "Saw a green tree.",
        "Heard a dog bark.",
        "Detected a Red Ball nearby.",
        "Found a Blue Box.",
        "The Red Ball is now in the garden."
    ]

    run_simulation(all_agents, environment_changes)

    print("\n--- Final Knowledge ---")
    for agent in all_agents:
        print(f"{agent.name}: {agent.knowledge}")
