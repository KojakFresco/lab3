import typer
import factorial as fac
import fibonacci as fib
import sorts

app = typer.Typer()


@app.command()
def factorial(n: int):
    print(fac.factorial(n))


@app.command()
def factorial_recursive(n: int):
    print(fac.factorial_recursive(n))


@app.command()
def fibo(n: int):
    print(fib.fibo(n))


@app.command()
def fibo_recursive(n: int):
    print(fib.fibo_recursive(n))


@app.command()
def bubble_sort(a: list[int]):
    sorts.bubble_sort(a)
    print(a)


@app.command()
def quick_sort(a: list[int]):
    print(sorts.quick_sort(a))


@app.command()
def counting_sort(a: list[int]):
    print(sorts.counting_sort(a))


@app.command()
def radix_sort(a: list[int]):
    print(sorts.radix_sort(a))


@app.command()
def bucket_sort(a: list[float], buckets: int | None = None):
    print(sorts.bucket_sort(a, buckets))


@app.command()
def heap_sort(a: list[int]):
    print(sorts.heap_sort(a))


@app.command()
def main() -> None:
    print("Hello World")


if __name__ == "__main__":
    app()
