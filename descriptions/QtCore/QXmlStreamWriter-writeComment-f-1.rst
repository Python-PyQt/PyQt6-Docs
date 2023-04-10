.. sip:method-description::
    :status: todo
    :pysig: 81445f071599e8ca359c5cd31fa289a9
    :realsig: (QAnyStringView)
    :digest: bd868b6428a0383a75c2a263b8597213

Writes *text* as XML comment, where *text* must not contain the forbidden sequence ``--`` or end with ``-``. Note that XML does not provide any way to escape ``-`` in a comment.

**Note:** In Qt versions prior to 6.5, this function took QString, not QAnyStringView.
