.. sip:method-description::
    :status: todo
    :pysig: 2e9add127f9be5f17ac04a5b45b66e9b
    :realsig: (QAnyStringView,QAnyStringView)
    :digest: 0bf301ead9c7ab0188aa5950236b75e9

Writes an XML processing instruction with *target* and *data*, where *data* must not contain the sequence "?>".

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
