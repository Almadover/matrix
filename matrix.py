import asyncio
import httpx
from typing import List


async def fetch_matrix(url: str) -> str:
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
        response.raise_for_status()
        return response.text


def get_spiral_order(matrix: List[List[int]]) -> List[int]:
    N = len(matrix)
    spiral_order = []
    top, bottom, left, right = 0, N - 1, 0, N - 1

    while left <= right and top <= bottom:
        # Добавляем верхнюю строку
        for i in range(left, right + 1):
            spiral_order.append(matrix[top][i])
        top += 1

        # Добавляем правый столбец
        for i in range(top, bottom + 1):
            spiral_order.append(matrix[i][right])
        right -= 1

        # Добавляем нижнюю строку
        if top <= bottom:
            for i in range(right, left - 1, -1):
                spiral_order.append(matrix[bottom][i])
            bottom -= 1

        # Добавляем левый столбец
        if left <= right:
            for i in range(bottom, top - 1, -1):
                spiral_order.append(matrix[i][left])
            left += 1

    return spiral_order


async def get_matrix(url: str) -> List[int]:
    matrix_str = await fetch_matrix(url)

    matrix = []
    for row in matrix_str.split('\n'):
        nums = [int(num) for num in row.split() if num.isdigit()]
        if nums:
            matrix.append(nums)

    return get_spiral_order(matrix)


async def main():
    url = 'https://raw.githubusercontent.com/avito-tech/python-trainee-assignment/main/matrix.txt'
    result = await get_matrix(url)
    print(result)


# Запускаем асинхронную функцию main()
asyncio.run(main())