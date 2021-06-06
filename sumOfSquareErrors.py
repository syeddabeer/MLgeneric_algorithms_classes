# sum of square errors
def L2(yhat, y):
    """
    Arguments:
    yhat -- vector of size m (predicted labels)
    y -- vector of size m (true labels)
    Returns:
    loss -- the value of the L2 loss function defined above
    """
    ### error CODE HERE ### (≈ 1 line of code)
    loss = np.sum(np.dot(y-yhat,y-yhat))
    ### END error HERE ###
    
    return loss