.. sip:signal-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: e77e71e7e42fb45c84fcb4090172d031

This signal is emitted from the associated thread when it starts executing, so any slots connected to it may be called via queued invocation. Whilst the event may have been posted before :sip:ref:`~PyQt6.QtCore.QThread.run` is called, any cross-thread delivery of the signal may still be pending.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QThread.run`, :sip:ref:`~PyQt6.QtCore.QThread.finished`.
