.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: a8fa71b15c8d17f48a22c1744263bdb9

Start a system-specific move operation

Calling this will start an interactive move operation on the window by platforms that support it. The actual behavior may vary depending on the platform. Usually, it will make the window follow the mouse cursor until a mouse button is released.

On platforms that support it, this method of moving windows is preferred over ``setPosition``, because it allows a more native look-and-feel of moving windows, e.g. letting the window manager snap this window against other windows, or special tiling or resizing behavior with animations when dragged to the edge of the screen. Furthermore, on some platforms such as Wayland, ``setPosition`` is not supported, so this is the only way the application can influence its position.

Returns true if the operation was supported by the system.
