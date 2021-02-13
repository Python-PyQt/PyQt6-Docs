.. sip:method-description::
    :status: todo
    :pysig: c0199cb465a8cea34ddeb3b3f26b2747
    :realsig: (const QWidget*) const
    :digest: eff35e792011c88d8c0181ca86ae8423

Returns ``true`` if this widget would become visible if *ancestor* is shown; otherwise returns ``false``.

The true case occurs if neither the widget itself nor any parent up to but excluding *ancestor* has been explicitly hidden.

This function will still return true if the widget is obscured by other windows on the screen, but could be physically visible if it or they were to be moved.

(0) is identical to :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.show`, :sip:ref:`~PyQt6.QtWidgets.QWidget.hide`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isVisible`.
