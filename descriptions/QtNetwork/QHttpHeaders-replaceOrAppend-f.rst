.. sip:method-description::
    :status: todo
    :pysig: 855a4ad1b2e634a6a8542e070e1324d3
    :realsig: (QHttpHeaders::WellKnownHeader, QAnyStringView)
    :digest: 36306297cdb67886639a8493037ea3ee

If :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` already contains *name*, replaces its value with *newValue* and removes possible additional *name* entries. If *name* didn't exist, appends a new entry. Returns ``true`` if successful.

This function is a convenience method for setting a unique *name* : *newValue* header. For most headers the relative order does not matter, which allows reusing an existing entry if one exists.

.. seealso:: replaceOrAppend(QAnyStringView, QAnyStringView).
