# sentient_node.py
# Simple starter for a "sentient" decision engine with retry/resilience logic.

import time
from typing import Any, Callable
from functools import wraps

class SentientNode:
    def __init__(self, name: str = "SovereignNode"):
        self.name = name

    def decide(self, context: dict) -> dict:
        """
        Make a decision based on context.
        Replace this stub with real logic / ML model inference.
        """
        # Example: trivial rule-based decision
        decision = {"action": "noop", "confidence": 0.0}
        if context.get("threat_level", 0) > 7:
            decision = {"action": "mitigate", "confidence": 0.95}
        elif context.get("opportunity", False):
            decision = {"action": "engage", "confidence": 0.8}
        return decision

def retry(times: int = 3, delay: float = 1.0):
    def decorator(fn: Callable):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            last_exc = None
            for attempt in range(1, times + 1):
                try:
                    return fn(*args, **kwargs)
                except Exception as e:
                    last_exc = e
                    time.sleep(delay)
            raise last_exc
        return wrapper
    return decorator

# Example usage
if __name__ == "__main__":
    node = SentientNode()
    ctx = {"threat_level": 8}
    print(node.decide(ctx))
