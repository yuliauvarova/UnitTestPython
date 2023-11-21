
def find_avrg(numbers: list) -> float:
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)


def compare_avrg(numbers1, numbers2):
    return "Средние значения равны" if find_avrg(numbers1) == find_avrg(
        numbers2) else "Первый список имеет большее среднее значение" if find_avrg(numbers1) > find_avrg(
        numbers2) else "Второй список имеет большее среднее значение"

def test_compare_avrg():
    assert compare_avrg([1, 2, 3], [2, 3, 4]) == "Второй список имеет большее среднее значение"
    assert compare_avrg([1, 2, 3], [1, 1, 2]) == "Первый список имеет большее среднее значение"
    assert compare_avrg([1, 2, 3], [1, 3, 2]) == "Средние значения равны"

