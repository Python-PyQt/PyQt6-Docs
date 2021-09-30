.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: ecf7f18e9d275e336d0149c5b44528bd

Returns ``true`` if the window is active.

This is the case for the window that has input focus as well as windows that are in the same parent / transient parent chain as the focus window.

Typically active windows should appear active from a style perspective.

To get the window that currently has focus, use :sip:ref:`~PyQt6.QtGui.QGuiApplication.focusWindow`.
