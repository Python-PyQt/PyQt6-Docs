.. sip:method-description::
    :status: todo
    :pysig: 58413b4abf8ce2e29dba4e96faa26ac0
    :realsig: (QWindow*,int)
    :digest: 6d40d366646b136b23f2faaf8d5a7e2f

Returns ``true``, if *window* is exposed within *timeout* milliseconds. Otherwise returns ``false``.

The method is useful in tests that call :sip:ref:`~PyQt6.QtGui.QWindow.show` and rely on the window actually being being visible before proceeding.

**Note:** A window mapped to screen may still not be considered exposed, if the window client area is not visible, e.g. because it is completely covered by other windows. In such cases, the method will time out and return ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowActive`, :sip:ref:`~PyQt6.QtGui.QWindow.isExposed`.
