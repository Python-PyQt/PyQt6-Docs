.. sip:class-description::
    :status: todo
    :brief: Used to locate data in a data model
    :digest: 1ebbfe43f12bdbf41cf131fe33a7e83b

The :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex` class is used to locate data in a data model.

A :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex` is a model index that can be stored by an application, and later used to access information in a model. Unlike the :sip:ref:`~PyQt6.QtCore.QModelIndex` class, it is safe to store a :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex` since the model will ensure that references to items will continue to be valid as long as they can be accessed by the model.

It is good practice to check that persistent model indexes are valid before using them.

**Note:** You cannot store a QStandardItemModel's :sip:ref:`~PyQt6.QtCore.QPersistentModelIndex` in one of the model's items.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QModelIndex`, :sip:ref:`~PyQt6.QtCore.QAbstractItemModel`, Model/View Programming.
