.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 08f03dc94d7b33fcfaecee4fd27c03b8

Unloads the library and returns ``true`` if the library could be unloaded; otherwise returns ``false``.

This happens automatically on application termination, so you shouldn't normally need to call this function.

If other instances of :sip:ref:`~PyQt6.QtCore.QLibrary` are using the same library, the call will fail, and unloading will only happen when every instance has called unload().

Note that on macOS, dynamic libraries cannot be unloaded. QLibrary::unload() will return ``true``, but the library will remain loaded into the process.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.resolve`, :sip:ref:`~PyQt6.QtCore.QLibrary.load`.
