.. sip:method-description::
    :status: todo
    :pysig: db547d59f57d25909df4080d41fbf34a
    :realsig: (const QString&)
    :digest: 0a7161f88bcd8c38e153803bbf540633

Configures which categories and message types should be enabled through a set of *rules*.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-qloggingcategory-main.py

**Note:** The rules might be ignored if a custom category filter is installed with installFilter(), or if the user has defined the ``QT_LOGGING_CONF`` or the ``QT_LOGGING_RULES`` environment variable.
