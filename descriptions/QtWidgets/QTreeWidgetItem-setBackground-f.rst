.. sip:method-description::
    :status: todo
    :pysig: 030e147e847b6532f0ce63595028bef8
    :realsig: (int,const QBrush&)
    :digest: be5c7990b2ba445ec8eaf51327221df3

Sets the background brush of the label in the given *column* to the specified *brush*. Setting a default-constructed brush will let the view use the default color from the style.

**Note:** If `Qt Style Sheets <https://doc.qt.io/qt-6/stylesheet.html>`_ are used on the same widget as , style sheets will take precedence if the settings conflict.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.background`, :sip:ref:`~PyQt6.QtWidgets.QTreeWidgetItem.setForeground`.
