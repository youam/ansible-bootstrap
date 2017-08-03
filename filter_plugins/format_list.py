# taken from https://stackoverflow.com/a/35187231/3492754

def format_list(list_, pattern):
    return [pattern % s for s in list_]


class FilterModule(object):
    def filters(self):
        return {
            'format_list': format_list,
        }
