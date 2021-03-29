.. sip:method-description::
    :status: todo
    :pysig: 4961e780006a785f3453b8c96ac851b2
    :realsig: (QWidget*,Qt::Key,Qt::KeyboardModifiers,int)
    :digest: 8259df3c3cc1c6cb3207d692fc0abc08

Simulates pressing a *key* with an optional *modifier* on a *widget*. If *delay* is larger than 0, the test will wait for *delay* milliseconds before pressing the key.

**Note:** At some point you should release the key using :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`.

.. seealso:: :sip:ref:`~PyQt6.QtTest.QTest.keyRelease`, :sip:ref:`~PyQt6.QtTest.QTest.keyClick`.
