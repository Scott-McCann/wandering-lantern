def get_next(objset, idn):
    next_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == len(all_things)-1:
                next_id = None
            else:
                next_id = all_things[i+1].id


    return next_id

def get_previous(objset, idn):
    previous_id = None
    all_things = objset

    for i in range(len(all_things)):
        if all_things[i].id == idn:
            if i == 0:
                previous_id = None
            else:
                previous_id = all_things[i-1].id

    return previous_id
