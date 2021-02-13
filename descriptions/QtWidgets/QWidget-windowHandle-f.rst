.. sip:method-description::
    :status: todo
    :pysig: 72e2cafa091a7d38d145ec5a6e8cba39
    :realsig: () const
    :digest: 601c23be6a5da8528dd5729277e3d728

If this is a native widget, return the associated :sip:ref:`~PyQt6.QtGui.QWindow`. Otherwise return null.

Native widgets include toplevel widgets, QGLWidget, and child widgets on which :sip:ref:`~PyQt6.QtWidgets.QWidget.winId` was called.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.winId`, :sip:ref:`~PyQt6.QtWidgets.QWidget.screen`.
