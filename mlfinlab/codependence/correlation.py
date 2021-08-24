"""
Correlation based distances and various modifications (angular, absolute, squared) described in Cornell lecture notes:
Codependence: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994&download=yes
"""

import numpy as np
import pandas as pd
from scipy.spatial.distance import squareform, pdist


# pylint: disable=invalid-name


def angular_distance(x: np.array, y: np.array) -> float:
    """
    Returns angular distance between two vectors. Angular distance is a slight modification of Pearson correlation which
    satisfies metric conditions.

    Formula used for calculation:

    Ang_Distance = (1/2 * (1 - Corr))^(1/2)

    Read Cornell lecture notes for more information about angular distance:
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994&download=yes.

    :param x: (np.array/pd.Series) X vector.
    :param y: (np.array/pd.Series) Y vector.
    :return: (float) Angular distance.
    """

    pass


def absolute_angular_distance(x: np.array, y: np.array) -> float:
    """
    Returns absolute angular distance between two vectors. It is a modification of angular distance where the absolute
    value of the Pearson correlation coefficient is used.

    Formula used for calculation:

    Abs_Ang_Distance = (1/2 * (1 - abs(Corr)))^(1/2)

    Read Cornell lecture notes for more information about absolute angular distance:
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994&download=yes.

    :param x: (np.array/pd.Series) X vector.
    :param y: (np.array/pd.Series) Y vector.
    :return: (float) Absolute angular distance.
    """

    pass


def squared_angular_distance(x: np.array, y: np.array) -> float:
    """
    Returns squared angular distance between two vectors. It is a modification of angular distance where the square of
    Pearson correlation coefficient is used.

    Formula used for calculation:

    Squared_Ang_Distance = (1/2 * (1 - (Corr)^2))^(1/2)

    Read Cornell lecture notes for more information about squared angular distance:
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994&download=yes.

    :param x: (np.array/pd.Series) X vector.
    :param y: (np.array/pd.Series) Y vector.
    :return: (float) Squared angular distance.
    """

    pass


def distance_correlation(x: np.array, y: np.array) -> float:
    """
    Returns distance correlation between two vectors. Distance correlation captures both linear and non-linear
    dependencies.

    Formula used for calculation:

    Distance_Corr[X, Y] = dCov[X, Y] / (dCov[X, X] * dCov[Y, Y])^(1/2)

    dCov[X, Y] is the average Hadamard product of the doubly-centered Euclidean distance matrices of X, Y.

    Read Cornell lecture notes for more information about distance correlation:
    https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3512994&download=yes.

    :param x: (np.array/pd.Series) X vector.
    :param y: (np.array/pd.Series) Y vector.
    :return: (float) Distance correlation coefficient.
    """

    pass

def kullback_leibler_distance(corr_a, corr_b):
    """
    Returns the Kullback-Leibler distance between two correlation matrices, all elements must be positive.
    Formula used for calculation:
    kullback_leibler_distance[X, Y] = 0.5 * ( Log( det(Y) / det(X) ) + tr((Y ^ -1).X - n )
    Where n is the dimension space spanned by X.
    Read Don H. Johnson's research paper for more information on Kullback-Leibler distance:
    `<https://scholarship.rice.edu/bitstream/handle/1911/19969/Joh2001Mar1Symmetrizi.PDF>`_

    :param corr_a: (np.array/pd.Series/pd.DataFrame) Numpy array of the first correlation matrix.
    :param corr_b: (np.array/pd.Series/pd.DataFrame) Numpy array of the second correlation matrix.
    :return: (np.float64) the Kullback-Leibler distance between the two matrices.
    """

    pass


def norm_distance(matrix_a, matrix_b, r_val=2):
    """
    Returns the normalized distance between two matrices.
    This function is a wrap for numpy's linear algebra method (numpy.linalg.norm).
    Link to documentation: `<https://numpy.org/doc/stable/reference/generated/numpy.linalg.norm.html>`_.
    Formula used to normalize matrix:
    norm_distance[X, Y] = sum( abs(X - Y) ^ r ) ^ 1/r
    Where r is a parameter. r=1 City block(L1 norm), r=2 Euclidean distance (L2 norm),
    r=inf Supermum (L_inf norm). For values of r < 1, the result is not really a mathematical ‘norm’.
    
    :param matrix_a: (np.array/pd.Series/pd.DataFrame) Array of the first matrix.
    :param matrix_b: (np.array/pd.Series/pd.DataFrame) Array of the second matrix.
    :param r_val: (int/str) The r value of the normalization formula. (``2`` by default, Any Integer)
    :return: (np.float64) The Euclidean distance between the two matrices.
    """

    pass