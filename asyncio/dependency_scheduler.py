"""An asyncio dependency scheduler using tasks and wait.

The first line contains the number of jobs. Each job has an ID, a delay
in milliseconds, and a comma-separated list of dependencies. A dash means
the job has no dependencies and can start immediately."""


import asyncio
import io
import sys


EXAMPLE_INPUT = """\
5
A 100 -
B 50 -
C 40 A
D 30 A,B
E 20 C,D
"""


async def process_task(task_id: str, duration_ms: int) -> str:
    duration_s = duration_ms / 1000
    await asyncio.sleep(duration_s)
    return task_id


async def main() -> None:
    task_count = int(sys.stdin.readline().strip())
    running_tasks: set[asyncio.Task[str]] = set()
    dependencies: dict[str, tuple[set[str], int]] = {}

    for _ in range(task_count):
        task_id, duration_ms, dependency_ids = sys.stdin.readline().strip().split()
        duration = int(duration_ms)
        if dependency_ids == "-":
            task = asyncio.create_task(process_task(task_id, duration))
            running_tasks.add(task)
        else:
            dependencies[task_id] = (set(dependency_ids.split(",")), duration)

    completed_tasks: set[str] = set()
    while running_tasks:
        finished_tasks, running_tasks = await asyncio.wait(
                                                           running_tasks,
                                                           return_when=asyncio.FIRST_COMPLETED
                                                          )

        for finished_task in finished_tasks:
            task_id = await finished_task
            completed_tasks.add(task_id)
            print(task_id)

        for task_id, (dependency_ids, duration) in list(dependencies.items()):
            if dependency_ids <= completed_tasks:
                task = asyncio.create_task(process_task(task_id, duration))
                running_tasks.add(task)
                del dependencies[task_id]


if __name__ == "__main__":
    sys.stdin = io.StringIO(EXAMPLE_INPUT)
    asyncio.run(main())