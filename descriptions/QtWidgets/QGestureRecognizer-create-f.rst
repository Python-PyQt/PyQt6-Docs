.. sip:method-description::
    :status: todo
    :pysig: 6c026e51dc2ba9caf6d98dd5cf67e7ad
    :realsig: (QObject*)
    :digest: 10d348f5bc296384284baaf6bb1944fc

This function is called by Qt to create a new :sip:ref:`~PyQt6.QtWidgets.QGesture` object for the given *target* (`QWidget <https://doc.qt.io/qt-6/widgets-changes-qt6.html#qwidget>`_ or :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject`).

Reimplement this function to create a custom :sip:ref:`~PyQt6.QtWidgets.QGesture`-derived gesture object if necessary.

The application takes ownership of the created gesture object.
