.. sip:class-description::
    :status: todo
    :brief: Access to the details about a compressed help file
    :digest: f1143d3dff19d6ece0bff305860f81e1

The :sip:ref:`~PyQt6.QtHelp.QCompressedHelpInfo` class provides access to the details about a compressed help file.

The detailed information about the compressed help file can be fetched by calling the :sip:ref:`~PyQt6.QtHelp.QCompressedHelpInfo.fromCompressedHelpFile` static method, providing the path to the compressed help file.

The class provides access to various information about a compressed help file. The namespace associated with the given compressed help file is :sip:ref:`~PyQt6.QtHelp.QCompressedHelpInfo.namespaceName`, the associated component name is :sip:ref:`~PyQt6.QtHelp.QCompressedHelpInfo.component` and :sip:ref:`~PyQt6.QtHelp.QCompressedHelpInfo.version` provides version information.

.. seealso:: :sip:ref:`~PyQt6.QtHelp.QHelpFilterEngine`.
