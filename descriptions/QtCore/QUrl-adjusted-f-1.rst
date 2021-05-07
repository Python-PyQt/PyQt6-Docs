.. sip:method-description::
    :status: todo
    :pysig: c9f11427cbcff87672be8f72abbf200d
    :realsig: (QUrl::FormattingOptions) const
    :digest: a532e49322ff85c35875fd893adaa7aa

Returns an adjusted version of the URL. The output can be customized by passing flags with *options*.

The encoding options from :sip:ref:`~PyQt6.QtCore.QUrl.ComponentFormattingOption` don't make much sense for this method, nor does :sip:ref:`~PyQt6.QtCore.QUrl.FormattingOptions.PreferLocalFile`.

This is always equivalent to :sip:ref:`~PyQt6.QtCore.QUrl`\ (url.\ :sip:ref:`~PyQt6.QtCore.QUrl.toString`\ (options)).

.. seealso:: FormattingOptions, :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`, :sip:ref:`~PyQt6.QtCore.QUrl.toString`.
