from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView
from django.http import HttpResponse, JsonResponse

User = get_user_model()


class UserDetailView(LoginRequiredMixin, DetailView):

    model = User
    slug_field = "username"
    slug_url_kwarg = "username"


user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert (
            self.request.user.is_authenticated
        )  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):

    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()


def strike(text):
    result = ''
    for c in text:
        result = result + c + '\u0336'
    return result


def employee_info(request):
    print(request.headers)
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
