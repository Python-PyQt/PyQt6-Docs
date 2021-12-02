.. sip:enum-description::
    :status: todo
    :digest: 1f8514a8c0edf693dd468a542a25c4db

This enum type defines the valid event types in Qt. The event types and the specialized classes for each type are as follows:

User events should have values between ``User`` and ``MaxUser``:

For convenience, you can use the :sip:ref:`~PyQt6.QtCore.QEvent.registerEventType` function to register and reserve a custom event type for your application. Doing so will allow you to avoid accidentally re-using a custom event type already in use elsewhere in your application.
