# create endpoints 
from django.http import JsonResponse
from .models import Plan
from .serializers import PlanSerializer


def plans_list(req):

    # store all data in the plans variable
    plans = Plan.objects.all()
    # covert the above data into a serializer
    serializer = PlanSerializer(plans, many=True)

    # response with a JSON data type
    # return JsonResponse({'plans':serializer.data}, safe=False)

    # convert the response to an array object
    return JsonResponse(serializer.data, safe=False)
