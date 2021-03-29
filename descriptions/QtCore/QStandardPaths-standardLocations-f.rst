.. sip:method-description::
    :status: todo
    :pysig: 7f0e6a6136be9ff51f6a3dbcf7929950
    :realsig: (QStandardPaths::StandardLocation)
    :digest: d79575e0c10b959661384e450e9c0ae4

Returns all the directories where files of *type* belong.

The list of directories is sorted from high to low priority, starting with :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation` if it can be determined. This list is empty if no locations for type are defined.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QStandardPaths.writableLocation`.
