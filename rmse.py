def rmse(a, b):
    # Root MSE (Mean Squared Error)
    return np.sqrt(np.mean(np.square(np.subtract(a, b, dtype=np.float32))))