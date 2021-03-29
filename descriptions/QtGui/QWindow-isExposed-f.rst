.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6ba1007a7552fe6ccffc96fedeb57aca

Returns if this window is exposed in the windowing system.

When the window is not exposed, it is shown by the application but it is still not showing in the windowing system, so the application should minimize animations and other graphical activities.

An :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent` is sent every time this value changes.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.exposeEvent`.
