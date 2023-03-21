from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

swagger_info = openapi.Info(
    title="Clients API",
    default_version="v1",
    description="""Platform Campos Developers 365 - Campos Developers API

## For Authentication - Token Request

# Dev:

URL: http://keycloak-alb-12577876.us-east-1.elb.amazonaws.com/protocol/openid-connect/token/
Using POST with body parameters: client_id, client_secret, grant_type(password), username and password.

    """,
    terms_of_service="https://www.camposdevelopers.com.br/",
    contact=openapi.Contact(email="thiago@camposdevelopers.com.br"),
)

schema_view = get_schema_view(
    info=swagger_info,
    validators=[],
    public=True,
    permission_classes=(permissions.AllowAny,),
)
