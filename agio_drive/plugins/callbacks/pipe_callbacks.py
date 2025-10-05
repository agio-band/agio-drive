from agio.core.events import callback


@callback('pipe.publish.before_start', raise_error=True)
def on_before_start_publish(event, payload = None):
    # check drive is started
    # get checking is enabled from settings
    from agio_drive.utils import drive_app
    if not drive_app.is_active():
        raise Exception('Drive Client is not active')
