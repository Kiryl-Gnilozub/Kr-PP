class Filter:
    def apply(self, o):
        pass


def custom_filter(array, filter_instance):
    return [item for item in array if filter_instance.apply(item)]


class StringLengthFilter(Filter):
    def apply(self, o):
        return isinstance(o, str) and len(o) > 5


class NumberFilter(Filter):
    def apply(self, o):
        return isinstance(o, (int, float)) and o > 10
