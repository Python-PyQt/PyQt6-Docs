.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: c0d7bad94b38c3d0b0d2b943ab0d214f

Returns ``true`` if the regular expression partially matched against the subject string, or false otherwise.

**Note:** Only a match that explicitly used the one of the partial match types can yield a partial match. Still, if such a match succeeds totally, this function will return false, while :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasMatch` will return true.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QRegularExpression.match`, :sip:ref:`~PyQt6.QtCore.QRegularExpression.MatchType`, :sip:ref:`~PyQt6.QtCore.QRegularExpressionMatch.hasMatch`.
