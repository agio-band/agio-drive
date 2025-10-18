from agio.core.events import callback, AEvent
from agio.tools.qt import show_message_dialog


@callback('pipe.publish.before_start', raise_error=True)
def on_before_start_publish(event: AEvent):
    # check drive is started
    # get checking is enabled from settings
    from agio_drive.utils import drive_app
    if not drive_app.is_active():
        show_message_dialog('Drive Client is not active', 'Error', 'error')
        raise Exception('Drive Client is not active')
