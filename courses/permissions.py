from django.contrib.auth.mixins import AccessMixin

import conftest


class OwnerRequiredMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):
        course = self.get_queryset().get(pk=kwargs.get('pk'))
        if conftest.user != course.owner:
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)
