.. sip:method-description::
    :status: todo
    :pysig: b730747ccdc682ff41f5a1b741c1a110
    :realsig: () const
    :digest: b2588f23ba40fe89e90473f830ecade1

Returns the drop actions supported by this model.

The default implementation returns :sip:ref:`~PyQt6.QtCore.Qt.DropActions.CopyAction`. Reimplement this function if you wish to support additional actions. You must also reimplement the :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData` function to handle the additional operations.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QAbstractItemModel.dropMimeData`, Qt::DropActions.
