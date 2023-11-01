.. sip:method-description::
    :status: todo
    :pysig: f2e940b49da3b908ab5d918eb9bd732e
    :realsig: (QAnyStringView, QAnyStringView)
    :digest: 0bf301ead9c7ab0188aa5950236b75e9

Writes an XML processing instruction with *target* and *data*, where *data* must not contain the sequence "?>".

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
