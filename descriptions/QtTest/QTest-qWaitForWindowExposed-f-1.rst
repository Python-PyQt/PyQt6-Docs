.. sip:method-description::
    :status: todo
    :pysig: 720d553c04b75d1e761b2ee2969113a6
    :realsig: (QWidget*,int)
    :digest: 10ba948af2e3c1d8590df711f7841a23

Waits for *timeout* milliseconds or until the *widget*'s window is exposed. Returns ``true`` if ``widget``'s window is exposed within *timeout* milliseconds, otherwise returns ``false``.

This is mainly useful for asynchronous systems like X11, where a window will be mapped to screen some time after being asked to show itself on the screen.

Note that a window that is mapped to screen may still not be considered exposed if the window client area is completely covered by other windows, or if the window is otherwise not visible. This function will then time out when waiting for such a window.

A specific configuration where this happens is when using QGLWidget as a viewport widget on macOS: The viewport widget gets the expose event, not the parent widget.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowActive`.
