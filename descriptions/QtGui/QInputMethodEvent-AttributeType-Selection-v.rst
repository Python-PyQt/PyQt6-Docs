.. sip:enum-member-description::
    :status: todo
    :value: 4
    :digest: e3ee25f587c36e2f0bdb45d3c6e5abfb

If set, the edit cursor should be moved to the specified position in the editor text contents. In contrast with ``Cursor``, this attribute does not work on the preedit text, but on the surrounding text. The cursor will be moved after the commit string has been committed, and the preedit string will be located at the new edit position. The start position specifies the new position and the length variable can be used to set a selection starting from that point. The value is unused.
