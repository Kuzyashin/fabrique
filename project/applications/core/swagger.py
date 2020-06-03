from drf_yasg import openapi

registration_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['password', 'email', ],
    properties={
        'email': openapi.Schema(
            type=openapi.TYPE_STRING,
            title='Email',
            description='Email'
        ),
        'password': openapi.Schema(
            type=openapi.TYPE_STRING,
            title='Password',
            description='Password'
        )
    },
    example={
        'email': 'alex@rocketcompute.com',
        'password': 'qwerty1234',
    }
)

login_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    required=['email', 'password', ],
    properties={
        'email': openapi.Schema(
            type=openapi.TYPE_STRING,
            title='email',
            description='Email'
        ),
        'password': openapi.Schema(
            type=openapi.TYPE_STRING,
            title='Password',
            description='Password'
        )
    },
    example={
        'email': 'alex@rocketcompute.com',
        'password': 'qwerty1234',
    }
)
