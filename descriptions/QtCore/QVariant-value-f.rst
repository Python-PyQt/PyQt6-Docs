.. sip:method-description::
    :status: todo
    :pysig: a8cfde6331bd59eb2ac96f8911c4b666
    :realsig: () const
    :digest: c52db72942e265c9f1739212e1fef6bb

Returns the stored value converted to the template type ``T``. Call :sip:ref:`~PyQt6.QtCore.QVariant.canConvert` to find out whether a type can be converted. If the value cannot be converted, a `default-constructed value <https://doc.qt.io/qt-6/containers.html#default-constructed-value>`_ will be returned.

If the type ``T`` is supported by :sip:ref:`~PyQt6.QtCore.QVariant`, this function behaves exactly as toString(), toInt() etc.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 112-121

If the :sip:ref:`~PyQt6.QtCore.QVariant` contains a pointer to a type derived from :sip:ref:`~PyQt6.QtCore.QObject` then ``T`` may be any :sip:ref:`~PyQt6.QtCore.QObject` type. If the pointer stored in the :sip:ref:`~PyQt6.QtCore.QVariant` can be qobject_cast to T, then that result is returned. Otherwise ``nullptr`` is returned. Note that this only works for :sip:ref:`~PyQt6.QtCore.QObject` subclasses which use the Q_OBJECT macro.

If the :sip:ref:`~PyQt6.QtCore.QVariant` contains a sequential container and ``T`` is QVariantList, the elements of the container will be converted into :sip:ref:`~PyQt6.QtCore.QVariant`\ s and returned as a QVariantList.

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qvariant.py
    :lines: 151-172

.. seealso:: setValue(), fromValue(), :sip:ref:`~PyQt6.QtCore.QVariant.canConvert`, Q_DECLARE_SEQUENTIAL_CONTAINER_METATYPE().
