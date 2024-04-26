.. sip:class-description::
    :status: todo
    :brief: Class for holding HTTP headers
    :digest: 0edc44dcc3850954f562b12fbba243e4

:sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` is a class for holding HTTP headers.

The class is an interface type for Qt networking APIs that use or consume such headers.

.. _qhttpheaders-allowed-field-name-and-value-characters:

Allowed field name and value characters
---------------------------------------

An HTTP header consists of *name* and *value*. When setting these, :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` validates *name* and *value* to only contain characters allowed by the HTTP RFCs. For detailed information see `RFC 9110 Chapters 5.1 and 5.5 <https://datatracker.ietf.org/doc/html/rfc9110#name-field-values>`_.

In all, this means:

* ``name`` must consist of visible ASCII characters, and must not be empty

* ``value`` may consist of arbitrary bytes, as long as header and use case specific encoding rules are adhered to. ``value`` may be empty

The setters of this class automatically remove any leading or trailing whitespaces from *value*, as they must be ignored during the *value* processing.

.. _qhttpheaders-combining-values:

Combining values
----------------

Most HTTP header values can be combined with a single comma ``','`` plus an optional whitespace, and the semantic meaning is preserved. As an example, these two should be semantically similar:

::

    // Values as separate header entries
    myheadername: myheadervalue1
    myheadername: myheadervalue2
    // Combined value
    myheadername: myheadervalue1, myheadervalue2

However, there is a notable exception to this rule: `Set-Cookie <https://datatracker.ietf.org/doc/html/rfc9110#name-field-order>`_. Due to this and the possibility of custom use cases, :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` does not automatically combine the values.

.. _qhttpheaders-performance:

Performance
-----------

Most :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders` functions provide both :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.WellKnownHeader` and QAnyStringView overloads. From a memory-usage and computation point of view it is recommended to use the :sip:ref:`~PyQt6.QtNetwork.QHttpHeaders.WellKnownHeader` overloads.
