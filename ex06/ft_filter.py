def ft_filter(function_to_apply, list_of_inputs):
    """filters the list of inputs with the function to apply"""
    if (function_to_apply is None):
        return [x for x in list_of_inputs if bool(x)]
    return [x for x in list_of_inputs if function_to_apply(x)]
