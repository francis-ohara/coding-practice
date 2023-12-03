"""Script for testing Python's asynchronous programming features"""
import asyncio
import time

def foo():
    """Wait 2 seconds and output 'Hello World!'."""
    time.sleep(2)
    print("Hello World!")

def bar():
    """Wait 2 seconds and output 'Goodbye Earth :(' """
    time.sleep(2)
    print("Goodbye Earth!")


# running the two functions sequentially and timing them
print("-----------SYNCHRONOUS------------")
start_time = time.time()
foo()
bar()
duration = time.time() - start_time
print(f"Runtime: {duration}")


# defining the two functions as coroutines!
async def foo_prime():
    """Wait 2 seconds and output 'Hello World!'."""
    await asyncio.sleep(2)
    print("Hello World!")


async def bar_prime():
    """Wait 2 seconds and output 'Goodbye Earth :(' """
    await asyncio.sleep(2)
    print("Goodbye Earth!")


# defining a top-level coroutine called `main` that runs the above coroutines
async def main():
    # converting the two coroutines into tasks (only tasks can run concurrently)
    task1 = asyncio.create_task(foo_prime())
    task2 = asyncio.create_task(bar_prime())

    # running the two tasks
    await task1
    await task2

# running the top-level coroutine
print("\n-----------ASYNCHRONOUS------------")
start_time = time.time()
asyncio.run(main())
duration = time.time() - start_time
print(f"Runtime: {duration}")


"""CONCLUSION
 - Python's asynchronous programming features include the following:
    1. `async`: keyword for creating coroutines (view usage above).
                - Simply place this keyword in front of a function to turn that function into a coroutine!
                - A coroutine is a function that can pause its execution without returning anything and resume its execution later on.
                 - Regular functions can't do this. Even if you don't explicitly specify a return value for a function, it will implicitly return None and be wiped out from memory after that.
                 - Coroutines on the other hand can persist in memory and be resumed later on.
                 - Coroutines by themselves do not engender concurrency. TASKS do!
    2. `await`: keyword for running coroutines and other awaitables.
                - await can only be called inside the scope of a coroutine.
                - Because of this, to run multiple coroutines, you typically await all those coroutines inside a single coroutine referred to as the top-level coroutine.
                  You then run that coroutine using `asyncio.run()`
    3. `asyncio.run()`: method which can execute a single coroutine(referred to as the top-level coroutine) outside of the scope of a coroutine.
                - A top-level coroutine is a coroutine that contains await calls to other co-routines or awaitables.
                - If you want to run multiple co-routines, you typically await them all inside 1 coroutine (the top-level coroutine),
                and then pass that top-level coroutine as argument to asyncio.run().
                - You can't run coroutines by simply calling them. 
                - You either have to
                    a. pass them as argument to `asyncio.run()` outside a coroutine.
                    b. `await` them inside a coroutine.
    4. Note that none of the above have anything to do with concurrency!
    5. `asyncio.create_task()`: where concurrency comes in!
            - This is a method that allows you to create a type of awaitable referred to as a task which is capable of concurrency.
            - A task is an awaitable created from a coroutine that has the ability to run concurrently with other tasks.
            - To run multiple coroutines concurrently, you have to 'schedule them' as tasks by passing them as argument to asyncio.create_task().
            - When multiple tasks are awaited, they run concurrently!
    6. `asyncio.gather()`: function for `scheduling` multiple coroutines as tasks to be awaited concurrently.
            - asyncio.create_task() only creates a single task from a single coroutine, but asyncio.gather can create multiple tasks from multiple coroutines 
              so they can run concurrently.
    7. time.sleep() overrides all asynchronous programming features. To pause task execution while allowing other tasks to execute,
        asyncio.sleep() can be used instead.
"""