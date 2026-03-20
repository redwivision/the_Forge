import requests
import time
import subprocess

# --- THE TEST COMMAND ---
# We will start the server, wait for it to heat up, 
# then send the "Forge Orders."

def run_api_tests():
    print("🚀 Starting the Forge API Server...")
    
    # Start the server locally in the background
    # uvicorn main:app --reload
    process = subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd="/Users/Learning/Desktop/projects/the_forge/backend"
    )
    
    # Wait for the oven to heat up
    time.sleep(3)
    
    try:
        base_url = "http://127.0.0.1:8000"
        
        # Test 1: Check the Root
        print("\n--- Test 1: Handshake ---")
        response = requests.get(base_url)
        print(response.json())
        
        # Test 2: Check the "Menu" (Topics)
        print("\n--- Test 2: Reading the Menu ---")
        response = requests.get(f"{base_url}/topics")
        print(f"Found {len(response.json())} topics.")
        
        # Test 3: Get Chef's Recommendation
        print("\n--- Test 3: What to Forge Next ---")
        response = requests.get(f"{base_url}/recommendation")
        print(f"Recommended: {response.json().get('name')}")
        
        # Test 4: Master arithmetic
        print("\n--- Test 4: Mastering Arithmetic ---")
        response = requests.post(f"{base_url}/evaluate/arithmetic")
        print(response.json())
        
        # Test 5: Verify if Logic Bridge updated
        print("\n--- Test 5: What to Forge Next (After Mastering) ---")
        response = requests.get(f"{base_url}/recommendation")
        print(f"Next Recommended: {response.json().get('name')}")

    except Exception as e:
        print(f"❌ Test Failed: {e}")
    finally:
        print("\n🚿 Shutting down the server...")
        process.terminate()

if __name__ == "__main__":
    run_api_tests()
