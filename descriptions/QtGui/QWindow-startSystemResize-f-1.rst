.. sip:method-description::
    :status: todo
    :pysig: bd0cd928b14c6bf2f84da9b3f4fecb24
    :realsig: (Qt::Edges)
    :digest: cfd5022df690bfcb460f03a9d182271a

Start a system-specific resize operation

Calling this will start an interactive resize operation on the window by platforms that support it. The actual behavior may vary depending on the platform. Usually, it will make the window resize so that its edge follows the mouse cursor.

On platforms that support it, this method of resizing windows is preferred over ``setGeometry``, because it allows a more native look and feel of resizing windows, e.g. letting the window manager snap this window against other windows, or special resizing behavior with animations when dragged to the edge of the screen.

*edges* should either be a single edge, or two adjacent edges (a corner). Other values are not allowed.

Returns true if the operation was supported by the system.
