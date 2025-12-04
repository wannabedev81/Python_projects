# Multiprcessing tasks processes can run parallel
# for tasks that need heavy CPU tasks
# depends on cpu core amount


from multiProcessing import Process, cpu_count
import time

def counter(num):
    count = 0
    while count < num: 
        count += 1

def main():

    print(cpu_count())

    a = Process(target=counter, args=(500000000,))
    b = Process(target=counter, args=(500000000,))
    
    a.start()
    b.start()

    a.join()
    b.join()

    print("finished in: ", time.perf_counter(), "seconds")


if __name__ == "__main__":
    main()

