import os
import sys
import asyncio
import time

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import build_science_batch2
import build_science_batch3
import build_science_batch4
import build_science_batch5
import build_science_batch6
import build_science_batch7
import build_science_batch8
import build_science_batch9

async def run_all():
    batches = [
        ("Batch 2 (B6-B10)", build_science_batch2.main),
        ("Batch 3 (B11-B15)", build_science_batch3.main),
        ("Batch 4 (B16-B19)", build_science_batch4.main),
        ("Batch 5 (C1-C4)", build_science_batch5.main),
        ("Batch 6 (C5-C8)", build_science_batch6.main),
        ("Batch 7 (C9-C12)", build_science_batch7.main),
        ("Batch 8 (P1-P3)", build_science_batch8.main),
        ("Batch 9 (P4-P6)", build_science_batch9.main),
    ]

    total_start = time.time()
    for name, runner in batches:
        print(f"\n=======================================================")
        print(f"STARTING {name}")
        print(f"=======================================================")
        b_start = time.time()
        try:
            await runner()
            print(f"--> {name} finished successfully in {round(time.time() - b_start, 1)}s")
        except Exception as e:
            print(f"--> ERROR in {name}: {e}")
            raise e
        
    print(f"\n=======================================================")
    print(f"ALL REMAINING BATCHES (2 TO 9) COMPLETED in {round(time.time() - total_start, 1)}s!")
    print(f"=======================================================")

if __name__ == '__main__':
    asyncio.run(run_all())
