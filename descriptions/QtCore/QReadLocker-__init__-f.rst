.. sip:method-description::
    :status: todo
    :pysig: 8a611c81aa892a862c71956d75a33554
    :realsig: (QReadWriteLock*)
    :digest: cb763498d20993c19d3cacccd79699a0

Constructs a :sip:ref:`~PyQt6.QtCore.QReadLocker` and locks *lock* for reading. The lock will be unlocked when the :sip:ref:`~PyQt6.QtCore.QReadLocker` is destroyed. If ``lock`` is zero, :sip:ref:`~PyQt6.QtCore.QReadLocker` does nothing.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QReadWriteLock.lockForRead`.
