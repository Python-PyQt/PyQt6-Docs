.. sip:method-description::
    :status: todo
    :pysig: 185bd06397c71792cb6d1af60a1f3dcf
    :realsig: (qreal,qreal) const
    :digest: 70bf51f86bce051bb46b58265f84413e

Returns the height of the lines in the paragraph based on the height of the script line given by *scriptLineHeight* and the specified *scaling* factor.

The value that is returned is also dependent on the given :sip:ref:`~PyQt6.QtGui.QTextFormat.Property.LineHeightType` of the paragraph as well as the :sip:ref:`~PyQt6.QtGui.QTextFormat.Property.LineHeight` setting that has been set for the paragraph.

The scaling is needed for heights that include a fixed number of pixels, to scale them appropriately for printing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.LineHeightTypes.LineHeightTypes`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.setLineHeight`, :sip:ref:`~PyQt6.QtGui.QTextBlockFormat.lineHeightType`.
