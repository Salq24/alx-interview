#!/usr/bin/python3
'''Module for pascal triangle'''


def pascal_triangle(n):
    '''
    Args:
      n (int): The num of triangle rows
    Returns:
      List of lists of integers to rep the triangle
    '''
    m_list = []
    if n == 0:
        return m_list
    for i in range(n):
        m_list.append([])
        m_list[i].append(1)
        if (i > 0):
            for j in range(1, i):
                m_list[i].append(m_list[i - 1][j - 1] + m_list[i - 1][j])
            m_list[i].append(1)
    return m_list
