.. sip:enum-member-description::
    :status: todo
    :value: 0x2
    :digest: cc36c5d8b6c6a5ed6d2e93cc9fc0fd7d

Indicates that the URL scheme provides access to local resources. The purpose of this flag is to prevent network content from accessing local resources. Only schemes with the ``LocalAccessAllowed`` flag may load resources from a scheme with the ``Local`` flag. The only builtin schemes with this flag are ``file`` and ``qrc``.
