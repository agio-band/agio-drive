from agio.core.plugins.base.service_base import ProcessServicePlugin


class DriveServicePlugin(ProcessServicePlugin):
    name = "drive"
    process_name = 'agio-drive'

    def get_startup_command(self) -> list[str]:
        return ['kcalc']

    def ensure_drive_installed(self) -> bool:
        pass