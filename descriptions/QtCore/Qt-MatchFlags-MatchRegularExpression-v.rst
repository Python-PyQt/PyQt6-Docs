.. sip:enum-member-description::
    :status: todo
    :value: 4
    :realname: Qt::MatchFlag::MatchRegularExpression
    :digest: 5129f811fc4adb8bee9a67c1a210c523

Performs string-based matching using a regular expression as the search term. Uses `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_. When using this flag, a `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object can be passed as parameter and will directly be used to perform the search. The case sensitivity flag will be ignored as the `QRegularExpression <https://doc.qt.io/qt-6/qtcore-changes-qt6.html#qregularexpression>`_ object is expected to be fully configured. This enum value was added in Qt 5.15.
