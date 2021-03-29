.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: ()
    :digest: 5dfd2ee723b84584d4c2924870fda443

Unloads the library and returns ``true`` if the library could be unloaded; otherwise returns ``false``.

This happens automatically on application termination, so you shouldn't normally need to call this function.

If other instances of :sip:ref:`~PyQt6.QtCore.QLibrary` are using the same library, the call will fail, and unloading will only happen when every instance has called .

Note that on Mac OS X 10.3 (Panther), dynamic libraries cannot be unloaded.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLibrary.resolve`, :sip:ref:`~PyQt6.QtCore.QLibrary.load`.
