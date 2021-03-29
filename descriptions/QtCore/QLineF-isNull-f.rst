.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: 6461a41995c1b7dabb4cfc6e92bdd8ab

Returns ``true`` if the line does not have distinct start and end points; otherwise returns ``false``. The start and end points are considered distinct if :sip:ref:`~PyQt6.QtCore.qFuzzyCompare` can distinguish them in at least one coordinate.

**Note:** Due to the use of fuzzy comparison,  may return ``true`` for lines whose :sip:ref:`~PyQt6.QtCore.QLineF.length` is not zero.

.. seealso:: :sip:ref:`~PyQt6.QtCore.qFuzzyCompare`, :sip:ref:`~PyQt6.QtCore.QLineF.length`.
