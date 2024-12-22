import numpy as np

def calculate(data_list):
    """
    This function uses Numpy to output the mean, variance, standard deviation, 
    max, min, and sum of the rows, columns, and elements in a 3 x 3 matrix.
    """

    if type(data_list) != list:
        raise ValueError("List must contain nine numbers.")
    elif len(data_list) != 9:
        raise ValueError("List must contain nine numbers.")
    elif not all(isinstance(item, (int, float)) for item in data_list):
        raise ValueError("List must contain nine numbers.")
    else:
        np_list = np.array(data_list)
        np_list = np_list.reshape(3, 3)

    mean_axis1 = np.mean(np_list, axis=0).tolist()
    mean_axis2 = np.mean(np_list, axis=1).tolist()
    mean_flattened = np.mean(np_list).tolist()

    var_axis1 = np.var(np_list, axis=0).tolist()
    var_axis2 = np.var(np_list, axis=1).tolist()
    var_flattened = np.var(np_list).tolist()

    std_axis1 = np.std(np_list, axis=0).tolist()
    std_axis2 = np.std(np_list, axis=1).tolist()
    std_flattened = np.std(np_list).tolist()

    max_axis1 = np.max(np_list, axis=0).tolist()
    max_axis2 = np.max(np_list, axis=1).tolist()
    max_flattened = np.max(np_list).tolist()

    min_axis1 = np.min(np_list, axis=0).tolist()
    min_axis2 = np.min(np_list, axis=1).tolist()
    min_flattened = np.min(np_list).tolist()

    sum_axis1 = np.sum(np_list, axis=0).tolist()
    sum_axis2 = np.sum(np_list, axis=1).tolist()
    sum_flattened = np.sum(np_list).tolist()

    calculations = {
  'mean': [mean_axis1, mean_axis2, mean_flattened],
  'variance': [var_axis1, var_axis2, var_flattened],
  'standard deviation': [std_axis1, std_axis2, std_flattened],
  'max': [max_axis1, max_axis2, max_flattened],
  'min': [min_axis1, min_axis2, min_flattened],
  'sum': [sum_axis1, sum_axis2, sum_flattened]
}
    return calculations


