.. sip:method-description::
    :status: done
    :pysig: 2dc4d027fd647cf7ed6349c52106fddb

This initialises a :sip:ref:`~PyQt6.QtCore.QPyTableRange` instance that
encapsulates a Python object that implements a table range.  If the
``editable`` parameter is ``True`` then the object can be modified by the view
that is used to display the object.

The Python object must be a sequence of sequences where the outer sequence
represents the table's rows and the inner sequences represent the columns for
each row.  If the range is editable then, more specifically, it must be a
sequence of lists.

The :sip:ref:`~PyQt6.QtCore.QRangeModel` takes ownership of the
:sip:ref:`~PyQt6.QtCore.QPyTableRange`.
