.. sip:method-description::
    :status: todo
    :pysig: f0bd926d1303296f0942b8a03a4e8842
    :realsig: (QStringView,Qt::CaseSensitivity,QRegularExpression::WildcardConversionOptions)
    :digest: 54aca3d425fedfb68f9dc6c860d19aff

Returns a regular expression of the glob pattern *pattern*. The regular expression will be case sensitive if *cs* is :sip:ref:`~PyQt6.QtCore.Qt.CaseSensitivity.CaseSensitive`, and converted according to *options*.

Equivalent to

::

    auto reOptions = cs == Qt::CaseSensitive ? QRegularExpression::NoPatternOption :
                                               QRegularExpression::CaseInsensitiveOption;
    return QRegularExpression(wildcardToRegularExpression(str, options), reOptions);
