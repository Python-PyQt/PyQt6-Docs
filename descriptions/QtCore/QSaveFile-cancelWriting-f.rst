.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fe7951da0cd67d54021ef9f5ffd0c062

Cancels writing the new file.

If the application changes its mind while saving, it can call cancelWriting(), which sets an error code so that :sip:ref:`~PyQt6.QtCore.QSaveFile.commit` will discard the temporary file.

Alternatively, it can simply make sure not to call :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`.

Further write operations are possible after calling this method, but none of it will have any effect, the written file will be discarded.

This method has no effect when direct write fallback is used. This is the case when saving over an existing file in a readonly directory: no temporary file can be created, so the existing file is overwritten no matter what, and cancelWriting() cannot do anything about that, the contents of the existing file will be lost.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSaveFile.commit`.
