.. sip:class-description::
    :status: todo
    :brief: Simple CBOR encoder operating on a one-way stream
    :digest: ad9a6a8f48f24d7101c065016e653917

The :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` class is a simple CBOR encoder operating on a one-way stream.

This class can be used to quickly encode a stream of CBOR content directly to either a :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice`. CBOR is the Concise Binary Object Representation, a very compact form of binary data encoding that is compatible with JSON. It was created by the IETF Constrained RESTful Environments (CoRE) WG, which has used it in many new RFCs. It is meant to be used alongside the `CoAP protocol <https://tools.ietf.org/html/rfc7252>`_.

:sip:ref:`~PyQt6.QtCore.QCborStreamWriter` provides a StAX-like API, similar to that of :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter`. It is rather low-level and requires a bit of knowledge of CBOR encoding. For a simpler API, see QCborValue and especially the encoding function QCborValue::toCbor().

The typical use of :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` is to create the object on the target :sip:ref:`~PyQt6.QtCore.QByteArray` or :sip:ref:`~PyQt6.QtCore.QIODevice`, then call one of the :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append` overloads with the desired type to be encoded. To create arrays and maps, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` provides :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray` and :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap` overloads, which must be terminated by the corresponding :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray` and :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap` functions.

The following example encodes the equivalent of this JSON content:

{ "label": "journald", "autoDetect": false, "condition": "libs.journald", "output": [ "privateFeature" ] }

.. literalinclude:: ../../../snippets/qtbase-src-corelib-doc-snippets-code-src_corelib_serialization_qcborstream.py
    :lines: 58-74

.. _qcborstreamwriter-cbor-support:

CBOR support
------------

:sip:ref:`~PyQt6.QtCore.QCborStreamWriter` supports all CBOR features required to create canonical and strict streams. It implements almost all of the features specified in `RFC 7049 <https://tools.ietf.org/html/rfc7049>`_.

The following table lists the CBOR features that :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` supports.

+-----------------------------------------------+------------------+
| Feature                                       | Support          |
+===============================================+==================+
| Unsigned numbers                              | Yes (full range) |
+-----------------------------------------------+------------------+
| Negative numbers                              | Yes (full range) |
+-----------------------------------------------+------------------+
| Byte strings                                  | Yes              |
+-----------------------------------------------+------------------+
| Text strings                                  | Yes              |
+-----------------------------------------------+------------------+
| Chunked strings                               | No               |
+-----------------------------------------------+------------------+
| Tags                                          | Yes (arbitrary)  |
+-----------------------------------------------+------------------+
| Booleans                                      | Yes              |
+-----------------------------------------------+------------------+
| Null                                          | Yes              |
+-----------------------------------------------+------------------+
| Undefined                                     | Yes              |
+-----------------------------------------------+------------------+
| Arbitrary simple values                       | Yes              |
+-----------------------------------------------+------------------+
| Half-precision float (16-bit)                 | Yes              |
+-----------------------------------------------+------------------+
| Single-precision float (32-bit)               | Yes              |
+-----------------------------------------------+------------------+
| Double-precision float (64-bit)               | Yes              |
+-----------------------------------------------+------------------+
| Infinities and NaN floating point             | Yes              |
+-----------------------------------------------+------------------+
| Determinate-length arrays and maps            | Yes              |
+-----------------------------------------------+------------------+
| Indeterminate-length arrays and maps          | Yes              |
+-----------------------------------------------+------------------+
| Map key types other than strings and integers | Yes (arbitrary)  |
+-----------------------------------------------+------------------+

.. _qcborstreamwriter-canonical-cbor-encoding:

Canonical CBOR encoding
.......................

Canonical CBOR encoding is defined by `Section 3.9 of RFC 7049 <https://tools.ietf.org/html/rfc7049#section-3.9>`_. Canonical encoding is not a requirement for Qt's CBOR decoding functionality, but it may be required for some protocols. In particular, protocols that require the ability to reproduce the same stream identically may require this.

In order to be considered "canonical", a CBOR stream must meet the following requirements:

* Integers must be as small as possible. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` always does this (no user action is required and it is not possible to write overlong integers).

* Array, map and string lengths must be as short as possible. As above, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` automatically does this.

* Arrays, maps and strings must use explicit length. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` always does this for strings; for arrays and maps, be sure to call :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startArray` and :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.startMap` overloads with explicit length.

* Keys in every map must be sorted in ascending order. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` offers no help in this item: the developer must ensure that before calling :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append` for the map pairs.

* Floating point values should be as small as possible. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` will not convert floating point values; it is up to the developer to perform this check prior to calling :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append` (see those functions' examples).

.. _qcborstreamwriter-strict-cbor-mode:

Strict CBOR mode
................

Strict mode is defined by `Section 3.10 of RFC 7049 <https://tools.ietf.org/html/rfc7049#section-3.10>`_. As for Canonical encoding above, :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` makes it possible to create strict CBOR streams, but does not require them or validate that the output is so.

* Keys in a map must be unique. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` performs no validation of map keys.

* Tags may be required to be paired only with the correct types, according to their specification. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` performs no validation of tag usage.

* Text Strings must be properly-encoded UTF-8. :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` always writes proper UTF-8 for strings added with :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.append`, but performs no validation for strings added with appendTextString().

.. _qcborstreamwriter-invalid-cbor-stream:

Invalid CBOR stream
...................

It is also possible to misuse :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` and produce invalid CBOR streams that will fail to be decoded by a receiver. The following actions will produce invalid streams:

* Append a tag and not append the corresponding tagged value (\ :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` produces no diagnostic).

* Append too many or too few items to an array or map with explicit length (\ :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endMap` and :sip:ref:`~PyQt6.QtCore.QCborStreamWriter.endArray` will return false and :sip:ref:`~PyQt6.QtCore.QCborStreamWriter` will log with :sip:ref:`~PyQt6.QtCore.qWarning`).

.. seealso:: :sip:ref:`~PyQt6.QtCore.QCborStreamReader`, QCborValue, :sip:ref:`~PyQt6.QtCore.QXmlStreamWriter`.
