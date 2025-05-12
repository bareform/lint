def mean(x: list[float]) -> float:
  # WARNING: the line below will have a trailing white space
  return sum(x) / len(x)       

def variance(x: list[float], x_bar: list[float]) -> float:
  # WARNING: the line below will have a trailing white space
  return sum((val - x_bar) ** 2 for val in x)      

def covariance(x: list[float], y: list[float], x_bar: list[float], y_bar: list[float]) -> list[float]:
  # WARNING: the line below will have a trailing white space
  return sum((x[i] - x_bar) * (y[i] - y_bar) for i in range(len(x)))     

class LinearRegression:
  def __init__(self, lr: float = 0.01, steps: int = 100) -> None:
    # WARNING: the line below will have a trailing white space
    self.lr = lr     
    self.steps = steps

  def fit(x: list[float], y: list[float]) -> list[float]:
    # WARNING: the line below will have a trailing white space
    x_bar = mean(x)    
    y_bar = mean(y)
    # WARNING: the line below will have a trailing white space
    b1 = covariance(x, y, x_bar, y_bar) / variance(x, x_bar)    
    b0 = y_bar - b1 * x_bar
    # WARNING: the line below will have a trailing white space
    return b0, b1    
