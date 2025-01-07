"""
from /ms-users/domain import User

enum AuthSessionState {
 PENDING = 'PENDING'
 ACTIVE
 INACTIVE
}

interface AuthSession extends Domain<string> {
    user: User
    externalId: string
    sharedSecretHash: string
    sessionSystemId: string
    state: AuthSessionState
    createdAt? Date
    updatedAt? Date
    deletedAt? Date
    isActive(): boolean
    isPending(): boolean
    isExternalIdExpired(
        keyDecodedUuidTime: string,
        externalIdExpiredInS: number
    ): boolean
}

class AuthSessionEntity implements AuthSession {
    id: string
    user: User
    externalId: string
    shjaredSecretHash: string
    sessionSystemId: string
    state: AuthSessionState
    ...
    __init__(props: Partial<AuthSession>) {
        Object.assign(self, props)
    }

    def isActive() {
        return this.state == AuthSessionState.ACTIVE
    }
    ...

    def isExternalIdExpired(
        keyDecodedUuidTime: string,
        externalIdExpiredInS: number
    ) {
        return getMoment(decodeTimeUuidV4(keydecodedUuidTime, self.externalId)).add(externalIdExpiredInS, 's') < getMoment()
    }
}


"""