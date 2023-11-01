.. sip:method-description::
    :status: todo
    :pysig: 1f92def01ce80c9570f8deb0064ab1a1
    :realsig: (const QModelIndex&, QModelRoleDataSpan) const
    :digest: 1be07f36765b2bbbc36ab1f1b15caedb

Fills the *roleDataSpan* with the requested data for the given *index*.

The default implementation will call simply :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` for each role in the span. A subclass can reimplement this function to provide data to views more efficiently:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 171-180

In the snippet above, ``index`` is the same for the entire call. This means that accessing to the necessary data structures in order to retrieve the information for ``index`` can be done only once (hoisting the relevant code out of the loop).

The usage of :sip:ref:`~PyQt6.QtCore.QModelRoleData.setData`, or similarly QVariant::setValue(), is encouraged over constructing a :sip:ref:`~PyQt6.QtCore.QVariant` separately and using a plain assignment operator; this is because the former allow to re-use the memory already allocated for the :sip:ref:`~PyQt6.QtCore.QVariant` object stored inside a :sip:ref:`~PyQt6.QtCore.QModelRoleData`, while the latter always allocates the new variant and then destroys the old one.

Note that views may call multiData() with spans that have been used in previous calls, and therefore may already contain some data. Therefore, it is imperative that if the model cannot return the data for a given role, then it must clear the data in the corresponding :sip:ref:`~PyQt6.QtCore.QModelRoleData` object. This can be done by calling :sip:ref:`~PyQt6.QtCore.QModelRoleData.clearData`, or similarly by setting a default constructed :sip:ref:`~PyQt6.QtCore.QVariant`, and so on. Failure to clear the data will result in the view believing that the "old" data is meant to be used for the corresponding role.

Finally, in order to avoid code duplication, a subclass may also decide to reimplement :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data` in terms of multiData(), by supplying a span of just one element:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 184-189

**Note:** Models are not allowed to modify the roles in the span, or to rearrange the span elements. Doing so results in undefined behavior.

**Note:** It is illegal to pass an invalid model index to this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QModelRoleDataSpan`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.data`.
