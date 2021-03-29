.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: d1f0d18d8c9a75c6f2c049e54ed1a348

Loads the library and returns ``true`` if the library was loaded successfully; otherwise returns ``false``. Since :sip:ref:`~PyQt6.QtCore.QLibrary.resolve` always calls this function before resolving any symbols it is not necessary to call it explicitly. In some situations you might want the library loaded in advance, in which case you would use this function.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.unload`.
