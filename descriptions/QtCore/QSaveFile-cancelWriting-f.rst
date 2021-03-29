.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: dd987c3f2b4b87ddbf1e6053bc7474fa

Cancels writing the new file.

If the application changes its mind while saving, it can call , which sets an error code so that :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` will discard the temporary file.

Alternatively, it can simply make sure not to call :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`.

Further write operations are possible after calling this method, but none of it will have any effect, the written file will be discarded.

This method has no effect when direct write fallback is used. This is the case when saving over an existing file in a readonly directory: no temporary file can be created, so the existing file is overwritten no matter what, and  cannot do anything about that, the contents of the existing file will be lost.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`.
