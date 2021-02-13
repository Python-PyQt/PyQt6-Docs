.. sip:method-description::
    :status: todo
    :pysig: 58413b4abf8ce2e29dba4e96faa26ac0
    :realsig: (QWindow*,int)
    :digest: 1859823e60e744e929f78bba5a8aeeb5

Waits for *timeout* milliseconds or until the *window* is active.

Returns ``true`` if ``window`` is active within *timeout* milliseconds, otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowExposed`, :sip:ref:`~PyQt6.QtGui.QWindow.isActive`.
