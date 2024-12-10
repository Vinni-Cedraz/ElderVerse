"""
interface Domain<T> {
    id?: T
}

class Entity {
    static generateUuid(baseId: string): string {
        return uuidV5(baseId, this['NAMESPACE'])
    }
}

"""