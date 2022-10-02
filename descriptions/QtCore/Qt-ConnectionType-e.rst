.. sip:enum-description::
    :status: todo
    :digest: 8f0b49eb5a8dfc3ea5f00e20d88a1441

This enum describes the types of connection that can be used between signals and slots. In particular, it determines whether a particular signal is delivered to a slot immediately or queued for delivery at a later time.

With queued connections, the parameters must be of types that are known to Qt's meta-object system, because Qt needs to copy the arguments to store them in an event behind the scenes. If you try to use a queued connection and get the error message:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-doc_src_qnamespace.qdoc
    :lines: 54-54

Call qRegisterMetaType() to register the data type before you establish the connection.

When using signals and slots with multiple threads, see Signals and Slots Across Threads.

.. seealso:: QObject::connect(), qRegisterMetaType(), Q_DECLARE_METATYPE(), Thread Support in Qt.
