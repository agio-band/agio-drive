from agio.core.events import subscribe
from agio.core.plugins.base_service import ProcessServicePlugin


class DriveServicePlugin(ProcessServicePlugin):
    name = "drive"
    process_name = 'agio-drive'

    def before_start(self):
        @subscribe('core.settings.local_settings_loaded')
        def update_settings_value(event, payload):
            pass
            # drive_settings = {}
            # payload['settings'].set('agio_drive.cache_dir', drive_settings['cacheDir'])

        @subscribe('core.settings.local_settings_saved')
        def update_settings_value(event, payload):
            pass
            # cache_dir = payload['settings'].get('agio_drive.cache_dir')


    def get_startup_command(self) -> list[str]:
        return []

    def ensure_drive_installed(self) -> bool:
        pass