.. sip:method-description::
    :status: todo
    :pysig: fd7aa0512f506807b53832094f6e0f7f
    :realsig: (const QFont&,QTextCharFormat::FontPropertiesInheritanceBehavior)
    :digest: cc44a2c4de097c6f47e9d0ac1cccf1cc

Sets the text format's *font*.

If *behavior* is :sip:ref:`~PyQt6.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior.FontPropertiesAll`, the font property that has not been explicitly set is treated like as it were set with default value; If *behavior* is :sip:ref:`~PyQt6.QtGui.QTextCharFormat.FontPropertiesInheritanceBehavior.FontPropertiesSpecifiedOnly`, the font property that has not been explicitly set is ignored and the respective property value remains unchanged.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QTextCharFormat.font`.
