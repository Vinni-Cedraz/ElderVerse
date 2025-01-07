from enum import Enum
from typing import Optional, List
from datetime import datetime
from libs.common.utils.helpers.domain_helper import Domain


class UserState(Enum):
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class InteractionState(Enum):
    INTRODUCTION = "INTRODUCTION"
    COMPANIONSHIP = "COMPANIONSHIP"
    LYRICS = "LYRICS"


class _User(Domain[int]):
    def __init__(
        self,
        id: Optional[int],
        uuid: str,
        password: str,
        pin: str,
        phone_number: int,
        state: UserState,
        i_state: InteractionState,
        intro: List[str],
        name: str,
        referral_code: str,
        referred_by: str,
        created_at: Optional[datetime] = None,
        updated_at: Optional[datetime] = None,
        email: Optional[str] = None,
        birth_date: Optional[datetime] = None,
    ):
        super().__init__(id)
        self.uuid = uuid
        self.password = password
        self.pin = pin
        self.phone_number = phone_number
        self.state = state
        self.i_state = i_state
        self.intro = intro
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.email = email
        self.referral_code = referral_code
        self.referred_by = referred_by
        self.birth_date = birth_date


class UserEntity(_User):
    def __init__(self, props: dict):
        super().__init__(
            id=props.get("id"),
            uuid=props.get("uuid"),
            password=props.get("password"),
            pin=props.get("pin"),
            phone_number=props.get("phone_number"),
            state=props.get("state"),
            i_state=props.get("i_state"),
            intro=props.get("intro", []),
            name=props.get("name"),
            referral_code=props.get("referral_code"),
            referred_by=props.get("referred_by"),
            created_at=props.get("created_at"),
            updated_at=props.get("updated_at"),
            email=props.get("email"),
            birth_date=props.get("birth_date"),
        )
