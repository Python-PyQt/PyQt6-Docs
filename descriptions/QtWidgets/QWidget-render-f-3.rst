.. sip:method-description::
    :status: todo
    :pysig: 7216fee2cc0c36a9b22ae3ed6d7b14a8
    :realsig: (QPainter*,const QPoint&,const QRegion&,QWidget::RenderFlags)
    :digest: de0c67f5eff8752312fd22d64aeaed62

This is an overloaded function.

Renders the widget into the *painter*'s :sip:ref:`~PyQt6.QtGui.QPainter.device`.

Transformations and settings applied to the *painter* will be used when rendering.

**Note:** The *painter* must be active. On macOS the widget will be rendered into a :sip:ref:`~PyQt6.QtGui.QPixmap` and then drawn by the *painter*.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.device`.
