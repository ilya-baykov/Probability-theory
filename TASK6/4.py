from main import bernoulli, combinations


def volume_control(probability: float = 0.01, accuracy: float = 0.95) -> int:
    volume = 1
    while (1 - bernoulli(volume, 0, probability)) < accuracy:
        volume += 1
    return volume


print(volume_control())
