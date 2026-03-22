import requests
import subprocess
import time

def test_crud():
    print("🚀 Starting Forge for CRUD Test...")
    process = subprocess.Popen(
        ["python3", "-m", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8002"],
        cwd="/Users/Learning/Desktop/projects/the_forge/backend"
    )
    time.sleep(3)
    base_url = "http://127.0.0.1:8002"

    try:
        # 1. CREATE
        print("Testing CREATE Topic...")
        topic_data = {"id": "test_topic", "name": "Test Subject", "prerequisites_raw": "", "mastery_score": 0.0}
        res = requests.post(f"{base_url}/topics", json=topic_data)
        print(f"Created: {res.json().get('id')}")

        # 2. UPDATE (PATCH)
        print("Testing UPDATE Topic...")
        update_res = requests.patch(f"{base_url}/topics/test_topic", json={"name": "Updated Subject"})
        print(f"Updated Name: {update_res.json().get('name')}")

        # 3. DELETE
        print("Testing DELETE Topic...")
        del_res = requests.delete(f"{base_url}/topics/test_topic")
        print(f"Delete Status: {del_res.json().get('status')}")

        # 4. VERIFY DELETE
        get_res = requests.get(f"{base_url}/topics/test_topic")
        if get_res.status_code == 404:
            print("✅ CRUD Verification: PASSED")
        else:
            print(f"❌ CRUD Verification: FAILED (Status: {get_res.status_code})")

    finally:
        process.terminate()

if __name__ == "__main__":
    test_crud()
