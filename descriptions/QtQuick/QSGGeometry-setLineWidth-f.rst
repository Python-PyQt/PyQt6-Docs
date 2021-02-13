.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: (float)
    :digest: b3f8d9e9ac025958c705121da7177764

Sets the line or point width to be used for this geometry to *width*. This property only applies to line width when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLines`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineStrip`, or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineLoop`. When supported, it also applies to point size when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawPoints`.

**Note:** Support for point and line drawing may be limited at run time, depending on the platform and graphics API. For example, some APIs do not support point sprites and so setting a size other than 1 is not possible.

**Note:** The width of ``1.0`` is always supported.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.lineWidth`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode`.
