from httpx import Client


def get_public_http_client() -> Client:
    """
    Создаёт HTTP-клиент с базовыми настройками.

    Returns:
        Готовый к использованию HTTP-клиент с базовыми настройками.
    """
    return Client(
        timeout=1,
        base_url="http://localhost:8000"
    )