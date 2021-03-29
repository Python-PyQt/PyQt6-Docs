.. sip:method-description::
    :status: todo
    :pysig: 7b302619a1f8d21d9efa913403e8d56b
    :realsig: (const QRegion&)
    :digest: 03314f617a3b9d2e460475089b11fe50

This is an overloaded function.

Causes only the parts of the widget which overlap *region* to be visible. If the region includes pixels outside the :sip:ref:`~PyQt6.QtWidgets.QWidget.rect` of the widget, window system controls in that area may or may not be visible, depending on the platform.

Note that this effect can be slow if the region is particularly complex.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QWidget.windowOpacity`.
