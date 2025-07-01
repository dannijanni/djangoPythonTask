"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from core.models import Users
from core.views_folder.login_view import LoginAPIView
from core.views_folder.project_view import CreateProject, GetAllProjects, GetProjectById, UpdateProjectById, DeleteProjectById
from core.views_folder.role_view import DeleteRoleById, ListRoles, CreateRole, GetRoleById,  UpdateRoleById
from core.views_folder.task_view import CreateTask, DeleteTaskById, GetAllTasks, GetTaskById, UpdateTaskById
from core.views_folder.user_view import CreateUser, GetAllUsers, UserDetailUpdateDelete
from django.views.decorators.csrf import csrf_exempt



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('create-user/', CreateUser.as_view(), name='create_user'),
    path('users/', GetAllUsers.as_view(), name='get-all-users'),
    path('users/<int:user_id>/', UserDetailUpdateDelete.as_view(), name='user-detail-update-delete'),
    path('tasks/create/', CreateTask.as_view(), name='create_task'),
    path('tasks/', GetAllTasks.as_view(), name='get_all_tasks'),
    path('tasks/<int:task_id>/', GetTaskById.as_view(), name='get_task_by_id'),
    path('tasks/<int:task_id>/update/', UpdateTaskById.as_view(), name='update_task_by_id'),
    path('tasks/<int:task_id>/delete/', DeleteTaskById.as_view(), name='delete_task_by_id'),
    path('projects/create/', CreateProject.as_view(), name='create_project'),
    path('projects/', GetAllProjects.as_view(), name='get_all_projects'),
    path('projects/<int:project_id>/', GetProjectById.as_view(), name='get_project_by_id'),
    path('projects/<int:project_id>/update/', UpdateProjectById.as_view(), name='update_project_by_id'),
    path('projects/<int:project_id>/delete/', DeleteProjectById.as_view(), name='delete_project_by_id'),
    path('roles/', ListRoles.as_view(), name='list_roles'),
    path('roles/create/', CreateRole.as_view(), name='create_role'),
    path('roles/<int:role_id>/', GetRoleById.as_view(), name='get_role_by_id'),
    path('roles/<int:role_id>/update/', UpdateRoleById.as_view(), name='update_role_by_id'),
    path('roles/<int:role_id>/delete/', DeleteRoleById.as_view(), name='delete_role_by_id'),
]
