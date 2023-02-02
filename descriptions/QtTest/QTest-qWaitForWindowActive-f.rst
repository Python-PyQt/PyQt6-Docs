.. sip:method-description::
    :status: todo
    :pysig: 58413b4abf8ce2e29dba4e96faa26ac0
    :realsig: (QWindow*,int)
    :digest: 23d9254f248649ebd97a8555cb159b64

Returns ``true``, if *window* is active within *timeout* milliseconds. Otherwise returns ``false``.

The method is useful in tests that call :sip:ref:`~PyQt6.QtGui.QWindow.show` and rely on the window actually being active (i.e. being visible and having focus) before proceeding.

**Note:** The method will time out and return ``false`` if another window prevents *window* from becoming active.

**Note:** Since focus is an exclusive property, *window* may loose its focus to another window at any time - even after the method has returned ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowExposed`, :sip:ref:`~PyQt6.QtGui.QWindow.isActive`.
