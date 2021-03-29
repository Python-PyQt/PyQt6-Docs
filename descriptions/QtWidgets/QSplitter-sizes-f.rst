.. sip:method-description::
    :status: todo
    :pysig: 547b203239a35d1de005c5b84090af5b
    :realsig: () const
    :digest: b06d076fb7976a0f25b68621a8ddb6f3

Returns a list of the size parameters of all the widgets in this splitter.

If the splitter's orientation is horizontal, the list contains the widgets width in pixels, from left to right; if the orientation is vertical, the list contains the widgets' heights in pixels, from top to bottom.

Giving the values to another splitter's :sip:ref:`~PyQt6.QtWidgets.QSplitter.setSizes` function will produce a splitter with the same layout as this one.

Note that invisible widgets have a size of 0.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.setSizes`.
