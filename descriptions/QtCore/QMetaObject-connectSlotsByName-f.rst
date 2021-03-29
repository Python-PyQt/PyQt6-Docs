.. sip:method-description::
    :status: todo
    :pysig: d24f736d504297483d6f5c3f5ebb6f4d
    :realsig: (QObject*)
    :digest: 8a0ae69b70588637a07a15955d91165a

Searches recursively for all child objects of the given *object*, and connects matching signals from them to slots of *object* that follow the following form:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 364-364

Let's assume our object has a child object of type ``QPushButton`` with the :sip:ref:`~PyQt6.QtCore.QObject.objectName` ``button1``. The slot to catch the button's ``clicked()`` signal would be:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qobject.py
    :lines: 369-369

If *object* itself has a properly set object name, its own signals are also connected to its respective slots.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QObject.setObjectName`.
