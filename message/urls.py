from django.urls import path
from .views import messageView

# urlpatterns = [
#     path('' , messageView , name="message"),  # fonctional coding
# ]


urlpatterns = [
    path('' , messageView.as_view() , name="message"),  # objectiv
]