from fastapi.security import OAuth2PasswordBearer
from dotenv import load_dotenv
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta, timezone
from fastapi import Depends
from fastapi.security import OAuth2PasswordRequestForm
from uuid import UUID
from typing import Annotated
import uuid

from src.entities.user import User
from . import model
from ..exceptions import AuthenticationError

import logging
import jwt
from jwt import PyJWTError
import os

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))

oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")
bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    return bcrypt_context.hash(password)


def authenticate_user(username: str, password: str, db: Session) -> User | bool:
    user = db.query(User).filter(User.username == username).first()
    if not user or not verify_password(password, user.password_hash):
        logging.warning(f"Failed login attempt for user: {username}")
        return False
    return user


def create_access_token(username: str, user_id: UUID, expires_delta: timedelta) -> str:
    encode = {
        "sub": username,
        "id": str(user_id),
        "exp": datetime.now(timezone.utc) + expires_delta,
    }
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_access_token(token: str) -> model.TokenData:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: UUID = UUID(payload.get("id"))
        return model.TokenData(user_id=str(user_id))
    except PyJWTError as e:
        logging.warning(f"Could not validate credentials: {e}")
        raise AuthenticationError()


def register_user(db: Session, user: model.RegisterUserRequest) -> None:
    try:
        user_model = User(
            id=uuid.uuid4(),
            username=user.username,
            email=user.email,
            password_hash=get_password_hash(user.password),
            created_at=datetime.now(timezone.utc),
            updated_at=datetime.now(timezone.utc),
        )
        db.add(user_model)
        db.commit()
    except Exception as e:
        logging.error(f"Error registering user: {user.username} with Error: {e}")
        raise


def get_current_user(token: str = Depends(oauth2_bearer)) -> User:
    return verify_access_token(token)


CurrentUser = Annotated[model.TokenData, Depends(get_current_user)]


def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends(oauth2_bearer)],
                           db: Session) -> model.Token:
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise AuthenticationError()
    token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    token = create_access_token(user.username, user.id, token_expires)
    return model.Token(access_token=token, token_type="bearer")
