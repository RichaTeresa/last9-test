import sys
import json
from app import add

auto_approve = "--auto-approve" in sys.argv

def ask_user_to_update():
    response = input("\nDo you want to update the baseline?say something(yes/no): ").strip().lower()
    return response in ["yes", "yy"]

def test_add():
    result = {
        "inputs": [10, 20],
        "expected": 30,
        "actual": add(10, 20)
    }

    # Save dummy report
    with open("evaluated_time_range.json", "w") as f:
        json.dump(result, f, indent=2)

    assert result["actual"] == 3  # Intentional fail to test report presence
