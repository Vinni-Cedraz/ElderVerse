"""
class JwtStrategy extends PassportStrategy(Strategy) {
    ttl? Milliseconds

    __init__() {
        super({
            jwtFromRequest: ExtractJwt.fromAuthHeaderAsBearerToken(),
            ignoreExpiration: configService('APP_JWT_IGNORE_EXPIRATION', true),
            secretOrKey: configService.get('APP_JWT_TOKEN')
        })
        self.ttl = configService.get('APP_JWT_CACHE_TTL_S', 900)
    }


    async validate(request, payload: AccessToken): Promise<AuthUser> {
        token: string = request.headers[HeaderParam.AUTHORIZATION]
        hash = createHash('sha1').update(token).digest('base64')

        #check if previous authorization exists
        cached = await redisService.get<AuthUser>('authorization-${hash})
        if (cached) {
            request.user = cached.data
            return request.user
        }

        requestId = request?.id ?? uuidV4()

        getRequest = new GetUserByPhoneNumberRequest({ phoneNumber })
        user = await getUserByPhoneNumberService.execute(getRequest)

        if (!user) {
            log('user not found')
            throw new UnauthorizedException()
        }
        if (!user.active) {
            log('user is not active')
            throw new UnauthorizedException()
        }

        authUser: AuthUser = {
            id: user.id,
            uuid: user.uuid,
            phoneNumber: user.phoneNumber,
            password: user.password,
            active: user.active,
            sessionSystemId: payload.session_system_ud
        }

        headers = request.headers

        self.redisService.set<string>({
            key:'authorization-${hash}',
            data: hash,
            ttl: self.ttl
        })

        return authUser
    }
}

"""