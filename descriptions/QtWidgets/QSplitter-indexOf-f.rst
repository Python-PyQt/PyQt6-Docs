.. sip:method-description::
    :status: todo
    :pysig: 2a38832352a50ffc5e738fd2b818b613
    :realsig: (QWidget*) const
    :digest: 1f73400cf67d8ac1d8f2c9d59775657a

Returns the index in the splitter's layout of the specified *widget*, or -1 if *widget* is not found. This also works for handles.

Handles are numbered from 0. There are as many handles as there are child widgets, but the handle at position 0 is always hidden.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSplitter.count`, :sip:ref:`~PyQt6.QtWidgets.QSplitter.widget`.
