.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&)
    :digest: 8050b1e62a7a8b12908cb22e80887b95

Registers the Qt compressed help file (.qch) contained in the file *documentationFileName*. One compressed help file, uniquely identified by its namespace can only be registered once. True is returned if the registration was successful, otherwise false.

.. seealso:: :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.unregisterDocumentation`, :sip:ref:`~PyQt6.QtHelp.QHelpEngineCore.error`.
