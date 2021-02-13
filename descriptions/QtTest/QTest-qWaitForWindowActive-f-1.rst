.. sip:method-description::
    :status: todo
    :pysig: 720d553c04b75d1e761b2ee2969113a6
    :realsig: (QWidget*,int)
    :digest: fcc230348add0e21298ac5a41c077d14

Waits for *timeout* milliseconds or until the *widget*'s window is active.

Returns ``true`` if ``widget``'s window is active within *timeout* milliseconds, otherwise returns ``false``.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.qWaitForWindowExposed`, :sip:ref:`~PyQt6.QtWidgets.QWidget.isActiveWindow`.
