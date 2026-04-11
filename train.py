import time
import sys

def main():
    print("Initiating expensive GPU training session...")
    time.sleep(2)  # Simulating overhead
    print("Loading data...")
    time.sleep(2)
    print("Training Epoch 1/10...")
    
    # Simulate potential failure condition
    # raise Exception("Out of Memory (OOM) on GPU0")
    
    print("Training completed successfully!")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"FATAL ERROR: {e}", file=sys.stderr)
        sys.exit(1)
