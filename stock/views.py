from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def stock_details(request):
    json_response = {
      "DueDate": "2013-02-15",
      "Balance": 1990.19,
      "DocNumber": "SAMP001",
      "Status": "Payable",
      "Line": [
        {
          "Description": "Sample Expense",
          "Amount": 500,
          "DetailType": "ExpenseDetail",
          "ExpenseDetail": {
            "Customer": {
              "value": "ABC123",
              "name": "Sample Customer"
            },
            "Ref": {
              "value": "DEF234",
              "name": "Sample Construction"
            },
            "Account": {
              "value": "EFG345",
              "name": "Fuel"
            },
            "LineStatus": "Billable"
          }
        }
      ],
      "Vendor": {
        "value": "GHI456",
        "name": "Sample Bank"
      },
      "APRef": {
        "value": "HIJ567",
        "name": "Accounts Payable"
      },
      "TotalAmt": 1990.19
    }
    return JsonResponse(json_response)