import subprocess
import sys
import time

SCRIPTS = [
    "scripts/build_lecture_5_1.py",
    "scripts/build_lecture_5_2.py",
    "scripts/build_lecture_5_3.py"
]

def main():
    print("=======================================================")
    print("Starting Batch Runner for Topic 5 (5.1 to 5.3)")
    print("=======================================================")
    
    results = {}
    for script in SCRIPTS:
        print(f"\n>>> Running {script} at {time.strftime('%X')}...")
        start_time = time.time()
        
        proc = subprocess.run([sys.executable, "-u", script])
        duration = time.time() - start_time
        
        if proc.returncode == 0:
            print(f">>> SUCCESS: {script} finished in {duration:.1f}s")
            results[script] = "SUCCESS"
        else:
            print(f">>> ERROR: {script} failed with exit code {proc.returncode}")
            results[script] = f"FAILED ({proc.returncode})"
            
    print("\n=======================================================")
    print("BATCH SUMMARY:")
    for script, status in results.items():
        print(f"  {script}: {status}")
    print("=======================================================")

if __name__ == "__main__":
    main()
