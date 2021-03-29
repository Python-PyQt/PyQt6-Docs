.. sip:method-description::
    :status: todo
    :pysig: b1b9bd588bc5178793bc3d194b600fda
    :realsig: (Qt::WindowStates)
    :digest: f33d891eaa359fc32cd1f7aef7887f25

set the screen-occupation state of the window

The window *state* represents whether the window appears in the windowing system as maximized, minimized and/or fullscreen.

The window can be in a combination of several states. For example, if the window is both minimized and maximized, the window will appear minimized, but clicking on the task bar entry will restore it to the maximized state.

The enum value :sip:ref:`~PyQt6.QtCore.Qt.WindowStates.WindowActive` should not be set.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QWindow.windowStates`, :sip:ref:`~PyQt6.QtGui.QWindow.showNormal`, :sip:ref:`~PyQt6.QtGui.QWindow.showFullScreen`, :sip:ref:`~PyQt6.QtGui.QWindow.showMinimized`, :sip:ref:`~PyQt6.QtGui.QWindow.showMaximized`.
