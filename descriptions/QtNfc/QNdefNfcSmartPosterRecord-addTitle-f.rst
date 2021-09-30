.. sip:method-description::
    :status: todo
    :pysig: 66c5f3936128fe8f6bd6d40988138fc4
    :realsig: (const QNdefNfcTextRecord&)
    :digest: 67efff2c4a37fa84a359b0abdd0b8140

Attempts to add a title record *text* to the smart poster. If the smart poster does not already contain a title record with the same locale as title record *text*, then the title record is added and the function returns ``true``. Otherwise ``false`` is returned.
