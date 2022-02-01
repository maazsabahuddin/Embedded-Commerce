# Django imports
from django.http import JsonResponse
from rest_framework.decorators import api_view

# Local imports


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


@api_view(['GET'])
def get_package(request):
    data = {
        'noOfPackages': 3,
        'packages': [
            {
                'starred': False,
                'starredDetail': '',
                'duration': '1 month',
                'cutCost': '$0.00',
                'isCutCost': False,
                'originalCost': '$12.95',
                'detail': 'Billed $12.95 every month',
                'appreciation': '30 day money back guarantee'
            },
            {
                'starred': True,
                'starredDetail': '+3 months free',
                'duration': '12 months (Save 49%)',
                'cutCost': '$12.95',
                'isCutCost': True,
                'originalCost': '$6.67',
                'detail': f'Billed ${strike("194.20")} $99.95 for the first 15 months, and every 12 months thereafter',
                'appreciation': '30 day money back guarantee'
            },
            {
                'starred': False,
                'starredDetail': '',
                'duration': '6 months',
                'cutCost': '$0.00',
                'isCutCost': False,
                'originalCost': '$9.99',
                'detail': 'Billed $59.95 every 6 months',
                'appreciation': '30 day money back guarantee'
            }
        ]
    }
    return JsonResponse(data)
