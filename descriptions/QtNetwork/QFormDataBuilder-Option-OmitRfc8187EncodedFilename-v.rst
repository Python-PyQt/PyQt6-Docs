.. sip:enum-member-description::
    :status: todo
    :value: 0x01
    :digest: 6eba0d3a68ea3fc6421f36fb6c20c3cd

When a body-part's file-name contains non-US-ASCII characters, `RFC 6266 Section 4.3 <https://datatracker.ietf.org/doc/html/rfc6266#section-4.3>`_ suggests to use `RFC 8187 <https://datatracker.ietf.org/doc/html/rfc8187>`_-style encoding (``filename\*=utf-8''...``). The more recent `RFC 7578 Section 4.2 <https://datatracker.ietf.org/doc/html/rfc7578#section-4.2>`_, however, bans the use of that mechanism. Both RFCs are current as of this writing, so this option allows you to choose which one to follow. The default is to include the RFC 8187-encoded ``filename\*`` alongside the unencoded ``filename``, as suggested by RFC 6266.
