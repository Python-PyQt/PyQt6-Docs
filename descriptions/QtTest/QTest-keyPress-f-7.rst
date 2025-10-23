.. sip:method-description::
    :status: todo
    :pysig: 8adf6519edc601294efee9ee2694c93a
    :realsig: (QWindow*,char,Qt::KeyboardModifiers,int)
    :digest: 4b55a04cb74370bef9d56fc6dad27bdf

Simulates pressing a *key* with an optional *modifier* on a *window*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before pressing the key.

**Note:** At some point you should release the key using :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`, :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
