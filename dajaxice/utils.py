from django.http import QueryDict
import six

def deserialize_form(data):
    """
    Create a new QueryDict from a serialized form.
    """
    return QueryDict(query_string=six.text_type(data).encode('utf-8'))
