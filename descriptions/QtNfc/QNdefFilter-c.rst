.. sip:class-description::
    :status: todo
    :brief: Filter for matching NDEF messages
    :digest: 25dbb12e10c8a2870852b1ead4510f4e

The :sip:ref:`~PyQt6.QtNfc.QNdefFilter` class provides a filter for matching NDEF messages.

The :sip:ref:`~PyQt6.QtNfc.QNdefFilter` encapsulates the structure of an NDEF message and is used for matching messages that have a particular structure.

The following filter matches NDEF messages that contain a single smart poster record:

::

    QNdefFilter filter;
    filter.append(QNdefRecord::NfcRtd, "Sp");

The following filter matches NDEF messages that contain a URI, a localized piece of text and an optional JPEG image. The order of the records must be in the order specified:

::

    QNdefFilter filter;
    filter.setOrderMatch(true);
    filter.appendRecord(QNdefRecord::NfcRtd, "U");
    filter.appendRecord<QNdefNfcTextRecord>();
    filter.appendRecord(QNdefRecord::Mime, "image/jpeg", 0, 1);

The :sip:ref:`~PyQt6.QtNfc.QNdefFilter.match` method can be used to check if a message matches the filter.

.. _qndeffilter-matching-algorithms:

Matching Algorithms
-------------------

The filter behavior depends on the value of :sip:ref:`~PyQt6.QtNfc.QNdefFilter.orderMatch` parameter.

**Note:** In the discussion below we will consider the filter records to be equal if their ``typeNameFormat`` and ``type`` parameters match. Joining two records means adding their ``minimum`` and ``maximum`` values, respectively.

.. _qndeffilter-unordered-matching:

Unordered Matching
..................

If the record order is not taken into account, all the equal records in the filter can be joined. The resulting filter will contain only unique records, each with the updated ``minimum`` and ``maximum`` value.

Consider the following example:

::

    QNdefFilter filter;
    filter.appendRecord<QNdefNfcTextRecord>(0, 1);
    filter.appendRecord<QNdefNfcTextRecord>(0, 1);
    filter.appendRecord(QNdefRecord::Mime, "", 1, 1);
    filter.appendRecord<QNdefNfcTextRecord>(1, 1);
    filter.setOrderMatch(false);

With the unordered matching, the filter will be simplified to the following:

::

    QNdefFilter filter;
    filter.appendRecord<QNdefNfcTextRecord>(1, 3);
    filter.appendRecord(QNdefRecord::Mime, "", 1, 1);
    filter.setOrderMatch(false);

Once the filter contains only the unique records, the matching algorithm iterates through the message and calculates the actual amount of records of each type. If all the actual amounts fit in the corresponding [minimum, maximum] ranges, the matching algorithm returns ``true``.

.. _qndeffilter-ordered-matching:

Ordered Matching
................

If the record order is important, a different approach is applied. In this case the equal records can't be simply joined together. However, the consecutive equal records can still be joined. Then, the matching algorithm iterates through the message, this time also taking the positions of the records into account.

.. _qndeffilter-handling-empty-type-in-filter-record:

Handling Empty Type in Filter Record
....................................

It's possible to add a filter record with an empty ``type``. In this case the empty type will act as a wildcard for any type.

For example, the filter can be defined as follows:

::

    QNdefFilter filter;
    filter.addRecord(QNdefRecord::Mime, "", 1, 1);

This filter specifies that the message must contain exactly one NDEF record with :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime` :sip:ref:`~PyQt6.QtNfc.QNdefRecord.typeNameFormat`\ (), and any :sip:ref:`~PyQt6.QtNfc.QNdefRecord.type`\ ().

.. _qndeffilter-handling-extra-records-in-the-message:

Handling Extra Records in the Message
.....................................

If the message contains some records that do not match *any* record in the filter, the matching algorithm will return ``false``.

.. _qndeffilter-filter-examples:

Filter Examples
...............

In the table below, each filter record is specified by the following parameters (in the given order):

* ``typeNameFormat`` - contains the :sip:ref:`~PyQt6.QtNfc.QNdefRecord.typeNameFormat`\ () of the record.

* ``type`` - contains the :sip:ref:`~PyQt6.QtNfc.QNdefRecord.type`\ () of the record.

* ``minimum`` - contains the minimum amount of occurrences of the record in the message.

* ``maximum`` - contains the maximum amount of occurrences of the record in the message.

The filter contains multiple records.

The message consists of multiple :sip:ref:`~PyQt6.QtNfc.QNdefRecord`\ s. In the table below, only the :sip:ref:`~PyQt6.QtNfc.QNdefRecord.typeNameFormat`\ () and :sip:ref:`~PyQt6.QtNfc.QNdefRecord.type`\ () of each record will be shown, because the other parameters do not matter for filtering.

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Filter                                                                                                                                                                                                                      | Message                                                                                                                                                                                                                                                                                                                                                 | Match Result     | Comment                                                                                                                                                                                                                |
+=============================================================================================================================================================================================================================+=========================================================================================================================================================================================================================================================================================================================================================+==================+========================================================================================================================================================================================================================+
| Empty filter                                                                                                                                                                                                                | Empty message                                                                                                                                                                                                                                                                                                                                           | Match            |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Empty filter                                                                                                                                                                                                                | Non-empty message                                                                                                                                                                                                                                                                                                                                       | No match         |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Non-empty filter                                                                                                                                                                                                            | Empty message                                                                                                                                                                                                                                                                                                                                           | No match         |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T", 1, 2), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "", 1, 1), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Empty`, "", 0, 100)] | [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "image/jpeg"), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Empty`, ""), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T"), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Empty`, ""), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T")] | Unordered: match | Ordered filter does not match because the message must start with a :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd` record, but it starts with :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`.      |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ordered: no match                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                         |                  |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T", 0, 2), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "", 1, 1), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T", 1, 1)] | [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T"), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T"), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "image/jpeg")]                                                                                                                                     | Unordered: match | Ordered filter does not match because an :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd` record is expected after :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, but the message does not have it. |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ordered: no match                                                                                                                                                                                                           |                                                                                                                                                                                                                                                                                                                                                         |                  |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T", 0, 2), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T", 1, 1), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "", 1, 1)] | [(\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.NfcRtd`, "T"), (\ :sip:ref:`~PyQt6.QtNfc.QNdefRecord.TypeNameFormat.Mime`, "image/jpeg")]                                                                                                                                                                                                         | Unordered: match | Both cases match because the message contains the required minimum of records in the correct order.                                                                                                                    |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Ordered: match                                                                                                                                                                                                              |                                                                                                                                                                                                                                                                                                                                                         |                  |                                                                                                                                                                                                                        |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
