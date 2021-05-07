.. sip:method-description::
    :status: todo
    :pysig: a29ebb5461372b347ff3abc2a8a150d2
    :realsig: (const QCollatorSortKey&) const
    :digest: e3ca8c89046b1e7a98e8d8011bc23b98

Compares this key to *otherKey*, which must have been created by the same :sip:ref:`~PyQt6.QtCore.QCollator`'s sortKey() as this key. The comparison is performed in accordance with that :sip:ref:`~PyQt6.QtCore.QCollator`'s sort order.

Returns a negative value if this key sorts before *otherKey*, 0 if the two keys are equal or a positive value if this key sorts after *otherKey*.

.. seealso:: operator<().
