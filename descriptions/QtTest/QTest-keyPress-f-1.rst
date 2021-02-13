.. sip:method-description::
    :status: todo
    :pysig: ab43e1ec5e249b661f37b326a7107294
    :realsig: (QWidget*,char,Qt::KeyboardModifiers,int)
    :digest: 6672aca5d9d8f4bebd24d29120fa0690

This is an overloaded function.

Simulates pressing a *key* with an optional *modifier* on a *widget*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before pressing the key.

**Note:** At some point you should release the key using :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`, :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
