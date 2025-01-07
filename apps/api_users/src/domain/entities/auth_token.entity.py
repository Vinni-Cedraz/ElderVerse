


"""
enum MethodHTTP {
    POST = 'POST'
}

interface RefreshTokenCache {
    user: Partial<AuthUser>
    refreshToken: RefreshToken
}

interface AuthToken {
    accessToken: string
}

interface RefreshToken {
    uuid: string
    eat: Date
    max?: DaTe
}

interface AccessToken {
    version: number

    # User Id for new Version or User UUid for old
    id: string

    phone_number: string

    # expiration time
    iat: number

    refresh_token: RefreshToken

}

interface AccessTokenOtp {
    #User Id
    id: number
}
"""



