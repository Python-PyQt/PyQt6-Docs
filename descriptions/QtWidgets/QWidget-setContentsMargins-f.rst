.. sip:method-description::
    :status: todo
    :pysig: 1cf12541c702e4d2092f5ca9947eb176
    :realsig: (const QMargins&)
    :digest: 12aba60cf68586d8abfd62052865ea61

The :sip:ref:`~PyQt6.QtWidgets.QWidget.setContentsMargins` function sets the margins around the widget's contents.

Sets the margins around the contents of the widget to have the sizes determined by *margins*. The margins are used by the layout system, and may be used by subclasses to specify the area to draw in (e.g. excluding the frame).

Changing the margins will trigger a :sip:ref:`~PyQt6.QtWidgets.QWidget.resizeEvent`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.contentsRect`, :sip:ref:`~PyQt6.QtWidgets.QWidget.contentsMargins`.
