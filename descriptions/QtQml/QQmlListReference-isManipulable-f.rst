.. sip:method-description::
    :status: todo
    :pysig: c506ff134babdd6e68ab3e6350e95305
    :realsig: () const
    :digest: d80518ccc63e33d464892de55fa4fcf4

Return true if :sip:ref:`~PyQt6.QtQml.QQmlListReference.at`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.count`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.append`, and either :sip:ref:`~PyQt6.QtQml.QQmlListReference.clear` or :sip:ref:`~PyQt6.QtQml.QQmlListReference.removeLast` are implemented, so you can manipulate the list.

Mind that :sip:ref:`~PyQt6.QtQml.QQmlListReference.replace` and :sip:ref:`~PyQt6.QtQml.QQmlListReference.removeLast` can be emulated by stashing all items and rebuilding the list using :sip:ref:`~PyQt6.QtQml.QQmlListReference.clear` and :sip:ref:`~PyQt6.QtQml.QQmlListReference.append`. Therefore, they are not required for the list to be manipulable. Furthermore, :sip:ref:`~PyQt6.QtQml.QQmlListReference.clear` can be emulated using :sip:ref:`~PyQt6.QtQml.QQmlListReference.removeLast`.

.. seealso:: :sip:ref:`~PyQt6.QtQml.QQmlListReference.isReadable`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.at`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.count`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.append`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.clear`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.replace`, :sip:ref:`~PyQt6.QtQml.QQmlListReference.removeLast`.
