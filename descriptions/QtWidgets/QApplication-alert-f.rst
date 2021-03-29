.. sip:method-description::
    :status: todo
    :pysig: 07d239d4f27d7bb66c85a40cee5bbf52
    :realsig: (QWidget*,int)
    :digest: 4a167a23d103e4c9f07788fe1fe9cf6f

Causes an alert to be shown for *widget* if the window is not the active window. The alert is shown for *msec* miliseconds. If *msec* is zero (the default), then the alert is shown indefinitely until the window becomes active again.

Currently this function does nothing on Qt for Embedded Linux.

On macOS, this works more at the application level and will cause the application icon to bounce in the dock.

On Windows, this causes the window's taskbar entry to flash for a time. If *msec* is zero, the flashing will stop and the taskbar entry will turn a different color (currently orange).

On X11, this will cause the window to be marked as "demands attention", the window must not be hidden (i.e. not have hide() called on it, but be visible in some sort of way) in order for this to work.
