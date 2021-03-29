.. sip:method-description::
    :status: todo
    :pysig: 029e87441b45d5e4d592e0b504ba7034
    :realsig: (const QItemSelectionRange&,const QItemSelectionRange&,QItemSelection*)
    :digest: 7a021fd03043948e12f98ffa2c5dd741

Splits the selection *range* using the selection *other* range. Removes all items in *other* from *range* and puts the result in *result*. This can be compared with the semantics of the *subtract* operation of a set.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QItemSelection.merge`.
