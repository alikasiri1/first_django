from django.urls import path
from .views import MessageView , messageView

urlpatterns = [
    path('' , messageView , name="message"),  # fonctional coding
]


# urlpatterns = [
#     path('' , MessageView.as_view() , name="message"),  # objectiv
# ]