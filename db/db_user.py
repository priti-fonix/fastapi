from sqlalchemy.orm.session import Session
from schema import UserBase
from db.models import Dbuser
from db.hash import Hash

def create_user(db:Session, request: UserBase):
    new_user = Dbuser(username =  request.username,
                      email = request.email,
                      password = Hash.bcrypt(request.password)
                      )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def get_all_users(db:Session):
    return db.query(Dbuser).all()

def get_user(db:Session,id :int):
    return db.query(Dbuser).filter(Dbuser.id == id).first()

def update_user(db:Session, id: int, request:UserBase):
    user = db.query(Dbuser).filter(Dbuser.id == id)
    user.update({
        Dbuser.username: request.username,
        Dbuser.email: request.email,
        Dbuser.password: Hash.bcrypt(request.password)
    })
    db.commit()
    return user.first()


def delete_user(db:Session, id: int):
    user = db.query(Dbuser).filter(Dbuser.id == id).first()
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    db.delete(user)
    db.commit()
    return user



'''
sess.query(User).filter(User.age == 25).update(
        {User.age: User.age - 10}, synchronize_session=False
    )
    '''