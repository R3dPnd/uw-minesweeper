import random


def generate_minefield(n: int, m: int, mine_density: float = 0.2) -> str:
    """
    Generate a single minefield of size n x m with given mine density.

    Args:
        n: Number of rows (1-100)
        m: Number of columns (1-100)
        mine_density: Probability of a cell being a mine (0.0-1.0)

    Returns:
        String representation of minefield with dimensions
    """
    field = []
    field.append(f"{n} {m}")

    for _ in range(n):
        row = ''
        for _ in range(m):
            row += '*' if random.random() < mine_density else '.'
        field.append(row)

    return '\n'.join(field)


def generate_test_file(num_fields: int, max_size: int = 100) -> str:
    """
    Generate a complete test file with multiple minefields.

    Args:
        num_fields: Number of minefields to generate
        max_size: Maximum dimension size (default 100)

    Returns:
        Complete test file content including terminator
    """
    fields = []

    for _ in range(num_fields):
        n = random.randint(1, max_size)
        m = random.randint(1, max_size)
        fields.append(generate_minefield(n, m))

    fields.append("0 0")
    return '\n'.join(fields)