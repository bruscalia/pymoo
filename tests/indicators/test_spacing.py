import numpy as np
from pymoo.indicators.spacing import SpacingIndicator


def test_spacing_values():
    
    F = np.array([
        [1.2, 7.8],
        [2.8, 5.1],
        [4.0, 2.8],
        [7.0, 2.2],
        [8.4, 1.2]
    ])
    
    assert abs(SpacingIndicator().do(F) - 0.73) <= 1e-3
    
    F = np.array([
        [1.0, 7.5],
        [1.1, 5.5],
        [2.0, 5.0],
        [3.0, 4.0],
        [4.0, 2.8],
        [5.5, 2.5],
        [6.8, 2.0],
        [8.4, 1.2]
    ])

    assert abs(SpacingIndicator().do(F) - 0.316) <= 1e-3