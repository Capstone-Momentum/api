
from decimal import Decimal

def json_serialize(obj):
    """JSON serializer for objects not serializable by default json code"""
    if (isinstance(obj, Decimal)):
        return float(obj)
    raise TypeError ("Type %s not serializable" % type(obj))
