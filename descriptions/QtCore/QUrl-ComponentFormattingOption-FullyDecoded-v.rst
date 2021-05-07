.. sip:enum-member-description::
    :status: todo
    :value: FullyEncoded | DecodeReserved | 0x4000000
    :digest: 8bb69669c0d7d7c607c67f1c67fa0e97

Attempt to decode as much as possible. For individual components of the URL, this decodes every percent encoding sequence, including control characters (U+0000 to U+001F) and UTF-8 sequences found in percent-encoded form. Use of this mode may cause data loss, see below for more information.
