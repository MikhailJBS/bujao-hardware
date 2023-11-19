from django.urls import path
from main.views import show_main, create_item, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user
from main.views import edit_item, delete_item, get_item_json, add_item_ajax, ajax_delete_item, create_product_flutter, get_user_item_json

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-item', create_item, name='create_item'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'), 
    path('xml/<int:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<int:id>/', show_json_by_id, name='show_json_by_id'), 
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),    
    path('edit-item/<int:id>/', edit_item, name='edit_item'),
    path('delete-item/<int:id>/', delete_item, name='delete_item'),
    path('get-item/', get_item_json, name='get_item_json'),
    path('create-ajax/', add_item_ajax, name='add_item_ajax'),
    path('delete-ajax/', ajax_delete_item, name='ajax_delete_item'),
    path('create-flutter/', create_product_flutter, name='create_product_flutter'),
    path('get-user-item/', get_user_item_json, name='get_user_item_json'),
]