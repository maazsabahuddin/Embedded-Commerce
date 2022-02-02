# Framework imports
from functools import wraps
from django.http import JsonResponse

# Local imports
from ec.utils import response as responseUtils, responseMessages, enums


def logging(view_function):

    @wraps(view_function)
    def wrapper(*args, **kwargs):

        try:
            response = view_function(*args, **kwargs)
            return response

        except Exception as e:
            print(str(e))
            response = responseUtils.getResponseObject(success=False,
                                                       responseMessage=responseMessages.MESSAGE_GENERAL_ERROR)
            return JsonResponse(response)

    return wrapper


def validateFields(requiredFields):
    def decorator(view_function):

        @wraps(view_function)
        def wrapper(request, *args, **kwargs):

            if not requiredFields:
                return view_function(*args, **kwargs)

            data = None
            if request.method == enums.RequestMethods.GET:
                data = request.GET
            elif request.method in [enums.RequestMethods.POST, enums.RequestMethods.PUT, enums.RequestMethods.PATCH]:
                data = request.data
            
            validated_keys = {
                key: data.get(key) for key in requiredFields
                    if data.get(key) not in [None, ""]
            }

            if set(validated_keys) != set(requiredFields):
                message = "Missing parameters keys: {}".format(' '.join(set(requiredFields) -
                                                                        set(validated_keys)))
                response = responseUtils.getResponseObject(success=False, responseMessage=message)
                return JsonResponse(response)

            # Might change later - TODO
            from django.http.request import QueryDict
            if isinstance(data, QueryDict):
                data._mutable = True

            return view_function(data, *args, **kwargs)

        return wrapper

    return decorator
