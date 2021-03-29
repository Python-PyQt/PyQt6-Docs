.. sip:method-description::
    :status: todo
    :pysig: 45b97e0942bb94ca81e22ff1293f6d73
    :realsig: (const QScrollerProperties&)
    :digest: 9ab400fa33b2cbc6647464f6e1802db4

Sets the scroller properties for all new :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties` objects to *sp*.

Use this function to override the platform default properties returned by the default constructor. If you only want to change the scroller properties of a single scroller, use :sip:ref:`~PyQt6.QtWidgets.QScroller.setScrollerProperties`

**Note:** Calling this function will not change the content of already existing :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties` objects.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QScrollerProperties.unsetDefaultScrollerProperties`.
