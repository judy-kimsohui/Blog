**[ 2023. Multicore Computing ]**
<br>

> Question1.
> Fill in the blanks (a)~(g) with the most appropriate English words

1. (a. **NVCC** ) is a proprietary compiler by Nvidia intended for use with CUDA. CUDA code runs on both the CPU and GPU. ( same as (a) ) separates these two parts and sends host code (the part of code which will be run on the CPU) to a C/C++ compiler like GCC or Intel C++ Compiler (ICC) or Microsoft Visual C++ Compiler, and sends the device code (the part which will run on the GPU) to the GPU. The device code is further compiled by ( same as (a) ).

NVCC는 CUDA와 함께 사용하기 위해 Nvidia에서 제작한 독점 컴파일러입니다.


2. (b. **Thrust** ) is a C++ template library for CUDA based on the **Standard Template Library (STL)**. ( same as (b) ) allows you to implement high performance parallel applications with minimal programming effort through a high-level interface that is fully interoperable with CUDA C. This means ( same as (b) ) is a library for high-level parallel algorithms and data structures that utilize GPU based on CUDA. It is a parallel analog of C++ STL and provides a productive way to program CUDA.


Thrust는 CUDA 기반의 C++ 템플릿 라이브러리로, 표준 템플릿 라이브러리(STL)를 기반으로 합니다. Thrust를 사용하면 최소한의 프로그래밍 노력으로 고성능 병렬 애플리케이션을 구현할 수 있으며, CUDA C와 완벽하게 호환되는 고급 인터페이스를 제공합니다.


3. The name of the OpenMP library function that returns the current thread index is (c. **omp_get_thread_num()** ).

OpenMP 라이브러리 함수에서 현재 스레드 인덱스를 반환하는 함수의 이름은 omp_get_thread_num()입니다.


4. In CUDA device, threads within the same (d. **block** ) can access the same data in a (e. **shared** ) memory which is much faster than global memory.

CUDA 장치에서 동일한 블록(block) 내의 스레드들은 공유 메모리에서 같은 데이터에 접근할 수 있습니다. 공유(shared) 메모리는 전역 메모리보다 훨씬 빠릅니다.

5. (f. **guided** ) is a type of OpenMP schedule that is similar to the dynamic schedule, but the size of the portion of work decreases as the program runs.

guided는 OpenMP 스케줄의 일종으로, 프로그램 실행 중 작업의 크기가 감소하는 동적 스케줄과 유사합니다.


6. [In OpenMP] By default, all variables declared outside a parallel block are shared variables except (g. **loop variables** ).

OpenMP에서 병렬 블록 외부에 선언된 모든 변수는 공유 변수입니다. 단, 루프 변수(loop variables)는 예외입니다.

7. In CUDA, (a. warp ) is a group of 32 threads where multiprocessors execute the same instruction at each clock cycle.

CUDA에서 (a. Warp)는 멀티 프로세서가 각 클록 사이클에서 동일한 명령을 실행하는 32 개의 스레드 그룹입니다.

8. CUDA keyword (b. __global__  ) indicates a function that runs on device, can only be callable from host code, and should have (c. void ) return type.

CUDA 키워드 (b. __global__)는 장치에서 실행되는 함수를 나타내고 호스트 코드에서만 호출 할 수 있으며 (c. void) 리턴 유형이 있어야합니다.

9. CUDA keyword (d. __host__  ) indicates a function that runs on host and can only be callable from host code.

CUDA 키워드 (d. __host__)는 호스트에서 실행되며 호스트 코드에서만 호출 할 수있는 함수를 나타냅니다.


10. CUDA keyword (e. __device__ ) indicates a function that runs on device and can only be callable from device code.

CUDA 키워드 (예 : __device__)는 장치에서 실행되며 장치 코드에서만 호출 할 수있는 함수를 나타냅니다.

11. [In CUDA] Because it is on-chip, (f. shared memory ) is much faster than local and global memory. In fact, ( same as (f) ) latency is roughly 100x lower than uncached global memory latency. ( same as (f) ) is allocated per (g. block ).

[CUDA에서] 칩이기 때문에 (f. 공유 메모리)는 로컬 및 글로벌 메모리보다 훨씬 빠릅니다. 실제로 ((F)와 동일) 대기 시간은 성분되지 않은 글로벌 메모리 대기 시간보다 대략 100 배 낮습니다. ((f)와 동일)는 (g. 블록) 당 할당됩니다.

12. So, ( same as (f) ) enables cooperation between threads in ( same as (g) ).

따라서 ((f)와 동일)는 ((g)와 동일) 사이의 협력을 가능하게합니다.

13. In OpenMP, variables declared in a parallel block are always (h. shared ).

OpenMP에서 병렬 블록으로 선언 된 변수는 항상 (h. 공유)입니다.

14. The word ‘mutex’ is from the abbreviation of (i. mutual exclusion ).

'Mutex'라는 단어는 (즉, 상호 배제)의 약어에서 나온 것입니다.

15. [In pthread] pthread_mutex_trylock behaves identically to pthread_mutex_lock, except that it does not (j. block ) the calling thread if the given mutex is already locked by another thread. Instead, pthread_mutex_trylock (k. returns ) immediately with the error code EBUSY.

[pthread에서] pthread_mutex_trylock은 주어진 뮤트가 이미 다른 스레드에 의해 잠겨있는 경우 호출 스레드를 제외하고는 pthread_mutex_lock에 동일하게 동작합니다. 대신, 오류 코드 ebusy와 함께 즉시 pthread_mutex_trylock (k. returns).

16. In pthread programming, (l. pthread_join ) subroutine blocks the calling thread until the specified thread terminates. The programmer is able to obtain the target thread's termination return status if it was specified in the target thread's call to (m. pthread_exit ).

pthread 프로그래밍에서 (l. pthread_join) 서브 루틴은 지정된 스레드가 종료 될 때까지 호출 스레드를 차단합니다. 프로그래머는 대상 스레드의 호출에 지정된 경우 대상 스레드의 종료 리턴 상태를 얻을 수 있습니다 (m. pthread_exit).

17. GPGPU stands for (a. General ) (b. Purpose ) computing on Graphics Processing Units. GPGPU is the use of GPU, which typically handles computation only for graphics, to perform computation in applications traditionally handled by CPU.

GPGPU는 그래픽 처리 장치에서 (a. General) (b. 목적) 컴퓨팅을 나타냅니다. GPGPU는 전통적으로 CPU가 처리하는 응용 프로그램에서 계산을 수행하기 위해 일반적으로 그래픽에 대한 계산을 처리하는 GPU를 사용합니다.

18.  CUDA C/C++ keyword __global__ indicates a function
- is executed on (c. device ), and
- is called from (d. host ). Any call to a __global__ function must specify (e. execution configuration ) for that call.

cuda c/c ++ 키워드 __global__는 함수를 나타냅니다.
 - (c. 장치)에서 실행되고
 - (d. host)에서 호출됩니다. __global__ 함수에 대한 호출은 해당 호출을 (예 : 실행 구성) 지정해야합니다.

19. In GPU, a stream multiprocessor (SM) is basically (f. parallel ) processor that executes a warp simultaneously.

GPU에서 스트림 다중 프로세서 (SM)는 기본적으로 (f. 병렬) 프로세서입니다.

20. [In OpenMP] By default, all variables declared outside a parallel block are (g. shared ), except (h.private ) variable, which is (i. private ).

[OpenMP에서] 기본적으로 병렬 블록 외부로 선언 된 모든 변수는 (h.private) 변수를 제외하고 (i. private)입니다.

21. (1) What does the function pthread_join do? Explain pthread_join with sufficient details. ( )

(1) pthread_join function description: pthread_join function allows one thread to wait for the exit of another thread. This function receives two arguments and blocks the call thread until the first argument is finished. This allows you to achieve synchronization between threads and obtain the return value of the finished thread through the second argument. This prevents memory leaks and allows the thread to safely handle the returned results.

(1) pthread_join 함수 설명: pthread_join 함수는 한 스레드가 다른 스레드의 종료를 기다리도록 합니다. 이 함수는 두 개의 인자를 받으며, 첫 번째 인자로 지정된 스레드가 종료될 때까지 호출 스레드를 차단합니다. 이를 통해 스레드 간의 동기화를 달성할 수 있으며, 두 번째 인자를 통해 종료된 스레드의 반환값을 얻을 수 있습니다. 이는 메모리 누수를 방지하고 스레드가 반환한 결과를 안전하게 처리할 수 있도록 합니다.

22. (2) What is the purpose of the argument variable A? Explain A with sufficient details. ( )

(2) Purpose of A variable: A is used as an identifier of the target thread in the pthread_join function. This argument is a pthread_t type identifier of the thread to wait for the end. In pthread_join (a, b), A specifies a waiting thread and the call thread is blocked until the thread is terminated.

(2) A 변수의 목적: A는 pthread_join 함수에서 대상 스레드의 식별자로 사용됩니다. 이 인자는 종료를 기다릴 스레드의 pthread_t 타입 식별자입니다. pthread_join(A, B)에서 A는 기다릴 스레드를 지정하며, 이 스레드가 종료될 때까지 호출 스레드가 차단됩니다.

23. (3) What is the purpose of the argument variable B? Explain B with sufficient details. ( )

(3) Purpose of B variable: B provides a pointer to which the return value of the thread terminated in the pthread_join function will be stored. This pointer is a void* type, and the ended thread will be returned through pthread_exit. This value allows you to deal with the execution results of the thread, and if not necessary, you can pass null.

(3) B 변수의 목적: B는 pthread_join 함수에서 종료된 스레드의 반환 값이 저장될 포인터를 제공합니다. 이 포인터는 void* 타입으로, 종료된 스레드가 pthread_exit을 통해 반환한 값을 담게 됩니다. 이 값을 통해 스레드의 실행 결과를 다룰 수 있으며, 필요하지 않은 경우 NULL을 전달할 수 있습니다.

24. In CUDA device, threads within the same (a. block ) can access the same data in a (b. shared ) memory which is much fster than global memory.

CUDA 장치에서 동일한 (a. 블록) 내의 스레드는 글로벌 메모리보다 훨씬 fster 인 (b. 공유) 메모리에서 동일한 데이터에 액세스 할 수 있습니다.

25.  In OpenMP, using (c. sections ) directive, individual code blocks are distributed over threads.

OpenMP에서 (c. 섹션) 지침을 사용하여 개별 코드 블록은 스레드에 분산됩니다.

26. [OpenMP] By default, all variables declared outside a parallel block are (d. shared ), except the (e. private ) variable, which is (f. private ).

[OpenMP] 기본적으로 평행 블록 외부로 선언 된 모든 변수는 (d. sared) (private) (f. private)를 제외하고 (d. 공유)입니다.
27. (i) static scheduling : ( )

(i) Static scheduling: Static scheduling in OpenMP divides the work among threads at the start of the parallel block based on a predetermined scheme. Each thread receives a fixed portion of the loop iterations or tasks before execution begins. This method is efficient for workload distributions that are predictable and evenly balanced among threads, reducing runtime overhead but potentially suffering from load imbalance if the tasks vary significantly in size or complexity.

(i) 정적 스케줄링 : OpenMP의 정적 스케줄링은 미리 정해진 체계를 기반으로 평행 블록의 시작시 스레드간에 작업을 나눕니다. 각 스레드는 실행이 시작되기 전에 루프 반복 또는 작업의 고정 된 부분을 수신합니다. 이 방법은 스레드간에 예측 가능하고 균등하게 균형을 이루는 워크로드 분포에 효율적이며 런타임 오버 헤드를 줄이지 만 작업이 크기 나 복잡성이 크게 다르면 부하 불균형으로 어려움을 겪을 수 있습니다.

28. (ii) dynamic scheduling : ( )

(ii) Dynamic scheduling: Dynamic scheduling in OpenMP assigns work to threads on-the-fly as they finish their assigned tasks. This approach is beneficial when dealing with loops or tasks where the execution times vary or are unpredictable. Dynamic scheduling can lead to better load balancing and potentially improved performance in heterogeneous or irregular workloads, though it may incur higher overhead due to the continuous distribution of tasks during execution.

(ii) 동적 스케줄링 : OpenMP의 동적 일정은 할당 된 작업을 완료 할 때 작업을 날개에 할당합니다. 이 접근법은 실행 시간이 다양하거나 예측할 수없는 루프 나 작업을 처리 할 때 유리합니다. 동적 스케줄링은 이질적이거나 불규칙한 작업량의로드 밸런싱을 개선하고 잠재적으로 향상된 성능으로 이어질 수 있지만, 실행 중 작업의 지속적인 분포로 인해 오버 헤드가 더 높아질 수 있습니다.


29. In OpenMP, by default all variables declared outside a parallel block are shared, except for (a. loop ) variable which is private.

OpenMP에서 기본적으로 평행 블록 외부로 선언 된 모든 변수는 비공개 인 (a. 루프) 변수를 제외하고 공유됩니다.

30.  In OpenMP, values of private variables are (b. undefined ) on entry and exit of parallel region.

OpenMP에서는 평행 영역의 진입 및 종료시 개인 변수의 값이 (b. 정의되지 않은)입니다.

31. In GPU, a stream multiprocessor (SM) is basically (c. parallel ) processor that executes a warp simultaneously.

GPU에서 스트림 다중 프로세서 (SM)는 기본적으로 (c. 병렬) 프로세서입니다.

32. [In CUDA] Any call to a __global__ function must specify (d. execution configuration ) for that call. List three other main characteristics of __global__ function :
- (e.  Executes on the device )
- (f. Callable from the host )
- (g. No return value )

[CUDA에서] __global__ 함수에 대한 모든 호출은 해당 호출을 (d. execution configuration) 지정해야합니다. __global__ 함수의 세 가지 주요 특성을 나열하십시오.
 - (예 : 장치에서 실행)
 - (f. 호스트에서 호출 가능)
 - (g. 반환 값 없음)

33. [In CUDA] Threads share data via shared memory within (h. a block ).

[CUDA에서] 스레드는 (h. 블록) 내에서 공유 메모리를 통해 데이터를 공유합니다.

34. In pthread programming, (i. pthread_join ) subroutine blocks the calling thread until the specified thread terminates. The programmer is able to obtain the target thread's termination return status if it was specified in the target thread's call to (j. pthread_exit ).

pthread 프로그래밍에서 (i. pthread_join) 서브 루틴은 지정된 스레드가 종료 될 때까지 호출 스레드를 차단합니다. 프로그래머는 대상 스레드의 호출 (j. pthread_exit)에 지정된 경우 대상 스레드의 종료 리턴 상태를 얻을 수 있습니다.

35. In CUDA, threads within a block can cooperate through (a. shared memory ). Threads in different blocks cannot cooperate.

 CUDA에서는 블록 내의 실이 (a. 공유 메모리)를 통해 협력 할 수 있습니다. 다른 블록의 스레드는 협력 할 수 없습니다.

36.  In CUDA, (b. warp ) is a group of threads where multiprocessor executes the same instruction at each clock cycle.

Cuda에서 (b. Warp)은 멀티 프로세서가 각 클록 사이클에서 동일한 명령을 실행하는 스레드 그룹입니다.

37. (c. scalability ) is the ability of a system, network, or process to handle a growing amount of work in a capable manner or its ability to be enlarged to accommodate that growth.

(c. 확장 성)는 시스템, 네트워크 또는 프로세스의 능력으로, 점점 더 많은 작업을 유능한 방식으로 처리하거나 그 성장을 수용 할 수 있도록 확대 할 수있는 능력입니다.

38. Main advantages of PSRS (Parallel Sorting by Regular Sampling) over parallel quicksort and hyper-quicksort algorithms, are - Better (d. scalability ) - Repeated communications of a same value are avoided - The number of processes does not have to be (e. a power of two ), which is required by the other two algorithms.

병렬 퀵조트 및 하이퍼 QuickSort 알고리즘에 대한 PSR (일반 샘플링에 의한 병렬 분류)의 주요 장점은 - 더 나은 (d. 확장 성) - 동일한 값의 반복 통신을 피할 수 있습니다. 프로세스의 수는 (e. 다른 두 알고리즘에 의해 요구되는 두 가지).

39. [In OpenMP] By default, all variables declared outside a parallel block are shared variables except (f. loop control variables ).

[OpenMP에서] 기본적으로 병렬 블록 밖에서 선언 된 모든 변수는 (f. 루프 제어 변수)를 제외한 공유 변수입니다.

40. (a. memory contention ) is the overhead in traffic to and from memory as a result of multiple threads concurrently attempting to access the same locations in memory.

(a. 메모리 경합)는 메모리의 동일한 위치에 동시에 액세스하려고 시도한 여러 스레드의 결과로 메모리를 오가는 트래픽의 오버 헤드입니다.

41. (b. compare-and-swap (CAS) ) is an atomic instruction used in multithreading to achieve synchronization. It compares the contents of a memory location to a given value and, only if they are the same, modifies the contents of that memory location to a given new value. This is done as a single atomic operation. The atomicity guarantees that the new value is calculated based on up-to-date information; if the value had been updated by another thread in the meantime, the write would (c. fail ).

(b. CAS (Compare-and-Swap)는 동기화를 달성하기 위해 멀티 스레딩에 사용되는 원자 명령어입니다. 메모리 위치의 내용을 주어진 값과 비교하고 동일 한 경우에만 해당 메모리 위치의 내용을 주어진 새 값으로 수정합니다. 이것은 단일 원자 작업으로 수행됩니다. 원자력은 새로운 값이 최신 정보에 따라 계산되도록 보장합니다. 그 동안 값이 다른 스레드에 의해 업데이트 된 경우, 쓰기는 (c. 실패)됩니다.

42. The divide-and-conquer paradigm improves program modularity, and often leads to simple and efficient algorithms. Since the subproblems created in the divide step are often (d. independent ), they can be solved in parallel. If the subproblems are solved recursively, each recursive divide step generates even more (d. independent ) subproblems to be solved in parallel. In order to obtain a highly parallel algorithm, it is often necessary to parallelize the (e. divide ) and (f. conquer ) steps, too

분열 및 대안 패러다임은 프로그램 모듈성을 향상시키고 종종 간단하고 효율적인 알고리즘으로 이어집니다. 분할 단계에서 생성 된 하위 문제는 종종 (d. 독립)이므로 동시에 해결할 수 있습니다. 하위 문제가 재귀 적으로 해결되면, 각각의 재귀 분열 단계는 더 많은 (d. 독립적 인) 하위 문제를 동시에 해결할 수있다. 매우 평행 한 알고리즘을 얻으려면 종종 (예 : Divide) 및 (f. Conquer) 단계를 병렬화해야합니다.

43. GPU is specialized for highly (g. parallelized ) computation, where the same program is executed on many data elements in parallel.

GPU는 많은 데이터 요소에서 동일한 프로그램이 병렬로 실행되는 높은 (g. 병렬화 된) 계산에 특화되어 있습니다.

44. In pthread programming, (h. pthread_join ) subroutine blocks the calling thread until the specified thread terminates. The programmer is able to obtain the target thread's termination return status if it was specified in the target thread's call to (i. pthread_exit ).

pthread 프로그래밍에서 (h. pthread_join) 서브 루틴은 지정된 스레드가 종료 될 때까지 호출 스레드를 차단합니다. 프로그래머는 대상 스레드의 호출 (i. pthread_exit)에 지정된 경우 대상 스레드의 종료 리턴 상태를 얻을 수 있습니다.

- ※ You should fill out the blank (h) and the blank (i) with appropriate pthread library function names. 2. (12points) In pthread programming, there are several ways in which a pthread (thread) can be terminated. List at least four ways.

pthread 적절한 pthread 라이브러리 기능 이름으로 공백 (h)과 공백 (i)을 작성해야합니다. 2. (12 점) pthread 프로그래밍에는 pthread (스레드)를 종료 할 수있는 몇 가지 방법이 있습니다. 적어도 네 가지 방법을 나열하십시오.

- (i) Return from the thread function: A pthread can terminate by simply returning from the thread function, which effectively ends the execution of the thread.

(i) 스레드 함수에서 반환 : 스레드 함수에서 간단하게 돌아와서 PTHREAD를 종료하여 스레드의 실행을 효과적으로 종료합니다.

- (ii) Calling pthread_exit: A pthread can explicitly call pthread_exit to terminate itself, optionally passing a return value that can be retrieved by another thread that joins it.

(ii) pthread_exit에 호출 : pthread는 pthread_exit을 명시 적으로 호출하여 스스로 종료 할 수 있으며, 선택적으로 결합하는 다른 스레드가 검색 할 수있는 리턴 값을 전달할 수 있습니다.

- (iii) Cancellation by another thread: A pthread can be terminated if another thread sends a cancellation request to it, using pthread_cancel.

(iii) 다른 스레드에 의한 취소 : 다른 스레드가 pthread_cancel을 사용하여 취소 요청을 보내면 pthread를 종료 할 수 있습니다.

- (iv) Thread termination due to process exit: All threads within a process will terminate if the entire process exits, whether through a call to exit, returning from main, or a call to exec.

(iv) 프로세스 종료로 인한 스레드 종료 : 프로세스 내의 모든 스레드는 종료 호출, 메인에서 돌아 오거나 exec 로의 통화를 통해 전체 프로세스 종료가 종료됩니다.













> Question2.
> Following program intends to compute the approximation value of numerical integration with multiple number of threads (i.e. 8 threads) using OpenMP.

<center><img src="image.png" width="160" height="80" /></center>
<br>

1. Insert in line 11 appropriate code that specifies the number of threads to use in subsequent parallel regions to be NUM.
<br>
2. a) The following program is not correct and may generate a wrong result. Which part in the program is wrong? : line ( )
<br>
3. b) Why is the program wrong? Your answer : ( [use less than 20 English words] )
<br>
4. c) How can you modify the program code for correction? Modify or insert your code directly in the following code.

```
#include <omp.h>
#include <stdio.h>
#define NUM 8

long num_steps = 10000000;
double step;

void main ()
{
    long i; double x, pi, sum = 0.0;
    step = 1.0/(double) num_steps;
  
    // specifies the number of threads to use
  
    // in subsequent parallel regions to be NUM

    #pragma omp parallel for reduction(+:sum)
    for (i=0;i< num_steps; i++){
        x = (i+0.5)*step;
        sum = sum + 4.0/(1.0+x*x);
    }
  
    pi = step * sum;
    printf("pi=%.4lf\n",pi);
}
```

![alt text](image-1.png)
<br>

**1. 스레드 수 지정 (11번 라인에 삽입할 코드)**

- pragma omp parallel for num_threads(NUM) reduction(+:sum)
- 병렬 영역에서 사용할 스레드의 수를 NUM으로 지정하고, 병렬 처리에서 사용되는 변수 sum에 대해 리덕션을 적용합니다.
<br>

**2-a. 잘못된 부분 지정**

- 잘못된 코드의 부분은 주로 sum 변수를 다루는 라인에서 발생할 가능성이 높습니다. 정확한 라인 번호는 제시된 코드 스니펫에서 확인할 수 없으나, 일반적으로 sum 업데이트 부분(예를 들면 for 루프 안에서의 sum += ...;)에서 문제가 발생합니다.
<br>

**2-b. 프로그램이 잘못된 이유**
"공유 변수 sum에 대한 동기화 누락" 때문입니다.
공유 변수에 대한 접근을 동기화하지 않으면, 다중 스레드 환경에서 데이터 레이스(data race)가 발생할 수 있습니다. 이는 잘못된 계산 결과를 초래할 수 있습니다.
<br>

**4-c. 프로그램 코드 수정**
프로그램 코드를 수정하여 정확하게 동작하게 하기 위해서는 sum 변수에 대한 리덕션을 명시적으로 지정해주어야 합니다. 수정된 코드는 다음과 같습니다

```
#include <omp.h>
#include <stdio.h>
#define NUM 8
long num_steps = 100000000;
double step;

int main () {
    long i; double x, pi, sum = 0.0;
    step = 1.0/(double) num_steps;

    #pragma omp parallel for num_threads(NUM) reduction(+:sum)
    for (i = 0; i < num_steps; i++) {
        x = (i + 0.5) * step;
        sum += 4.0 / (1.0 + x * x);
    }

    pi = step * sum;
    printf("pi=%.4lf\n", pi);
}
```

<br>

- 리덕션 (reduction(+:sum)): 이 지시어는 각 스레드로 하여금 sum의 개인 복사본을 가지고 계산을 수행하도록 하고, 모든 스레드의 계산이 끝난 후 이들 값을 모두 합치도록 합니다.
- num_threads(NUM): 병렬 블록을 실행할 스레드의 수를 NUM으로 설정합니다.
- 각 스레드가 독립적으로 작업을 수행하고 결과를 안전하게 합치게 함으로써 정확한 계산 결과를 얻을 수 있습니다.
<br>

> Question3.

- (a) What is the meaning of the OpenMP directive “#pragma omp parallel sections”?
  **English**: Divides code into independent sections to run in parallel.
  **Korean**: 코드를 독립적인 섹션으로 나누어 병렬로 실행하게 하는 지시어입니다.
<br>
- (b) What is the main similarity between private variables and firstprivate variables in OpenMP?
  **English**: Both are unique to each thread.
  **Korean**: 둘 다 각 스레드마다 고유합니다.
<br>
- (c) What is the main difference between private variables and firstprivate variables in OpenMP?
  **(i) private**
  **English**: Uninitialized for each thread.
  **Korean**: 각 스레드에 대해 초기화되지 않음.
  **(ii) firstprivate**
  **English**: Initialized with the value from outside.
  **Korean**: 외부 값으로 초기화됨.
