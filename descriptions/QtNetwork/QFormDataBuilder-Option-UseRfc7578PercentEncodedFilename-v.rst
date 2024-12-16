.. sip:enum-member-description::
    :status: todo
    :value: 0x02
    :digest: d640f0f530d5dd1646b008024ed05bf0

When a body-part's file-name contains non-US-ASCII characters, `RFC 7578 Section 4.2 <https://datatracker.ietf.org/doc/html/rfc7578#section-4.2>`_ suggests to use percent-encoding of the octets of the UTF-8-encoded file-name. It goes on to note that many implementations, however, do *not* percent-encode the UTF-8-encoded file-name, but just emit "raw" UTF-8 (with ``"`` and ``\`` escaped using ``\``). This is the default of :sip:ref:`~PyQt6.QtNetwork.QFormDataBuilder`, too.
