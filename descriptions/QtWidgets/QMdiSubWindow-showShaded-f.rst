.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 1640a772d3de9e1fa08c2776364f4c33

Calling this function makes the subwindow enter the shaded mode. When the subwindow is shaded, only the title bar is visible.

Although shading is not supported by all styles, this function will still show the subwindow as shaded, regardless of whether support for shading is available. However, when used with styles without shading support, the user will be unable to return from shaded mode through the user interface (e.g., through a shade button in the title bar).

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QMdiSubWindow.isShaded`.
