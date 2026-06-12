"""An asyncio TaskGroup example that reports failures and cancellations.

The first line contains the number of jobs. Each job has an ID, a delay
in milliseconds, and an outcome. Jobs marked OK complete successfully,
while jobs marked FAIL raise an error and cause remaining tasks in the
TaskGroup to be cancelled."""


import asyncio
import io
import sys


EXAMPLE_INPUT = """\
4
A 50 OK
B 100 OK
C 70 FAIL
D 200 OK
"""


async def process_task(job_id: str, delay_ms: int, outcome: str) -> str:
    delay_s = delay_ms / 1000
    await asyncio.sleep(delay_s)
    if outcome == "OK":
        return job_id
    raise RuntimeError(job_id)


async def main() -> None:
    job_count = int(sys.stdin.readline().strip())
    jobs: list[tuple[str, int, str]] = []
    for _ in range(job_count):
        job_id, delay_ms, outcome = sys.stdin.readline().strip().split()
        jobs.append((job_id, int(delay_ms), outcome))

    tasks: list[asyncio.Task[str]] = []
    try:
        async with asyncio.TaskGroup() as task_group:
            for job_id, delay_ms, outcome in jobs:
                task = task_group.create_task(process_task(job_id, delay_ms, outcome))
                tasks.append(task)
    except* RuntimeError:
        pass

    successful_jobs: list[str] = []
    failed_job = ""
    cancelled_count = 0
    for task in tasks:
        if task.cancelled():
            cancelled_count += 1
        elif task.exception() is not None:
            failed_job = str(task.exception())
        else:
            successful_jobs.append(task.result())

    for job_id in successful_jobs:
        print(f"DONE {job_id}")
    if failed_job:
        print(f"FAILED {failed_job}")
    print(f"CANCELLED {cancelled_count}")


if __name__ == "__main__":
    sys.stdin = io.StringIO(EXAMPLE_INPUT)
    asyncio.run(main())