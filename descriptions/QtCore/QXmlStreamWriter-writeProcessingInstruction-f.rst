.. sip:method-description::
    :status: todo
    :pysig: 9a0a225b1d77510a8f81553abb1cfe88
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: 0bf301ead9c7ab0188aa5950236b75e9

Writes an XML processing instruction with *target* and *data*, where *data* must not contain the sequence "?>".

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
