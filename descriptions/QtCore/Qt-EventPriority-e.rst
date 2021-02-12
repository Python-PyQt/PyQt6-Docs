.. sip:enum-description::
    :status: todo
    :digest: 9aae73a0a10daf6b672fd02fff22da11

This enum can be used to specify event priorities.

Note that these values are provided purely for convenience, since event priorities can be any value between ``INT_MAX`` and ``INT_MIN``, inclusive. For example, you can define custom priorities as being relative to each other:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-doc_src_qnamespace.py
    :lines: 54-70

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCoreApplication.postEvent`.
