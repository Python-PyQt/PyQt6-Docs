.. sip:method-description::
    :status: todo
    :pysig: 8a611c81aa892a862c71956d75a33554
    :realsig: (QReadWriteLock*)
    :digest: 6a0adfc99d484a1692a23b31bb8439b0

Constructs a :sip:ref:`~PyQt6.QtCore.QWriteLocker` and locks *lock* for writing. The lock will be unlocked when the :sip:ref:`~PyQt6.QtCore.QWriteLocker` is destroyed. If ``lock`` is zero, :sip:ref:`~PyQt6.QtCore.QWriteLocker` does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForWrite`.
