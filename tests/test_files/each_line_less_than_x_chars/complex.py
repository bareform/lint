def mean(x: list[float]) -> float:
  # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
  return sum(x) / len(x)

def variance(x: list[float], x_bar: list[float]) -> float:
  # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
  return sum((val - x_bar) ** 2 for val in x)

def covariance(x: list[float], y: list[float], x_bar: list[float], y_bar: list[float]) -> list[float]:
  # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
  return sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(len(x)))

class LinearRegression:
  def __init__(self, lr: float = 0.01, steps: int = 100) -> None:
    self.lr = lr
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    self.steps = steps

  def fit(x: list[float], y: list[float]) -> list[float]:
    x_bar = mean(x)
    y_bar = mean(y)
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    b1 = covariance(x, y, x_bar, y_bar) / variance(x, x_bar)
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    b0 = y_bar - b1 * x_bar
    # WARNING: This line here should be catched by the EachLineLessThanXChars Rule since this line is going to be 132 characters long
    return b0, b1
