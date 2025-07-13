import tomli
import tomli_w
import os

CONFIG_FILE = 'config.toml'

DEFAULT_SETTINGS = {
    'settings': {
        'quality': 80,
        'lossless': False,
        'output_directory': 'output'
    }
}

def load_settings():
    if not os.path.exists(CONFIG_FILE):
        return DEFAULT_SETTINGS['settings']
    try:
        with open(CONFIG_FILE, 'rb') as f:
            settings = tomli.load(f)
            # Make sure all keys are present
            for key, value in DEFAULT_SETTINGS['settings'].items():
                if key not in settings.get('settings', {}):
                    settings.setdefault('settings', {})[key] = value
            return settings.get('settings', DEFAULT_SETTINGS['settings'])
    except tomli.TOMLDecodeError:
        return DEFAULT_SETTINGS['settings']

def save_settings(settings_data):
    with open(CONFIG_FILE, 'wb') as f:
        tomli_w.dump({'settings': settings_data}, f)
