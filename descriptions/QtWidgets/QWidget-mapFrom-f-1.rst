.. sip:method-description::
    :status: todo
    :pysig: 06ddee45f8e0cb9ee88ed5a6f8bcb797
    :realsig: (const QWidget*,const QPointF&) const
    :digest: 70784e5c123efe48a76dbacc3e80517a

Translates the widget coordinate *pos* from the coordinate system of *parent* to this widget's coordinate system. The *parent* must not be ``nullptr`` and must be a parent of the calling widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mapTo`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapFromParent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapFromGlobal`, :sip:ref:`~PyQt6.QtWidgets.QWidget.underMouse`.
