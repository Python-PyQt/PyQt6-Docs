.. sip:class-description::
    :status: todo
    :brief: Holds a role and the data associated to that role
    :digest: 7dfa473ded0a16b33bc9ffa57023be86

The :sip:ref:`~PyQt6.QtCore.QModelRoleData` class holds a role and the data associated to that role.

:sip:ref:`~PyQt6.QtCore.QModelRoleData` objects store an item role (which is a value from the :sip:ref:`~PyQt6.QtCore.Qt.ItemDataRole` enumeration, or an arbitrary integer for a custom role) as well as the data associated with that role.

A :sip:ref:`~PyQt6.QtCore.QModelRoleData` object is typically created by views or delegates, setting which role they want to fetch the data for. The object is then passed to models (see QAbstractItemModel::multiData()), which populate the data corresponding to the role stored. Finally, the view visualizes the data retrieved from the model.

.. seealso:: QModelRoleDataSpan, Model/View Programming.
