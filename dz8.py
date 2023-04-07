import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Function {func.__name__} took {(end - start) * 1000:.6f} ms")
        return result
    return wrapper

def test_func_1():
    time.sleep(1)


def test_func_2():
    time.sleep(2)

def test_time_it():
    import io
    from contextlib import redirect_stdout

    with io.StringIO() as buf, redirect_stdout(buf):
        test_func_1()
        assert "Function test_func_1 took" in buf.getvalue()

    with io.StringIO() as buf, redirect_stdout(buf):
        test_func_2()
        assert "Function test_func_2 took" in buf.getvalue()
