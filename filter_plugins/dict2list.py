def dict2list (dict_, keyarg):
    list_ = [];
    for i in dict_.keys():
        e = dict_[i]
        e[keyarg] = i
        list_.append(e)
    return list_


class FilterModule(object):
    def filters(self):
        return {
            'dict2list': dict2list,
        }
