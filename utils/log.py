from datetime import datetime


def log(tag: str, msg: str) -> None:
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] [{tag}] [{msg}]")
