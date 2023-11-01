.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (float)
    :digest: b5c09a7418a162e577a784a4f3bdc49f

Sets the line or point width to be used for this geometry to *width*. This property only applies to line width when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLines` or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineStrip`. When supported, it also applies to point size when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawPoints`.

**Note:** Support for point and line drawing may be limited at run time, depending on the platform and graphics API. For example, some APIs do not support point sprites and so setting a size other than 1 is not possible.

**Note:** The width of ``1.0`` is always supported.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.lineWidth`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode`.
