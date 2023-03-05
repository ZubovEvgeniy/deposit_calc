from django.views import View
from django.http.response import HttpResponse, JsonResponse
from dateutil.relativedelta import relativedelta
from rest_framework import status
import json
from datetime import datetime

from .serializers import DepositSerializer


class DepositView(View):
    def post(self, request, *args, **kwargs):
        serializer = DepositSerializer(data=json.loads(request.body))
        if not serializer.is_valid(raise_exception=True):
            return HttpResponse(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST,
            )

        response_data = {}
        current_date = datetime.strptime(
            serializer.data["date"], "%d.%m.%Y").date()
        new_amount = serializer.data["amount"]
        for i in range(serializer.data["periods"]):
            new_date = current_date + relativedelta(months=i)
            new_amount = new_amount + \
                (new_amount * serializer.data["rate"] / 100) / 12
            response_data[new_date.strftime("%d.%m.%Y")] = round(new_amount, 2)
        return JsonResponse(response_data)
