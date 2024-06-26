from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('index', views.index, name='index'),
    path('add-post', views.add_post, name='add-post'),
    path('edit-post', views.edit_post, name='edit-post'),
    path('adding-job', views.adding_job, name='adding-job'),
    path('editing-job', views.editing_job, name='editing-job'),
    path('GroziitDynamicSpace', views.GroziitDynamicSpace, name='GroziitDynamicSpace'),
    path('postdetail', views.postdetail, name='postdetail'),
    path('payment', views.payment, name='payment'),
    path('cancelsub', views.cancelsub, name='cancelsub'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('charts-apexcharts', views.charts_apexcharts, name="charts-apexcharts"),
    path('charts-chartjs', views.charts_chartjs, name="charts-chartjs"),
    path('charts-echarts', views.charts_echarts, name="charts-echarts"),
    path('components-accordion', views.components_accordion, name="components-accordion"),
    path('components-alerts', views.components_alerts, name="components-alerts"),
    path('components-badges', views.components_badges, name="components-badges"),
    path('components-breadcrumbs', views.components_breadcrumbs, name="components-breadcrumbs"),
    path('components-buttons', views.components_buttons, name="components-buttons"),
    path('components-cards', views.components_cards, name="components-cards"),
    path('components-carousel', views.components_carousel, name="components-carousel"),
    path('components-list-group', views.components_list_group, name="components-list-group"),
    path('components-modal', views.components_modal, name="components-modal"),
    path('components-pagination', views.components_pagination, name="components-pagination"),
    path('components-progress', views.components_progress, name="components-progress"),
    path('components-spinners', views.components_spinners, name="components-spinners"),
    path('components-tabs', views.components_tabs, name="components-tabs"),
    path('components-tooltips', views.components_tooltips, name="components-tooltips"),
    path('forms-editors', views.forms_editors, name="forms-editors"),
    path('forms-elements', views.forms_elements, name="forms-elements"),
    path('forms-layouts', views.forms_layouts, name="forms-layouts"),
    path('forms-validation', views.forms_validation, name="forms-validation"),
    path('icons-bootstrap', views.icons_bootstrap, name="icons-bootstrap"),
    path('icons-boxicons', views.icons_boxicons, name="icons-boxicons"),
    path('icons-remix', views.icons_remix, name="icons-remix"),
    path('pages-blank', views.pages_blank, name="pages-blank"),
    path('pages-contact', views.pages_contact, name="pages-contact"),
    path('pages-faq', views.pages_faq, name="pages-faq"),
    path('pages-login', views.pages_login, name="pages-login"),
    path('pages-register', views.pages_register, name="pages-register"),
    path('tables-data', views.tables_data, name="tables-data"),
    path('tables-general', views.tables_general, name="tables-general"),
    path('users-profile', views.users_profile, name="users-profile"),
    path('edit-profile', views.edit_profile, name="edit_profile"),
    path('change-password', views.change_password, name="change-password"),
    path('get-otp', views.get_otp, name="get_otp"),

    # path('dynamicspace', views.)
]
