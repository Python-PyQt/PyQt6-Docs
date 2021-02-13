.. sip:method-description::
    :status: todo
    :pysig: 05c287a441ae03c4134102d2a8e2c97b
    :realsig: (Qt::TextFormat)
    :digest: ab6b667872db47f62b7fb2c52af6dae2

Sets the text format of the :sip:ref:`~PyQt6.QtGui.QStaticText` to *textFormat*. If *textFormat* is set to :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.AutoText` (the default), the format of the text will try to be determined using the function Qt::mightBeRichText(). If the text format is :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.PlainText`, then the text will be displayed as is, whereas it will be interpreted as HTML if the format is :sip:ref:`~PyQt6.QtCore.Qt.TextFormat.RichText`. HTML tags that alter the font of the text, its color, or its layout are supported by :sip:ref:`~PyQt6.QtGui.QStaticText`.

**Note:** This function will cause the layout of the text to require recalculation.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QStaticText.textFormat`, :sip:ref:`~PyQt6.QtGui.QStaticText.setText`, :sip:ref:`~PyQt6.QtGui.QStaticText.text`.
