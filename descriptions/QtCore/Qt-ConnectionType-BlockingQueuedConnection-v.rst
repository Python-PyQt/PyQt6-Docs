.. sip:enum-member-description::
    :status: todo
    :value: 3
    :digest: 4b521a4dddd62b627747148eff218438

Same as , except that the signalling thread blocks until the slot returns. This connection must *not* be used if the receiver lives in the signalling thread, or else the application will deadlock.
