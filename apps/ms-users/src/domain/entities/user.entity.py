"""

enum UserState {
    PENDING = 'PENDING'
    ACTIVE = 'ACTIVE'
    INACTIVE = 'INACTIVE'
}

enum InteractionState {
    INTRODUCTION = 'INTRODUCTION'
    COMPANIONSHIP = 'COMPANIONSHIP'
    LYRICS = 'LYRICS'
}

interface User extends Domain<number> {
    uuid: string
    password: string
    pin: string
    phoneNumber: number
    state: UserState
    iState: InteractionState
    intro: string[]
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
    iState: InteractionState
    intro: string[]
    name: string
    createdAt? Date
    updatedAt? Date
    email? string
    referralCode: string
    referredBy: string
    birthDate? Date

    def __init__(props: Partial<User>) {
        Object.assign(self, props)
    }
}
"""