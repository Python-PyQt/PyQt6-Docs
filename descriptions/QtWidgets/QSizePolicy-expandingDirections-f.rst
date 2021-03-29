.. sip:method-description::
    :status: todo
    :pysig: 85a9c432f1c6b1045b6a2985f6e19517
    :realsig: () const
    :digest: 2148ceb9f012711d13dc3090f4267dc3

Returns whether a widget can make use of more space than the :sip:ref:`~PyQt6.QtWidgets.QWidget.sizeHint` function indicates.

A value of :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Horizontal` or :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical` means that the widget can grow horizontally or vertically (i.e., the horizontal or vertical policy is :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.Expanding` or :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.Policy.MinimumExpanding`), whereas :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Horizontal` | :sip:ref:`~PyQt6.QtCore.Qt.Orientations.Vertical` means that it can grow in both dimensions.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.horizontalPolicy`, :sip:ref:`~PyQt6.QtWidgets.QSizePolicy.verticalPolicy`.
