.. sip:method-description::
    :status: todo
    :pysig: 06ddee45f8e0cb9ee88ed5a6f8bcb797
    :realsig: (const QWidget*,const QPointF&) const
    :digest: 59e144958ca61447c11d0e5c10b9e667

Translates the widget coordinate *pos* to the coordinate system of *parent*. The *parent* must not be ``nullptr`` and must be a parent of the calling widget.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.mapFrom`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToParent`, :sip:ref:`~PyQt6.QtWidgets.QWidget.mapToGlobal`, :sip:ref:`~PyQt6.QtWidgets.QWidget.underMouse`.
