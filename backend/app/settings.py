from future.lifespan import Lifespan

from app.plugins import MalSharePlugin
from app.plugins import VirusTotalPlugin
from app.plugins import MalwareBazaarPlugin
from app.plugins import KasperskyPlugin
from app.plugins import HybridAnalysisPlugin
from app.plugins import AnyRunPlugin
from app.plugins import TriagePlugin


# Register app config (FIXME: should load from .env)
config = {
    "APP_NAME": "VXSamples",
    "APP_DOMAIN": "vxsamples.com",
    "APP_DEBUG": True,
    "APP_LOG_LEVEL": "debug",
}

# Register application lifespan tasks (cronjobs)
lifespan = Lifespan(startup_tasks=[], shutdown_tasks=[], cron_tasks=[])

# Registered plugins
plugins = {
    "MalShare": MalSharePlugin(),
    "VirusTotal": VirusTotalPlugin(),
    "MalwareBazaar": MalwareBazaarPlugin(),
    "Kaspersky": KasperskyPlugin(),
    "HybridAnalysis": HybridAnalysisPlugin(),
    "AnyRun": AnyRunPlugin(),
    "Triage": TriagePlugin()
}
