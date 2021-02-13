.. sip:method-description::
    :status: todo
    :pysig: 92a6828c6230a796b46106f4f9380970
    :realsig: (Qt::Axis)
    :digest: 40dcabfdafc9aeb3eb5b1efffd090dda

Convenience function to set the axis to *axis*.

Note: the :sip:ref:`~PyQt6.QtCore.Qt.Axis.YAxis` rotation for :sip:ref:`~PyQt6.QtGui.QTransform` is inverted from the correct mathematical rotation in 3D space. The :sip:ref:`~PyQt6.QtWidgets.QGraphicsRotation` class implements a correct mathematical rotation. The following two sequences of code will perform the same transformation:

::

    QTransform t;
    t.rotate(45, Qt::YAxis);

    QGraphicsRotation r;
    r.setAxis(Qt::YAxis);
    r.setAngle(-45);
