.. sip:method-description::
    :status: todo
    :pysig: ae0ebe165472162f97541d6aa5e727b1
    :realsig: (int,QItemEditorCreatorBase*)
    :digest: 64335148e54901b32fdc2349fb3cf460

Registers an item editor creator specified by *creator* for the given *userType* of data.

**Note:** The factory takes ownership of the item editor creator and will destroy it if a new creator for the same type is registered later.

.. seealso:: :sip:ref:`~PyQt6.QtWidgets.QItemEditorFactory.createEditor`.
