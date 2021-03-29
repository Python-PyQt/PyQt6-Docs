.. sip:method-description::
    :status: todo
    :pysig: 19e986133b3c5dfcb100df1c8826ed60
    :realsig: () const
    :digest: 37f21ca9219e0629ceee6c76538905ab

Returns the offscreen :sip:ref:`~PyQt6.QtQuick.QQuickWindow` which is used by this widget to drive the Qt Quick rendering. This is useful if you want to use :sip:ref:`~PyQt6.QtQuick.QQuickWindow` APIs that are not currently exposed by :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, for instance connecting to the :sip:ref:`~PyQt6.QtQuick.QQuickWindow.beforeRendering` signal in order to draw native OpenGL content below Qt Quick's own rendering.

**Warning:** Use the return value of this function with caution. In particular, do not ever attempt to show the :sip:ref:`~PyQt6.QtQuick.QQuickWindow`, and be very careful when using other :sip:ref:`~PyQt6.QtGui.QWindow`-only APIs.

**Warning:** The offscreen window may be deleted (and recreated) during the life time of the :sip:ref:`~PyQt6.QtQuickWidgets.QQuickWidget`, particularly when the widget is moved to another :sip:ref:`~PyQt6.QtQuick.QQuickWindow`. If you need to know when the window has been replaced, connect to its destroyed() signal.
