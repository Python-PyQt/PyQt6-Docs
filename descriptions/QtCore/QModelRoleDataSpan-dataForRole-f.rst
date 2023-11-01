.. sip:method-description::
    :status: todo
    :pysig: 929edda6a97571ebce7151ff0802751f
    :realsig: (int) const
    :digest: 8317ea5b0042096deb758ecd4306554d

Returns the data associated with the first :sip:ref:`~PyQt6.QtCore.QModelRoleData` in the span that has its role equal to *role*. If such a :sip:ref:`~PyQt6.QtCore.QModelRoleData` object does not exist, the behavior is undefined.

**Note:** Avoid calling this function from the model's side, as a model cannot possibly know in advance which roles are in a given :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan`. This function is instead suitable for views and delegates, which have control over the roles in the span.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QModelRoleData.data`.
