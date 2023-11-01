.. sip:method-description::
    :status: todo
    :pysig: 96e648b0c213feb955e3dc2c56751cf2
    :realsig: (const QString&)
    :digest: e451f94177157e7513661a5cdcc95d3c

Constructs a new lock file object. The object is created in an unlocked state. When calling :sip:ref:`~PyQt6.QtCore.QLockFile.lock` or :sip:ref:`~PyQt6.QtCore.QLockFile.tryLock`, a lock file named *fileName* will be created, if it doesn't already exist.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QLockFile.lock`, :sip:ref:`~PyQt6.QtCore.QLockFile.unlock`.
