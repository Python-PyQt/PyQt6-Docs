.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 7ea1465435be16c44efd5818756be802

Returns ``true`` if the window should appear active from a style perspective.

This is the case for the window that has input focus as well as windows that are in the same parent / transient parent chain as the focus window.

To get the window that currently has focus, use :sip:ref:`~PyQt6.QtGui.QGuiApplication.focusWindow`.
