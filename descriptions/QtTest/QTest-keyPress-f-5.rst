.. sip:method-description::
    :status: todo
    :pysig: f87a8f7e8ce2932757048a1316eab485
    :realsig: (QWidget*,char,Qt::KeyboardModifiers,int)
    :digest: 6672aca5d9d8f4bebd24d29120fa0690

This is an overloaded function.

Simulates pressing a *key* with an optional *modifier* on a *widget*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before pressing the key.

**Note:** At some point you should release the key using :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`, :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
