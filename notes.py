###You can use this one if list = [0,1,2,3,4,5,6,7,8] :

List_to_array = np.array(list).reshape(3, 3)
cal_mean = (np.mean(List_to_array , axis = 0), np.mean(List_to_array , axis = 1),
            np.mean(List_to_array ))

this variable will give you package of 3
different values of axis1, axis2 and flattened.
By above code for cal_mean you can repeat the same process to
get veriance, std dev, max, min and sum then zip all
this variables with the a
list of keys like ['mean','variance','standard deviation','max','min','sum']
to get result as a Dictionary.