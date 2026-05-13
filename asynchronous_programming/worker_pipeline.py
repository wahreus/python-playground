"""An asyncio two-stage worker pipeline using queues.

The first line contains the number of download workers, parse workers,
and jobs. Each job has an ID, a download delay, and a parse delay in
milliseconds."""


import asyncio
import io
import sys


EXAMPLE_INPUT = """\
2 1 4
A 100 50
B 20 30
C 30 40
D 10 20
"""


async def parse_worker(parse_queue: asyncio.Queue[tuple[str, int]]) -> None:
    while True:
        job_id, parse_ms = await parse_queue.get()
        try:
            await asyncio.sleep(parse_ms/1000)
            print(job_id)
        finally:
            parse_queue.task_done()


async def download_worker(
                          download_queue: asyncio.Queue[tuple[str, int, int]],
                          parse_queue: asyncio.Queue[tuple[str, int]]
                         ) -> None:
    while True:
        job_id, download_ms, parse_ms = await download_queue.get()
        try:
            await asyncio.sleep(download_ms / 1000)
            await parse_queue.put((job_id, parse_ms))
        finally:
            download_queue.task_done()


async def main() -> None:
    download_worker_count, parse_worker_count, job_count = map(
                                                               int,
                                                               sys.stdin.readline().strip().split(),
                                                              )

    download_queue: asyncio.Queue[tuple[str, int, int]] = asyncio.Queue()
    parse_queue: asyncio.Queue[tuple[str, int]] = asyncio.Queue()

    for _ in range(job_count):
        job_id, download_ms, parse_ms = sys.stdin.readline().strip().split()
        await download_queue.put((job_id, int(download_ms), int(parse_ms)))

    download_tasks: list[asyncio.Task[None]] = []
    for _ in range(download_worker_count):
        task = asyncio.create_task(download_worker(download_queue, parse_queue))
        download_tasks.append(task)

    parse_tasks: list[asyncio.Task[None]] = []
    for _ in range(parse_worker_count):
        task = asyncio.create_task(parse_worker(parse_queue))
        parse_tasks.append(task)

    worker_tasks = download_tasks + parse_tasks
    await download_queue.join()
    await parse_queue.join()

    for task in worker_tasks:
        task.cancel()
    await asyncio.gather(*worker_tasks, return_exceptions=True)


if __name__ == "__main__":
    sys.stdin = io.StringIO(EXAMPLE_INPUT)
    asyncio.run(main())