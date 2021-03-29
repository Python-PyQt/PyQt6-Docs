.. sip:method-description::
    :status: todo
    :pysig: 546ade640b6edfbc8a086ef31347e768
    :realsig: () const
    :digest: 74f8da85d628804ec619f9c1f4be8d0b

Gets the current line or point width or to be used for this geometry. This property only applies to line width when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLines`, DarwLineStrip, or :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawLineLoop`. When supported, it also applies to point size when the :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode` is :sip:ref:`~PyQt6.QtQuick.QSGGeometry.DrawingMode.DrawPoints`.

The default value is ``1.0``

**Note:** Support for point and line drawing may be limited at run time, depending on the platform and graphics API. For example, some APIs do not support point sprites and so setting a size other than 1 is not possible.

**Note:** The width of ``1.0`` is always supported.

.. seealso:: :sip:ref:`~PyQt6.QtQuick.QSGGeometry.setLineWidth`, :sip:ref:`~PyQt6.QtQuick.QSGGeometry.drawingMode`.
