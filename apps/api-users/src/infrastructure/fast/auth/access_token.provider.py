"""
#builds access token from an authenticated users

class AccessTokenProvider {
    ttl: Milliseconds
    version: number
    sessionSystemId: string
    jwtExpiresInSeconds: number

    __init__(jwtService: JwtService, configService) {
        self.ttl = configService.get(APP_REFRESH_TOKEN_TTL_MS, defaultTime)
        self.version = configService(APP_JWT_VERSION, 300)
        self.jwtExpiresInSeconds = configService(APP_JWT_EXPIRES_IN_S)
    }

    def generateAccessToken(user: AuthUser): Promise {
        hashKey = 'refresh-token-users-${user.uuid}'
        expiresIn = self.jwtExpiresInSeconds

        refreshTokenCache: RefreshTokenCache = {
            user: {
                uuid: user.uuid,
                phoneNumber: user.phoneNumber
            },
            refreshToken: {
                uuid: uuidV4(),
                eat: getMoment().add(self.ttl, 'ms').toDate()
                max:
            }
        }

        await self.redisService.set({
            key: hashKey,
            data: refreshTokenCache,
            ttl: self.ttl
        })

        payload: AccessToken = {
            phone_number: user.phoneNumber,
            iat: 0,
            version: self.version
            id: user.uuid,
            refresh_token: refreshTokenCache.refreshToke
        }

        return self.jwtService.sign(payload, {expiresIn})
    }


}

"""