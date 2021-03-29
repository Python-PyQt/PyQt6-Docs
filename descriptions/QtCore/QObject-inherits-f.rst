.. sip:method-description::
    :status: todo
    :pysig: 9d2496c01394f04863ec354dfad3b4be
    :realsig: (const char*) const
    :digest: 371e3ce5070e7f9b21db83a0b4679a7e

Returns ``true`` if this object is an instance of a class that inherits *className* or a :sip:ref:`~PyQt6.QtCore.QObject` subclass that inherits *className*; otherwise returns ``false``.

A class is considered to inherit itself.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 81-89

If you need to determine whether an object is an instance of a particular class for the purpose of casting it, consider using qobject_cast<Type \*>(object) instead.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.metaObject`, qobject_cast().
