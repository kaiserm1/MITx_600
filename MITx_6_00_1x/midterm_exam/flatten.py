def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    ''' 
    if not any(isinstance(item, list) for item in aList):
        return aList
    else:    
        aList_helper = []
        for item in aList:
            if isinstance(item, list):
                for item_helper in item:
                    aList_helper.append(item_helper)
            else:
                aList_helper.append(item)
        aList = list(aList_helper)
    return flatten(aList)