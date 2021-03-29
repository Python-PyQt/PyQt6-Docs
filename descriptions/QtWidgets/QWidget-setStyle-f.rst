.. sip:method-description::
    :status: todo
    :pysig: 7cce74340329521a145f04963f5c9bd7
    :realsig: (QStyle*)
    :digest: 5ee24d68e7b0bf16af3dbb78900cd23a

Sets the widget's GUI style to *style*. The ownership of the style object is not transferred.

If no style is set, the widget uses the application's style, :sip:ref:`~PyQt6.QtWidgets.QApplication.style` instead.

Setting a widget's style has no effect on existing or future child widgets.

**Warning:** This function is particularly useful for demonstration purposes, where you want to show Qt's styling capabilities. Real applications should avoid it and use one consistent GUI style instead.

**Warning:** Qt style sheets are currently not supported for custom :sip:ref:`~PyQt6.QtWidgets.QStyle` subclasses. We plan to address this in some future release.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.style`, :sip:ref:`~PyQt6.QtWidgets.QStyle`, :sip:ref:`~PyQt6.QtWidgets.QApplication.style`, :sip:ref:`~PyQt6.QtWidgets.QApplication.setStyle`.
