.. sip:method-description::
    :status: todo
    :pysig: 302a41fe379c5b50639ac636a926b5a6
    :realsig: (Qt::LayoutDirection,Qt::Alignment)
    :digest: 011ab8cc464efe57e4407008a30060bb

Transforms an *alignment* of :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignLeft` or :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignRight` without :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignAbsolute` into :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignLeft` or :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignRight` with :sip:ref:`~PyQt6.QtCore.Qt.Alignment.AlignAbsolute` according to the layout *direction*. The other alignment flags are left untouched.

If no horizontal alignment was specified, the function returns the default alignment for the given layout *direction*.

:sip:ref:`~PyQt6.QtWidgets.QWidget.layoutDirection`
