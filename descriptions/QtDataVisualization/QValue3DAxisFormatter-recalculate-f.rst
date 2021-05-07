.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 2d030a6a9cd2dcb0e076ee0570aac5b5

Resizes and populates the label and grid line position arrays and the label strings array, as well as calculates any values needed to map a value to its position. The parent axis can be accessed from inside this function.

This method must be reimplemented in a subclass if the default array contents are not suitable.

See :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.gridPositions`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.subGridPositions`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.labelPositions`, and :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.labelStrings` methods for documentation about the arrays that need to be resized and populated.

.. seealso:: :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.gridPositions`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.subGridPositions`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.labelPositions`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.labelStrings`, :sip:ref:`~PyQt6.QtDataVisualization.QValue3DAxisFormatter.axis`.
