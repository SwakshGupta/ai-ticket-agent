# evaluation/metrics.py

import json
from agent.agent import run_agent


def evaluate():
    with open("evaluation/test_cases.json") as f:
        test_cases = json.load(f)

    correct = 0

    for case in test_cases:
        output = run_agent(case["query"])

        if case["expected"].lower() in output.lower():
            correct += 1

    accuracy = correct / len(test_cases)
    print(f"Accuracy: {accuracy:.2f}")


if __name__ == "__main__":
    evaluate()