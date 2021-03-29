.. sip:method-description::
    :status: todo
    :pysig: 30985e3a4dd64cc7ba58e0a7032868a2
    :realsig: (const QList<int>&)
    :digest: 2aff09daccb726b0c1270494573b32f4

Sets the child widgets' respective sizes to the values given in the *list*.

If the splitter is horizontal, the values set the width of each widget in pixels, from left to right. If the splitter is vertical, the height of each widget is set, from top to bottom.

Extra values in the *list* are ignored. If *list* contains too few values, the result is undefined, but the program will still be well-behaved.

The overall size of the splitter widget is not affected. Instead, any additional/missing space is distributed amongst the widgets according to the relative weight of the sizes.

If you specify a size of 0, the widget will be invisible. The size policies of the widgets are preserved. That is, a value smaller than the minimal size hint of the respective widget will be replaced by the value of the hint.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.sizes`.
