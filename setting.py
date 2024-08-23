# # import os
# # DATABASES = {
# #     'default': {
# #         'ENGINE': 'django.db.backends.postgresql',
# #         'NAME': os.getenv('DB_NAME'),
# #         'USER': os.getenv('DB_USER'),
# #         'PASSWORD': os.getenv('DB_PASSWORD'),
# #         'HOST': os.getenv('DB_HOST'),
# #         'PORT': '5432',
# #     }
# # }

# # ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# import os
# from sqlalchemy import create_engine
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': os.getenv('DB_NAME'),
#         'USER': os.getenv('DB_USER'),
#         'PASSWORD': os.getenv('DB_PASSWORD'),
#         'HOST': os.getenv('DB_HOST'),
#         'PORT': '5432',
#     }
# }

# # PostgreSQL接続設定
# DATABASE_URL = f"postgresql+psycopg2://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_HOST')}/{os.getenv('DB_NAME')}"
# # SQLAlchemyエンジンを作成
# ENGINE = create_engine(DATABASE_URL)