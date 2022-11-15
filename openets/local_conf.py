from django.conf import settings

ets_settings = {

}

# Check global settings and override local ones
if hasattr(settings, 'OPEN_ETS'):
    for key in ets_settings.keys():
        val = settings.OPEN_ETS.get(key)
        if val:
            ets_settings[key] = val
