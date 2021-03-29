.. sip:method-description::
    :status: todo
    :pysig: 9e1886ac630cf2cdefc520d9e42edfb2
    :realsig: (const QBitArray&)
    :digest: bfefa8c3cff4cc05277fa95c3f6d3d03

Constructs a copy of *other*.

This operation takes `constant time <https://doc.qt.io/qt-6/containers.html#constant-time>`_, because :sip:ref:`~PyQt6.QtCore.QBitArray` is `implicitly shared <https://doc.qt.io/qt-6/implicit-sharing.html>`_. This makes returning a :sip:ref:`~PyQt6.QtCore.QBitArray` from a function very fast. If a shared instance is modified, it will be copied (copy-on-write), and that takes `linear time <https://doc.qt.io/qt-6/containers.html#linear-time>`_.

.. seealso:: operator=().
