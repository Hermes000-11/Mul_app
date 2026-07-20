# # check_redis.py
# import os
# import django
# from channels.layers import get_channel_layer
# from asgiref.sync import async_to_sync

# # Настрой Django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Mul.settings')  # ← замени myproject на имя твоей папки!
# django.setup()

# # Получаем channel layer
# channel_layer = get_channel_layer()

# try:
#     # Пробуем отправить тестовое сообщение в группу
#     async_to_sync(channel_layer.group_send)(
#         "test_group",
#         {"type": "test.message", "text": "Hello from channel layer!"}
#     )
#     print("✅ Channel Layer работает! Сообщение отправлено в Redis.")
# except Exception as e:
#     print("❌ Ошибка:", e)

