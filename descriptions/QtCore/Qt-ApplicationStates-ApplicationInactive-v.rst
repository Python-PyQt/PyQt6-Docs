.. sip:enum-member-description::
    :status: todo
    :value: 0x00000002
    :realname: Qt::ApplicationState::ApplicationInactive
    :digest: 25903135fe66f73976f45a8d7f82014a

The application is visible, but not selected to be in front. On desktop platforms, this typically means that the user activated another application. On mobile platforms, it is more common to enter this state when the OS is interrupting the user with e.g. incoming calls or SMS-messages. While in this state, consider reducing CPU-intensive tasks.
