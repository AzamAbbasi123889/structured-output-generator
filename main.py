"""
Structured Output Generator - Main Entry Point
"""

from src.core import Pipeline
from src.config import SAMPLE_INPUT


def main():
    print("=" * 60)
    print("Structured Output Generator")
    print("=" * 60)

    pipeline = Pipeline()
    result = pipeline.process(SAMPLE_INPUT)

    print(f"\nInput: {SAMPLE_INPUT[:100]}...")
    print(f"\nResult:")
    for key, value in result.items():
        print(f"  {key}: {value}")


if __name__ == "__main__":
    main()
