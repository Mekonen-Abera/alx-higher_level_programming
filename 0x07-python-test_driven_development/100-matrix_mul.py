#!/usr/bin/python3
"""Write a function that multiplies 2 matrices:"""


def matrix_mul(m_a, m_b):
    """Multiplies two matrices and returns a new list

    Args:
        m_a (list): a list of lists containing integers or floats
        m_b (list): a list of lists containing integers or floats

    Raises:
        TypeError: if m_a is not a list
        TypeError: if m_b is not a list
        TypeError: if m_a is not a list of lists
        TypeError: if m_b is not a list of lists
        ValueError: if m_a is empty
        ValueError: if m_b is empty
        TypeError: if m_a is not a rectangle
        TypeError: if m_b is not a rectangle
        ValueError: if m_a and m_b can not be multiplied
        TypeError: if m_a contains an element not an integer or float
        TypeError: if m_b contains an element not an integer or float

    Returns:
        list: a new list which is the matrix product
    """
    # row_a - will store the rows of m_a: len(m_a)
    # col_a - will store the columns of m_a: len(m_a[0])
    # row_b - will store the rows of m_b: len(m_b)
    # col_b - will store the columns of m_b: len(m_b[0])
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if not all(isinstance(item, list) for item in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(item, list) for item in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    row_a = len(m_a)
    row_b = len(m_b)
    col_a = len(m_a[0])
    col_b = len(m_b[0])

    end_list = []
    elem = 0
    row_len_a = len(m_a[0])
    row_len_b = len(m_b[0])

    # Check for not rectangle
    for i in m_a:
        if row_len_a != len(i):
            raise TypeError("each row of m_a must be of the same size")
    # Check for not rectangle
    for i in m_b:
        if row_len_b != len(i):
            raise TypeError("each row of m_b must be of the same size")
    if col_a != row_b:
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(row_a):  # loop to iterate through m_a
        sub_list = []
        for j in range(col_b):  # loop to iterate through m_b
            for k in range(col_a):  # loop to add elements of the products
                if not isinstance(m_a[i][k], (int, float)):
                    msg1 = "m_a should contain only integers or floats"
                    raise TypeError(msg1)
                if not isinstance(m_b[k][j], (int, float)):
                    msg2 = "m_b should contain only integers or floats"
                    raise TypeError(msg2)
                elem += m_a[i][k] * m_b[k][j]
            sub_list.append(elem)
            elem = 0
        end_list.append(sub_list)

    return end_list


if __name__ == '__main__':
    import doctest
    doctest.testfile('./tests/100-matrix_mul.txt')
