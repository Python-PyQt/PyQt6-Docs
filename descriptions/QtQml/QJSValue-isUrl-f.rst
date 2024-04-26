.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: fd377a560f61cb90c950d939ca11585f

Returns true if this :sip:ref:`~PyQt6.QtQml.QJSValue` is an object of the URL JavaScript class; otherwise returns false.

**Note:** For a :sip:ref:`~PyQt6.QtQml.QJSValue` that contains a :sip:ref:`~PyQt6.QtCore.QUrl`, this function returns false. However, ``toVariant().value<QUrl>()`` works in both cases.
