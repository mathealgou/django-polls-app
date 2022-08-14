from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import views
from .views.signup import signup, signup_submit
from .views.login import login, login_submit, logout
from .views.detail import detail
from .views.vote import vote

app_name = 'polls'
urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', signup, name='signup'),
    path('signup_submit/', signup_submit, name='signup_submit'),
    path('login/', login, name='login'),
    path('login_submit/', login_submit, name='login_submit'),
    path('logout/', logout, name='logout'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
    path('<int:question_id>/clear_votes/', views._clear_votes, name='_clear_votes'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)