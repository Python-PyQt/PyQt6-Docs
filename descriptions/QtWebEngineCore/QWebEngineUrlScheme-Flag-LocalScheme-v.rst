.. sip:enum-member-description::
    :status: todo
    :value: 0x2
    :digest: fa213d50c870e35f2ba6b22ccfc9f225

Indicates that the URL scheme provides access to local resources. The purpose of this flag is to prevent network content from accessing local resources. Only schemes with the ``LocalAccessAllowed`` flag may load resources from a scheme with the ``LocalScheme`` flag. The only builtin scheme with this flag is ``file``.
