from dataclasses import dataclass


@dataclass(frozen=True)
class Difference:
    path: str
    expected: object
    actual: object


def compare_json(
    expected: object,
    actual: object,
    path: str = "$",
) -> list[Difference]:

    differences: list[Difference] = []

    if isinstance(expected, bool) != isinstance(actual, bool):
        return [
            Difference(
                path=path,
                expected=expected,
                actual=actual,
            )
        ]

    if isinstance(expected, list) and isinstance(actual, list):
        if len(expected) != len(actual):
            return [Difference(path=path, expected=expected, actual=actual)]

        for index, (expected_item, actual_item) in enumerate(
            zip(expected, actual, strict=True)
        ):
            differences.extend(
                compare_json(
                    expected_item,
                    actual_item,
                    path=f"{path}[{index}]",
                )
            )

        return differences

    if isinstance(expected, dict) and isinstance(actual, dict):
        if expected.keys() != actual.keys():
            return [Difference(path=path, expected=expected, actual=actual)]

        for key in expected:
            differences.extend(
                compare_json(
                    expected[key],
                    actual[key],
                    path=f"{path}.{key}",
                )
            )

        return differences

    if expected == actual:
        return []

    return [
        Difference(
            path=path,
            expected=expected,
            actual=actual,
        )
    ]
