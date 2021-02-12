.. sip:class-description::
    :status: todo
    :brief: Holds a sequence of bytes that can be quickly matched in a byte array
    :digest: 5d7702fb69b78e3a2709eecc147bcda0

The :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher` class holds a sequence of bytes that can be quickly matched in a byte array.

This class is useful when you have a sequence of bytes that you want to repeatedly match against some byte arrays (perhaps in a loop), or when you want to search for the same sequence of bytes multiple times in the same byte array. Using a matcher object and :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.indexIn` is faster than matching a plain :sip:ref:`~PyQt6.QtCore.QByteArray` with :sip:ref:`~PyQt6.QtCore.QByteArray.indexOf` if repeated matching takes place. This class offers no benefit if you are doing one-off byte array matches.

Create the :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher` with the :sip:ref:`~PyQt6.QtCore.QByteArray` you want to search for. Then call :sip:ref:`~PyQt6.QtCore.QByteArrayMatcher.indexIn` on the :sip:ref:`~PyQt6.QtCore.QByteArray` that you want to search.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QByteArray`, QStringMatcher.
