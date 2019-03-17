from rest_framework.response import Response

def required_fields(*fields):
    def dec(function):
        def wrap(request, *args, **kwargs):
            try:
                [request.data[j] for j in fields]
            except KeyError:
                return Response({'error': 'required fields: ' + ' '.join(fields)}, status=400)
            return function(request, *args, **kwargs)
        return wrap
    return dec