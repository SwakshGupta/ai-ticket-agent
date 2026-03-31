

from agent.agent import run_agent

if __name__ == "__main__":
    while True:
        query = input("Enter query: ")
        response = run_agent(query)
        print("Agent:", response)