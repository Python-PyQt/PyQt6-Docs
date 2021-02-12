.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: 9840b9b12ae233292f67eeb3d246746e

This slot is called just after the internal data of a model is cleared while it is being reset.

This slot is provided the convenience of subclasses of concrete proxy models, such as subclasses of :sip:ref:`~PyQt6.QtCore.QSortFilterProxyModel` which maintain extra data.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qabstractitemmodel.py
    :lines: 114-143

**Note:** Due to a mistake, this slot is missing in Qt 5.0.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelAboutToBeReset`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.modelReset`.
