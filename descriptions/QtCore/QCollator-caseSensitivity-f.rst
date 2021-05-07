.. sip:method-description::
    :status: todo
    :pysig: 2c020bcaf381441b1fc0a2acfce2932b
    :realsig: () const
    :digest: 6a2274a65682f07a2c48d6f82713a235

Returns case sensitivity of the collator.

This defaults to case-sensitive until set.

**Note:** In the C locale, when case-sensitive, all lower-case letters sort after all upper-case letters, where most locales sort each lower-case letter either immediately before or immediately after its upper-case partner. Thus "Zap" sorts before "ape" in the C locale but after in most others.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCollator.setCaseSensitivity`.
