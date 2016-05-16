#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    cleaned_data = []
    #print "predictions: ", predictions
    #print "ages: ", ages
    #print "net_worths: ", net_worths
    error = [(a-b)*(a-b) for a,b in zip(predictions,net_worths)]
    cleaned_data = zip(ages, net_worths, error)
    #cleaned_data.sort(key=(predictions-net_worth)*(predictions-net_worth))
    cleaned_data = sorted(cleaned_data, key=lambda x: x[2])
    n = int(len(cleaned_data)-0.9*len(cleaned_data))
    del cleaned_data[-n:]

    ### your code goes here

    
    return cleaned_data

