.. sip:method-description::
    :status: todo
    :pysig: 5585619ac7706749d93aa933194581de
    :realsig: (QUrl::ComponentFormattingOptions) const
    :digest: 6e55e9937a157663786d1b421cb129cd

Returns the fragment of the URL. To determine if the parsed URL contained a fragment, use :sip:ref:`~PyQt6.QtCore.QUrl.hasFragment`.

The *options* argument controls how to format the fragment component. All values produce an unambiguous result. With :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded`, all percent-encoded sequences are decoded; otherwise, the returned value may contain some percent-encoded sequences for some control sequences not representable in decoded form in QString.

Note that :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOptions.FullyDecoded` may cause data loss if those non-representable sequences are present. It is recommended to use that value when the result will be used in a non-URL context.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QUrl.setFragment`, :sip:ref:`~PyQt6.QtCore.QUrl.hasFragment`.
