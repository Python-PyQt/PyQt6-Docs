.. sip:method-description::
    :status: todo
    :pysig: 3492941b7185ab01b7b322b81d6a6906
    :realsig: (const QRectF&, int, const QString&)
    :digest: 565edc2c78575c0bda9b0e1a9a98a2fc

Returns the bounding rectangle of the *text* as it will appear when drawn inside the given *rectangle* with the specified *flags* using the currently set :sip:ref:`~PyQt6.QtGui.QPainter.font`; i.e the function tells you where the :sip:ref:`~PyQt6.QtGui.QPainter.drawText` function will draw when given the same arguments.

If the *text* does not fit within the given *rectangle* using the specified *flags*, the function returns the required rectangle.

The *flags* argument is a bitwise OR of the following flags:

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignLeft`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignRight`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignHCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignTop`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignBottom`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignVCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignCenter`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextSingleLine`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextExpandTabs`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextShowMnemonic`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextWordWrap`

* :sip:ref:`~PyQt6.QtCore.Qt.TextFlag.TextIncludeTrailingSpaces`

If several of the horizontal or several of the vertical alignment flags are set, the resulting alignment is undefined.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainter.drawText`, Qt::Alignment, :sip:ref:`~PyQt6.QtCore.Qt.TextFlag`.
