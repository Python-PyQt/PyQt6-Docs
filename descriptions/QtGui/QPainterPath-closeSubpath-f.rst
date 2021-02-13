.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 7a706891ecca9aaf48d085a124796941

Closes the current subpath by drawing a line to the beginning of the subpath, automatically starting a new path. The current point of the new path is (0, 0).

If the subpath does not contain any elements, this function does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtGui.QPainterPath.moveTo`, Composing a QPainterPath.
