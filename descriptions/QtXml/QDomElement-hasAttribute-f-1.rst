.. sip:method-description::
    :status: todo
    :pysig: 1ab98a4411fb7d10d5134d664f82b37e
    :realsig: (const QString&) const
    :digest: f5afabf179bbcd5a4f652bb4d7f295b0

Returns ``true`` if this element has an attribute called *name*; otherwise returns ``false``.

**Note:** This function does not take the presence of namespaces into account. As a result, the specified name will be tested against fully-qualified attribute names that include any namespace prefixes that may be present.

Use :sip:ref:`~PyQt6.QtXml.QDomElement.hasAttributeNS` to explicitly test for attributes with specific namespaces and names.
