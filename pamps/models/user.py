from typing import Optional,List,TYPE_CHECKING
from sqlmodel import Field , SQLModel,Relationship
from pamps.security import HashedPassword
from pydantic import BaseModel



if TYPE_CHECKING:
    from pamps.models.post import Post



class User(SQLModel,table=True):

    """Represents the User Model"""
    id: Optional[int] = Field(default=None,primary_key=True)
    email: str = Field(unique=True, nullable=False)
    username: str = Field(unique=True,nullable=False)
    avatar: Optional[str] = None
    bio: Optional[str] = None
    password: HashedPassword 
    posts: List["Post"] = Relationship(back_populates="user")

class UserResponse(BaseModel):
    """Serializer for user Response"""

    username:str
    avatar: Optional[str]=None
    bio:Optional[str]=None


class UserRequest(BaseModel):
    """Serializer for User requests payload"""

    email:str
    username:str
    password:str
    avatar:Optional[str]=None
    bio:Optional[str]=None