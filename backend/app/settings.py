from future.lifespan import Lifespan

from app.plugins import (
    MalSharePlugin,
    VirusTotalPlugin,
    MalwareBazaarPlugin,
    KasperskyPlugin,
    HybridAnalysisPlugin,
    AnyRunPlugin,
    TriagePlugin,
    MetaDefenderPlugin,
    ThreatFoxPlugin,
    BFKPlugin,
    ELFDigestPlugin,
    HuntIOPlugin
)


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
