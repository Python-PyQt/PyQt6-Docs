.. sip:class-description::
    :status: todo
    :brief: Additional information about a class
    :digest: 765dfeebb71fa623a0c6f9575c7316c6

The :sip:ref:`~PyQt6.QtCore.QMetaClassInfo` class provides additional information about a class.

Class information items are simple *name*–\ *value* pairs that are specified using Q_CLASSINFO() in the source code. The information can be retrieved using :sip:ref:`~PyQt6.QtCore.QMetaClassInfo.name` and :sip:ref:`~PyQt6.QtCore.QMetaClassInfo.value`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 98-106

This mechanism is free for you to use in your Qt applications.

**Note:** It's also used by the `Active Qt <https://doc.qt.io/qt-6/activeqt-index.html>`_, `Qt D-Bus <https://doc.qt.io/qt-6/qtdbus-index.html>`_, `Qt Qml <https://doc.qt.io/qt-6/qtqml-index.html>`_, and `Qt Remote Objects <https://doc.qt.io/qt-6/qtremoteobjects-index.html>`_ modules. Some keys might be set when using these modules.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject`.
