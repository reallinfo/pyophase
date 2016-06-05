from django.conf.urls import url

from staff import views

urlpatterns = [
    url(r'^$', views.StaffAdd.as_view(), name='registration'),
    url(r'success/$', views.StaffAddSuccess.as_view(), name='registration_success'),
    url(r'tutortypen/$', views.GroupCategoryList.as_view(), name='tutor_group_category_list'),
    url(r'orgaaufgaben/$', views.OrgaJobList.as_view(), name='orgajob_list'),
    url(r'helferaufgaben/$', views.HelperJobList.as_view(), name='helperjob_list'),
]
