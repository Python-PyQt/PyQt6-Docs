.. sip:enum-member-description::
    :status: todo
    :value: EncodeSpaces | EncodeUnicode | EncodeDelimiters | EncodeReserved
    :realname: QUrl::ComponentFormattingOption::FullyEncoded
    :digest: 51b5ba656b4258d3dd44c2e20c68c5d1

Leave all characters in their properly-encoded form, as this component would appear as part of a URL. When used with :sip:ref:`~PyQt6.QtCore.QUrl.toString`, this produces a fully-compliant URL in QString form, exactly equal to the result of :sip:ref:`~PyQt6.QtCore.QUrl.toEncoded`
