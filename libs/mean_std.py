from typing import List


def get_mean(norm_value: float = 255) -> List[float]:
    # mean of imagenet
    return [123.675 / norm_value, 116.28 / norm_value, 103.53 / norm_value]


def get_std(norm_value: float = 255) -> List[float]:
    # std fo imagenet
    return [58.395 / norm_value, 57.12 / norm_value, 57.375 / norm_value]
