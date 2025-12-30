from passlib.context import CryptContext

# Using bcrypt (with 72-byte limit)
#---------  use (argon2) instead of (bcrypt)  -------------//
pwd_cxt = CryptContext(schemes=["argon2"], deprecated="auto")

class Hash:

    @staticmethod
    def create(password: str) -> str:
        # Truncate password to 72 bytes for bcrypt
        # password = password[:72]
        return pwd_cxt.hash(password)

    @staticmethod
    def verify(plain_pass: str,hashed_pass: str) -> bool:
        # Truncate password to 72 bytes for bcrypt
        # plain_pass = plain_pass[:72]
        return pwd_cxt.verify(plain_pass, hashed_pass)

