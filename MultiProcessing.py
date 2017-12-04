import multiprocessing
from time import sleep

semaphore = multiprocessing.Semaphore(0)

def do_job(job_id):
    with semaphore:
        sleep(1)
    print("Finished job")

def release_job(job_id):
    print("Doing the first pring and releasing semaphore")
    semaphore.release()
def main():
    pool = multiprocessing.Pool(6)
    for job_id in range(6):
        print("Starting job")
        pool.apply_async(do_job, [job_id])
    pool.close()
    pool.join()

if __name__ == "__main__":
    main()
