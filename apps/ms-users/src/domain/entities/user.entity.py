"""

enum UserState {
    PENDING = 'PENDING'
    ACTIVE
    EXPIRED
}

interface User extends Domain<number> {
    uuid: string
    password: string
    pin: string
    phoneNumber: number
    state: UserState
    name: string
    createdAt? Date
    updatedAt? Date
    email? string
    referralCode: string
    referredBy: string
    birthDate? Date
}

class UserEntity implements User {
    id: number
    uuid: string
    password: string
    pin: string
    phoneNumber: number
    state: UserState
    name: string
    createdAt? Date
    updatedAt? Date
    email? string
    referralCode: string
    referredBy: string
    birthDate? Date

    __init__(props: Partial<User>) {
        Object.assign(self, props)
    }
}
"""