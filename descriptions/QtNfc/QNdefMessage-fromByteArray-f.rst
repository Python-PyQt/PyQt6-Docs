.. sip:method-description::
    :status: todo
    :pysig: 636b600f21b8787daec34c5fb74a59bb
    :realsig: (const QByteArray&)
    :digest: 5c5102b97f65b0d165cea78deb456aa8

Returns an NDEF message parsed from the contents of *message*.

The *message* parameter is interpreted as the raw message format defined in the NFC Data Exchange Format technical specification.

If a parse error occurs an empty NDEF message is returned.
