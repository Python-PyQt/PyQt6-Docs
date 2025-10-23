.. sip:method-description::
    :status: todo
    :pysig: 6c026e51dc2ba9caf6d98dd5cf67e7ad
    :realsig: (QObject*)
    :digest: edd4d1d2b9de331fa06e6a9ecbb2fdba

This function is called by Qt to create a new :sip:ref:`~PyQt6.QtWidgets.QGesture` object for the given *target* (\ :sip:ref:`~PyQt6.QtWidgets.QWidget` or :sip:ref:`~PyQt6.QtWidgets.QGraphicsObject`).

Reimplement this function to create a custom :sip:ref:`~PyQt6.QtWidgets.QGesture`-derived gesture object if necessary.

:sip:ref:`~PyQt6.QtWidgets.QApplication` takes ownership of the created gesture object.
