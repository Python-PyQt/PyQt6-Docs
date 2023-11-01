.. sip:method-description::
    :status: todo
    :pysig: 24dcc4ff91a300d0661b8ec68ace05e4
    :realsig: (const QString&, int, QSystemSemaphore::AccessMode)
    :digest: 26b828a0fca9fa3e16c6e3010152d578

Requests a system semaphore identified by the legacy key *key*. This constructor does the same as:

::

    QSystemSemaphore(QSystemSemaphore::legacyNativeKey(key), initialValue, mode)

except that it stores the legacy native key to retrieve using :sip:ref:`~PyQt6.QtCore.QSystemSemaphore.key`.
