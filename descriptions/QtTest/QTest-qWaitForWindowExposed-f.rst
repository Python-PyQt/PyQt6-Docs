.. sip:method-description::
    :status: todo
    :pysig: 58413b4abf8ce2e29dba4e96faa26ac0
    :realsig: (QWindow*,int)
    :digest: e2b4c92a4a8e3d6718ae88a946fc8d9d

Waits for *timeout* milliseconds or until the *window* is exposed. Returns ``true`` if ``window`` is exposed within *timeout* milliseconds, otherwise returns ``false``.

This is mainly useful for asynchronous systems like X11, where a window will be mapped to screen some time after being asked to show itself on the screen.

Note that a window that is mapped to screen may still not be considered exposed if the window client area is completely covered by other windows, or if the window is otherwise not visible. This function will then time out when waiting for such a window.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowActive`, :sip:ref:`~PyQt6.QtGui.QWindow.isExposed`.
