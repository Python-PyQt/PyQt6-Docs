.. sip:method-description::
    :status: todo
    :pysig: 0c984aa5f8699fdaa47ca7ca1eb6cc0d
    :realsig: (int,int) const
    :digest: b18dba759a5b4d0f3d011d099c885c91

Returns the geometry of the cell with row *row* and column *column* in the grid. Returns an invalid rectangle if *row* or *column* is outside the grid.

**Warning:** in the current version of Qt this function does not return valid results until :sip:ref:`~PyQt6.QtWidgets.QGridLayout.setGeometry` has been called, i.e. after the parentWidget() is visible.
