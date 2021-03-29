.. sip:method-description::
    :status: todo
    :pysig: 960328c85553ae1600ceaa798f7f1902
    :realsig: (int) const
    :digest: 9c7602d2e28b2b6137032a3c022ad15d

Returns the handle to the left of (or above) the item in the splitter's layout at the given *index*, or ``nullptr`` if there is no such item. The handle at index 0 is always hidden.

For right-to-left languages such as Arabic and Hebrew, the layout of horizontal splitters is reversed. The handle will be to the right of the widget at *index*.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.count`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.indexOf`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.createHandle`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.setHandleWidth`.
