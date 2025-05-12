def mean(x: list[float]) -> float:
  return sum(x) / len(x)

def variance(x: list[float], x_bar: list[float]) -> float:
  return sum((val - x_bar) ** 2 for val in x)

def covariance(x: list[float], y: list[float], x_bar: list[float], y_bar: list[float]) -> list[float]:
  return sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(len(x)))

class LinearRegression:
  # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
  def __init__(self, lr: float = 0.01, steps: int = 100) -> None:
    self.lr = lr
    self.steps = steps

  def fit(x: list[float], y: list[float]) -> list[float]:
    x_bar = mean(x)
    y_bar = mean(y)
    b1 = covariance(x, y, x_bar, y_bar) / variance(x, x_bar)
    b0 = y_bar - b1 * x_bar
    return b0, b1
