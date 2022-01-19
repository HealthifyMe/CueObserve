import os
from pathlib import Path

import sentry_sdk
import newrelic.agent
from sentry_sdk.integrations.flask import FlaskIntegration

from src.app import app

if __name__ == '__main__':
    BASE_DIR = Path(__file__).resolve().parent

    NEWRELIC_INI = os.path.join(BASE_DIR, 'newrelic.ini')

    ENABLE_NEWRELIC = os.environ.get("ENABLE_NEWRELIC", False)
    if ENABLE_NEWRELIC:
        newrelic.agent.initialize(NEWRELIC_INI, 'cue_observe')

    sentry_dsn = os.environ.get("SENTRY_DSN", '')
    if sentry_dsn:
        sentry_sdk.init(
            dsn=sentry_dsn,
            integrations=[FlaskIntegration()],
        )
    app.run(host="0.0.0.0", port=8100)
