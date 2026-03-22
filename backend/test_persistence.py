import requests
import subprocess
import time
import os

def run_persistence_test():
    print("🚀 Starting the Forge API (Phase 1)...")
    
    # 1. Start Server on port 8001
    process = subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"],
        cwd="/Users/Learning/Desktop/projects/the_forge/backend"
    )
    time.sleep(3)
    
    base_url = "http://127.0.0.1:8001"
    
    try:
        # 2. Master arithmetic
        print("\n--- Mastering Arithmetic ---")
        requests.post(f"{base_url}/evaluate/arithmetic")
        
        # 3. Verify in current session
        res = requests.get(f"{base_url}/recommendation")
        print(f"Current Recommendation: {res.json().get('name')}") # Should be Algebra
        
        # 4. KILL SERVER
        print("\n🔪 KILLING THE SERVER (Simulating Crash/Restart)...")
        process.terminate()
        process.wait()
        
    except Exception as e:
        print(f"❌ Error: {e}")

    # 5. RESTART SERVER on port 8001
    process2 = subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8001"],
        cwd="/Users/Learning/Desktop/projects/the_forge/backend"
    )
    time.sleep(3)
    
    base_url = "http://127.0.0.1:8001"
    
    try:
        # 6. VERIFY PERSISTENCE
        print("\n--- Verifying Persistence ---")
        res = requests.get(f"{base_url}/recommendation")
        name = res.json().get('name')
        print(f"Post-Restart Recommendation: {name}") 
        
        if name == "Linear Equations":
            print("\n✅ SUCCESS: The Ghost is Pinned! Mastery survived the restart.")
        else:
            print("\n❌ FAILURE: Data was lost in the restart.")
            
    finally:
        process2.terminate()

if __name__ == "__main__":
    run_persistence_test()
