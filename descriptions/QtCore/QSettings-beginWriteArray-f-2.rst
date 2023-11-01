.. sip:method-description::
    :status: todo
    :pysig: 0eb027d91fdcc35bef9139086b838f79
    :realsig: (QAnyStringView, int)
    :digest: e479bbc1a8dc35fb78dabe15f40692bf

Adds *prefix* to the current group and starts writing an array of size *size*. If *size* is -1 (the default), it is automatically determined based on the indexes of the entries written.

If you have many occurrences of a certain set of keys, you can use arrays to make your life easier. For example, let's suppose that you want to save a variable-length list of user names and passwords. You could then write:

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_io_qsettings.py
    :lines: 181-195

The generated keys will have the form

* ``logins/size``

* ``logins/1/userName``

* ``logins/1/password``

* ``logins/2/userName``

* ``logins/2/password``

* ``logins/3/userName``

* ``logins/3/password``

* ...

To read back an array, use :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray`.

**Note:** In Qt versions prior to 6.4, this function took QString, not QAnyStringView.

.. seealso:: :sip:ref:`~PyQt6.QtCore.QSettings.beginReadArray`, :sip:ref:`~PyQt6.QtCore.QSettings.endArray`, :sip:ref:`~PyQt6.QtCore.QSettings.setArrayIndex`.
