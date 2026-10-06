from semantic_kernel.functions import kernel_function


@kernel_function(
    name="add",
    description="Add two numbers."
)
def add(a: int, b: int) -> int:
    return a + b


result = add(10, 20)

print(result)