.. sip:method-description::
    :status: todo
    :pysig: 2b9057d9b4a06375acf76e6922f506e2
    :realsig: () const
    :digest: 84da7518c9030e644817c992c8479cec

If the source of the drag operation is a widget in this application, this function returns that source; otherwise it returns ``nullptr``. The source of the operation is the first parameter to the :sip:ref:`~PyQt6.QtGui.QDrag` object used instantiate the drag.

This is useful if your widget needs special behavior when dragging to itself.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QDrag.__init__`.
