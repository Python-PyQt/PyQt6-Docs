.. sip:method-description::
    :status: todo
    :pysig: 720d553c04b75d1e761b2ee2969113a6
    :realsig: (QWidget*,int)
    :digest: bab51e2d38d5bf48261c74296f7a610b

Returns ``true`` if *widget* is active within *timeout* milliseconds. Otherwise returns ``false``.

The method is useful in tests that call :sip:ref:`~PyQt6.QtWidgets.QWidget.show` and rely on the widget actually being active (i.e. being visible and having focus) before proceeding.

**Note:** The method will time out and return ``false`` if another window prevents *widget* from becoming active.

**Note:** Since focus is an exclusive property, *widget* may loose its focus to another window at any time - even after the method has returned ``true``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowExposed`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isActiveWindow`.
