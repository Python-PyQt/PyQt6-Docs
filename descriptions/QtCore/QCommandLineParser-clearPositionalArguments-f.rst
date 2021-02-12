.. sip:method-description::
    :status: todo
    :pysig: d41d8cd98f00b204e9800998ecf8427e
    :realsig: ()
    :digest: fc359e6edfe76ff2cd1d1fde76b30939

Clears the definitions of additional arguments from the help text.

This is only needed for the special case of tools which support multiple commands with different options. Once the actual command has been identified, the options for this command can be defined, and the help text for the command can be adjusted accordingly.

Example:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_tools_qcommandlineparser.py
    :lines: 103-138
