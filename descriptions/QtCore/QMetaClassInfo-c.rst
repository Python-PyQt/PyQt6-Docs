.. sip:class-description::
    :status: todo
    :brief: Additional information about a class
    :digest: d6088490717e73c791295f7731f17025

The :sip:ref:`~PyQt6.QtCore.QMetaClassInfo` class provides additional information about a class.

Class information items are simple *name*--\ *value* pairs that are specified using Q_CLASSINFO() in the source code. The information can be retrieved using :sip:ref:`~PyQt6.QtCore.QMetaClassInfo.name` and :sip:ref:`~PyQt6.QtCore.QMetaClassInfo.value`. For example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_kernel_qmetaobject.py
    :lines: 98-106

This mechanism is free for you to use in your Qt applications. Qt doesn't use it for any of its classes.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QMetaObject`.
