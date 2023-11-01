.. sip:method-description::
    :status: todo
    :pysig: 59deef16a694b0a586880f637fa3acb0
    :realsig: (const QByteArray&)
    :digest: 8d523f1bf580eda9c0118b1e2b8eaf98

Constructs a copy of *other*.

This operation takes `constant time <https://doc.qt.io/qt-6/containers.html#constant-time>`_, because :sip:ref:`~PyQt6.QtCore.QByteArray` is `implicitly shared <https://doc.qt.io/qt-6/implicit-sharing.html>`_. This makes returning a :sip:ref:`~PyQt6.QtCore.QByteArray` from a function very fast. If a shared instance is modified, it will be copied (copy-on-write), taking `linear time <https://doc.qt.io/qt-6/containers.html#linear-time>`_.

.. seealso:: operator=().
