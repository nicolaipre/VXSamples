from future.lifespan import Lifespan

from app.plugins.MalSharePlugin import MalSharePlugin
from app.plugins.VirusTotalPlugin import VirusTotalPlugin
from app.plugins.MalwareBazaarPlugin import MalwareBazaarPlugin
from app.plugins.KasperskyPlugin import KasperskyPlugin
from app.plugins.HybridAnalysisPlugin import HybridAnalysisPlugin
from app.plugins.AnyRunPlugin import AnyRunPlugin
from app.plugins.TriagePlugin import TriagePlugin
from app.plugins.MetaDefenderPlugin import MetaDefenderPlugin
from app.plugins.ThreatFoxPlugin import ThreatFoxPlugin
from app.plugins.BFKPlugin import BFKPlugin
from app.plugins.ELFDigestPlugin import ELFDigestPlugin
from app.plugins.HuntIOPlugin import HuntIOPlugin


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
    "Triage": TriagePlugin(),
    "MetaDefender": MetaDefenderPlugin(),
    "ThreatFox": ThreatFoxPlugin(),
    "BFK": BFKPlugin(),
    "ELFDigest": ELFDigestPlugin(),
    "HuntIO": HuntIOPlugin()
}
