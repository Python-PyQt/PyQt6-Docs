.. sip:method-description::
    :status: todo
    :pysig: 91c276dfd3be4716580ee2e83e676947
    :realsig: (QWindow*,Qt::Key,Qt::KeyboardModifiers,int)
    :digest: 7a9b0ec47f4e71e5e5e47e1388c875dc

This is an overloaded function.

Simulates pressing a *key* with an optional *modifier* on a *window*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before pressing the key.

**Note:** At some point you should release the key using :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`, :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
