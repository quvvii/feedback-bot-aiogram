import humanize
from datetime import datetime
from zoneinfo import ZoneInfo


def time_ago(created_at: datetime) -> str:
    now = datetime.now(ZoneInfo("UTC"))
    delta = now - created_at

    humanize.i18n.activate("ru_RU")
    return str(humanize.naturaltime(delta))
