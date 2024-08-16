def timed(reps):
    def decorator(func):
        from time import perf_counter
        def inner(*args, **kwargs):
            total_elapsed = 0
            for i in range(reps):
                start = perf_counter()
                result = func(*args, **kwargs)
                total_elapsed += perf_counter() - start
            avg_elapsed = total_elapsed / reps
            print(f'{avg_elapsed=:.10f} seconds')
            return result
        return inner
    return decorator
