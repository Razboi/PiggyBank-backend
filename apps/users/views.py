from rest_framework import generics, mixins
from .models import Account
from .serializers import UserSerializer


class UsersCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = "pk"
    serializer_class = UserSerializer
    # queryset = User.objects.all()

    def get_queryset(self):
        qs = Account.objects.all()
        query = self.request.GET.get("q")
        if query is not None:
            qs = qs.filter(name__icontains=query).distinct()
        return qs

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# using mixins to add the post method on the listAPIview
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UsersRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = "pk"
    serializer_class = UserSerializer
    # queryset = User.objects.all()

    def get_queryset(self):
        return Account.objects.all()
