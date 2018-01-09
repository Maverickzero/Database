#!/usr/bin/python3

import multiprocessing
from time import sleep

semaphore = multiprocessing.Semaphore(0)

def do_job(job_id):
    with semaphore:
        sleep(1)
    print("Finished job")

def release_job(job_id):
    print("Doing the first thing and releasing semaphore")
    semaphore.release()

def main():
    pool = multiprocessing.Pool(2)
    pool.apply_async(do_job, [1])
    pool.apply_async(release_job, [2])
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()

